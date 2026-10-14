---
title: Plateformes et compatibilité
description: Applications, protocoles et compatibilité iPhone et PC au 14 octobre
  2026.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 58
---

# Plateformes et compatibilité

La comparaison distingue application, protocole, réseau et opérateur. Matrix est un protocole fédéré; Element est un ensemble de clients et de services. XMPP est un protocole, OMEMO une extension E2EE, et l’opérateur du serveur ainsi que le client choisi déterminent le résultat. Tox/qTox, Jami, Cwtch ou Ricochet Refresh ne partagent pas une infrastructure unique. Les architectures P2P réduisent parfois la visibilité centrale mais peuvent exposer l’IP aux pairs.

| Produit | Nature / architecture dominante | iPhone | PC | État pratique pertinent au 14-10-2026 |
|---|---|---:|---:|---|
| Signal | Service centralisé; E2EE Signal Protocol; téléphone à l’inscription | Oui | Windows/macOS/Linux | Desktop officiel appairé au téléphone. La disponibilité multiplateforme ne rend pas le compte anonyme. [Téléchargements](https://signal.org/download/) |
| SimpleX | Relais store-and-forward, pas d’identifiant global d’utilisateur | Oui | Windows/macOS/Linux | Profils locaux; appairage mobile–desktop documenté sur le même réseau local. Builds desktop actuels marqués bêta sur la page téléchargements. [Téléchargements](https://simplex.chat/downloads/) |
| Olvid | Service centralisé de rendez-vous/transport; identité cryptographique | Oui | Windows/macOS/Linux | Multi-device simultané sous licence après essai; historique antérieur non transféré automatiquement au nouvel appareil. [FAQ multi-appareil](https://olvid.io/faq/use-olvid-on-multiple-devices/) |
| Session | Réseau décentralisé de nœuds de service/onion routing pour messages | Oui | Windows/macOS/Linux | Appels audio/vidéo bêta, activés opt-in, P2P; statut des mitigations de l’étude WOOT 2026 non établi ici. [FAQ](https://getsession.org/faq) |
| Threema | Service centralisé et identifiant Threema aléatoire | Oui | Windows/macOS/Linux | Desktop 2.0 multi-device est bêta, jusqu’à deux ordinateurs, PFS non supportée; le client Web/Desktop ancien dépend du téléphone. [Limites bêta](https://threema.com/en/faq/md-limit) |
| Cwtch | Messages via services onion/Tor; profils locaux, pas de service central unique | Pas de client officiel établi | Windows/macOS/Linux, Android | Candidat de niche; mainteneurs et assurance moins étendus que les services grand public. L’absence d’iOS exclut l’usage iPhone natif. [Téléchargements](https://docs.cwtch.im/it/download/) |
| Briar | Android : store-and-forward chiffré via Tor, avec options locales Bluetooth/Wi-Fi; client desktop distinct en bêta | Non | Desktop Linux/Windows/macOS bêta | En maintenance depuis juillet 2026 : correctifs essentiels et de sécurité uniquement; desktop ne comble pas l’absence d’iOS. [Annonce maintenance](https://briarproject.org/news/2026-maintenance-mode/), [desktop](https://briarproject.org/download-briar-desktop/) |
| Jami | P2P distribué/DHT, appels et messages | Oui | Windows/macOS/Linux | Pas de serveur central unique, mais DHT, bootstrap, relais, NAT traversal et clients restent dans le modèle de confiance. |
| Tox/qTox | Protocole P2P et implémentations indépendantes | Dépend d’un client tiers; qTox n’est pas le client iOS | qTox surtout desktop | Les garanties varient fortement entre implémentations; IP directe lors de connexions/appels P2P possible. |
| Matrix / Element | Protocole fédéré + homeservers; Element clients/hosting | Oui | Windows/macOS/Linux/Web | Choix du homeserver, salons chiffrés, fédération, push, identité et SFU changent le threat model. [Spécification](https://spec.matrix.org/latest/) |
| XMPP / OMEMO | Protocole fédéré + extension E2EE + client/serveur choisis | Dépend du client | Dépend du client | Pas de verdict générique sans nommer serveur, client, version et réglages OMEMO. [XEP-0384](https://xmpp.org/extensions/xep-0384.html) |
| Telegram | Service centralisé cloud; Secret Chats séparés | Oui | Windows/macOS/Linux/Web | Cloud Chats et groupes ne sont pas E2EE; Secret Chats sont un mode distinct, généralement 1:1 et lié aux appareils. |
| WhatsApp | Service centralisé Meta; E2EE de contenu par défaut pour conversations personnelles | Oui | Windows/macOS/Web | Numéro et graphe d’usage restent identifiants importants; sauvegardes et comptes Meta/OS sont à considérer. |
| Discord | Plateforme centralisée de communautés/DM | Oui | Windows/macOS/Linux/Web | Texte non E2EE; DAVE chiffre l’audio/vidéo des appels éligibles, pas les messages texte. |
| Wire | Service centralisé orienté équipes, code client partiellement public | Oui | Windows/macOS/Linux/Web | Compte, configuration et services hébergés importent; un cas public établit la remise d’un e-mail d’inscription. |
| Delta Chat | Client de messagerie basé sur e-mail/chatmail; chiffrement Autocrypt selon conversation | Oui | Windows/macOS/Linux | La confidentialité et l’E2EE dépendent aussi du fournisseur e-mail, de la compatibilité du contact et du client. |
| Ricochet Refresh | Messagerie desktop 1:1 via Tor onion services | Non | Windows/macOS/Linux | Petit projet; mises à jour, assurance actuelle, groupes/appels et supply chain peu établis. Audit du Ricochet historique non transférable au Refresh actuel. |
| Status / Waku | Application et protocoles Waku/Logos, infrastructure de nœuds distribuée | Mobile selon versions | Client desktop stable non établi dans cette étude | À distinguer d’une messagerie centralisée; les nœuds gérés peuvent quand même observer IP/topics et métadonnées. |

**Candidats complémentaires.** Molly est un fork Android de Signal : il change certaines propriétés locales et de transport, mais conserve le réseau Signal et son exigence de numéro; ce n’est pas un réseau indépendant. Bitchat est un projet mesh Bluetooth/Nostr expérimental; son auditabilité, son modèle d’identité et son comportement selon les versions ne justifient pas de le classer au même niveau que les services matures. Les détails figurent dans la Phase 2.
