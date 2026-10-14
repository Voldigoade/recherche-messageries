---
title: XMPP / OMEMO
description: 'Conclusion canonique sur XMPP / OMEMO : propriétés utiles, limites et
  sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 268
---

# XMPP / OMEMO

Une pile à configurer, pas un produit unique. OMEMO protège le contenu seulement si client, appareils, contacts et extension sont compatibles et correctement vérifiés; serveur voit JID, présence, connexions et groupe/roster selon extension. Pour comparer, il faut fixer un client iOS, client PC, serveur précis et politique de logs. Source protocole : [XEP-0384](https://xmpp.org/extensions/xep-0384.html).

## Preuves détaillées

[Lire le dossier XMPP / OMEMO en Phase 2](../recherche/32-xmpp-omemo-dossier-individuel-dinvestigation-13-octobre-2026.md).

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
