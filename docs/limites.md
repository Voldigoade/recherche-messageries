---
title: Limites et inconnues
description: Inconnues conservées et expériences contrôlées nécessaires pour faire
  évoluer le verdict.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 397
---

# Limites et inconnues

## Inconnues importantes

- **Session :** versions exactes de Protocol V1 affectées; correctifs réellement distribués à chaque plateforme; analyses indépendantes post-fix; statut des attaques d’usurpation, timestamp, drop/replay.
- **Signal :** comportement réseau complet par OS/version en username-only; payload APNs exact; effet post-iOS 26.4.2 sur extraction de notifications; association effective du numéro dans différentes modalités d’inscription.
- **SimpleX :** journaux de tous opérateurs tiers, durée des données anti-abus ponctuelles, comportement réel du push iOS et du desktop bêta; capture de call/ICE par version.
- **Olvid :** rétention et accès en production, comportement complet du backend, évaluation du binaire 2026, propriétés de chaque plateforme/build et scopes exacts de reports de certification.
- **Threema :** retest Cure53 sur Beta 66, date/commit précis, arrivée de PFS desktop, build du canal stable, contenu exact des retours de demandes agrégées.
- **Briar/Cwtch/Ricochet/Status/Jami/Tox :** nombre d’opérateurs/mainteneurs actuels, deploiement courant, sécurité des clients mobiles, appels et artefacts forensic/versionnés.
- **Forensique :** pour la plupart des clients, aucun résultat public récent ne donne simultanément outil Cellebrite/GrayKey/Magnet, modèle exact, version OS, version application, verrouillage BFU/AFU, résultat et date. La capacité d’un ancien outil ne doit pas être propagée aux versions récentes.
- **Infrastructure :** snapshots DNS/BGP/OSINT n’indiquent pas origine derrière CDN, régions de stockage, journaux internes ou contrôle effectif; les régions changent. Pas d’audit actif d’endpoints.
- **Mobile privacy :** pas d’inspection comparative complète des IPA/APK actuels, de leurs SDK, entitlements, payload push et captures réseau sur les mêmes versions.
- **Droit :** cas scellés, pays non couverts, données FAI/stores/relays et transferts transfrontaliers peuvent modifier le risque; vérification juridique pays/version nécessaire pour un enjeu concret.

## Tests sûrs qui apporteraient le plus de preuve

1. Tester dans un laboratoire avec deux appareils contrôlés le username-only Signal, lookup par numéro désactivé, contacts déjà dans l’adresse et affichage du profil; comparer Android et iOS sans utiliser de comptes tiers.
2. Capturer DNS/connexions/ICE lors d’appels de test sur comptes propres, avec relay activé/désactivé, et vérifier l’IP vue par le pair et par le serveur STUN/TURN pour les versions exactes.
3. Comparer payloads de notifications iOS/Android et comportement avec contenu masqué, push instantané/retardé, comptes et appareils test dédiés.
4. Reconstruire les APK/desktop où une procédure reproductible est documentée, comparer aux artefacts officiels, vérifier signatures, dépendances et provenance; ne pas inférer IPA reproductible à partir d’Android.
5. Créer un jeu d’essai avec photos/docs et examiner localement EXIF, thumbnails, caches, clipboard, bases et notifications; état verrouillé/déverrouillé documenté par modèle/version/heure.
6. Tester l’état du correctif Session uniquement sur environnements et profils contrôlés, avec protocole d’étude et autorisation; faire confirmer les mitigations par les auteurs ou une évaluation indépendante. Pas d’attaque de nœuds réels ni d’utilisateurs.
7. Mesurer la censure uniquement à partir de mesures publiques et appareils autorisés, en enregistrant pays, opérateur, AS, date, DNS/transport et version; ne pas présenter une mesure passée comme état actuel.

## Ce qu’aucune messagerie ne peut complètement résoudre

Un endpoint compromis ou déverrouillé peut exposer l’écran, les bases, les clés, les fichiers et les notifications; un participant peut copier ou photographier le message; une personne peut être corrélée par pseudo, avatar, style, horaire, voix, EXIF ou liens. Un observateur global peut tenter une corrélation de trafic même quand l’IP du pair est masquée. Aucun paramètre d’application ne remplace la maîtrise des appareils, des sauvegardes, des identités et du comportement.
