---
title: Telegram
description: 'Conclusion canonique sur Telegram : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 272
---

# Telegram

Les Cloud Chats et groupes sont côté serveur; les Secret Chats sont un mode E2EE distinct. Les channels et groupes ne sont donc pas privés de la plateforme au même sens. Numéro et user discovery ont une surface de corrélation. Usage de communauté grand public acceptable si l’objectif n’est pas la confidentialité de contenu vis-à-vis du service; ne jamais résumer comme « E2EE par défaut ».

## Preuves détaillées

[Lire le dossier Telegram en Phase 2](../recherche/33-telegram-dossier-individuel-dinvestigation-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🔴 |
| TM2 Infrastructure compromise | 🔴 |
| TM3 Opérateur malveillant | 🔴 |
| TM4 ISP / Wi-Fi / LAN | 🟠 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟠 |
| TM9 Demande judiciaire classique | 🟠 |
| TM10 Enquête sophistiquée multi-source | 🔴 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟠 |
