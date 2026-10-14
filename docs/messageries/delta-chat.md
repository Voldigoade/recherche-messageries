---
title: Delta Chat
description: 'Conclusion canonique sur Delta Chat : propriétés utiles, limites et
  sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 288
---

# Delta Chat

Modèle e-mail familier, client multiplateforme et plusieurs audits ciblés. L’adresse mail et ses opérateurs forment l’infrastructure d’identité/transport; les métadonnées mail restent visibles, et l’E2EE dépend de l’état de la conversation. Appel P2P peut divulguer l’IP. Favorable si portabilité/interopérabilité e-mail priment, moins si unlinkability réseau et simplicité cryptographique sont prioritaires.

## Preuves détaillées

[Lire le dossier Delta Chat en Phase 2](../recherche/21-delta-chat-dossier-probatoire-approfondi-etat-au-13-octobre-2026.md).

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
| TM7 Contact malveillant | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟠 |
