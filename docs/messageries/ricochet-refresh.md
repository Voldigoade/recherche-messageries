---
title: Ricochet Refresh
description: 'Conclusion canonique sur Ricochet Refresh : propriétés utiles, limites
  et sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 292
---

# Ricochet Refresh

Le canal Tor onion évite un compte central et limite l’exposition IP dans son chemin normal, mais le projet est de faible maturité/activité et l’assurance actuelle est faible. L’audit NCC souvent cité vise Ricochet historique, pas Refresh 3.x. Desktop seulement, 1:1, pas de service multi-device/appels établi. Candidat de recherche, pas recommandation par défaut.

## Preuves détaillées

[Lire le dossier Ricochet Refresh en Phase 2](../recherche/31-ricochet-refresh-dossier-de-preuves-situation-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | ✅ |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟡 |
| TM5 Observateur passif multipoint | 🟡 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🟡 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | 🟡 |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟡 |
