---
title: Status / Waku
description: 'Conclusion canonique sur Status / Waku : propriétés utiles, limites
  et sources, rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 296
---

# Status / Waku

Réseau distribuable, mais les opérateurs de nœuds gérés peuvent observer IP/topics/activité selon le service; certaines rétentions annoncées doivent être distinguées du contenu chiffré. Profil wallet/clé peut être durable et corrélable. Appels, clients desktop, builds, gouvernance et opérateurs effectifs restent à vérifier pour le cas précis.

## Preuves détaillées

[Lire le dossier Status / Waku en Phase 2](../recherche/38-dossier-de-preuve-complementaire-status-app-waku-au-14-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🟠 |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟠 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🟠 |
| TM7 Contact malveillant | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟠 |
| TM9 Demande judiciaire classique | 🟠 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟠 |
