---
title: Signal
description: 'Conclusion canonique sur Signal : propriétés utiles, limites et sources,
  rapport 1.0 du 14 octobre 2026.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 228
---

# Signal

**À retenir :** E2EE mûr, réseau centralisé, forte adoption et clients officiels iPhone + Windows/macOS/Linux. Pour séparer un pseudo, créer un username unique non réutilisé, mettre la visibilité du numéro et la recherche par numéro sur « personne », ne pas synchroniser/importer les contacts si inutile, et partager uniquement le lien/username souhaité. **Limite :** le service exige toujours un numéro à l’inscription; une clé transparente garantit une association identifiant–clé cohérente, pas que la personne contrôle l’identité annoncée. L’autoverification du correspondant via le log ne fonctionne pas dans le scénario username seul si son numéro n’est pas connu; comparer un Safety Number via canal indépendant. Desktop reste un appareil lié au téléphone principal. Sources : [privacy phone/username](https://signal.org/blog/phone-number-privacy-usernames/), [AKV](https://signal.org/blog/automatic-key-verification/), [desktop](https://signal.org/download/).

## Preuves détaillées

[Lire le dossier Signal en Phase 2](../recherche/18-signal-dossier-probatoire-approfondi-etat-au-13-octobre-2026.md).

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
| TM7 Contact malveillant | 🟡 |
| TM8 Harceleur / doxxer OSINT | 🟡 |
| TM9 Demande judiciaire classique | 🟡 |
| TM10 Enquête sophistiquée multi-source | 🟠 |
| TM11 Appareil verrouillé | ❓ |
| TM12 Appareil déverrouillé | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 |
| TM14 Supply-chain compromise | 🟡 |
| TM15 Censure étatique | 🟠 |
