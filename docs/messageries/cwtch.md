---
title: Cwtch
description: 'Conclusion canonique sur Cwtch : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 248
---

# Cwtch

**À retenir :** architecture onion et absence de serveur central unique réduisent la concentration de métadonnées de compte. **Limites :** modèle Tor ne masque pas contre le global passive adversary; pas d’iOS, pas d’appels établis, maturité/assurance et audits plus limités. Utilisable pour utilisateurs qui acceptent une application niche et une configuration particulière. Sources : [intro](https://docs.cwtch.im/docs/intro/), [downloads](https://docs.cwtch.im/it/download/).

## Preuves détaillées

[Lire le dossier Cwtch en Phase 2](../recherche/28-cwtch-dossier-de-preuves-situation-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | ✅ |
| TM2 Infrastructure compromise | ✅ |
| TM3 Opérateur malveillant | ✅ |
| TM4 ISP / Wi-Fi / LAN | 🟡 |
| TM5 Observateur passif multipoint | 🟡 |
| TM6 Adversaire global passif | 🟠 |
| TM7 Contact malveillant | 🟡 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | ✅ |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | 🟡 |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟡 |
