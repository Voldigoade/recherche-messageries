# V2 — contrat des outils de lecture

Source du besoin : objectif V2 fourni par l’utilisateur. Autorité technique : `research/rapport-final-messageries.md`, puis registre Phase 2 pour les détails explicitement bornés. La couche `data/messengers.json` est une reformulation traçable, pas une nouvelle recherche.

| Capability | Canonical owner | Source of truth | Allowed variants | Verification |
|---|---|---|---|---|
| Select/Listbox | HTML select natif dans le générateur V2 | Ce contrat | Sélection de messagerie et réponses du guide ; popup du système accepté | Clavier et tests navigateur |
| Form | Formulaire local avec labels, fieldsets et validation propre | Ce contrat | Guide de choix ; comparateur | Erreur, réinitialisation, résultats |
| Scrollbar | `docs/stylesheets/documentation.css` | DESIGN.md | Matrices massives uniquement | Petites largeurs et couleurs calculées |

Les outils utilisent JavaScript vanilla. Le catalogue est incorporé dans la page, sans requête réseau supplémentaire. Le guide ne conserve ni ne transmet les réponses, et ne les met pas dans l’URL. Le comparateur conserve uniquement les identifiants publics des applications dans `?apps=…`, avec un maximum de quatre applications distinctes ; le retour navigateur restaure cette sélection. Les paramètres invalides reviennent à une comparaison valide avec un message explicite.

Le guide applique les règles publiées dans le catalogue, puis filtre les incompatibilités documentées. Une compatibilité conditionnelle reste conditionnelle. Il peut retourner moins de trois candidats. Il n’attribue aucun score, et n’ajoute pas un candidat incompatible pour remplir la liste. Un adversaire global, un terminal compromis et les copies du correspondant restent des limites explicites.

Les résultats sont annoncés par une région de statut concise. Les formulaires ont `novalidate`, des labels et des messages d’erreur associés. Le bouton de réinitialisation remet le focus sur le premier champ. Les contrôles natifs conservent leur interaction clavier et leur popup système ; aucune apparence de popup personnalisée n’est promise.

Sans JavaScript, les synthèses, tableaux, comparaisons dédiées et règles restent lisibles. Les contrôles interactifs sont cachés jusqu’à leur initialisation. Les données inconnues sont indiquées dans chaque langue. Les pages traduites signalent que les preuves complètes sont en français.

Les tableaux principaux n’imposent pas de défilement horizontal à 320 px : chaque ligne devient une fiche avec des libellés visibles, tout en conservant les relations sémantiques des cellules. Les matrices de plus de sept colonnes conservent leur région défilante accessible au clavier.
