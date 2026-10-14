# Contribuer

Le rapport `research/rapport-final-messageries.md` définit la conclusion actuelle. Le fichier `research/enquete-messageries-progress.md` conserve les preuves et les synthèses historiques. Une modification technique doit être documentée, jamais déduite d’un classement arbitraire.

## Issues

Utiliser les formulaires « Information obsolète » ou « Proposer une source ». Fournir la page, l’affirmation exacte, une URL primaire, la date, la version et la plateforme. Distinguer déclaration, fait observé, recherche indépendante et inférence. Une erreur HTTP ou l’absence de cas public ne constitue pas à elle seule une preuve technique.

## Pull requests

1. Modifier la source dans `research/` pour une conclusion technique. La couche de lecture V2 est dans `data/messengers.json` et `content/learning.json` ; conserver les références et les traductions FR/EN/ES. Pour la présentation, modifier CSS, templates ou configuration.
2. Exécuter `python scripts/structure_docs.py` pour régénérer les pages et leur manifeste.
3. Exécuter `python scripts/check_catalog.py`, `python scripts/check_generated.py`, `npm test`, `python -m mkdocs build --strict`, `python scripts/check_site.py` et `npm run test:browser`. Les dépendances navigateur s’installent avec `npm ci` puis `npx playwright install chromium`. Le contrôle du générateur travaille dans une copie temporaire et ne modifie pas les pages.
4. Revoir les diffs : aucune conclusion, réserve, source ni `UNKNOWN` ne doit disparaître sans justification.
5. Décrire le changement, le périmètre de preuve et la validation dans la pull request.

Ne pas éditer directement les pages générées : leur régénération les remplace. Les versions et dates doivent être explicites. Ne pas généraliser un audit à un autre client, backend, version ou binaire.

Les contributions à la documentation sont sous CC BY-SA 4.0, et celles aux scripts/configuration sous MIT. Conserver les attributions et les références ; ne pas importer de contenu sans droit de réutilisation. Les citations tierces restent soumises aux droits de leurs auteurs.
