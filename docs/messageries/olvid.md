---
title: Olvid
description: 'Conclusion canonique sur Olvid : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 236
---

# Olvid

**À retenir :** compte cryptographique sans téléphone/e-mail obligatoire, calls documentés via TURN-only et étude indépendante formelle récente. **Limites :** serveur voit des éléments de routage/timing/taille dans le modèle analysé; multi-device simultané et appels nécessitent licence après l’essai; discussion historique non synchronisé automatiquement. N’est pas une solution d’anonymat réseau. Sources : [specifications](https://www.olvid.io/assets/documents/2024-10-07_Olvid-specifications.pdf), [formal study](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf), [multi-device](https://olvid.io/faq/use-olvid-on-multiple-devices/).

## Preuves détaillées

[Lire le dossier Olvid en Phase 2](../recherche/20-olvid-dossier-probatoire-approfondi-etat-au-13-octobre-2026.md).

## Threat models

Transposition exacte de la [matrice canonique TM1–TM15](../threat-models.md), avec les mêmes réserves de configuration et de preuve. `✅` : résistance relativement forte ; `🟡` : partielle ; `🟠` : exposition importante ; `🔴` : faible résistance ; `❓` : données insuffisantes.

| Menace | Résistance relative |
|---|---|
| TM1 Fournisseur curieux | 🟠 |
| TM2 Infrastructure compromise | 🟡 |
| TM3 Opérateur malveillant | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟠 |
| TM5 Observateur passif multipoint | 🟠 |
| TM6 Adversaire global passif | 🔴 |
| TM7 Contact malveillant | 🟡 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟠 |
| TM15 Censure étatique | 🟠 |
