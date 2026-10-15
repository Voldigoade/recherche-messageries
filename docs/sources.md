---
title: Sources
description: Références primaires et indépendantes portant les conclusions du rapport
  ; bibliographie élargie en Phase 2.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 426
---

# Sources

Les sources ci-dessous sont les références primaires/indépendantes qui portent les conclusions de premier ordre. La bibliographie élargie, les audits détaillés (organisme, date, version, scope, exclusions, findings, corrections/retest), vulnérabilités et matrices par service sont dans le [dossier Phase 2](recherche/index.md). Les références sont classées par rôle; l’éditeur établit ses déclarations, pas une preuve indépendante de leur application en production.

## Sources transversales et référentiels

- [Spécification Matrix](https://spec.matrix.org/latest/) : protocole/API, source primaire.
- [XEP-0384 OMEMO](https://xmpp.org/extensions/xep-0384.html) : extension XMPP E2EE, spécification.
- [USENIX WOOT 2026 — Practical Attacks on a Decentralized Secure Messenger Session](https://www.usenix.org/conference/woot26/presentation/urushigaki) : recherche indépendante, Session Protocol V1.
- [DFRWS / Forensic Science International 2026 — analyse forensique Matrix/Synapse](https://dfrws.org/wp-content/uploads/2026/03/DFRWS-down-the-Rabbit-Hole-A-forensic-analy_2026_Forensic-Science-Internati.pdf) : étude de serveur en environnement/version précisés; pas extraction Cellebrite mobile.
- [Apple Security Updates, CVE-2026-28950](https://support.apple.com/en-us/127002) : avis primaire sur correctif iOS/iPadOS 26.4.2.

## Signal

- [Phone Number Privacy and Usernames](https://signal.org/blog/phone-number-privacy-usernames/) : billet officiel, réglages d’identité et limites du username.
- [Automatic Key Verification](https://signal.org/blog/automatic-key-verification/) : billet officiel, key transparency et limites d’authentification humaine.
- [Signal download](https://signal.org/download/) et [support linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices) : plateformes et appairage.
- [Dossier de subpoena D.C. 2026](https://signal.org/bigbrother/district-of-columbia/) : documents et réponse fournisseur.

## SimpleX, Olvid, Session

- [SimpleX download](https://simplex.chat/downloads/), [policy](https://simplex.chat/privacy/), [calls guide](https://simplex.chat/docs/guide/audio-video-calls.html), [transparency](https://simplex.chat/transparency/) : sources officielles; les affirmations de logs ne sont pas indépendamment mesurées.
- [Olvid specifications](https://www.olvid.io/assets/documents/2024-10-07_Olvid-specifications.pdf), [formal analysis 2026](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf), [multi-device](https://olvid.io/faq/use-olvid-on-multiple-devices/) : protocol, étude et contraintes produit.
- [Session FAQ](https://getsession.org/faq), [USENIX WOOT 2026](https://www.usenix.org/conference/woot26/presentation/urushigaki) : calls et analyse indépendante, périmètres distincts.

## Threema, Briar, Cwtch, réseaux onion/P2P

- [Threema transparency report](https://threema.com/en/transparency-report), [Desktop beta limitations](https://threema.com/en/faq/md-limit), [2026 cryptography whitepaper](https://threema.com/assets/8-press/2026-04-20-threema-cryptography-whitepaper.pdf).
- [Briar how it works](https://briarproject.org/how-it-works/), [Briar Desktop downloads](https://briarproject.org/download-briar-desktop/), [maintenance mode notice, 9 July 2026](https://briarproject.org/news/2026-maintenance-mode/).
- [Cwtch overview](https://docs.cwtch.im/docs/intro/), [downloads](https://docs.cwtch.im/it/download/), [reproducible bindings report](https://docs.cwtch.im/blog/cwtch-bindings-reproducible/).
- Les sources de Jami, Tox/qTox et Ricochet Refresh sont inventoriées par dépôt/protocole et limite de client dans le dossier de Phase 2; ne pas généraliser un résultat d’un client à l’autre.

## Discord, Matrix, Wire, Telegram, WhatsApp, Delta Chat

- [Discord DAVE protocol and code](https://github.com/discord/libdave) : périmètre médias audio/vidéo, distinct du texte; voir aussi son advisory traité en Phase 2.
- [Matrix.org privacy notice](https://matrix.org/legal/privacy-notice/), [law enforcement guide](https://matrix.org/legal/law-enforcement-guidelines/), [Element privacy](https://element.io/en/legal/privacy) : sources de fournisseur sur matrix.org/Element, pas tous homeservers.
- [Wire iOS advisory CVE-2026-35049](https://github.com/wireapp/wire-ios/security/advisories/GHSA-v6wg-c7qc-x66g) : avis de sécurité avec versions et correction.
- [U.S. v. Bryant](https://app.midpage.ai/document/united-states-v-bryant-1000161304572) : opinion judiciaire concernant Discord et retour de mandat.
- [Telegram Delhi High Court order](https://indiankanoon.org/doc/119238688/) et [follow-up](https://indiankanoon.org/doc/2402568/) : production civile sous pli; champs/portée partiellement contradictoires.
- [Wire investigation reporting with company confirmation](https://techcrunch.com/2024/05/08/encrypted-services-apple-proton-and-wire-helped-spanish-police-identify-activist/) : remise d’e-mail de compte, sans preuve de remise de contenu Wire.
- Delta Chat : audits Cure53/OTF Webxdc, études ETH/USENIX et doc Autocrypt sont cités individuellement dans le [registre Phase 2](recherche/index.md); chaque audit couvre un périmètre distinct.

## Repère de lecture final

Ne pas citer ce rapport comme certification de sécurité ni comme conseil juridique. Pour refaire une comparaison après une mise à jour majeure, la première tâche est de vérifier les versions et configurations, le statut de correctifs Session/Threema/Signal, les labels mobiles, les builds installés et les disclosures légales depuis les sources primaires. Le document canonique conserve les inconnues plutôt que de remplir les cases par supposition.
