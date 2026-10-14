---
title: Maintenir et publier le site
description: Instructions de maintenance MkDocs, publication GitHub Pages et connexion
  ultérieure d’un domaine personnalisé.
search:
  boost: 2
---

# Maintenir et publier le site

## Construire localement

```console
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/structure_docs.py
python -m mkdocs build --strict
python scripts/check_site.py
python -m mkdocs serve
```

Activer l’environnement virtuel avant l’installation (`.venv\Scripts\Activate.ps1` sous PowerShell, `source .venv/bin/activate` sous Linux/macOS).

Le workflow GitHub Actions reconstruit les pages, vérifie les liens internes et publie chaque push sur `main`. Les pull requests construisent et vérifient sans déployer. La recherche est locale au navigateur ; aucune base de données ni backend applicatif n’est utilisé. Les fichiers statiques sont servis par GitHub Pages.

## Modifier les conclusions

Modifier `research/rapport-final-messageries.md` pour la conclusion canonique et `research/enquete-messageries-progress.md` pour les preuves. Exécuter le générateur et revoir le diff. Mettre à jour la version et la date dans le générateur et le template lors d’une nouvelle version du rapport. `research/manifest.json` assure la traçabilité des sections ; la matrice par messagerie transpose les cellules sans les changer.

## Domaine personnalisé

1. Dans les réglages Pages du dépôt, saisir le domaine souhaité et le vérifier auprès de GitHub.
2. Configurer le DNS conformément à la [documentation GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
3. Remplacer `site_url` dans `mkdocs.yml` par l’URL HTTPS du domaine, avec une barre finale. Ajouter `docs/CNAME` avec le domaine seul et mettre à jour le lien du README.
4. Pousser sur `main`, puis activer HTTPS lorsque le certificat est prêt. Le build recalcule canonical, sitemap et robots.txt depuis `site_url`.

## Liens externes

`python scripts/check_external.py` vérifie les URL citées et écrit un journal dans `.qa/`. Un refus HTTP, un challenge anti-bot ou un timeout ne prouve pas qu’une source a disparu. Le site conserve les citations d’origine ; un changement de source exige une revue documentaire.
