---
title: Dépôts publics / activité observée — échantillon borné, pas audit exhaustif
description: 'Registre Phase 2 : Dépôts publics / activité observée — échantillon
  borné, pas audit exhaustif. Preuves, périmètres et inconnues documentaires au 14
  octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 266
---

# Dépôts publics / activité observée — échantillon borné, pas audit exhaustif

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

| Dépôt client | Observation vérifiable au 13 oct. 2026 | Ce qu’on ne peut pas en déduire |
|---|---|---|
| Signal Android | GitHub liste des releases fréquentes; v8.31.1 (8 oct.) est explicitement marquée pré-release, alors que v8.30.3 est marquée latest dans la page observée. Les tags affichent des commits courts; la page consultée n’établit pas à elle seule une signature cryptographique/reproductibilité. [Releases](https://github.com/signalapp/Signal-Android/releases). | La fréquence prouve une maintenance observable de ce dépôt, pas le nombre réel de mainteneurs, la sécurité du backend ou que le Play APK correspond au code taggé. Les artifacts et build pipeline n’ont pas été reproduits. |
| SimpleX Chat | Releases affichent v7.0.3 comme latest (26 sept. selon la page) et v7.1.0-beta.6 (3 oct.). Le tag et commit de cette beta sont marqués « verified » par GitHub pour la clé GPG D53BDFD153C366BA de Simplex Operations. La politique SECURITY.md est révisée le 25 mai 2026. [Releases](https://github.com/simplex-chat/simplex-chat/releases), [security](https://github.com/simplex-chat/simplex-chat/security). | Signature vérifiée GitHub ≠ build reproductible ni attestation que l’APK/IPA provient de ce commit; disponibilité de la clé/révocation et contrôle de la chaîne complète encore à documenter. |
| Element Android | Releases publiques jusqu’à v1.6.66. Un correctif high de sécurité est publié en v1.6.58 (13 mai, commit `80285ed` selon la page) contre l’usurpation de `sender_device_keys` sur événements to-device chiffrés Olm, CVE-2026-45056/GHSA-wfq4-36m3-9g42; v1.6.62 (21 juillet, commit `e2df418`) corrige aussi la sanitisation d’emplacement de fichiers (GHSA-fr74-76wm-x6pp). [Releases](https://github.com/element-hq/element-android/releases). | Ces correctifs doivent être reliés aux versions effectives utilisées; ils ne démontrent pas l’état de toutes les implémentations Matrix/clients ou serveurs. Date/commit courant de v1.6.66 pas suffisamment établi dans la lecture actuelle. |
| Briar | Page GitHub de releases consultée ne donne pas une liste exploitable dans l’extraction Web. | Ce résultat ne permet pas d’affirmer « projet sans releases » ni inactif; il faut interroger le dépôt, tags, F-Droid et site officiel de manière croisée. |
| Threema Android / iOS / Desktop / Web / Push Relay | Les dépôts officiels Android/iOS indiquent un commit par release publique non-bêta et commits PGP signés; Desktop publie l’historique des commits; Push Relay documente les champs de requête/payload. Au snapshot GitHub du 14 oct. 2026, l’activité était récente; Web est explicitement en maintenance (correctifs critiques, pas de nouveautés majeures). [Android](https://github.com/threema-ch/threema-android), [iOS](https://github.com/threema-ch/threema-ios), [Desktop](https://github.com/threema-ch/threema-desktop), [Web](https://github.com/threema-ch/threema-web), [Push Relay](https://github.com/threema-ch/push-relay). | Cela ne prouve pas que les binaires distribués correspondent au code. Android décrit la reproductibilité comme expérimentale; iOS dit qu’elle reste à l’étude. Le README iOS signale une dépendance WebRTC fournie en binaire par Threema. Aucun rebuild/comparaison de hash ni audit du backend principal n’a été effectué. La clé PGP Web indiquée dans le README expire le 4 sept. 2026 : rotation/révocation à vérifier; cette date seule n’invalide pas rétroactivement les signatures. |

## Échantillon reproductible d’activité visible — branche par défaut, 90 jours

Au 14 octobre 2026, j’ai demandé à l’API publique GitHub les commits depuis le 16 juillet 2026, page 1 (100 éléments max), puis compté les identifiants d’auteurs distincts dans les commits retournés. Les nombres ci-dessous sont des **comptes d’auteurs visibles dans l’échantillon**, pas des mainteneurs vérifiés, développeurs équivalents temps plein, reviewers ou personnes qui gèrent les releases. Les dépôts à 100 sont tronqués par la limite de page; les contributions de bots, translations, merges et comptes secondaires peuvent gonfler ou fragmenter le compte.

| Produit / dépôt réellement compté | Commits renvoyés | Auteurs distincts visibles | Portée |
|---|---:|---:|---|
| Signal — [Signal-Android](https://api.github.com/repos/signalapp/Signal-Android/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 7 | Dépôt client Android seulement; les 100 résultats sont un plafond, pas le total. |
| SimpleX — [simplex-chat](https://api.github.com/repos/simplex-chat/simplex-chat/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 5 | Monorepo du client/protocoles; plafond atteint. |
| Olvid — [olvid-android](https://api.github.com/repos/olvid-io/olvid-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | 2 | 1 | Dépôt Android public seulement; services/backend séparés non comptés. |
| Session — [session-android](https://api.github.com/repos/session-foundation/session-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 5 | Dépôt Android; un compte auteur représente la majorité de l’échantillon, mais bots inclus. |
| Threema — [threema-android](https://api.github.com/repos/threema-ch/threema-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | 3 | 1 | Android seulement; autres clients/repos non agrégés. |
| Tox — [c-toxcore](https://api.github.com/repos/TokTok/c-toxcore/commits?since=2026-07-16T00:00:00Z&per_page=100) | 23 | 6 | Cœur protocolaire. |
| qTox — [TokTok/qTox](https://api.github.com/repos/TokTok/qTox/commits?since=2026-07-16T00:00:00Z&per_page=100) | 23 | 10 | Client desktop; le fork actif est distinct de l’ancien dépôt archivé. |
| Matrix — [Element X Android](https://api.github.com/repos/element-hq/element-x-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 9 | Client Android uniquement. |
| Matrix — [Synapse](https://api.github.com/repos/element-hq/synapse/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 25 | Homeserver Matrix; il n’est pas agrégé avec les clients. |
| Telegram — [Android source](https://api.github.com/repos/DrKLO/Telegram/commits?since=2026-07-16T00:00:00Z&per_page=100) | 38 | 6 | Source Android publique du client; iOS/backend non comptés. |
| Discord — [libdave](https://api.github.com/repos/discord/libdave/commits?since=2026-07-16T00:00:00Z&per_page=100) | 15 | 2 | Bibliothèque DAVE seulement; ne mesure pas l’équipe du client Discord fermé. |
| Wire — [wire-android](https://api.github.com/repos/wireapp/wire-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 10 | Client Android uniquement; plafond atteint. |
| Delta Chat — [deltachat-android](https://api.github.com/repos/deltachat/deltachat-android/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 4 | Client Android seulement; le core Rust et desktop ne sont pas agrégés. |
| Ricochet Refresh — [ricochet-refresh](https://api.github.com/repos/blueprint-freespeech/ricochet-refresh/commits?since=2026-07-16T00:00:00Z&per_page=100) | 2 | 1 | Branche stable par défaut; alpha séparée non incluse. |
| Status — [status-app](https://api.github.com/repos/status-im/status-app/commits?since=2026-07-16T00:00:00Z&per_page=100) | ≥100 | 10 | App seulement; Logos/Waku/projets voisins non agrégés. |

**Hors mesure GitHub dans cette passe :** Cwtch publie ses dépôts sur [git.openprivacy.ca](https://git.openprivacy.ca/cwtch.im/cwtch); Briar sur son [GitLab officiel](https://code.briarproject.org/briar/briar); Jami sur son infrastructure de revue/dépôt [jami.net](https://review.jami.net/). Le lien GitHub Conversations cité dans le dossier XMPP a renvoyé 404 via l’API interrogée; le bon dépôt/miroir de la version 2.20.4+free reste à confirmer, donc aucun auteur n’est compté. Aucun dépôt public complet du client WhatsApp ou Discord n’est revendiqué ici. Ces absences d’échantillon GitHub ne signifient pas absence d’activité ou de source publique ailleurs.

**Bilan supply chain de cette sous-étape.** Rien ici ne prouve des builds reproductibles. Une release signée, un tag publié, du code source accessible ou une CI verte ne démontrent pas que l’installateur servi au téléphone a été construit à partir de ce code. Il faut comparer des builds locaux reproductibles aux binaires de chaque canal, vérifier signatures/digests, attestations CI, dépendances vendored et provenance des stores. Ce travail n’a pas été effectué.
