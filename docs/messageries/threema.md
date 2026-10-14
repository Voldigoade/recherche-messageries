---
title: Threema
description: 'Conclusion canonique sur Threema : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 244
---

# Threema

**À retenir :** l’identifiant aléatoire et l’inscription sans téléphone/e-mail sont utiles au pseudonymat envers le contact. **Limites :** le fournisseur peut détenir des données d’ID/connexion et en publie des remises agrégées; l’achat via store peut créer une relation store; Desktop 2.0 bêta, PFS non supportée, fonctionnalité limitée et rétention de certaines propriétés dépend des clients. Sources : [privacy and reports](https://threema.com/en/transparency-report), [Desktop 2 beta limits](https://threema.com/en/faq/md-limit), [cryptography whitepaper](https://threema.com/assets/8-press/2026-04-20-threema-cryptography-whitepaper.pdf).

## Preuves détaillées

[Lire le dossier Threema en Phase 2](../recherche/25-threema-dossier-probatoire-approfondi-etat-documentaire-au-13-octobre-2026.md).

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
| TM15 Censure étatique | 🟠 |
