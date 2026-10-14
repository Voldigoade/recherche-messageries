---
title: Session
description: 'Conclusion canonique sur Session : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 240
---

# Session

**À retenir :** identifiant non téléphonique et routage onion des messages. **Réserves critiques :** étude WOOT 2026 sur Protocol V1 établit trois familles d’attaques dans les implémentations étudiées; aucun correctif/retest courant n’est établi dans cette consolidation. Appels bêta opt-in P2P révèlent IP au correspondant et au serveur STUN/TURN. Sources : [USENIX](https://www.usenix.org/conference/woot26/presentation/urushigaki), [FAQ appels](https://getsession.org/faq). Reclasser seulement après version corrective documentée et retest indépendant suffisant.

## Preuves détaillées

[Lire le dossier Session en Phase 2](../recherche/24-session-dossier-de-preuves-approfondi-complement-etat-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🟡 |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟠 |
| TM4 ISP / Wi-Fi / LAN | 🟡 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟠 |
