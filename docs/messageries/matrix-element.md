---
title: Matrix / Element
description: 'Conclusion canonique sur Matrix / Element : propriétés utiles, limites
  et sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 264
---

# Matrix / Element

La fédération permet de choisir un homeserver ou de l’auto-héberger, mais les événements de membership, appareils, IP et timestamps restent visibles à l’opérateur correspondant. E2EE est activé par salon/client et n’efface pas metadata. Appels via SFU/TURN ont leur propre opérateur et visibilité IP. Source technique : [Matrix specification](https://spec.matrix.org/latest/), [Element privacy](https://element.io/en/legal/privacy), [matrix.org law enforcement guide](https://matrix.org/legal/law-enforcement-guidelines/).

## Preuves détaillées

[Lire le dossier Matrix / Element en Phase 2](../recherche/27-matrix-element-dossier-de-preuves-individuel-reference-13-octobre-2026.md).

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
| TM9 Demande judiciaire classique | 🟠 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟡 |
