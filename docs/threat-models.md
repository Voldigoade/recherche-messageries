---
title: Threat models — TM1 à TM15
description: 'Résistance relative aux menaces : fournisseurs, réseau, contacts, demandes
  judiciaires et appareils.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 108
---

# Threat models — TM1 à TM15

La matrice évalue une résistance relative et non la sécurité absolue. La cellule dépend du mode par défaut ou de la configuration courante documentée; un réglage explicite (par exemple TURN, salons E2EE ou visibilité du numéro) peut la déplacer. `✅` signifie une résistance relativement forte à cette menace, `🟡` partielle, `🟠` exposition importante, `🔴` faible résistance, `❓` données insuffisantes. Les cellules `❓` ne sont pas des notes négatives.

| Threat model | Signal | SimpleX | Olvid | Session | Threema | Cwtch | Briar | Jami | Tox/qTox | Matrix/Element | XMPP/OMEMO | Telegram | WhatsApp | Discord | Wire | Delta Chat | Ricochet | Status/Waku |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| TM1 Fournisseur curieux | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟠 | 🟡 | ✅ | 🟠 |
| TM2 Infrastructure compromise | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM3 Opérateur malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | ✅ | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM5 Observateur passif multipoint | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM6 Adversaire global passif | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 |
| TM7 Contact malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | 🟠 |
| TM9 Demande judiciaire classique | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | ✅ | ✅ | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM10 Enquête sophistiquée multi-source | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 |
| TM11 Appareil verrouillé | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | 🟡 | 🟡 | 🟡 | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | ❓ |
| TM12 Appareil déverrouillé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM14 Supply-chain compromise | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM15 Censure étatique | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |

## Justification courte des lignes

- **TM1–TM3 :** le chiffrement protège le contenu face à un serveur honnêtement curieux ou compromis, mais un opérateur peut voir les métadonnées qu’expose l’architecture et contrôler disponibilité, rendez-vous, distribution client et mises à jour. SimpleX/Cwtch/Briar/Ricochet réduisent l’identifiant central; ce n’est pas une preuve qu’aucun nœud ou client ne peut les corréler. Pour Session, le résultat WOOT 2026 pèse particulièrement sur TM2/TM3.
- **TM4–TM6 :** TLS/E2EE masque le contenu, pas l’IP du service, les horaires et le volume. Tor/onion peut masquer une IP de destination à certains observateurs locaux, mais ne prouve pas l’immunité à l’analyse de trafic. Aucun service ne démontre une résistance générale à TM6.
- **TM7–TM8 :** absence de numéro/annuaire et identités par contact aident contre un pair/doxxer, mais profil, pseudo réutilisé, fichiers, liens, voix, habitudes et appels P2P peuvent défaire la séparation. La relation Discord initiale demeure chez Discord si le lien d’invitation y est partagé.
- **TM9–TM10 :** la possibilité de remettre une donnée et une remise observée sont distinctes. Données fournisseurs, télécom, store, FAI, appareils, participants et OSINT s’additionnent. Les rangs ne sont pas une garantie juridique; voir §9.
- **TM11–TM13 :** la forensique d’appareil verrouillé est versionnée et les preuves contemporaines sont rares; les nombreuses cellules restent `❓`. Déverrouillé/compromis, l’app peut afficher le texte en clair, donc résistance faible pour tous.
- **TM14 :** le code public facilite l’inspection mais aucun build distribué de l’ensemble des clients n’a été reproduit dans cette mission. Le client fermé, pipeline d’update, dépendances, magasins et clés de signature restent des surfaces.
- **TM15 :** Briar dispose de Tor/bridges et transports locaux sur Android, mais l’état maintenance réduit la pérennité; fédération, P2P, Tor et auto-hébergement peuvent diversifier les points de panne, pas empêcher blocages de stores, DNS, IP, protocoles ou bootstrap.

Cette matrice reprend la grille consolidée de la Phase 2, après contrôle de configuration et d’actualité; chaque colonne renvoie au dossier individuel correspondant dans le [registre Phase 2](recherche/index.md), où se trouvent les justifications courtes et les liens de preuve par menace. Elle n’ajoute pas une précision expérimentale : les symboles sont des appréciations qualitatives et restent conditionnels. Pour censure, forensique, supply chain et demandes judiciaires, le dossier individuel fait foi si le cas précis est plus nuancé.

## Lecture par messagerie

Chaque fiche propose les mêmes cellules dans un tableau étroit, adapté au mobile. Aucune appréciation n’est modifiée.

- [Signal](messageries/signal.md#threat-models)
- [SimpleX](messageries/simplex.md#threat-models)
- [Olvid](messageries/olvid.md#threat-models)
- [Session](messageries/session.md#threat-models)
- [Threema](messageries/threema.md#threat-models)
- [Cwtch](messageries/cwtch.md#threat-models)
- [Briar](messageries/briar.md#threat-models)
- [Jami](messageries/jami.md#threat-models)
- [Tox/qTox](messageries/tox-qtox.md#threat-models)
- [Matrix/Element](messageries/matrix-element.md#threat-models)
- [XMPP/OMEMO](messageries/xmpp-omemo.md#threat-models)
- [Telegram](messageries/telegram.md#threat-models)
- [WhatsApp](messageries/whatsapp.md#threat-models)
- [Discord](messageries/discord.md#threat-models)
- [Wire](messageries/wire.md#threat-models)
- [Delta Chat](messageries/delta-chat.md#threat-models)
- [Ricochet](messageries/ricochet-refresh.md#threat-models)
- [Status/Waku](messageries/status-waku.md#threat-models)