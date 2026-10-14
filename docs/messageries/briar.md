---
title: Briar
description: 'Conclusion canonique sur Briar : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 252
---

# Briar

**À retenir :** utile pour contacts Android quand résilience hors réseau et Tor/transport local comptent; le client Desktop existe en bêta pour Linux/Windows/macOS. **Limites :** pas d’app iOS, coûts UX/fonctionnels, pas d’appels, versions de desktop et mobile séparées; projet désormais maintenance seulement (correctifs essentiels/sécurité). Ne pas en faire le choix pratique pour un utilisateur iPhone. Sources : [how it works](https://briarproject.org/how-it-works/), [desktop](https://briarproject.org/download-briar-desktop/), [maintenance](https://briarproject.org/news/2026-maintenance-mode/).

## Preuves détaillées

[Lire le dossier Briar en Phase 2](../recherche/23-briar-dossier-probatoire-approfondi-etat-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | ✅ |
| TM2 Infrastructure compromise | ✅ |
| TM3 Opérateur malveillant | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟡 |
| TM5 Observateur passif multipoint | 🟠 |
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
