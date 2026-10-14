---
title: OPSEC
description: Recommandations proportionnées pour les identités, appels, appareils,
  fichiers et notifications.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 363
---

# OPSEC

## Pour SimpleX

- Créer un profil distinct et une invitation à usage unique par relation; ne pas utiliser de nom public `.simplex` pour un pseudonyme.
- Éviter de synchroniser des contacts qui ne sont pas nécessaires; ne pas injecter le profil dans un compte cloud/personnel.
- Sur iOS, choisir consciemment entre notification instantanée et moindre exposition des métadonnées; masquer le contenu des previews écran verrouillé.
- Garder TURN/relais imposé pour les appels si le contact ne doit pas voir l’IP; le relais verra l’adresse et la durée. Désactiver les appels si aucun besoin.
- Ne jamais envoyer originaux photo/documents sans inspecter EXIF, auteur, chemins, miniatures, noms de fichiers et historiques.

## Pour Signal en configuration pseudonyme

- Inscrire avec un numéro que l’utilisateur accepte d’exposer au service et à l’opérateur télécom; « non-public » n’est pas synonyme de « non-lié ».
- Mettre la visibilité ET la recherche par numéro sur `Nobody`; partager seulement un username neuf par canal choisi.
- Ne pas réutiliser profil, avatar, nom, groupe, lien public, sauvegarde ou carnet de contacts identifiant.
- Appairer uniquement ses propres PCs, contrôler les appareils liés et les retirer après usage; garder l’iPhone et le PC à jour.
- Vérifier les safety numbers par canal indépendant, surtout avec un nouveau correspondant; AKV n’atteste pas son identité civile.
- Limiter les notifications sur écran verrouillé; tenir compte du cas historique iOS de notifications, corrigé par Apple selon l’avis 26.4.2, sans extrapoler avant/après correctif.

## Pour Olvid / Threema

- Vérifier en personne/par canal séparé l’identité ou l’empreinte attendue; ne pas supposer que clé/profile de compte signifie personne vérifiée.
- Si PC nécessaire, considérer explicitement le coût et les propriétés de multi-device; sur Threema beta, accepter l’absence de PFS sur Desktop 2.0 ou éviter ce mode si PFS exigée.
- Régler les calls sur TURN/relais si l’IP au contact importe; distinguer l’IP exposée au relais.

## Pour tous

- Un terminal à jour, code robuste, chiffrement OS, verrouillage court et sauvegarde maîtrisée protègent souvent plus qu’un changement de messagerie.
- Réduire les comptes liés et permissions contacts/localisation/micro/caméra; activer micro/caméra seulement lors d’usage explicite.
- Couper previews de notifications, vérifier les appareils liés et les clés après migration ou ajout d’appareil.
- Ne pas choisir VPN/Tor mécaniquement : identifier l’observateur déplacé, tester le chemin réellement pris, éviter une fuite hors tunnel et considérer l’empreinte liée aux horaires.
- Séparer l’identité avant le premier contact : pseudo, image, signature linguistique, heures, e-mail, téléphone, cloud et partage de fichier peuvent reconstituer le lien.
- Ne jamais compter sur message éphémère pour empêcher sauvegarde, capture, caméra externe ou export par le destinataire.
