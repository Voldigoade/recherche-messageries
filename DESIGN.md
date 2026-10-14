# Direction du site

Documentation technique francophone, destinée à lire et vérifier une recherche. Références demandées : ArchWiki, Wikipédia, documentation Linux classique. La priorité est la lisibilité et la traçabilité, sans marketing ni effets.

## Système visuel

Le fichier `docs/stylesheets/documentation.css` est la source des tokens de présentation. Fond blanc `#ffffff`, texte `#202122`, secondaire `#54595d`, liens `#0645ad`, bordures `#a2a9b1`, surface `#f8f9fa`. Georgia pour le titre de page ; Arial/Helvetica système pour corps et navigation ; Consolas pour le code. Aucune police distante.

Navigation Material standard avec groupes sobres, sommaire de la page, recherche locale en français et anglais, navigation précédente/suivante. Un pictogramme de conversation et de lignes de texte sert de favicon. Les matrices ne sont pas des scores ; les symboles sont accompagnés de noms accessibles selon la légende canonique.

## Comportement

Liens et boutons sémantiques, focus visible, pas d’animation ajoutée. Les tableaux conservent leurs colonnes et défilent horizontalement dans une région nommée accessible au clavier. Leur largeur ne provoque pas de défilement horizontal du document. Les pages restent lisibles sans JavaScript ; la recherche utilise le moteur local Material. Le bouton d’effacement de recherche et les états vides sont ceux du thème, vérifiés dans le navigateur.

Fond blanc et contraste AA pour le texte et les liens ; zoom autorisé, réduction du mouvement et couleurs forcées respectés. Aucun backend, suivi analytique, cookie applicatif ou appel à une police externe ajouté. GitHub Pages et les liens vers les sources externes ont leurs propres politiques.

## Contenu

Rapport 1.0 du 14 octobre 2026 canonique. Phase 2 intégralement préservée, marquée comme registre daté ; synthèse Phase 1 marquée historique. Provenance par section et copies originales téléchargeables. Les conclusions, réserves et inconnues ne sont pas inventées. Les pages sont produites par `scripts/structure_docs.py`.
