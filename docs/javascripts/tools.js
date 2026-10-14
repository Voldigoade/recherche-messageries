/* Progressive enhancement: the report-derived content works without this file. */
(function () {
  'use strict';
  const payload = document.getElementById('study-data');
  if (!payload || !window.StudyDecision) return;
  const data = JSON.parse(payload.textContent);
  const byId = new Map(data.messengers.map(m => [m.id,m]));
  const fieldMap = new Map(data.fields.map(f => [f.id,f]));
  const localeRoot = data.root + (data.lang === 'fr' ? '' : data.lang + '/');
  function element(tag, text, className) {
    const node=document.createElement(tag);
    if (text !== undefined) node.textContent=text;
    if (className) node.className=className;
    return node;
  }
  function link(text, href) {
    const a=element('a',text); a.href=href; return a;
  }
  function evidence(container, refs, context) {
    refs.forEach((id,index) => {
      const ref=data.sources[id];
      const a=link('['+(index+1)+']','https://github.com/Voldigoade/recherche-messageries/blob/main/research/'+ref.file+'#L'+ref.start_line);
      a.className='fact-source';a.setAttribute('aria-label',data.ui.evidence+': '+context+' — '+id);
      container.append(' ',a);
    });
  }
  function fact(m,key) {return m.facts[key]?.text || data.unknown;}
  function renderTable(ids,keys) {
    const table=element('table',undefined,'study-table');
    const head=element('thead'),row=element('tr');
    const first=element('th',data.ui.property);first.scope='col';row.append(first);
    ids.forEach(id => {const h=element('th',byId.get(id).name);h.scope='col';row.append(h);});
    head.append(row);table.append(head);
    const body=element('tbody');
    keys.forEach(key => {
      const r=element('tr'),h=element('th');h.scope='row';
      const f=fieldMap.get(key);
      h.append(f.concept ? link(f.label,localeRoot+'concepts/'+f.concept+'/') : document.createTextNode(f.label));
      r.append(h);
      ids.forEach(id => {
        const m=byId.get(id),cell=element('td',fact(m,key));
        if(m.facts[key]) evidence(cell,m.facts[key].sources,m.name+' / '+f.label);
        r.append(cell);
      });body.append(r);
    });table.append(body);return table;
  }
  function renderComparison(ids) {
    const result=document.getElementById('comparison-results');
    const basic=renderTable(ids,data.basic);
    const details=element('details',undefined,'technical-details');
    details.append(element('summary',data.ui.details),renderTable(ids,data.fields.map(f=>f.id).filter(k=>!data.basic.includes(k))));
    result.replaceChildren(basic,details);
    window.StudyTables?.enhance();
  }
  const comparator=document.getElementById('messenger-comparator');
  if (comparator) {
    const status=document.getElementById('compare-status');
    let selection=StudyDecision.normaliseSelection(new URL(location.href).searchParams.get('apps'),data.messengers);
    let ids=selection.ids;
    function save(push) {
      const next=new URL(location.href);next.searchParams.set('apps',ids.join(','));
      if(push) history.pushState({},'',next); else history.replaceState({},'',next);
      document.querySelectorAll('.md-select__link').forEach(a=>{const alternate=new URL(a.href);if(alternate.pathname.endsWith('/comparer/')){alternate.searchParams.set('apps',ids.join(','));a.href=alternate.href;}});
    }
    function render(push=false,announce=true) {
      const controls=document.getElementById('compare-selects');controls.replaceChildren();
      ids.forEach((id,index) => {
        const field=element('div',undefined,'study-field');
        const label=element('label',data.ui.selection+' '+(index+1));
        const select=element('select');select.id='compare-'+index;select.name='messenger-'+index;label.htmlFor=select.id;
        data.messengers.forEach(m=>{const option=element('option',m.name);option.value=m.id;select.append(option);});select.value=id;
        select.addEventListener('change',()=> {
          if(ids.includes(select.value)) {select.value=id;status.textContent=data.ui.duplicate;return;}
          ids[index]=select.value;render(true);document.getElementById('compare-'+index).focus();
        });
        const remove=element('button',data.ui.remove+' '+byId.get(id).name);remove.type='button';remove.disabled=ids.length<=2;
        remove.addEventListener('click',()=>{ids.splice(index,1);render(true);document.getElementById('compare-'+Math.min(index,ids.length-1)).focus();});
        field.append(label,select,remove);controls.append(field);
      });
      document.getElementById('add-messenger').disabled=ids.length>=4;
      renderComparison(ids);save(push);
      if(announce) status.textContent=data.ui.updated+' '+ids.map(id=>byId.get(id).name).join(', ')+'.';
    }
    document.getElementById('add-messenger').addEventListener('click',()=> {
      if(ids.length>=4)return;
      ids.push(data.messengers.find(m=>!ids.includes(m.id)).id);render(true);document.getElementById('compare-'+(ids.length-1)).focus();
    });
    window.addEventListener('popstate',()=>{ids=StudyDecision.normaliseSelection(new URL(location.href).searchParams.get('apps'),data.messengers).ids;render(false);});
    render(false,false);if(selection.corrected&&new URL(location.href).searchParams.has('apps'))status.textContent=data.ui.invalid;
    comparator.hidden=false;
  }
  const guide=document.getElementById('study-decision-form');
  if (guide) {
    const status=document.getElementById('guide-status'),error=document.getElementById('guide-error'),output=document.getElementById('guide-results');
    guide.hidden=false;
    guide.addEventListener('submit',event=> {
      event.preventDefault();error.textContent='';
      const priority=document.getElementById('choice-priority');priority.removeAttribute('aria-invalid');
      const result=StudyDecision.recommend(Object.fromEntries(new FormData(guide)),data);
      if(result.error){error.textContent=data.ui.choose_priority;priority.setAttribute('aria-invalid','true');priority.focus();output.replaceChildren();status.textContent='';return;}
      const nodes=[];
      if(result.globalWarning)nodes.push(element('p',data.ui.global,'scope-note'));
      const rule=data.rules.find(r=>r.id===result.ruleId);
      nodes.push(element('h2',data.ui.results),element('p',rule.reason));
      if(!result.candidates.length)nodes.push(element('p',data.ui.none));
      const list=element('ol');
      result.candidates.forEach(({id,conditional})=> {
        const m=byId.get(id),li=element('li');
        li.append(element('h3',m.name),element('p',data.ui.reason+': '+fact(m,'best')),element('p',fact(m,'weakness')),element('p',data.ui.configuration+': '+fact(m,'configuration')));
        const confidence=element('p',fieldMap.get('confidence').label+': '+fact(m,'confidence'));
        evidence(confidence,m.facts.confidence.sources,m.name+' / '+fieldMap.get('confidence').label);
        li.append(confidence);
        if(conditional)li.append(element('p',data.ui.conditional,'scope-note'));
        li.append(link(data.ui.profile,localeRoot+'messageries/'+id+'/'),' · ',link(data.ui.compare,localeRoot+'comparer/?apps='+id+','+(id==='signal'?'simplex':'signal')));
        list.append(li);
      });nodes.push(list,element('p',data.ui.confidence));output.replaceChildren(...nodes);
      status.textContent=data.ui.results+': '+result.candidates.map(c=>byId.get(c.id).name).join(', ')+(result.candidates.length?'.':data.ui.none);
    });
    guide.addEventListener('reset',()=> {
      output.replaceChildren();status.textContent='';error.textContent='';
      const priority=document.getElementById('choice-priority');priority.removeAttribute('aria-invalid');priority.focus();
    });
  }
})();
