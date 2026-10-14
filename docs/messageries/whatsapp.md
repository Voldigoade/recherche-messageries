---
title: WhatsApp
description: 'Conclusion canonique sur WhatsApp : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 276
---

# WhatsApp

E2EE par défaut pour messages et appels personnels; contenu chiffré ne rend pas le numéro, le graphe d’usage, l’IP, les infos de compte et les sauvegardes inconnus à Meta/OS. Les études 2025–2026 de l’enquête sont versionnées et certaines attaques de découverte de numéros ont été corrigées selon les auteurs; ne pas présenter un état historique comme faille actuelle.

## Preuves détaillées

[Lire le dossier WhatsApp en Phase 2](../recherche/34-whatsapp-dossier-individuel-dinvestigation-13-octobre-2026.md).

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
| TM10 Enquête sophistiquée multi-source | 🔴 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟠 |
