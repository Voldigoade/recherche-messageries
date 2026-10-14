"""Build the documentation from the two authoritative research files.

No technical claim is generated. Sections are extracted verbatim; the editorial
transformations (headings, link destinations and table transposition) are explicit.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

import yaml
from build_experience import generate as generate_experience

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO = "https://github.com/Voldigoade/recherche-messageries"
FINAL = "rapport-final-messageries.md"
PHASE = "enquete-messageries-progress.md"
manifest = []
phase_anchor_pages = {}


def slug(text):
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", plain).strip("-")


def parts(text, level):
    matches = list(re.finditer(rf"^{'#' * level} (.+)$", text, re.M))
    return [(m.group(1), m.start(), matches[i + 1].start() if i + 1 < len(matches) else len(text))
            for i, m in enumerate(matches)]


def repair_links(body, destination):
    """Only replace references to local documents missing from the supplied corpus."""
    prefix = "../" * (len(Path(destination).parts) - 1)
    body = re.sub(r"\[([^\]]+)\]\(enquete-messageries-progress\.md\)",
                  lambda m: f"[{m[1]}]({prefix}recherche/index.md)", body)
    body = re.sub(r"\[([^\]]+)\]\(enquete-messageries-phase3\.md\)",
                  lambda m: f"{m[1]} (archive historique non fournie)", body)
    body = re.sub(r"\[([^\]]+)\]\(rapport-final-messageries\.md\)",
                  lambda m: f"[{m[1]}]({prefix}resume.md)", body)
    if destination.startswith("recherche/"):
        def phase_anchor(match):
            key = slug(match[2])
            if key in phase_anchor_pages:
                target = Path(phase_anchor_pages[key]).name
                return f"[{match[1]}]({target})"
            return match[0]
        body = re.sub(r"\[([^\]]+)\]\(#([^\)]+)\)", phase_anchor, body)
    return body


def page(path, title, body, description, source=None, start=None, end=None, historical=False):
    meta = {"title": title, "description": description, "search": {"boost": 0.5 if source == PHASE else 2}}
    if source:
        meta["source_file"] = source
        meta["source_line"] = start
        manifest.append({"page": path, "source": source, "start_line": start, "end_line": end})
    out = DOCS / path
    out.parent.mkdir(parents=True, exist_ok=True)
    note = ""
    if source == PHASE:
        note = ('!!! note "Registre de preuves — Phase 2"\n'
                '    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) '
                'est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 '
                'restent historiques. `UNKNOWN` reste `UNKNOWN`.\n\n')
    if historical:
        note += ('!!! warning "Synthèse historique"\n'
                 '    Cette synthèse antérieure est conservée pour la traçabilité. '
                 'Consulter le [résumé actuel](../resume.md) pour les conclusions de référence.\n\n')
    body = repair_links(body, path)
    out.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n# " + title + "\n\n" + note + body.strip() + "\n", encoding="utf-8")


def extract(path, title, text, a, b, source, description, level=2, historical=False):
    chunk = text[a:b]
    body = chunk.split("\n", 1)[1]
    if level == 2:
        body = re.sub(r"^(#{3,6}) ", lambda m: m[1][1:] + " ", body, flags=re.M)
    if level == 3:
        body = re.sub(r"^(#{4,6}) ", lambda m: m[1][2:] + " ", body, flags=re.M)
    page(path, title, body, description, source, text[:a].count("\n") + 1, text[:b].count("\n"), historical)


def main():
    final = (ROOT / "research" / FINAL).read_text(encoding="utf-8-sig")
    phase = (ROOT / "research" / PHASE).read_text(encoding="utf-8-sig")
    for number, (heading, _, _) in enumerate(parts(phase, 2), 1):
        phase_anchor_pages[slug(heading)] = f"recherche/{number:02d}-{slug(heading)[:85]}.md"
    availability_path = ROOT / "research" / "source-accessibility.json"
    if availability_path.exists():
        availability = json.loads(availability_path.read_text(encoding="utf-8"))
        rows = ["| Référence d’origine | Réponse au contrôle |", "|---|---|"]
        for item in availability["issues"]:
            code = item["status"]
            status = {404: "HTTP 404 — URL indisponible au contrôle", 403: "HTTP 403 — accès refusé au robot", 429: "HTTP 429 — limitation de requêtes", 500: "HTTP 500 — erreur du serveur", "unverified": "Non vérifié — timeout ou erreur réseau"}.get(code, f"HTTP {code}")
            rows.append(f"| [{item['url']}]({item['url']}) | {status} |")
        page("disponibilite-sources.md", "Disponibilité des références", f'''Contrôle de disponibilité effectué le **{availability['date_fr']}** sur {availability['total']} URL citées : {availability['available']} ont répondu HTTP 200 ou 202. Les autres réponses sont consignées ci-dessous.

Ce contrôle technique porte sur l’accès aux URL, pas sur la validité des conclusions. HTTP 200 ne prouve pas que la page soutient une affirmation ; HTTP 403, 429 ou un timeout ne prouve pas qu’une source a disparu. Une URL indisponible limite la vérification par le lecteur.

Les deux fichiers de recherche restent intacts. Les mentions « accès à vérifier » du site indiquent les réponses incertaines. Les liens vers des commits historiques ne sont pas remplacés par une version récente, qui ne serait pas la même preuve.

## Références à vérifier

''' + "\n".join(rows) + f"\n\n[Proposer une URL primaire corrigée ou une archive fidèle]({REPO}/issues/new/choose). Ne pas remplacer une référence par une preuve de périmètre différent.\n\nLe relevé versionné est dans [`research/source-accessibility.json`]({REPO}/blob/main/research/source-accessibility.json).", "Disponibilité des URL citées : erreurs HTTP et vérifications bloquées, sans modification des conclusions scientifiques.")
    sections = parts(final, 2)
    section_map = {
        1: ("resume.md", "Résumé", "Les conclusions du rapport sur la sécurité, la vie privée et le pseudonymat des messageries, avec leurs limites."),
        2: ("lecture.md", "Comment lire cette étude", "Définitions : E2EE, pseudonymat, anonymat, métadonnées et statuts de preuve."),
        3: ("methodologie.md", "Méthodologie", "Travaux documentaires réalisés et limites : pas de laboratoire réseau, de tests forensiques contrôlés ni de builds reproduits."),
        4: ("compatibilite.md", "Plateformes et compatibilité", "Applications, protocoles et compatibilité iPhone et PC au 14 octobre 2026."),
        5: ("comparatif.md", "Comparatif général", "Comparaison qualitative des identités, contenus, métadonnées, appels et limites des 18 solutions."),
        6: ("threat-models.md", "Threat models — TM1 à TM15", "Résistance relative aux menaces : fournisseurs, réseau, contacts, demandes judiciaires et appareils."),
        7: ("metadonnees.md", "Métadonnées", "Ce que les fournisseurs, correspondants, réseaux, Apple, Google et autorités peuvent observer."),
        8: ("audits.md", "Audits et vulnérabilités", "Périmètres des audits, vulnérabilités datées, permissions mobiles et limites de la chaîne de build."),
        9: ("affaires.md", "Demandes judiciaires et cas publics", "Remises observées, rapports de transparence et distinction entre capacité technique et production réelle."),
        11: ("usages.md", "Choisir selon son usage", "Paliers conditionnels par usage, configuration pseudonyme Signal et contraintes iPhone et PC."),
        12: ("discord-migration.md", "Discord → messagerie privée", "Gains et limites d’une migration depuis Discord vers SimpleX, Signal renforcé, Threema ou Olvid."),
        13: ("opsec.md", "OPSEC", "Recommandations proportionnées pour les identités, appels, appareils, fichiers et notifications."),
        14: ("limites.md", "Limites et inconnues", "Inconnues conservées et expériences contrôlées nécessaires pour faire évoluer le verdict."),
        15: ("sources.md", "Sources", "Références primaires et indépendantes portant les conclusions du rapport ; bibliographie élargie en Phase 2."),
    }
    product_pages = []
    for number, (heading, a, b) in enumerate(sections, 1):
        if number == 10:
            product_chunk = final[a:b]
            for name, p, q in parts(product_chunk, 3):
                dest = f"messageries/{slug(name)}.md"
                extract(dest, name, final, a+p, a+q, FINAL,
                        f"Conclusion canonique sur {name} : propriétés utiles, limites et sources, rapport 1.0 du 14 octobre 2026.", 3)
                product_pages.append((name, dest))
        else:
            dest, title, desc = section_map[number]
            extract(dest, title, final, a, b, FINAL, desc)

    # Preserve every original section of Phase 2, including historical summaries.
    phase_pages = []
    product_evidence = {}
    for number, (heading, a, b) in enumerate(parts(phase, 2), 1):
        dest = f"recherche/{number:02d}-{slug(heading)[:85]}.md"
        extract(dest, heading, phase, a, b, PHASE,
                f"Registre Phase 2 : {heading}. Preuves, périmètres et inconnues documentaires au 14 octobre 2026.", historical=number == 1)
        phase_pages.append((heading, dest))
        for name, _ in product_pages:
            if (heading.startswith(name + " — dossier") or
                name == "Status / Waku" and "Status App / Waku" in heading):
                product_evidence[name] = dest

    # Cross-link conclusions directly to the detailed dossier, and back.
    for name, dest in product_pages:
        evidence = product_evidence.get(name)
        if evidence:
            with (DOCS / dest).open("a", encoding="utf-8") as f:
                f.write(f"\n## Preuves détaillées\n\n[Lire le dossier {name} en Phase 2](../{evidence}).\n")
            with (DOCS / evidence).open("a", encoding="utf-8") as f:
                f.write(f"\n## Conclusion actuelle\n\n[Lire la fiche de référence {name}](../{dest}).\n")

    # Exact transposition of the wide threat matrix; no assessment is changed.
    threat = (DOCS / "threat-models.md").read_text(encoding="utf-8")
    lines = threat.splitlines()
    header = next(i for i, line in enumerate(lines) if line.startswith("| Threat model |"))
    cells = [[c.strip() for c in line.strip("|").split("|")] for line in lines[header:header+17]]
    transposed = ["## Lecture par messagerie", "", "Chaque fiche propose les mêmes cellules dans un tableau étroit, adapté au mobile. Aucune appréciation n’est modifiée.", ""]
    for col, name in enumerate(cells[0][1:], 1):
        product = next((dest for title, dest in product_pages if slug(title).replace('-', '') == slug(name).replace('-', '') or name == "Ricochet" and title == "Ricochet Refresh"), None)
        if product:
            transposed += [f"- [{name}]({product}#threat-models)"]
            narrow = ["## Threat models", "", "Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.", "", "| Menace | Résistance relative |", "|---|---|"]
            narrow += [f"| {row[0]} | {row[col]} |" for row in cells[2:]]
            with (DOCS / product).open("a", encoding="utf-8") as f:
                f.write("\n" + "\n".join(narrow) + "\n")
    with (DOCS / "threat-models.md").open("a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(transposed))

    page("index.md", "Messageries : sécurité, vie privée et pseudonymat", '''Recherche indépendante et évolutive sur 18 solutions de messagerie. Les conclusions dépendent de l’adversaire, de la version, des appareils et de la configuration.

**Rapport 1.0 · Dernière mise à jour : 14 octobre 2026.**

## L’essentiel en deux minutes

- **Il n’existe pas de gagnant universel.** E2EE protège le contenu ; il ne garantit ni l’anonymat ni l’absence de métadonnées.
- **Pour séparer une identité après un contact Discord : SimpleX**, si le correspondant l’accepte et si ses contraintes de configuration sont réalistes. Les relais, notifications iOS, terminaux et traces Discord restent à considérer.
- **Pour iPhone + PC : Signal est un compromis très praticable.** Masquer le numéro et désactiver sa découverte, partager un username non réutilisé et vérifier les clés améliorent le pseudonymat envers le contact. Le numéro reste nécessaire à l’inscription et connu du service.
- **Olvid et Threema évitent de donner un numéro au contact**, avec des limites de multi-appareil ; ils ne fournissent pas un anonymat réseau. Cwtch et Briar restent spécialisés, sans client iOS officiel établi ici.
- **Session est rétrogradé provisoirement pour l’assurance élevée** : le statut des corrections et retests des attaques WOOT 2026 doit être établi. Aucun service étudié ne démontre une résistance générale à un adversaire passif global.

Un appareil compromis ou déverrouillé et un destinataire qui copie les messages peuvent exposer le contenu, quelle que soit la messagerie.

[Lire les 14 conclusions du résumé](resume.md) · [Choisir selon son usage](usages.md) · [Comparer les capacités et limites](comparatif.md)

## Commencer la lecture

| Votre question | Page à consulter |
|---|---|
| Que signifient les termes et les statuts ? | [Comment lire cette étude](lecture.md) |
| Contre quel adversaire comparer ? | [Threat models](threat-models.md) |
| Qui peut observer quelles données ? | [Métadonnées](metadonnees.md) |
| Comment quitter Discord pour une conversation privée ? | [Discord → messagerie privée](discord-migration.md) |
| Qu’est-ce qui est réellement prouvé ? | [Méthodologie](methodologie.md), [audits](audits.md), [cas judiciaires](affaires.md) |
| Où vérifier les affirmations ? | [Sources](sources.md) et [registre complet Phase 2](recherche/index.md) |

## Limites à garder en tête

Pas de laboratoire réseau, pas de tests forensiques contrôlés, pas de reproduction bit à bit des binaires distribués. **UNKNOWN reste UNKNOWN.** Une déclaration du fournisseur, un résultat d’audit borné et une observation indépendante sont des preuves de nature différente.

Les scores numériques de l’ancienne Phase 3 ne sont pas les conclusions actuelles. Le [rapport final](rapport/index.md) fait référence ; le registre Phase 2 expose les preuves et leurs périmètres.

[Signaler une information obsolète ou proposer une source](contribuer.md).''', "Étude indépendante des messageries : sécurité, vie privée, pseudonymat et métadonnées. Conclusions conditionnelles, sources et limites explicites.")

    page("messageries/index.md", "Autres messageries et fiches par produit",
         "Chaque fiche reprend la conclusion du rapport final, avec ses réserves. Les preuves détaillées sont reliées au registre Phase 2.\n\n" +
         "\n".join(f"- [{name}]({Path(path).name})" for name, path in product_pages) +
         "\n\nMolly et Bitchat sont des candidats complémentaires, sans rang commun avec les réseaux principaux : [dossier Phase 2](../recherche/06-candidats-supplementaires-retenus-pour-examen.md).",
         "Index des 18 messageries étudiées, avec fiches de conclusion et liens vers leurs preuves détaillées.")

    evidence_list = "\n".join(f"- [{name}]({Path(dest).name})" for name, dest in phase_pages)
    page("recherche/index.md", "Recherche complète — Phase 2", '''Le registre est conservé intégralement et découpé par section pour faciliter la lecture. Il contient les fiches individuelles, audits, matrices, observations et inconnues.

**Priorité éditoriale :** le [rapport final 1.0](../resume.md) fixe les conclusions actuelles. La synthèse Phase 1 et les mentions de classement Phase 3 dans ce registre sont des traces historiques, sans autorité sur la conclusion actuelle. L’ancienne Phase 3 n’a pas été fournie et n’est pas publiée ici.

[Télécharger le registre original en Markdown](../downloads/enquete-messageries-progress.txt) · [Voir le fichier versionné](https://github.com/Voldigoade/recherche-messageries/blob/main/research/enquete-messageries-progress.md)

## Toutes les sections

''' + evidence_list, "Registre complet de la recherche Phase 2, découpé par dossier : sources, audits, métadonnées, matrices et questions ouvertes.")

    canonical_links = "\n".join(f"- [{title}](../{dest})" for _, (dest, title, _) in section_map.items())
    page("rapport/index.md", "Rapport canonique — version 1.0", '''Le rapport final fourni est la référence technique. Les pages du site en reprennent les sections et les fiches sans créer de notes ni de conclusions nouvelles.

**Version : 1.0 · Date de référence : 14 octobre 2026.**

[Lire le fichier original versionné](https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md) · [Télécharger le Markdown original](../downloads/rapport-final-messageries.txt)

## Sections du rapport

''' + canonical_links + "\n- [Dossiers par messagerie](../messageries/index.md)\n\nLes copies originales sont préservées octet pour octet lors de la première publication. Le manifeste `research/manifest.json` enregistre leurs empreintes SHA-256 et les lignes d’origine des pages générées.", "Version, provenance et accès au rapport canonique intégral ; index de ses sections et fiches.")

    page("contribuer.md", "Contribuer", f'''Les contributions doivent améliorer les preuves et leur traçabilité. Les conclusions actuelles ne changent qu’avec une justification documentée.

## Signaler une information obsolète

Ouvrir une [issue]({REPO}/issues/new/choose) avec la page, l’affirmation, la source primaire, la date, la plateforme et la version concernées. Séparer déclaration de fournisseur, observation, recherche indépendante et inférence.

## Proposer une modification

Lire les [instructions de contribution]({REPO}/blob/main/CONTRIBUTING.md), modifier la source dans `research/`, régénérer les pages, puis proposer une pull request. Le lien « Modifier la source » des pages extraites ouvre le fichier d’origine.

Pas de classement numérique inventé. Une absence de cas public retrouvé ne prouve pas l’absence de cas. `UNKNOWN` ne devient pas une réussite ou un échec par supposition.

## Crédits et réutilisation

Recherche indépendante et évolutive, publiée et maintenue par [Voldigoade]({REPO.rsplit('/', 1)[0]}). Les références distinguent les travaux des fournisseurs, chercheurs, auditeurs et juridictions ; leur inclusion ne signifie pas une approbation du projet.

Texte de recherche et documentation : CC BY-SA 4.0. Scripts et configuration : MIT. Voir la [licence]({REPO}/blob/main/LICENSE).''', "Contribuer à l’étude : proposer des sources, signaler une information obsolète et documenter versions et périmètres.")

    page("maintenance.md", "Maintenir et publier le site", '''## Construire localement

```console
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/structure_docs.py
python -m mkdocs build --strict
python scripts/check_site.py
python -m mkdocs serve
```

Activer l’environnement virtuel avant l’installation (`.venv\\Scripts\\Activate.ps1` sous PowerShell, `source .venv/bin/activate` sous Linux/macOS).

Le workflow GitHub Actions reconstruit les pages, vérifie les liens internes et publie chaque push sur `main`. Les pull requests construisent et vérifient sans déployer. La recherche est locale au navigateur ; aucune base de données ni backend applicatif n’est utilisé. Les fichiers statiques sont servis par GitHub Pages.

## Modifier les conclusions

Modifier `research/rapport-final-messageries.md` pour la conclusion canonique et `research/enquete-messageries-progress.md` pour les preuves. Exécuter le générateur et revoir le diff. Mettre à jour la version et la date dans le générateur et le template lors d’une nouvelle version du rapport. `research/manifest.json` assure la traçabilité des sections ; la matrice par messagerie transpose les cellules sans les changer.

## Domaine personnalisé

1. Dans les réglages Pages du dépôt, saisir le domaine souhaité et le vérifier auprès de GitHub.
2. Configurer le DNS conformément à la [documentation GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
3. Remplacer `site_url` dans `mkdocs.yml` par l’URL HTTPS du domaine, avec une barre finale. Ajouter `docs/CNAME` avec le domaine seul et mettre à jour le lien du README.
4. Pousser sur `main`, puis activer HTTPS lorsque le certificat est prêt. Le build recalcule canonical, sitemap et robots.txt depuis `site_url`.

## Liens externes

`python scripts/check_external.py` vérifie les URL citées et écrit un journal dans `.qa/`. Un refus HTTP, un challenge anti-bot ou un timeout ne prouve pas qu’une source a disparu. Le site conserve les citations d’origine ; un changement de source exige une revue documentaire.''', "Instructions de maintenance MkDocs, publication GitHub Pages et connexion ultérieure d’un domaine personnalisé.")

    downloads = DOCS / "downloads"
    downloads.mkdir(exist_ok=True)
    for name in (FINAL, PHASE):
        (downloads / Path(name).with_suffix(".txt")).write_bytes((ROOT / "research" / name).read_bytes())
    hashes = {name: hashlib.sha256((ROOT / "research" / name).read_bytes()).hexdigest() for name in (FINAL, PHASE)}
    (ROOT / "research" / "manifest.json").write_text(json.dumps({"version": "1.0", "date": "2026-10-14", "sha256": hashes, "sections": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    config["nav"] = [
        {"Accueil": "index.md"},
        {"Lire l’étude": [{"Résumé": "resume.md"}, {"Comment lire cette étude": "lecture.md"}, {"Méthodologie": "methodologie.md"}]},
        {"Comparer": [{"Comparatif général": "comparatif.md"}, {"Plateformes et compatibilité": "compatibilite.md"}, {"Threat models": "threat-models.md"}, {"Métadonnées": "metadonnees.md"}, {"Choisir selon son usage": "usages.md"}]},
        {"Messageries": [{"Index des fiches": "messageries/index.md"}] + [{name: dest} for name, dest in product_pages[:7]] + [{"Autres messageries": [{name: dest} for name, dest in product_pages[7:]]}]},
        {"Pratique et preuves": [{"Discord → messagerie privée": "discord-migration.md"}, {"OPSEC": "opsec.md"}, {"Audits et vulnérabilités": "audits.md"}, {"Demandes judiciaires et cas publics": "affaires.md"}, {"Limites et inconnues": "limites.md"}, {"Sources": "sources.md"}] + ([{"Disponibilité des références": "disponibilite-sources.md"}] if availability_path.exists() else [])},
        {"Recherche complète / Phase 2": [{"Index du registre": "recherche/index.md"}, {"Dossiers par messagerie": [{name: dest} for name, dest in phase_pages if dest in product_evidence.values()]}, {"Enquêtes transversales": [{name: dest} for name, dest in phase_pages if dest not in product_evidence.values()]}]},
        {"Le projet": [{"Rapport canonique": "rapport/index.md"}, {"Contribuer": "contribuer.md"}, {"Maintenance et domaine": "maintenance.md"}]},
    ]
    generate_experience(DOCS, config, config["nav"])
    (ROOT / "mkdocs.yml").write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")
    print(f"Generated {len(list(DOCS.rglob('*.md')))} pages from {len(manifest)} traceable sections.")


if __name__ == "__main__":
    main()
