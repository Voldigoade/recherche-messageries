---
title: Méthodologie
description: 'Travaux documentaires réalisés et limites : pas de laboratoire réseau,
  de tests forensiques contrôlés ni de builds reproduits.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 46
---

# Méthodologie

Le rapport consolide le travail des Phases 1–3, les fiches de Phase 2, les audits, articles académiques, advisories, politiques, rapports de transparence, affaires judiciaires et vérifications web actualisées. Les sources de la Phase 2 restent la pièce principale pour les détails d’implémentation, les audits lus, les vulnérabilités, les observations d’infrastructure, les métadonnées par produit et les questions expérimentales.

Les conclusions sont conditionnelles à la date **14 octobre 2026**. Les produits changent; une conclusion sur une version ne vaut pas pour toutes les plateformes ni toutes les versions. Les politiques officielles décrivent les engagements de l’éditeur, pas nécessairement une observation indépendante des systèmes de production. Les études académiques sont limitées à leurs modèles, builds et protocoles examinés. Les décisions judiciaires décrivent un cas, une juridiction et un périmètre donnés.

**Travail effectivement réalisé :** recherches web et consultation de sources primaires; lecture des dossiers existants; lecture détaillée de plusieurs rapports PDF consignés en Phase 2; échantillons d’activité Git/release et manifests Android source; observations DNS/BGP passives limitées, datées et consignées pour quelques endpoints. Aucun scan de ports, accès non autorisé, compte de test, capture de paquets applicative, extraction Cellebrite/GrayKey/Magnet ni reconstruction bit-à-bit d’un binaire n’a été réalisé ici.

**Limite documentaire locale :** le répertoire `sources/` du miroir de projet était vide lors du contrôle. Le rapport cite donc des URL de sources externes et renvoie au dossier Phase 2, sans prétendre que des PDFs locaux absents ont été relus durant cette consolidation.

**Confiance globale :** moyenne pour les propriétés protocolaires bien documentées et les résultats judiciaires explicitement publiés; faible à moyenne pour les métadonnées en production, les appels par version, les builds distribués, la forensique mobile actuelle et la résistance à la censure par pays/opérateur. Les inconnues ne sont pas converties en échec certain ou en réussite certaine.
