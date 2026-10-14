---
title: Tox / qTox
description: 'Conclusion canonique sur Tox / qTox : propriétés utiles, limites et
  sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 260
---

# Tox / qTox

Identité par clé et protocole P2P, mais qTox n’est qu’une implémentation desktop. Clients mobiles, forks, maintenance et fonctions ne sont pas interchangeables. Les appels P2P et IP publique exposent le pair; un ID long terme peut être corrélé par réutilisation. Le protocole et chaque client doivent être évalués séparément.

## Preuves détaillées

[Lire le dossier Tox / qTox en Phase 2](../recherche/30-tox-qtox-dossier-de-preuves-situation-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🟡 |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟠 |
| TM4 ISP / Wi-Fi / LAN | 🟠 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🔴 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | 🟡 |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟡 |
