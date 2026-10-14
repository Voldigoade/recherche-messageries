---
title: Éléments probatoires à préserver dans la matrice globale
description: 'Registre Phase 2 : Éléments probatoires à préserver dans la matrice
  globale. Preuves, périmètres et inconnues documentaires au 14 octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 189
---

# Éléments probatoires à préserver dans la matrice globale

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

1. **Status/Waku** : ne pas écrire « les nœuds ne voient pas l’IP ou le graphe topic »; page d’infrastructure Status admet IP + topics et rétention de 15 jours pour certains services gérés. Distinguer données de transport/topic du contenu chiffré.
2. **Signal forensic** : ajouter preuve de récupération d’aperçus Signal iOS depuis le système dans un dossier pénal 2026, puis le correctif CVE-2026-28950. Cette preuve est locale et historique; version/capture exacte manquante.
3. **Signal remise fournisseur** : le cas D.C. 2026 ne se réduit pas à « Signal n’a rien remis » : Signal rapporte la remise des dates de création et dernière connexion pour six comptes; 24 autres sans données pour la période, 7 comptes absents.
4. **SimpleX requests** : le rapport publié dit 12 demandes policières en 2025 et aucune donnée responsive trouvée/remise. C’est la déclaration du fournisseur, pas une preuve que des données n’existent chez aucun relai, ISP ou endpoint.
5. **SimpleX audits** : les PDF ToB d’implémentation 2022 (avec fix review 2023) et de design 2024 ont été lus; le premier laisse le finding mémoire non résolu, le second couvre les designs et non l’implémentation générale. Une assessment ToB 2026 est déclarée réalisée, mais son rapport reste **UNKNOWN** au 13 octobre et n’apporte pas encore de preuve consultable.
6. **Threema légal** : le rapport 2025/2026 montre des remises effectives agrégées d’informations par ID (pas de contenus selon les catégories listées). L’acte d’accusation U.S. v. Wedding contient du contenu Threema, mais le canal de preuve paraît participant/co-conspirateur et ne doit pas être appelé « remise de Threema » sans dossier complémentaire.
7. **WhatsApp et Discord** : ne pas traiter E2EE/absence de serveur-content après livraison comme absence de données remises. WhatsApp documente des catégories d’account/contact/group records et collecte ciblée future; un dossier Discord documente un retour effectif de contenus et IP à la suite d’un mandat.
8. **Olvid — anonymat et routage** : le papier formel 2026, lu en entier, établit que dans le protocole modélisé le serveur voit les clés publiques des destinataires, la taille et le timing; il rapporte que l’équipe Olvid emploie « anonymat » dans un sens non technique et reconnaît l’identification par clés publiques. Ce point doit apparaître dans toute matrice de métadonnées, sans en déduire que le serveur connaît nécessairement le nom civil de tout utilisateur.
