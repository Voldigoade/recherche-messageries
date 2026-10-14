/* End-to-end verification, including source-independent layout and fallback checks. */
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {spawn}=require('node:child_process');
const {chromium}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const root=path.resolve(__dirname,'..');
const port=Number(process.env.STUDY_TEST_PORT || 8773);
const base=`http://127.0.0.1:${port}/recherche-messageries/`;
const python=process.env.STUDY_PYTHON || (process.platform==='win32'?path.join(root,'.venv/Scripts/python.exe'):'python');
const server=spawn(python,['scripts/serve_preview.py','--port',String(port)],{cwd:root,stdio:'ignore',windowsHide:true});
const report={responsive:[],interactions:[],accessibility:[],noJavaScript:[],errors:[]};
fs.mkdirSync(path.join(root,'.qa'),{recursive:true});
async function ready() {
  for(let i=0;i<50;i++){try{if((await fetch(base)).ok)return;}catch{} await new Promise(r=>setTimeout(r,100));}
  throw Error('Preview server did not start');
}
async function main() {
  await ready();
  const browser=await chromium.launch({headless:true});
  try {
    for(const lang of ['fr','en','es']) {
      const prefix=lang==='fr'?'':lang+'/';
      const context=await browser.newContext({viewport:{width:1440,height:900},reducedMotion:'reduce'});
      const page=await context.newPage();
      const consoleErrors=[];const offsite=[];
      page.on('pageerror',e=>consoleErrors.push(e.message));
      page.on('console',m=>{if(m.type()==='error')consoleErrors.push(m.text());});
      page.on('request',r=>{if(!r.url().startsWith('http://127.0.0.1:')&&!r.url().startsWith('data:'))offsite.push(r.url());});
      for(const width of [320,375,768,1024,1440]) {
        await page.setViewportSize({width,height:900});
        for(const route of ['', 'comparatif/', 'comparer/?apps=signal,simplex,olvid,threema', 'choisir/', 'messageries/signal/', 'threat-models/']) {
          await page.goto(base+prefix+route);await page.locator('article h1').waitFor();
          const dimensions=await page.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth,tables:[...document.querySelectorAll('.study-table')].filter(t=>t.getBoundingClientRect().width>0).map(t=>({width:t.getBoundingClientRect().width,scroll:t.scrollWidth}))}));
          assert.ok(dimensions.document<=width+1,`${lang} ${width} ${route}: document overflow ${JSON.stringify(dimensions)}`);
          assert.ok(dimensions.tables.every(t=>t.scroll<=t.width+2),`${lang} ${width} ${route}: ordinary table needs horizontal scroll`);
          report.responsive.push({lang,width,route});
        }
      }
      await page.setViewportSize({width:1440,height:900});
      await page.goto(base+prefix+'comparer/?apps=signal,simplex');
      await page.locator('#add-messenger').click();await page.locator('#add-messenger').click();
      assert.equal(await page.locator('#compare-selects select').count(),4);
      assert.equal(await page.locator('#add-messenger').isDisabled(),true);
      await page.locator('#compare-0').selectOption('briar');
      assert.ok(new URL(page.url()).searchParams.get('apps').startsWith('briar,'));
      await page.goBack();assert.equal(await page.locator('#compare-0').inputValue(),'signal');
      await page.locator('#compare-1').selectOption('signal');
      assert.equal(await page.locator('#compare-1').inputValue(),'simplex');
      assert.ok((await page.locator('#compare-status').innerText()).length>0);
      await page.locator('#compare-selects button').last().click();
      assert.equal(await page.locator('#compare-selects select').count(),3);
      await page.goto(base+prefix+'comparer/?apps=bad,signal,signal,simplex,olvid,threema,session');
      assert.equal(await page.locator('#compare-selects select').count(),4);
      assert.match(await page.locator('#compare-status').innerText(),/Paramètres|parameters|Parámetros/);
      await page.locator('#compare-0').focus();await page.keyboard.press('ArrowDown');await page.keyboard.press('Enter');
      const alternate=page.locator('.md-select__link').filter({hasText:lang==='en'?'Español':'English'}).first();
      assert.equal(new URL(await alternate.getAttribute('href')).searchParams.get('apps'),new URL(page.url()).searchParams.get('apps'));
      report.interactions.push({lang,flow:'Comparator: add/max4/change/history/duplicate/remove/invalid URL/native select'});
      await page.goto(base+prefix+'choisir/');
      await page.locator('#study-decision-form button[type=submit]').click();
      assert.equal(await page.locator('#choice-priority').getAttribute('aria-invalid'),'true');
      assert.equal(await page.evaluate(()=>document.activeElement.id),'choice-priority');
      await page.locator('#choice-priority').selectOption('pseudonymity');await page.locator('#choice-iphone').selectOption('yes');
      await page.locator('#choice-desktop').selectOption('yes');await page.locator('#choice-phone').selectOption('none');
      await page.locator('#study-decision-form button[type=submit]').click();
      assert.deepEqual(await page.locator('#guide-results h3').allTextContents(),['SimpleX','Threema','Olvid']);
      assert.equal(new URL(page.url()).search,'');
      assert.equal(await page.evaluate(()=>localStorage.length+sessionStorage.length),0);
      await page.locator('#choice-adversary').selectOption('global');await page.locator('#study-decision-form button[type=submit]').click();
      assert.match(await page.locator('#guide-results').innerText(),/global/);
      await page.locator('#choice-priority').selectOption('teams');await page.locator('#choice-adversary').selectOption('general');
      await page.locator('#study-decision-form button[type=submit]').click();assert.equal(await page.locator('#guide-results h3').count(),0);
      await page.locator('#study-decision-form button[type=reset]').click();assert.equal(await page.locator('#guide-results h3').count(),0);
      assert.equal(await page.evaluate(()=>document.activeElement.id),'choice-priority');
      report.interactions.push({lang,flow:'Chooser: invalid/focus/no-phone+iPhone/global/empty/reset/no persistence'});
      // Search must reach meaningful results in the selected language.
      await page.goto(base+prefix);
      // Material searches keyboard events; exercise the actual typing path.
      await page.locator('.md-search__input').pressSequentially('SimpleX', {delay:100});
      await page.waitForFunction(()=>document.querySelector('.md-search-result__meta')?.textContent.match(/\d/));
      assert.ok(await page.locator('.md-search-result__link').count()>0);
      await page.locator('.md-search__form button').click();assert.equal(await page.locator('.md-search__input').inputValue(),'');
      await page.locator('.md-search__input').pressSequentially('zzzzaucunresultat', {delay:30});
      await page.waitForFunction(()=>document.querySelector('.md-search-result__list').children.length===0);
      report.interactions.push({lang,flow:'Search: results/clear/empty'});
      for(const route of ['', 'choisir/', 'comparer/?apps=signal,simplex', 'concepts/e2ee/', 'messageries/session/']) {
        await page.goto(base+prefix+route);
        const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
        assert.deepEqual(result.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)})),[],`Accessibility ${lang} ${route}`);
        report.accessibility.push({lang,route,violations:0});
        await page.setViewportSize({width:375,height:844});
        const mobile=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
        assert.deepEqual(mobile.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})),[],`Mobile accessibility ${lang} ${route}`);
        report.accessibility.push({lang,route,width:375,violations:0});
        await page.setViewportSize({width:1440,height:900});
      }
      // Browser 200% zoom is modelled with equivalent reduced CSS viewport.
      await page.setViewportSize({width:720,height:450});await page.goto(base+prefix+'comparer/?apps=signal,simplex,olvid,threema');
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
      await page.evaluate(()=>document.querySelector('.study-table tbody td').append(document.createTextNode('long-unbroken-test-string-'.repeat(30))));
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Long comparison text must wrap');
      await page.emulateMedia({forcedColors:'active'});assert.ok(await page.locator('#add-messenger').isVisible());await page.emulateMedia({forcedColors:'none'});
      await page.setViewportSize({width:375,height:844});await page.goto(base+prefix);
      await page.locator('label.md-header__button[for="__drawer"]').focus();await page.keyboard.press('Enter');
      assert.equal(await page.locator('#__drawer').isChecked(),true);await page.keyboard.press('Escape');
      assert.equal(await page.locator('#__drawer').isChecked(),false);
      await page.goto(base+prefix+'threat-models/');
      const matrix=page.locator('.study-matrix').first();
      if(await matrix.count()) {
        const region=page.locator('.md-typeset__scrollwrap').filter({has:page.locator('.study-matrix')}).first();await region.focus();
        assert.equal(await region.getAttribute('tabindex'),'0');
        await page.keyboard.press('ArrowRight');
        await page.waitForFunction(()=>[...document.querySelectorAll('.md-typeset__scrollwrap')].some(e=>e.querySelector('.study-matrix')&&e.scrollLeft>0));
      }
      await page.goto(base+prefix);
      await page.screenshot({path:path.join(root,'.qa',`home-${lang}-375.png`),fullPage:false});
      await page.setViewportSize({width:1440,height:900});await page.screenshot({path:path.join(root,'.qa',`home-${lang}-1440.png`),fullPage:false});
      assert.deepEqual(consoleErrors,[],`Console errors ${lang}`);assert.deepEqual(offsite,[],`Unnecessary external resources ${lang}`);
      await context.close();
      const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:844}});
      const staticPage=await nojs.newPage();
      for(const route of ['', 'comparatif/', 'comparer/', 'choisir/', 'messageries/signal/', 'concepts/pseudonymity/', 'idees-recues/', 'threat-models/']) {
        await staticPage.goto(base+prefix+route);
        assert.ok((await staticPage.locator('article').innerText()).length>200,`${lang} ${route}: empty no-JS content`);
        assert.ok(await staticPage.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
        if(route==='comparer/')assert.ok(await staticPage.locator('.study-table').count()>=1);
        report.noJavaScript.push({lang,route});
      }await nojs.close();
    }
  } finally {await browser.close();}
}
main().then(()=>{fs.writeFileSync(path.join(root,'.qa/browser-report.json'),JSON.stringify(report,null,2));console.log(`PASS: ${report.responsive.length} responsive views, ${report.interactions.length} multilingual interaction flows, ${report.accessibility.length} WCAG audits, ${report.noJavaScript.length} no-JS views, zero external requests.`);}).catch(error=>{console.error(error);report.errors.push(String(error));fs.writeFileSync(path.join(root,'.qa/browser-report.json'),JSON.stringify(report,null,2));process.exitCode=1;}).finally(()=>server.kill());
