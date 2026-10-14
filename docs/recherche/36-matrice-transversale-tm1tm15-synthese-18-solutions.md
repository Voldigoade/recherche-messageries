---
title: Matrice transversale TM1–TM15 — synthèse 18 solutions
description: 'Registre Phase 2 : Matrice transversale TM1–TM15 — synthèse 18 solutions.
  Preuves, périmètres et inconnues documentaires au 14 octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 2256
---

# Matrice transversale TM1–TM15 — synthèse 18 solutions

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

**Lecture:** ces 15 lignes reprennent les mêmes scénarios TM1–TM15 définis dans la mission originale. Chaque case donne uniquement la notation normalisée; la justification courte, ses limites et les liens de preuve figurent dans le tableau TM1–TM15 propre au produit immédiatement après son dossier (pour XMPP, Telegram, WhatsApp, Discord ci-dessus; pour les 13 autres, plus haut). Cette grille est une vue croisée, pas un ordre de préférence. Les cases ne sont pas des résultats de laboratoire; certaines décrivent une inférence d’architecture explicitement signalée dans les fiches.

Colonnes abrégées: **Sig** Signal; **Sx** SimpleX; **Olv** Olvid; **Ses** Session; **Thr** Threema; **Cwt** Cwtch; **Bri** Briar; **Jam** Jami; **Tox** Tox/qTox; **Mx** Matrix/Element; **XMPP** XMPP/OMEMO; **TG** Telegram; **WA** WhatsApp; **Dis** Discord; **Wir** Wire; **Delta** Delta Chat; **RR** Ricochet Refresh; **Status** Status App/Waku.

| Menace | Sig | Sx | Olv | Ses | Thr | Cwt | Bri | Jam | Tox | Mx | XMPP | TG | WA | Dis | Wir | Delta | RR | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TM1 fournisseur curieux | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟠 | 🟡 | ✅ | 🟠 |
| TM2 fournisseur compromis | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM3 fournisseur malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | ✅ | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM4 ISP / Wi-Fi | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM5 observation passive multi-points | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM6 adversaire global passif | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 |
| TM7 contact malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM8 harceleur / doxxer OSINT | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | 🟠 |
| TM9 demande judiciaire classique | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | ✅ | ✅ | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM10 enquête policière sophistiquée | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 |
| TM11 appareil verrouillé saisi | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | 🟡 | 🟡 | 🟡 | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | ❓ |
| TM12 appareil déverrouillé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM13 spyware ciblé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM14 supply-chain compromise | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM15 censure étatique | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |

**Citations / source de la grille:** les faits différentiels proviennent de la politique/protocole/étude/cas liés dans chaque justification détaillée; pour Olvid, l’élément déterminant nouvellement intégré est l’[analyse formelle 2026 lue intégralement](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf); pour Discord, l’actualité déterminante est le [dossier DOJ 2026](https://www.justice.gov/usao-wdwa/media/1464546/dl) et [CVE DAVE](https://github.com/advisories/GHSA-3q99-x36r-rchh); pour WhatsApp, le [guide forces de l’ordre](https://faq.whatsapp.com/444002211197967/?category=5245250&locale=fr_FR), la [recherche NDSS 2026](https://www.ndss-symposium.org/ndss-paper/hey-there-you-are-using-whatsapp-enumerating-three-billion-accounts-for-security-and-privacy/) et l’étude [runtime 2026](https://arxiv.org/abs/2609.11882); Telegram: [policy](https://telegram.org/privacy) et [Delhi HC](https://dhccaseinfo.nic.in/jupload/dhc/PMS/judgement/31-08-2022/PMS30082022SC2822020_121640.pdf); XMPP: [XEP-0384](https://xmpp.org/extensions/xep-0384.html) et [ROS 2025](https://conversations.im/2025_audit_conversations.pdf). Pour les autres services, voir leurs cases-source inline dans leurs tables TM. Un scoring qui change de threat-model, version ou réglage doit être recalculé.
