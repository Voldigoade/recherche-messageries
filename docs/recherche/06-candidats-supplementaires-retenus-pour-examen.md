---
title: Candidats supplémentaires retenus pour examen
description: 'Registre Phase 2 : Candidats supplémentaires retenus pour examen. Preuves,
  périmètres et inconnues documentaires au 14 octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 70
---

# Candidats supplémentaires retenus pour examen

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

## Molly (Android uniquement; client/fork, pas réseau indépendant)

- **F/VC** : dépôt officiel décrit un fork Android de Signal, compatible avec le réseau Signal, avec chiffrement local par passphrase, verrouillage automatique, prise en charge Tor/SOCKS, UnifiedPush, variante Molly-FOSS et fingerprints de certificat de signature publiés ([repo](https://github.com/mollyim/mollyim-android), [site](https://molly.im/)).
- **Portée** : améliore surtout la sécurité locale, la réduction de dépendance Google et le routage du client. Il ne supprime pas le numéro d’inscription ni le fournisseur Signal, et l’usage de Tor ne neutralise pas le correspondant, le contenu partagé ou les corrélations temporelles.
- **Points à vérifier avant notation** : activité/release exacte en octobre 2026, correspondance Signal protocol version, vérification indépendante des builds reproductibles, provenance du F-Droid repo et comportement de push/calls en mode Tor.

## Status App (Waku/Logos Messaging; app distincte et réseau P2P)

- **Fiche approfondie distincte ajoutée en annexe** : Status demeure un candidat supplémentaire, hors matrice de base des 17 tant que le périmètre de la Phase 3 n’est pas arrêté. L’annexe distingue spécifications 2026, marketing, observables indépendants, versions et inconnues.
- **Point d’attention étayé** : la publication d’infrastructure de Status décrit IP + content-topic visibles pour plusieurs services Waku gérés et une rétention annoncée de 15 jours pour certaines IP; cela ne révèle pas le contenu E2EE, mais exclut de lire « décentralisé » comme « aucun nœud ne voit de métadonnées ».
- **Incident historique distinct** : en 2018, Status a indiqué qu’un bug d’intégration TestFairy dans des builds nightly pouvait enregistrer des phrases de récupération malgré leur masquage attendu. L’éditeur dit avoir retiré TestFairy et supprimé les enregistrements; il déclarait alors n’avoir aucune preuve d’exploitation. Ce cas ne décrit pas les versions courantes.

## Candidats non ajoutés à ce stade

Nym dispose d’une architecture mixnet et de recherches pertinentes, mais aucun client de messagerie grand public mature et actuellement supporté n’a été établi dans les sources consultées; ne pas confondre une bibliothèque/réseau mixnet avec une app utilisable. La recherche continue pour d’autres clients sérieux, sans ajouter de projets obscurs uniquement parce qu’ils revendiquent Tor ou P2P.

## Bitchat (candidat expérimental, pas une messagerie Internet classique)

- **F/VC** : projet public de mesh Bluetooth LE hors ligne avec passerelle optionnelle vers Nostr quand Internet est disponible; le whitepaper décrit Noise XX, X25519, ChaCha20-Poly1305, SHA-256, et une identité à clé stable. [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).
- **IE / limite de confidentialité** : le whitepaper indique que la clé statique sert à une identité persistante et que l’ID pair est dérivé de sa fingerprint; les annonces publient nom et clés en clair. Dans le mesh, voisinage radio, RSSI, temps et tailles de trafic sont observables. La politique de confidentialité précise que les relays Nostr voient IP, taille/heure et tags de routage; l’affirmation « identité expéditeur non exposée » reste une revendication du projet à valider selon le chemin et la version. [Privacy policy](https://github.com/permissionlesstech/bitchat/blob/main/PRIVACY_POLICY.md).
- **Incident historique sourcé, statut corrigé à vérifier** : une analyse indépendante de 2025 a décrit un défaut précoce d’authentification/liaison d’identité permettant une usurpation/MITM; le projet a ensuite ajouté un avertissement de vérification et remplacé la conception d’échange par Noise selon l’analyse. Cela ne prouve pas une faille dans le code courant. [Analyse technique indépendante](https://www.supernetworks.org/pages/blog/agentic-insecurity-vibes-on-bitchat), [couverture contemporaine de l’absence d’audit externe en 2025](https://techcrunch.com/2025/07/09/jack-dorsey-says-his-secure-new-bitchat-app-has-not-been-tested-for-security/).
- **Supply chain / maturité** : le tag v1.7.1 apparaît avec signature GitHub vérifiée dans la page de releases; cela n’authentifie pas indépendamment l’identité du signataire ni ne prouve un build reproductible. Le dépôt ne listait aucun advisory public au moment de la consultation; absence d’advisory ≠ absence de défaut. L’audit formel actuel et le retest indépendant ne sont pas établis. [Releases](https://github.com/permissionlesstech/bitchat/releases), [Security](https://github.com/permissionlesstech/bitchat/security).
- **Inconnus importants** : état du correctif du bug d’identité dans la version Android/iOS actuelle; comparaison des implémentations; tests de build reproductible; audit; conservation forensic des messages/caches; comportement exact avec Tor désactivé, réseau Nostr donné, et groupes privés. Un tag signé ne clôt aucun de ces points.
