---
title: Synthèse antérieure — Phase 1 conservée comme repère
description: 'Registre Phase 2 : Synthèse antérieure — Phase 1 conservée comme repère.
  Preuves, périmètres et inconnues documentaires au 14 octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 5
---

# Synthèse antérieure — Phase 1 conservée comme repère

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

!!! warning "Synthèse historique"
    Cette synthèse antérieure est conservée pour la traçabilité. Consulter le [résumé actuel](../resume.md) pour les conclusions de référence.

Le bloc ci-dessous reprend la synthèse comparative déjà établie avant cette Phase 2; il est conservé pour garder le contexte et ne doit pas être lu comme le résultat d’un nouveau classement. En cas d’écart, les fiches probatoires et leurs limites de version/configuration font foi.

Il n’existe pas de messagerie qui maximise simultanément confidentialité du contenu, anonymat réseau, minimisation des métadonnées, maturité, résistance aux appareils saisis et disponibilité grand public. Les gagnants changent avec l’adversaire et le mode d’usage. Chiffrement E2EE, pseudonymat et anonymat sont des propriétés différentes; aucune ne neutralise un téléphone compromis, un correspondant qui divulgue la conversation ou une corrélation de trafic globale.

**Pour le scénario principal — une personne rencontrée sur Discord, sans révéler numéro, email ni identité civile, et en cherchant à éviter l’IP et les liens entre comptes — SimpleX est le meilleur point de départ pratique parmi les solutions évaluées**, sous réserve de créer un profil neuf, de ne pas publier un identifiant réutilisé, de désactiver la synchronisation des contacts, de garder les appels relayés ou de ne pas appeler, et de ne pas partager d’éléments identifiants. Son avantage distinctif est l’absence d’identifiant global public et l’usage de coordonnées de connexion propres aux relations; cela n’empêche ni ses serveurs de voir des connexions/IP et des horaires selon le chemin, ni un observateur réseau de corréler le trafic, ni le contact de conserver le contenu. Confiance : **moyenne**, car aucune capture de trafic ou inspection des binaires mobiles actuels n’a été faite.

**Si masquer l’IP à l’infrastructure est plus important que la simplicité et que les deux personnes peuvent adopter un outil de niche**, Cwtch (Tor v3) et Briar (Tor, plus synchronisation de proximité hors Internet) méritent un essai ciblé. Cwtch expose une adresse de profil persistante et des indices de présence si elle est rendue publique; Briar est principalement une solution Android et ses capacités d’usage distant/offline sont différentes. Leur Tor protège contre certains observateurs locaux, pas contre un adversaire capable de corréler les deux extrémités. Ricochet Refresh présente une architecture similaire mais sa maintenance et sa maturité sont nettement moins établies.

**Je ne recommande pas Session comme choix de sécurité maximale pour le scénario sans vérification corrective préalable** : il a un très bon modèle d’identifiants et de routage des messages, mais le protocole courant reste V1, sans PFS selon sa documentation et avec des attaques indépendantes publiées en 2026 contre l’authentification/l’ordre des messages; ses appels P2P exposent l’IP au correspondant et au service STUN/TURN. Le changement d’Oxen vers le Session Network en 2025 rend en revanche inapplicable, sans nouvelle analyse, toute attaque de consensus portant spécifiquement sur l’ancien réseau Oxen.

Signal demeure un choix de sécurité de contenu et de maturité très solide, mais l’inscription utilise toujours un numéro de téléphone que l’opérateur connaît; un username peut éviter de le montrer au contact, pas de l’effacer du modèle fournisseur/télécom. Olvid et Threema évitent l’obligation d’un numéro ou email, mais ne fournissent pas d’anonymat réseau; Olvid a des observables serveur (clés publiques de destinataires, tailles/horaires dans le modèle étudié), et Threema publie des remises judiciaires agrégées de dates de compte/connexion et, sur opt-in, de hash ou push token. Les messageries grand public comme WhatsApp, Telegram et Discord ne conviennent pas à cet objectif d’identité minimisée; Discord conserve en outre le contexte historique de la rencontre.

L’échange initial sur Discord est lui-même une trace : Discord peut connaître les deux comptes, le texte de l’invitation et l’heure du passage vers une autre app. Un changement de messagerie ne supprime ni l’historique Discord ni le lien déjà visible au contact. Dans un dossier pénal américain rendu public en 2026, Discord a fourni des informations à la police puis a remis des messages directs après mandat; c’est une preuve réelle pour Discord, pas une preuve générale sur les autres services. [Affidavit DOJ, U.S. v. Bryant](https://www.justice.gov/usao-wdwa/media/1464546/dl).
