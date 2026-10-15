"""Generate the V2 reading layer from reviewed, source-linked data.

The canonical report and Phase 2 remain unchanged. No grades are computed.
"""
import html
import json
import posixpath
from pathlib import Path
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'data/messengers.json').read_text(encoding='utf-8'))
LEARNING = json.loads((ROOT / 'content/learning.json').read_text(encoding='utf-8'))
LANGS = ('fr', 'en', 'es')
REPO = 'https://github.com/Voldigoade/recherche-messageries'
E = html.escape
FIELDS = {f['id']: f for f in CATALOG['fields']}
CONCEPTS = {c['id']: c for c in LEARNING['concepts']}
BASIC = ['identifier', 'phone', 'e2ee', 'metadata', 'ip', 'devices', 'strength', 'weakness', 'best', 'confidence']
OVERVIEW = ['e2ee', 'metadata', 'identifier', 'network', 'ease', 'ios', 'android', 'windows', 'macos', 'linux', 'strength', 'weakness', 'best', 'confidence']


def tr(fr, en, es, lang):
    return dict(fr=fr, en=en, es=es)[lang]


def route(path):
    p = Path(path)
    return (p.parent.as_posix().strip('.') + '/' if p.name == 'index.md' else str(p.with_suffix('')).replace('\\', '/') + '/').lstrip('/')


def url(path, lang):
    return PREFIX + ('' if lang == 'fr' else lang + '/') + route(path)


def fr_url(path):
    return PREFIX + route(path)


def ref_html(refs, lang, context=''):
    label = tr('Source', 'Evidence', 'Fuente', lang)
    return ' '.join(f'<a class="fact-source" href="{REPO}/blob/main/research/{CATALOG["sources"][r]["file"]}#L{CATALOG["sources"][r]["start_line"]}" aria-label="{E(label + ": " + context + " — " + r)}">[{i}]</a>' for i, r in enumerate(refs, 1))


def value(item, key, lang):
    return item['facts'].get(key, {}).get('text', CATALOG['unknown'])[lang]


def fact_html(item, key, lang):
    fact = item['facts'].get(key)
    return E(value(item, key, lang)) + (' ' + ref_html(fact['sources'], lang, item['name'] + ' / ' + key) if fact else '')


def label_html(key, lang):
    field = FIELDS[key]
    text = E(field['label'][lang])
    if field['concept']:
        return f'<a href="{url("concepts/"+field["concept"]+".md", lang)}" title="{E(CONCEPTS[field["concept"]]["definition"][lang])}">{text}</a>'
    return text


def definitions(keys, lang):
    concepts = list(dict.fromkeys(FIELDS[k]['concept'] for k in keys if FIELDS[k]['concept']))
    return '<div class="context-help">' + ''.join(f'<details><summary>{E(CONCEPTS[c]["title"][lang])}</summary><p>{E(CONCEPTS[c]["definition"][lang])} <a href="{url("concepts/"+c+".md",lang)}">{tr("Comprendre", "Learn more", "Entender", lang)}</a></p></details>' for c in concepts) + '</div>'


def dl(item, keys, lang, overview=False):
    aliases = {'e2ee':tr('Sécurité / E2EE','Security / E2EE','Seguridad / E2EE',lang),'metadata':tr('Vie privée / métadonnées','Privacy / metadata','Privacidad / metadatos',lang),'identifier':tr('Pseudonymat / identité','Pseudonymity / identity','Seudonimato / identidad',lang)}
    return '<dl class="fact-list">' + ''.join(f'<div><dt>{E(aliases[k]) if overview and k in aliases else label_html(k,lang)}</dt><dd>{fact_html(item,k,lang)}</dd></div>' for k in keys) + '</dl>'


def table(items, keys, lang, orient='attributes'):
    if orient == 'products':
        head = ['<th scope="col">' + tr('Messagerie','Messenger','Mensajería',lang) + '</th>'] + [f'<th scope="col" data-label="{E(FIELDS[k]["label"][lang])}">{label_html(k,lang)}</th>' for k in keys]
        rows = [f'<tr><th scope="row"><a href="{url("messageries/"+m["id"]+".md",lang)}">{E(m["name"])}</a></th>' + ''.join(f'<td>{fact_html(m,k,lang)}</td>' for k in keys) + '</tr>' for m in items]
    else:
        head = ['<th scope="col">' + tr('Propriété','Property','Propiedad',lang) + '</th>'] + [f'<th scope="col">{E(m["name"])}</th>' for m in items]
        rows = [f'<tr><th scope="row">{label_html(k,lang)}</th>' + ''.join(f'<td>{fact_html(m,k,lang)}</td>' for m in items) + '</tr>' for k in keys]
    return '<table class="study-table"><thead><tr>' + ''.join(head) + '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'


def comparison(items, lang):
    advanced = [k for k in FIELDS if k not in BASIC]
    return table(items,BASIC,lang) + f'<details class="technical-details"><summary>{tr("Détails techniques : identité, clés, push, appareils, audits et preuves", "Technical details: identity, keys, push, devices, audits and evidence", "Detalles técnicos: identidad, claves, push, dispositivos, auditorías y pruebas", lang)}</summary>' + table(items,advanced,lang) + '</details>'


def note(lang):
    return '<p class="scope-note">' + tr('Rapport 1.0 · 14 octobre 2026. Pas de laboratoire réseau, de tests forensiques contrôlés ni de reproduction bit à bit des binaires. Inconnu reste Inconnu.', 'Report 1.0 · 14 October 2026. No network lab, controlled forensic testing or bit-for-bit reproduction of binaries. Unknown remains Unknown.', 'Informe 1.0 · 14 de octubre de 2026. Sin laboratorio de red, pruebas forenses controladas ni reproducción bit a bit de binarios. Desconocido sigue siendo Desconocido.',lang) + '</p>'


def evidence_note(lang, path='recherche/index.md'):
    return '<p>' + tr('Les preuves détaillées sont conservées dans le', 'The detailed evidence is maintained in the French', 'Las pruebas detalladas se conservan en el',lang) + f' <a href="{fr_url(path)}">' + tr('registre Phase 2 en français','Phase 2 register','registro Fase 2 en francés',lang) + '</a>. ' + tr('La traduction est une reformulation, pas une nouvelle preuve.','The translation is a restatement, not new evidence.','La traducción es una reformulación, no evidencia nueva.',lang) + '</p>'


def write(docs, path, lang, title, body, description=None, editorial='data/messengers.json'):
    p = Path(path)
    target = docs / (path if lang == 'fr' else str(p.with_name(p.stem + '.' + lang + p.suffix)))
    target.parent.mkdir(parents=True, exist_ok=True)
    meta = dict(title=title,description=description or title,generated_v2=True,editorial_source=editorial,search=dict(boost=3))
    body = body.replace('\n## ', '\n\n## ')
    target.write_text('---\n' + yaml.safe_dump(meta,allow_unicode=True,sort_keys=False) + '---\n\n# ' + title + '\n\n' + body.rstrip() + '\n',encoding='utf-8')


def ui_separator(lang):
    return ' : ' if lang == 'fr' else ': '


def paths_html(lang):
    paths = [
        (tr('Une recommandation (2 à 5 minutes)','A recommendation (2–5 minutes)','Una recomendación (2–5 minutos)',lang),'guide-rapide.md','choisir.md'),
        (tr('Comprendre la vie privée (10 à 20 minutes)','Understand privacy (10–20 minutes)','Entender la privacidad (10–20 minutes)',lang),'concepts/index.md','idees-recues.md'),
        (tr('Comparer deux applications','Compare two applications','Comparar dos aplicaciones',lang),'comparer.md','comparatif.md'),
        (tr('OPSEC et contacts pseudonymes','OPSEC and pseudonymous contacts','OPSEC y contactos seudónimos',lang),'opsec.md','usages.md'),
        (tr('Vérifier la recherche','Verify the research','Verificar la investigación',lang),'methodologie.md','audits.md'),
    ]
    return '<ol class="reading-paths">' + ''.join(f'<li><strong>{E(title)}</strong>{ui_separator(lang)}<a href="{url(a,lang)}">{E(page_name(a,lang))}</a> → <a href="{url(b,lang)}">{E(page_name(b,lang))}</a></li>' for title,a,b in paths) + '</ol>'


def page_name(path,lang):
    names = {'guide-rapide.md':('Guide rapide','Quick guide','Guía rápida'),'choisir.md':('Guide interactif','Decision guide','Guía interactiva'),'comparer.md':('Comparateur','Compare messengers','Comparador'),'comparatif.md':('Comparatif général','General comparison','Comparación general'),'concepts/index.md':('Concepts','Learn the concepts','Conceptos'),'idees-recues.md':('Idées reçues','Common misconceptions','Ideas equivocadas'),'opsec.md':('OPSEC','OPSEC','OPSEC'),'usages.md':('Par objectif','By use case','Por objetivo'),'methodologie.md':('Méthodologie','Methodology','Metodología'),'audits.md':('Audits','Audits','Auditorías'),'affaires.md':('Cas publics','Public legal evidence','Evidencia judicial pública'),'limites.md':('Limites','Limitations','Limitaciones'),'metadonnees.md':('Métadonnées','Metadata','Metadatos'),'threat-models.md':('Threat models','Threat models','Modelos de amenaza'),'resume.md':('Résumé','Summary','Resumen'),'parcours.md':('Parcours de lecture','Reading paths','Rutas de lectura'),'messageries/index.md':('Fiches','Messenger profiles','Fichas')}
    return names.get(path,('Documentation','Documentation','Documentación'))[LANGS.index(lang)]


def generate(docs, config, old_nav):
    global PREFIX
    PREFIX = urlparse(config['site_url']).path.rstrip('/') + '/'
    messages = CATALOG['messengers']
    by_id = {m['id']:m for m in messages}
    original_profiles = {m['id']:(docs / ('messageries/'+m['id']+'.md')).read_text(encoding='utf-8') for m in messages}
    for lang in LANGS:
        title = tr('Quelle messagerie utiliser ?','Which messenger should I use?','¿Qué mensajería debería usar?',lang)
        home = '<p><strong>' + tr('Il n’existe pas de messagerie universellement « la plus sûre ».','There is no universal “most secure messenger”.','No existe una mensajería universalmente «más segura».',lang) + '</strong> ' + tr('Le bon point de départ dépend de vos appareils, de ce que vous protégez et de votre adversaire.','The right starting point depends on your devices, what you protect and your adversary.','El punto de partida depende de sus dispositivos, qué protege y su adversario.',lang) + '</p>'
        home += '<nav class="study-actions" aria-label="' + tr('Commencer','Start here','Empezar',lang) + '">' + ''.join(f'<a href="{url(p,lang)}">{page_name(p,lang)}</a>' for p in ['choisir.md','comparer.md','guide-rapide.md']) + '</nav>' + note(lang)
        home += '\n## ' + tr('Comparer les principales solutions','Compare the main messengers','Comparar las principales mensajerías',lang) + '\n\n'
        home += '<p>' + tr('Ouvrez une ligne pour voir les propriétés et leurs limites. Les descriptions sont qualitatives ; aucune note n’est calculée.','Open a row to see properties and limits. Descriptions are qualitative; no grade is calculated.','Abra una fila para ver propiedades y límites. Las descripciones son cualitativas; no se calcula ninguna nota.',lang) + '</p>'
        for m in messages[:7]:
            home += f'<details class="messenger-overview"><summary><strong>{E(m["name"])}</strong><span>{E(value(m,"strength",lang))}</span><small>'+tr('Limite : ','Limit: ','Límite: ',lang)+E(value(m,'weakness',lang))+'</small></summary>' + dl(m,OVERVIEW,lang,overview=True) + f'<p><a href="{url("messageries/"+m["id"]+".md",lang)}">{tr("Lire la fiche", "Read profile", "Leer ficha",lang)}</a> · <a href="{url("comparer.md",lang)}?apps={m["id"]},'+ ('signal' if m['id']!='signal' else 'simplex') + '">' + tr('Comparer','Compare','Comparar',lang) + '</a></p></details>'
        home += '\n## ' + tr('Comprendre avant de choisir','Understand before choosing','Entender antes de elegir',lang) + '\n\n' + definitions(['e2ee','metadata','identifier','network'],lang)
        home += '\n## ' + tr('Choisir votre parcours','Choose a reading path','Elegir una ruta',lang) + '\n\n' + paths_html(lang)
        write(docs,'index.md',lang,title,home,title+' '+tr('Choix conditionnels, métadonnées, pseudonymat et sources.','Conditional choices, metadata, pseudonymity and evidence.','Elecciones condicionadas, metadatos, seudonimato y pruebas.',lang))
        write(docs,'parcours.md',lang,page_name('parcours.md',lang),paths_html(lang) + '\n\n' + evidence_note(lang))

        quick = '<p>' + tr('Commencez par votre besoin, puis vérifiez la réserve. Ce sont des points de départ, jamais des garanties.','Start with your need, then check the caveat. These are starting points, never guarantees.','Empiece por su necesidad y compruebe la reserva. Son puntos de partida, nunca garantías.',lang) + '</p>'
        quick += '<ul>' + ''.join(f'<li><strong>{E(by_id[id]["name"])}</strong>{ui_separator(lang)}{E(value(by_id[id],"best",lang))}<br>{E(value(by_id[id],"weakness",lang))} <a href="{url("messageries/"+id+".md",lang)}">{tr("Conditions", "Conditions", "Condiciones",lang)}</a></li>' for id in ['signal','simplex','olvid','threema']) + '</ul>'
        quick += '<p>' + tr('Session reste rétrogradé pour l’assurance élevée ; Cwtch et Briar n’ont pas de client iOS officiel établi ici.','Session remains downgraded for high assurance; Cwtch and Briar have no official iOS client established here.','Session sigue rebajado para alta garantía; no se establece cliente iOS oficial de Cwtch ni Briar.',lang) + '</p>'
        quick += f'<p><a href="{url("choisir.md",lang)}">{page_name("choisir.md",lang)}</a> · <a href="{url("usages.md",lang)}">{page_name("usages.md",lang)}</a></p>' + definitions(['phone','e2ee','network'],lang) + note(lang)
        write(docs,'guide-rapide.md',lang,page_name('guide-rapide.md',lang),quick)

        # Complete comparison is statically available in every language.
        general = '<p>' + tr('18 architectures, sans classement absolu. Cliquez sur une propriété pour sa définition, et sur les références pour les preuves.','18 architectures, without an absolute ranking. Follow property definitions and references for evidence.','18 arquitecturas, sin clasificación absoluta. Siga definiciones y referencias para consultar pruebas.',lang) + '</p>'
        general += f'<p><a href="{url("comparer.md",lang)}">{page_name("comparer.md",lang)}</a></p>' + table(messages,['e2ee','identifier','metadata','ip','weakness'],lang,'products') + evidence_note(lang)
        # Keep the canonical French section below the simpler new comparison.
        if lang=='fr':
            original=(docs/'comparatif.md').read_text(encoding='utf-8').split('\n# ',1)[1].split('\n',1)[1]
            general += '\n## Texte canonique intégral\n\n'+original
        write(docs,'comparatif.md',lang,page_name('comparatif.md',lang),general)

        # Concept pages use the same definitions as contextual disclosures.
        concept_index = '<p>' + tr('Chaque concept commence par une réponse simple, puis un exemple, ses limites et les sources.','Each concept starts with a simple answer, then an example, its limits and sources.','Cada concepto empieza con una respuesta sencilla, un ejemplo, sus límites y fuentes.',lang) + '</p><dl class="concept-index">'
        for concept in LEARNING['concepts']:
            concept_index += f'<dt><a href="{url("concepts/"+concept["id"]+".md",lang)}">{E(concept["title"][lang])}</a></dt><dd>{E(concept["definition"][lang])}</dd>'
            headings = [('definition',tr('Définition courte','Short definition','Definición breve',lang)),('example',tr('Exemple concret','Concrete example','Ejemplo concreto',lang)),('protects',tr('Ce que cela protège','What it protects','Qué protege',lang)),('not_protects',tr('Ce que cela ne protège pas','What it does not protect','Qué no protege',lang)),('why',tr('Pourquoi cela compte','Why it matters','Por qué importa',lang))]
            body='\n\n'.join('## '+heading+'\n\n'+concept[key][lang] for key,heading in headings)
            if concept['behaviour']: body+='\n\n## '+tr('Comportement d’une messagerie','Example messenger behaviour','Ejemplo de comportamiento',lang)+'\n\n'+concept['behaviour'][lang]
            body += '\n\n<details class="technical-details"><summary>'+tr('Détails techniques','Technical details','Detalles técnicos',lang)+'</summary><p>'+E(concept['technical'][lang])+'</p></details>\n\n## '+tr('Preuves et lecture associée','Evidence and related reading','Pruebas y lectura relacionada',lang)+'\n\n'+ref_html(concept['sources'],lang,concept['id'])+f'<p><a href="{url("idees-recues.md",lang)}">{page_name("idees-recues.md",lang)}</a> · <a href="{url("comparer.md",lang)}">{page_name("comparer.md",lang)}</a></p>'
            write(docs,'concepts/'+concept['id']+'.md',lang,concept['title'][lang],body,concept['definition'][lang],editorial='content/learning.json')
        write(docs,'concepts/index.md',lang,page_name('concepts/index.md',lang),concept_index+'</dl>',editorial='content/learning.json')
        misconceptions = ''
        for entry in LEARNING['misconceptions']:
            misconceptions += '\n## '+entry['title'][lang]+'\n\n'+entry['answer'][lang]+f'\n\n<a href="{url("concepts/"+entry["concept"]+".md",lang)}">{E(CONCEPTS[entry["concept"]]["title"][lang])}</a> · '+ref_html(entry['sources'],lang,entry['id'])+'\n'
        write(docs,'idees-recues.md',lang,page_name('idees-recues.md',lang),misconceptions,editorial='content/learning.json')

        for m in messages:
            body = dl(m,['best','avoid','strength','weakness','identifier','ios','android','windows','macos','linux','confidence'],lang)
            body += f'<p><a class="study-link" href="{url("comparer.md",lang)}?apps={m["id"]},'+('signal' if m['id']!='signal' else 'simplex')+'">'+tr('Comparer ','Compare ','Comparar ',lang)+E(m['name'])+'</a></p>'
            sections = [(['contact'],tr('Ce que votre contact apprend','What your contact learns','Qué aprende su contacto',lang)),(['provider'],tr('Ce que le fournisseur apprend','What the provider learns','Qué aprende el proveedor',lang)),(['isp','apple_google','legal'],tr('Autres observateurs','Other observers','Otros observadores',lang)),(['e2ee','pfs','pcs','verification'],tr('Chiffrement et clés','Encryption and keys','Cifrado y claves',lang)),(['metadata','global_id','username','push'],tr('Métadonnées et identité','Metadata and identity','Metadatos e identidad',lang)),(['ip','relay','calls','groups'],tr('Appels, IP et groupes','Calls, IP and groups','Llamadas, IP y grupos',lang)),(['devices','backups'],tr('Appareils et sauvegardes','Devices and backups','Dispositivos y copias',lang)),(['audits','source','weakness','legal'],tr('Audits, limites et cas publics','Audits, limitations and public cases','Auditorías, límites y casos públicos',lang)),(['configuration','unknowns'],tr('Configuration et inconnues','Configuration and unknowns','Configuración e incógnitas',lang))]
            for keys,title2 in sections: body+='\n## '+title2+'\n\n'+dl(m,keys,lang)
            body += '\n## '+tr('Comprendre les termes','Understand the terms','Entender los términos',lang)+'\n\n'+definitions(['e2ee','metadata','identifier','network'],lang)
            if lang=='fr':
                original=original_profiles[m['id']].split('\n# ',1)[1].split('\n',1)[1]
                body+='\n## Conclusion canonique et matrice de référence\n\n'+original
            else: body+=evidence_note(lang,'messageries/'+m['id']+'.md')
            write(docs,'messageries/'+m['id']+'.md',lang,m['name'],body,tr('Fiche de référence : ','Reference profile: ','Ficha de referencia: ',lang)+m['name']+'. '+value(m,'weakness',lang))
        index = '<ul>'+''.join(f'<li><a href="{url("messageries/"+m["id"]+".md",lang)}">{m["name"]}</a>{ui_separator(lang)}{E(value(m,"best",lang))}</li>' for m in messages)+'</ul>'
        write(docs,'messageries/index.md',lang,page_name('messageries/index.md',lang),index)

        # A rules-backed, accessible guide with no answer persistence.
        ui = ui_strings(lang)
        projection = dict(lang=lang,root=PREFIX,ui=ui,unknown=CATALOG['unknown'][lang],fields=[dict(id=k,label=v['label'][lang],concept=v['concept']) for k,v in FIELDS.items()],messengers=[dict(id=m['id'],name=m['name'],facts={k:dict(text=f['text'][lang],sources=f['sources']) for k,f in m['facts'].items()},constraints=m['constraints']) for m in messages],rules=[dict(id=r['id'],candidates=r['candidates'],reason=r['reason'][lang]) for r in CATALOG['decision_rules']],sources=CATALOG['sources'],basic=BASIC)
        payload='<script id="study-data" type="application/json">'+json.dumps(projection,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+'</script>'
        form='<form id="study-decision-form" class="interactive-only study-form" hidden novalidate><fieldset><legend>'+ui['questions']+'</legend>'
        for key,label,options in questions(lang):
            form+=f'<div class="study-field"><label for="choice-{key}">{E(label)}</label><select id="choice-{key}" name="{key}" aria-describedby="guide-error">'+''.join(f'<option value="{val}">{E(text)}</option>' for val,text in options)+'</select></div>'
        form+='</fieldset><p id="guide-error" class="form-error" role="status"></p><div class="form-actions"><button type="submit">'+ui['show']+'</button><button type="reset">'+ui['reset']+'</button></div></form><p id="guide-status" role="status" aria-live="polite"></p><section id="guide-results" aria-label="'+ui['results']+'"></section>'
        chooser='<p>'+ui['intro']+'</p>'+form+'<noscript><p>'+ui['nojs']+'</p></noscript>'+payload
        chooser+='\n## '+ui['not_protected']+'\n\n'+unprotected(lang)+'\n\n## '+ui['rules_title']+'\n\n'+rules_html(lang)+note(lang)
        write(docs,'choisir.md',lang,page_name('choisir.md',lang),chooser)
        compare='<p>'+ui['compare_intro']+'</p><form id="messenger-comparator" class="interactive-only study-form" hidden novalidate><fieldset><legend>'+ui['selection']+'</legend><div id="compare-selects"></div><button type="button" id="add-messenger">'+ui['add']+'</button><p>'+ui['maximum']+'</p></fieldset></form><p id="compare-status" role="status" aria-live="polite"></p><div id="comparison-results">'+comparison([by_id['signal'],by_id['simplex']],lang)+'</div><noscript><p>'+ui['compare_nojs']+'</p></noscript>'+payload
        pairs=[('signal','simplex'),('signal','threema'),('simplex','session'),('olvid','threema'),('cwtch','briar'),('signal','whatsapp'),('telegram','signal')]
        pair_links=[]
        for a,b in pairs:
            pair_path=f'comparaisons/{a}-vs-{b}.md'
            pair_title=by_id[a]['name']+' vs '+by_id[b]['name']
            pair_links.append(f'<li><a href="{url(pair_path,lang)}">{pair_title}</a></li>')
            write(docs,pair_path,lang,pair_title,'<p>'+ui['compare_intro']+'</p>'+comparison([by_id[a],by_id[b]],lang)+f'<p><a href="{url("comparer.md",lang)}?apps={a},{b}">'+ui['customise']+'</a></p>'+unprotected(lang),pair_title+': '+tr('identité, E2EE, métadonnées, appels, plateformes et limites.','identity, E2EE, metadata, calls, platforms and limits.','identidad, E2EE, metadatos, llamadas, plataformas y límites.',lang))
        compare+='\n## '+tr('Comparaisons rapides','Quick comparisons','Comparaciones rápidas',lang)+'\n\n<ul>'+''.join(pair_links)+'</ul>\n\n'+definitions(['e2ee','identifier','metadata','network'],lang)+note(lang)
        write(docs,'comparer.md',lang,page_name('comparer.md',lang),compare)
        cases_html=''
        for case in use_cases(lang):
            cases_html+='\n## '+case['title']+'\n\n'+ '<p>'+case['reason']+'</p>'
            cases_html += '<ol>'+''.join(f'<li><a href="{url("messageries/"+id+".md",lang)}">{by_id[id]["name"]}</a>{ui_separator(lang)}{E(value(by_id[id],"weakness",lang))}<br><strong>'+tr('Conditions : ','Conditions: ','Condiciones: ',lang)+'</strong>'+E(value(by_id[id],'configuration',lang))+'</li>' for id in case['candidates'])+'</ol>'
            cases_html+='<p><strong>'+tr('Confiance : ','Confidence: ','Confianza: ',lang)+'</strong>'+ui['confidence']+'</p>'+ref_html(['report.uses','report.threats'],lang,case['title'])
        # Preserve the canonical use-case tables and Signal configuration in French.
        if lang=='fr': cases_html+='\n## Analyse canonique intégrale\n\n'+(docs/'usages.md').read_text(encoding='utf-8').split('\n# ',1)[1].split('\n',1)[1]
        write(docs,'usages.md',lang,tr('Les messageries par objectif','Best messengers by use case','Mensajerías por objetivo',lang),cases_html)
        if lang!='fr': generate_research_summaries(docs,lang)

    common = ['guide-rapide.md','choisir.md','comparer.md','usages.md','parcours.md','concepts/index.md','idees-recues.md','messageries/index.md','resume.md','methodologie.md','threat-models.md','metadonnees.md','opsec.md','audits.md','affaires.md','limites.md']
    def navigation(lang):
        return [{tr('Accueil','Home','Inicio',lang):'index.md'}, {tr('Choisir et comparer','Choose and compare','Elegir y comparar',lang):[{page_name(p,lang):p} for p in common[:5]]}, {tr('Comprendre','Learn','Aprender',lang):[{page_name(p,lang):p} for p in common[5:7]]}, {tr('Messageries','Messengers','Mensajerías',lang):[{page_name('messageries/index.md',lang):'messageries/index.md'}]+[{m['name']:'messageries/'+m['id']+'.md'} for m in messages[:7]]+[{tr('Autres solutions','Other messengers','Otras mensajerías',lang):[{m['name']:'messageries/'+m['id']+'.md'} for m in messages[7:]]}]}, {tr('Vérifier et approfondir','Verify and go deeper','Verificar y profundizar',lang):[{page_name(p,lang):p} for p in common[8:]]}]
    frnav=navigation('fr')
    frnav[-1]['Vérifier et approfondir'] += [{"Plateformes":'compatibilite.md'},{"Comment lire les preuves":'lecture.md'},{"Sources":'sources.md'},{"Disponibilité des références":'disponibilite-sources.md'},{"Discord → messagerie privée":'discord-migration.md'}]
    # Keep every research page navigable inside collapsed evidence groups.
    frnav += [old_nav[-2],old_nav[-1]]
    for lang in LANGS:
        pairnav=[{by_id[a]['name']+' vs '+by_id[b]['name']:f'comparaisons/{a}-vs-{b}.md'} for a,b in pairs]
        conceptnav=[{c['title'][lang]:'concepts/'+c['id']+'.md'} for c in LEARNING['concepts']]
        nav=frnav if lang=='fr' else navigation(lang)
        nav[1][next(iter(nav[1]))].append({page_name('comparatif.md',lang):'comparatif.md'})
        nav[1][next(iter(nav[1]))].append({tr('Comparaisons dédiées','Dedicated comparisons','Comparaciones específicas',lang):pairnav})
        nav[2][next(iter(nav[2]))].append({tr('Tous les concepts','All concepts','Todos los conceptos',lang):conceptnav})
        if lang=='fr': config['nav']=nav
        else:
            for plugin in config['plugins']:
                if isinstance(plugin,dict) and 'i18n' in plugin:
                    for language in plugin['i18n']['languages']:
                        if language['locale']==lang: language['nav']=nav
    config['not_in_nav']=''
    config['extra_javascript']=['javascripts/tables.js','javascripts/decision.js','javascripts/tools.js']


def ui_strings(lang):
    strings={
    'questions':('Vos besoins','Your needs','Sus necesidades'),
    'show':('Voir les points de départ','Show starting points','Ver puntos de partida'),
    'reset':('Recommencer','Reset','Reiniciar'),
    'results':('Points de départ recommandés','Recommended starting points','Puntos de partida recomendados'),
    'intro':('Ce guide traduit les conclusions du rapport, sans score ni garantie. Répondez seulement aux questions que vous comprenez. Rien n’est envoyé ni conservé.','This guide translates the report’s conclusions without scores or guarantees. Answer the questions you understand. Nothing is sent or stored.','Esta guía traduce las conclusiones sin notas ni garantías. Responda lo que entienda. Nada se envía ni se almacena.'),
    'nojs':('Sans JavaScript, les règles ci-dessous et le guide rapide restent lisibles.','Without JavaScript, the rules below and quick guide remain readable.','Sin JavaScript, las reglas y la guía rápida siguen legibles.'),
    'not_protected':('Ce que ces recommandations ne protègent pas','What these recommendations do NOT protect you from','Lo que estas recomendaciones NO protegen'),
    'rules_title':('Règles de décision et sources','Decision rules and evidence','Reglas de decisión y fuentes'),
    'compare_intro':('Choisissez deux à quatre messageries. Chaque propriété vient du même catalogue traçable ; les inconnues restent explicites.','Choose two to four messengers. Every property comes from the same traceable catalogue; unknowns remain explicit.','Elija de dos a cuatro mensajerías. Cada propiedad viene del mismo catálogo trazable; las incógnitas siguen explícitas.'),
    'selection':('Applications à comparer','Messengers to compare','Mensajerías a comparar'),
    'add':('Ajouter une messagerie','Add messenger','Añadir mensajería'),
    'remove':('Retirer','Remove','Quitar'),
    'maximum':('Deux à quatre applications distinctes.','Two to four distinct applications.','De dos a cuatro aplicaciones distintas.'),
    'compare_nojs':('Sans JavaScript, cette comparaison Signal / SimpleX et les comparaisons dédiées restent disponibles.','Without JavaScript, this Signal / SimpleX comparison and dedicated comparisons remain available.','Sin JavaScript, esta comparación Signal / SimpleX y las específicas siguen disponibles.'),
    'customise':('Personnaliser cette comparaison','Customise this comparison','Personalizar esta comparación'),
    'confidence':('Moyenne pour les propriétés bien documentées ; plus faible pour les métadonnées de production et les versions non testées.','Medium for well-documented properties; lower for production metadata and untested versions.','Media para propiedades bien documentadas; menor para metadatos de producción y versiones no probadas.'),
    'choose_priority':('Choisissez une priorité pour afficher une recommandation.','Choose a priority to show recommendations.','Elija una prioridad para mostrar recomendaciones.'),
    'none':('Aucun point de départ de cette règle ne satisfait toutes les contraintes. Revoyez une contrainte ou lisez les fiches ; aucun candidat incompatible n’est ajouté.','No starting point from this rule satisfies all constraints. Revisit a constraint or read the profiles; no incompatible candidate is added.','Ningún punto de partida de esta regla cumple todas las restricciones. Revise una o lea las fichas; no se añade ningún candidato incompatible.'),
    'global':('Aucune application ne démontre une résistance générale à un observateur passif global. Ces options ne concernent que des observateurs limités.','No application demonstrates general resistance to a global passive observer. These options address limited observers only.','Ninguna aplicación demuestra resistencia general a un observador pasivo global. Estas opciones solo tratan observadores limitados.'),
    'conditional':('Vérification de compatibilité / configuration requise.','Compatibility / configuration needs verification.','Hay que verificar compatibilidad / configuración.'),
    'updated':('Comparaison mise à jour.','Comparison updated.','Comparación actualizada.'),
    'invalid':('Paramètres invalides ou trop nombreux : comparaison normalisée à deux à quatre applications connues.','Invalid or excessive parameters: comparison normalised to two to four known messengers.','Parámetros inválidos o excesivos: comparación normalizada a dos a cuatro mensajerías conocidas.'),
    'duplicate':('Cette application est déjà sélectionnée.','This messenger is already selected.','Esta mensajería ya está seleccionada.'),
    'property':('Propriété','Property','Propiedad'),
    'details':('Détails techniques : identité, clés, push, appareils, audits et preuves','Technical details: identity, keys, push, devices, audits and evidence','Detalles técnicos: identidad, claves, push, dispositivos, auditorías y pruebas'),
    'evidence':('Preuve','Evidence','Prueba'),
    'profile':('Lire la fiche','Read profile','Leer ficha'),
    'compare':('Comparer','Compare','Comparar'),
    'configuration':('Configuration','Configuration','Configuración'),
    'reason':('Pourquoi','Why','Por qué'),
    }
    return {k:v[LANGS.index(lang)] for k,v in strings.items()}


def questions(lang):
    yes=tr('Oui','Yes','Sí',lang);no=tr('Non','No','No',lang);unsure=tr('Je ne sais pas','Not sure','No lo sé',lang)
    return [
    ('priority',tr('Votre priorité','Your priority','Su prioridad',lang),[('',unsure),('daily',tr('Sécurité quotidienne','Everyday security','Seguridad diaria',lang)),('pseudonymity',tr('Pseudonymat','Pseudonymity','Seudonimato',lang)),('metadata',tr('Minimisation des métadonnées','Metadata minimisation','Minimizar metadatos',lang)),('network',tr('Anonymat réseau','Network anonymity','Anonimato de red',lang)),('ease',tr('Facilité d’usage','Ease of use','Facilidad de uso',lang)),('teams',tr('Équipes / serveur choisi','Teams / chosen server','Equipos / servidor elegido',lang))]),
    ('iphone',tr('Utilisez-vous iPhone ?','Do you use iPhone?','¿Usa iPhone?',lang),[('either',unsure),('yes',yes),('no',no)]),
    ('desktop',tr('Avez-vous besoin d’un PC ?','Do you need a desktop client?','¿Necesita un cliente de PC?',lang),[('no',no),('yes',yes)]),
    ('phone',tr('Votre numéro','Your phone number','Su número de teléfono',lang),[('okay',tr('Je peux le fournir au service','I can provide it to the service','Puedo facilitarlo al servicio',lang)),('peer',tr('Le cacher au correspondant','Hide it from the contact','Ocultarlo al contacto',lang)),('none',tr('Ne pas le donner même au service','Not give it even to the service','No darlo ni al servicio',lang))]),
    ('calls',tr('Avez-vous besoin d’appels ?','Do you need calls?','¿Necesita llamadas?',lang),[('no',no),('yes',yes)]),
    ('hide_ip',tr('Cacher votre IP au correspondant importe-t-il ?','Is hiding your IP from the contact important?','¿Importa ocultar su IP al contacto?',lang),[('no',no),('yes',yes)]),
    ('adversary',tr('Votre adversaire principal','Your main adversary','Su adversario principal',lang),[('general',unsure),('contact',tr('Contact malveillant','Malicious contact','Contacto malicioso',lang)),('provider',tr('Fournisseur','Provider','Proveedor',lang)),('isp',tr('FAI / Wi-Fi','ISP / Wi-Fi','ISP / Wi-Fi',lang)),('legal',tr('Enquête judiciaire','Legal investigation','Investigación judicial',lang)),('osint',tr('OSINT / doxxing','OSINT / doxxing','OSINT / doxxing',lang)),('censorship',tr('Censure','Censorship','Censura',lang)),('global',tr('Surveillance réseau globale','Global network surveillance','Vigilancia global de red',lang))])]


def rules_html(lang):
    by_id={m['id']:m for m in CATALOG['messengers']}
    labels={key:dict(options).get(key,key) for _,_,options in questions(lang) for key,_ in options}
    labels['contact']=tr('Contact malveillant','Malicious contact','Contacto malicioso',lang)
    labels['legal']=tr('Demandes judiciaires','Legal requests','Solicitudes judiciales',lang)
    return '<dl>'+''.join(f'<dt><strong>{E(labels.get(r["id"],r["id"]))}</strong></dt><dd>{E(r["reason"][lang])}<br>'+', '.join(E(by_id[id]['name']) for id in r['candidates'])+' '+ref_html(r['sources'],lang,r['id'])+'</dd>' for r in CATALOG['decision_rules'])+'</dl><p><a href="'+REPO+'/blob/main/data/messengers.json">data/messengers.json</a> · <a href="'+REPO+'/blob/main/docs/javascripts/decision.js">decision.js</a></p>'


def unprotected(lang):
    return '<ul>'+''.join('<li>'+text+'</li>' for text in [tr('Terminal compromis / déverrouillé et spyware.','Compromised / unlocked device and spyware.','Dispositivo comprometido / desbloqueado y spyware.',lang),tr('Copie, capture ou divulgation par le correspondant.','Copying, screenshots or disclosure by the contact.','Copias, capturas o divulgación por el contacto.',lang),tr('Traces Discord initiales, réutilisation de pseudo, avatar, voix ou fichiers.','Initial Discord traces, reused alias, avatar, voice or files.','Rastros iniciales de Discord, alias, avatar, voz o archivos reutilizados.',lang),tr('Corrélation globale ; données des relais, FAI, télécom, stores et sauvegardes selon le chemin.','Global correlation; relay, ISP, telecom, store and backup data depending on the path.','Correlación global; datos de relés, ISP, operador, tiendas y copias según la ruta.',lang)])+'</ul>'


def use_cases(lang):
    names=[('daily',('Sécurité quotidienne','Everyday secure messaging','Mensajería segura diaria')),('pseudonymity',('Contacts pseudonymes inconnus','Pseudonymous strangers','Desconocidos seudónimos')),('no-phone',('Sans numéro fourni au service','Without a phone number at the service','Sin número al servicio')),('iphone-pc',('iPhone + PC','iPhone + PC','iPhone + PC')),('contact',('Contact malveillant','Malicious contacts','Contactos maliciosos')),('metadata',('Minimiser les métadonnées','Metadata minimisation','Minimizar metadatos')),('network',('Anonymat réseau limité','Limited network anonymity','Anonimato limitado de red')),('censorship',('Résistance à la censure','Censorship resistance','Resistencia a censura')),('ease',('Maturité et adoption','Mature usability and adoption','Madurez y adopción')),('teams',('Équipes / auto-hébergement','Teams / self-hosting','Equipos / alojamiento propio'))]
    rules={r['id']:r for r in CATALOG['decision_rules']}
    result=[]
    for id,titles in names:
        rule=rules['pseudonymity' if id=='no-phone' else 'daily' if id=='iphone-pc' else id]
        candidates=rule['candidates'][:3]
        if id=='no-phone':candidates=['simplex','threema','olvid']
        if id=='iphone-pc':candidates=['signal','simplex','olvid','threema']
        result.append(dict(title=titles[LANGS.index(lang)],reason=rule['reason'][lang],candidates=candidates))
    return result


def generate_research_summaries(docs,lang):
    """Careful translations of first-order findings; full evidence stays French."""
    methodology=tr('', 'This is independent documentary research, not a security certification. Sources include specifications, public code, audits, academic papers, advisories, transparency reports and public legal records. Vendor statements are distinguished from independent evidence and explicit inference.\n\nThe conclusions are dated **14 October 2026**, report **1.0**. They do not automatically apply to other platforms, versions or settings. Limited passive DNS/BGP observations and source-manifest samples are not a production infrastructure audit.\n\n**Not performed:** a comparative network laboratory, controlled forensic acquisition of current phones, complete current APK/IPA inspection, or bit-for-bit reproduction of distributed binaries. No port scanning or unauthorised access was performed.\n\nConfidence is medium for well-documented protocol properties and explicitly published legal results, and low to medium for production metadata, version-specific calling, distributed builds, contemporary mobile forensics and censorship. **Unknown remains Unknown.**', 'Investigación documental independiente, no certificación de seguridad. Las fuentes incluyen especificaciones, código público, auditorías, artículos académicos, avisos, transparencia y documentos judiciales públicos. Se distinguen declaraciones del proveedor, evidencia independiente e inferencias explícitas.\n\nConclusiones fechadas el **14 de octubre de 2026**, informe **1.0**. No se trasladan automáticamente a otras plataformas, versiones o ajustes. Observaciones pasivas limitadas de DNS/BGP y muestras de manifests no son una auditoría de producción.\n\n**No realizado:** laboratorio comparativo de red, adquisición forense controlada de móviles actuales, inspección completa de APK/IPA ni reproducción bit a bit de binarios distribuidos. No hubo escaneo de puertos ni acceso no autorizado.\n\nConfianza media para propiedades protocolarias bien documentadas y resultados judiciales publicados; baja a media para metadatos de producción, llamadas por versión, binarios, forense móvil y censura. **Desconocido sigue siendo Desconocido.**',lang)
    write(docs,'methodologie.md',lang,page_name('methodologie.md',lang),methodology+'\n\n'+ref_html(['report.methodology'],lang)+evidence_note(lang,'methodologie.md'))
    limitations='<p>'+ui_strings(lang)['confidence']+'</p>'+unprotected(lang)+'<p>'+tr('', 'High-impact unknowns include Session fixes and independent retests, exact mobile push payloads, relay logging, Threema desktop PFS and retests, current distributed binaries, and forensic results pinned to device, OS, app version and locked state. A historical extraction cannot be assumed to work after a documented fix.', 'Entre las incógnitas importantes están correcciones y retests de Session, payloads push móviles exactos, logs de relés, PFS y retests del escritorio Threema, binarios actuales y resultados forenses con dispositivo, sistema, app y bloqueo precisos. Una extracción histórica no se presupone efectiva tras una corrección documentada.',lang)+'</p>'+ref_html(['report.limits'],lang)+evidence_note(lang,'limites.md')
    write(docs,'limites.md',lang,page_name('limites.md',lang),limitations)
    metadata='<p>'+CONCEPTS['metadata']['definition'][lang]+'</p>'+definitions(['metadata','e2ee','phone','network'],lang)+table(CATALOG['messengers'],['provider','contact','isp','apple_google','legal'],lang,'products')+evidence_note(lang,'metadonnees.md')
    write(docs,'metadonnees.md',lang,page_name('metadonnees.md',lang),metadata)
    threats=[('Curious provider','Proveedor curioso'),('Compromised infrastructure','Infraestructura comprometida'),('Malicious operator','Operador malicioso'),('ISP / Wi-Fi / LAN','ISP / Wi-Fi / LAN'),('Multipoint passive observer','Observador pasivo multipunto'),('Global passive adversary','Adversario pasivo global'),('Malicious contact','Contacto malicioso'),('Harassment / OSINT doxxing','Acoso / doxxing OSINT'),('Ordinary legal request','Solicitud judicial ordinaria'),('Sophisticated multisource investigation','Investigación sofisticada con varias fuentes'),('Locked device','Dispositivo bloqueado'),('Unlocked device','Dispositivo desbloqueado'),('Spyware / controlled endpoint','Spyware / dispositivo controlado'),('Supply-chain compromise','Compromiso de cadena de suministro'),('State censorship','Censura estatal')]
    body='<p>'+CONCEPTS['threat-model']['definition'][lang]+'</p><ol>'+''.join('<li>TM'+str(i)+' — '+pair[0 if lang=='en' else 1]+'</li>' for i,pair in enumerate(threats,1))+'</ol><p>'+tr('', 'The matrix is qualitative and configuration-dependent. Strong, partial, exposed, weak and unknown are relative assessments, not absolute grades. Unknown is not a negative score. No general global-passive resistance is established; an unlocked or controlled endpoint is a different threat from a provider request.', 'La matriz es cualitativa y depende de configuración. Fuerte, parcial, expuesta, débil y desconocida son valoraciones relativas, no notas absolutas. Desconocido no es negativo. No se establece resistencia general al observador global; un dispositivo desbloqueado o controlado es distinto de una solicitud al proveedor.',lang)+'</p>'+evidence_note(lang,'threat-models.md')+ref_html(['report.threats'],lang)
    write(docs,'threat-models.md',lang,page_name('threat-models.md',lang),body)
    opsec='<p>'+tr('', 'Protect devices, identities and files before changing the messenger. Use current OS/app versions, a strong lock, controlled backups, hidden notification previews and only your own linked devices. A disappearing message cannot prevent a recipient from copying it.', 'Proteja dispositivos, identidades y archivos antes de cambiar de mensajería. Use sistemas y apps actualizados, bloqueo robusto, copias controladas, vistas previas ocultas y solo sus dispositivos vinculados. Un mensaje temporal no impide que el destinatario lo copie.',lang)+'</p><p>'+tr('', 'Do not reuse aliases, avatars, signatures or cloud accounts. Inspect photo/document metadata, authors, filenames and thumbnails. Consider voice, language and schedules. VPN/Tor move an observer; verify the actual path instead of assuming protection.', 'No reutilice alias, avatares, firmas ni cuentas cloud. Inspeccione metadatos de fotos/documentos, autores, nombres y miniaturas. Considere voz, lenguaje y horarios. VPN/Tor desplazan un observador; compruebe la ruta real.',lang)+'</p>'
    for m in CATALOG['messengers'][:7]: opsec+='\n## '+m['name']+'\n\n'+dl(m,['configuration','weakness','devices','ip'],lang)
    write(docs,'opsec.md',lang,page_name('opsec.md',lang),opsec+ref_html(['report.opsec'],lang)+evidence_note(lang,'opsec.md'))
    audits='<p>'+tr('', 'An audit is limited by its date, version, commits, components and exclusions. Corrections and retests must be distinguished from initial findings. Public source code is not proof that installed binaries match it. An advisory about availability is not automatically a break of content encryption.', 'Una auditoría está limitada por fecha, versión, commits, componentes y exclusiones. Distinguir correcciones y retests de hallazgos iniciales. Código público no prueba que el binario instalado corresponda. Un aviso sobre disponibilidad no implica automáticamente romper el cifrado.',lang)+'</p>'+table(CATALOG['messengers'][:7],['audits','weakness'],lang,'products')
    audits+='<p>'+tr('', 'Wire iOS CVE-2026-35049 affected clients before 4.16.0 and described crashes / loops from malformed Proteus data, with a fix reported in 4.16.0. Discord DAVE audits concern eligible audio/video, not text. Delta Chat audits have distinct Webxdc, client and SecureJoin/Autocrypt scopes. WhatsApp Private Processing audits do not audit the entire messenger.', 'Wire iOS CVE-2026-35049 afectó clientes anteriores a 4.16.0 y describió fallos / bucles por datos Proteus malformados, con corrección declarada en 4.16.0. Auditorías DAVE de Discord tratan audio/vídeo compatible, no texto. Delta Chat tiene ámbitos Webxdc, cliente y SecureJoin/Autocrypt distintos. Auditar Private Processing de WhatsApp no audita toda la mensajería.',lang)+'</p>'+ref_html(['report.audits'],lang)+evidence_note(lang,'audits.md')
    write(docs,'audits.md',lang,page_name('audits.md',lang),audits)
    legal='<p>'+tr('', 'A provider’s capability, its policy, an aggregate transparency report and an actual case are different evidence. Data from phones, witnesses, telecom, stores and relays must not be attributed to the messenger provider without proof. Absence of a public case is not proof of absence. This research is not legal advice.', 'Capacidad del proveedor, política, transparencia agregada y caso concreto son pruebas distintas. Datos de teléfonos, testigos, operador, tiendas y relés no se atribuyen al proveedor sin prueba. Ausencia de caso público no prueba ausencia. No es asesoramiento jurídico.',lang)+'</p>'+table([m for m in CATALOG['messengers'] if m['id'] in ['signal','simplex','threema','telegram','discord','wire','matrix-element']],['legal'],lang,'products')+ref_html(['report.legal'],lang)+evidence_note(lang,'affaires.md')
    write(docs,'affaires.md',lang,page_name('affaires.md',lang),legal)
