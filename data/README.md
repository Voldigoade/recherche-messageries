# Données de la V2

`messengers.json` est la seule couche structurée pour les faits affichés dans l’accueil, les fiches, les comparaisons et le guide de choix. Chaque fait renseigné cite un identifiant de source du catalogue, qui pointe vers des lignes du rapport canonique ou du registre Phase 2. Un champ absent se rend comme **Inconnu**, jamais comme une absence de risque.

Les valeurs FR/EN/ES sont des reformulations éditoriales des mêmes faits. Les niveaux affichés sont des descriptions qualitatives des conclusions ; aucun pourcentage ni score universel n’est calculé. Les règles de décision sont dans `decision_rules`, leurs filtres dans `docs/javascripts/decision.js`. Elles choisissent des points de départ conditionnels, pas une certification.

Modifier ce fichier, conserver les références et périmètres, puis exécuter `python scripts/structure_docs.py`, `python scripts/check_catalog.py`, `node --test tests/decision.test.cjs`, le build strict et `python scripts/check_site.py`. Les contenus pédagogiques sont dans `content/learning.json`. Ne pas modifier directement les pages générées.
