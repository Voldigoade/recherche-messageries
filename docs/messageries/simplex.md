---
title: SimpleX
description: 'Conclusion canonique sur SimpleX : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 232
---

# SimpleX

**À retenir :** le modèle sans identifiant global et les liens propres à chaque relation sont adaptés au cloisonnement; profils et historique restent locaux, les relais stockent temporairement des messages chiffrés. Les notifications instantanées iOS donnent au serveur push une partie des métadonnées de queues/fréquence selon la politique; Apple voit un nombre de notifications et des métadonnées chiffrées, pas le contenu selon la conception publiée. TURN masque l’IP au contact dans le réglage par défaut des appels, mais le relay voit IP/durée. Profil mobile–desktop via le même LAN est une contrainte concrète. Source de politique (éditeur) : [privacy policy](https://simplex.chat/privacy/); calls [guide](https://simplex.chat/docs/guide/audio-video-calls.html); [downloads](https://simplex.chat/downloads/).

## Preuves détaillées

[Lire le dossier SimpleX en Phase 2](../recherche/19-simplex-dossier-probatoire-approfondi-etat-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🟡 |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟠 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🟡 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟡 |
