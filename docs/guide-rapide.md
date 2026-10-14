---
title: Guide rapide — quelle messagerie choisir ?
description: Choisir une messagerie selon le besoin réel : sécurité, pseudonymat, iPhone + PC, métadonnées, IP, groupes et contact inconnu.
search:
  boost: 4
---

# Guide rapide — quelle messagerie choisir ?

Cette page est faite pour quelqu’un qui ne veut pas lire toute l’étude.

Le point important : **il n’existe pas de meilleure messagerie dans l’absolu**. Le bon choix dépend surtout de ce que vous essayez de protéger et contre qui.

## Réponse courte

| Votre besoin principal | À regarder en premier | Pourquoi | Limite principale |
|---|---|---|---|
| Messagerie sûre et simple sur iPhone + PC | **Signal** | E2EE mûr, applications officielles, bonne ergonomie | Numéro toujours nécessaire à l’inscription et connu du service |
| Parler sous un pseudonyme à quelqu’un rencontré en ligne | **SimpleX** | Pas de numéro, pas d’e-mail, pas d’identifiant utilisateur global | Les relais, le push et les appareils voient encore des métadonnées |
| Ne pas donner son numéro au contact | **SimpleX, Threema, Olvid** | Aucun numéro n’est nécessaire pour être joint | Cela ne rend pas automatiquement anonyme sur le réseau |
| Cacher au mieux son IP au correspondant | **SimpleX avec TURN, Olvid, Signal en mode relayé** | L’appel passe par un relais au lieu d’être direct | Le relais voit alors l’IP et la durée de la connexion |
| Réduire l’observation réseau avec Tor | **Cwtch ou Briar** | Architecture Tor/onion | Pas de client iOS officiel établi ici ; outils spécialisés |
| Grande équipe / serveur choisi | **Matrix / Element** | Fédération, contrôle du homeserver, groupes et multi-device | Le homeserver conserve beaucoup de métadonnées |
| Adoption maximale auprès de proches | **Signal**, puis WhatsApp si nécessaire | Faciles à faire adopter | WhatsApp lie fortement le compte au numéro et à l’écosystème Meta |

## Les cinq choses à comprendre avant de choisir

1. **E2EE ne veut pas dire anonyme.** Le texte peut être illisible par le serveur alors que l’IP, les horaires, le compte ou les destinataires restent observables.
2. **Le téléphone compte autant que l’application.** Un appareil déverrouillé, compromis ou mal sauvegardé peut exposer les messages après déchiffrement.
3. **Les appels ont leur propre chemin réseau.** Un appel P2P peut révéler l’IP au correspondant ; TURN masque l’IP au pair mais la donne au relais.
4. **Le pseudonyme doit être réellement séparé.** Réutiliser avatar, pseudo, e-mail, photo, fichier, style ou horaires peut relier les comptes.
5. **Changer de Discord vers une autre app n’efface pas Discord.** Le compte d’origine, l’heure et le message d’invitation peuvent déjà former une corrélation.

## Signal ou SimpleX ?

**Signal** est généralement plus simple, plus mature et plus pratique sur iPhone + PC. Avec la visibilité du numéro et la découverte par numéro réglées sur `Nobody`, puis un username distinct partagé directement, le contact n’a pas besoin de connaître votre numéro. Le service Signal, lui, reçoit toujours un numéro valide lors de l’inscription.

**SimpleX** est plus intéressant si l’objectif principal est de séparer des relations pseudonymes : pas de numéro obligatoire, pas d’e-mail obligatoire et pas d’identifiant utilisateur global. En contrepartie, l’écosystème, le multi-device et certains flux réseau sont moins simples à raisonner.

## Et Session ?

Session a un modèle d’identité et de routage intéressant, mais le rapport le rétrograde pour les usages d’assurance élevée en attendant une clarification documentée des correctifs et retests après les attaques publiées à WOOT 2026. Les appels bêta sont également P2P et peuvent révéler l’IP au correspondant.

## Si vous ne savez toujours pas quoi prendre

- **Usage quotidien classique : Signal.**
- **Identité pseudonyme séparée : SimpleX.**
- **Pas de numéro à donner : SimpleX, Threema ou Olvid.**
- **Tor / environnement réseau hostile : Cwtch ou Briar si vos plateformes le permettent.**

Ce ne sont pas des garanties absolues. Pour comprendre pourquoi, lire ensuite [le comparatif](comparatif.md), [les métadonnées](metadonnees.md) et [les threat models](threat-models.md).
