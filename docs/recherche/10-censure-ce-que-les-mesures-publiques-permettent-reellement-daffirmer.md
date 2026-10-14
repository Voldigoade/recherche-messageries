---
title: Censure — ce que les mesures publiques permettent réellement d’affirmer
description: 'Registre Phase 2 : Censure — ce que les mesures publiques permettent
  réellement d’affirmer. Preuves, périmètres et inconnues documentaires au 14 octobre
  2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 180
---

# Censure — ce que les mesures publiques permettent réellement d’affirmer

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

- **Signal** : OONI rapporte mesures du produit de 2021 suggérant le blocage en Iran, Chine et Ouzbékistan pendant la période avril–septembre 2021, et un blocage temporaire de quelques jours à Cuba en juillet 2021. Les mécanismes observés étaient différents : interférence DNS, injection DNS et échecs TLS compatibles avec DPI. OONI décrit aussi à cette date domain-fronting/censorship-circumvention et proxies TLS Android; les réglages/protocoles actuels doivent être revalidés. C’est un cas documenté de contournement et de blocage, pas la preuve que cela marche encore en 2026 sur chaque réseau. [Analyse OONI](https://ooni.org/post/2021-how-signal-private-messenger-blocked-around-the-world/).
- **Briar** : le fournisseur décrit Tor comme transport Internet et Bluetooth/Wi-Fi/carte mémoire quand Internet est coupé; son threat model admet un adversaire qui bloque ou manipule les canaux longue portée et une capacité limitée de surveiller/bloquer le court rayon. C’est une propriété d’architecture et un modèle produit, pas une garantie de disponibilité universelle. App stores, téléchargement initial, Tor/bridges, densité de contacts proches, matériel radio et répression physique restent des dépendances. [How it works / modèle de menace Briar](https://briarproject.org/how-it-works/).
- **Limite de couverture de mesure** : OONI indique que seules Signal, WhatsApp, Telegram et Facebook Messenger ont actuellement des expériences OONI Probe dédiées parmi les messageries; les autres apps peuvent être sondées par domaine/serveur, mais l’absence d’expérience dédiée ou de mesure publiée n’est pas une preuve d’accessibilité. [Méthodologie OONI Explorer](https://ooni.org/post/2025-ooni-explorer-thematic-censorship-pages/).
- **À ne pas conclure** : aucun résultat public exact consulté ici ne démontre en octobre 2026 qu’une messagerie de la liste est bloquée ou accessible dans tous les AS d’un pays. Les cartes OONI changent dans le temps et couvrent seulement des réseaux/probes observés; les pays, opérateurs, versions, mécanismes anti-censure et périodes doivent être explicitement indiqués avant de noter TM15.

**Conclusion forensic bornée** : E2EE limite la remise du fournisseur; le terminal déverrouillé, snapshots, pièces jointes, base locale, OS notification store, sauvegarde et appareil du correspondant restent des surfaces indépendantes. Les cas publics datés prouvent l’existence d’extractions dans des environnements précis, mais pas leur succès sur toute version actuelle.
