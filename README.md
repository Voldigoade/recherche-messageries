# Étude des messageries

Recherche indépendante et évolutive sur la sécurité, la vie privée et le pseudonymat de 18 solutions de messagerie.

**[Lire l’étude](https://voldigoade.github.io/recherche-messageries/)**

Rapport de référence **1.0**, mis à jour le **14 octobre 2026**. Les conclusions sont conditionnelles aux versions, configurations et adversaires considérés. Il n’existe pas de gagnant universel.

Le [rapport final](research/rapport-final-messageries.md) est la source canonique. Le [registre Phase 2](research/enquete-messageries-progress.md) conserve les preuves détaillées et leurs limites ; ses synthèses historiques ne remplacent pas le rapport final. Aucun classement numérique de l’ancienne Phase 3 n’est repris.

## Méthodologie

Recherche documentaire et sources primaires. Pas de laboratoire réseau, pas de tests forensiques contrôlés, pas de reproduction bit à bit des binaires. **UNKNOWN reste UNKNOWN.** Une déclaration fournisseur et une preuve indépendante sont distinguées.

## Construire et maintenir

Python 3.12 ou ultérieur. Créer et activer un environnement virtuel, puis :

```console
python -m pip install -r requirements.txt
python scripts/structure_docs.py
python -m mkdocs build --strict
python scripts/check_site.py
python -m mkdocs serve
```

MkDocs et Material simplifié, recherche locale, aucun backend. GitHub Actions vérifie les pull requests et déploie chaque push sur `main` via GitHub Pages. Les pages sont extraites de `research/` ; ne pas éditer directement les pages générées. Les liens « Modifier la source » ouvrent leur fichier d’origine. [Maintenance et domaine personnalisé](docs/maintenance.md).

## Contribution et licence

[Signaler une information obsolète ou proposer une source](https://github.com/Voldigoade/recherche-messageries/issues/new/choose). Lire [CONTRIBUTING.md](CONTRIBUTING.md) avant une pull request.

Recherche et documentation sous CC BY-SA 4.0 ; scripts et configuration sous MIT. Voir [LICENSE](LICENSE) et [LICENSE-CODE](LICENSE-CODE).
