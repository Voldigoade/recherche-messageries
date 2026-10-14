---
title: Comment lire cette étude
description: 'Définitions : E2EE, pseudonymat, anonymat, métadonnées et statuts de
  preuve.'
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 25
---

# Comment lire cette étude

| Terme | Sens opérationnel retenu ici |
|---|---|
| Chiffrement en transit | Protège une connexion entre deux points (par exemple appareil–serveur). Le serveur termine généralement ce chiffrement et peut lire ce qu’il reçoit si le contenu n’est pas autrement chiffré. |
| Chiffrement côté serveur | Chiffrement au repos contrôlé par l’opérateur; il protège surtout contre certains accès aux supports, pas nécessairement contre l’opérateur qui détient les clés. |
| Chiffrement de bout en bout (E2EE) | Les clés de contenu sont contrôlées par les terminaux des participants; l’opérateur de transport ne devrait pas pouvoir lire le contenu applicatif. Cela ne cache pas automatiquement IP, temps, volume, identité, graphe social, push, fichiers locaux ou destinataire. |
| Sécurité | Capacité à prévenir, détecter ou limiter les violations de confidentialité, intégrité, disponibilité et authenticité face à un adversaire défini. |
| Confidentialité / vie privée | Réduction des données révélées, observées, conservées, corrélées ou réutilisées; peut concerner le contenu ou les métadonnées. |
| Pseudonymat | Usage d’une identité distincte de l’identité civile. Un numéro, appareil, adresse IP, achat ou profil réutilisé peut la relier à la personne. |
| Anonymat | L’adversaire défini ne peut raisonnablement distinguer l’utilisateur de l’ensemble d’anonymat pertinent. Un compte sans téléphone n’est pas automatiquement anonyme. |
| Unlinkability | Difficulté à établir que deux identifiants, relations, sessions ou activités renvoient au même utilisateur. |
| Unobservability / résistance aux métadonnées | Difficulté à détecter qu’une communication a eu lieu, ou à en inférer les participants et le rythme. Chiffrement seul ne fournit pas cette propriété. |
| Forward secrecy (PFS) | Une compromission ultérieure de clés à long terme ne devrait pas permettre de déchiffrer les anciens messages protégés par des clés éphémères déjà supprimées. La propriété est dépendante du protocole et de son implémentation; elle n’est pas uniforme dans tous clients/appareils liés. |
| Post-compromise security | Après compromission temporaire d’un état de session, des échanges futurs peuvent retrouver la confidentialité après une évolution sûre des clés. Ce n’est pas une réparation d’un terminal encore contrôlé. |
| Deniability | Possibilité de contester cryptographiquement l’origine d’un message, selon le protocole. Ce n’est pas l’impossibilité de prouver un contenu par une capture, un terminal ou un témoin. |
| Key transparency | Mécanisme permettant de vérifier la cohérence de l’association identifiant–clé publiée; il ne certifie pas l’identité civile de la personne contrôlant cet identifiant. |
| Résistance à l’analyse de trafic | Capacité à limiter les inférences tirées des horaires, tailles, volumes et chemins réseau; du padding, des délais, du trafic de couverture ou un mixnet peuvent aider, mais aucun mécanisme ne garantit automatiquement l’immunité à la corrélation globale. |

Les statuts de preuve sont utilisés comme suit : **FAIT / OBSERVÉ** signifie établi par une source ou une observation datée; **DÉCLARATION** est la position officielle du fournisseur; **INDÉPENDANT** est une étude, audit, décision ou preuve externe; **INFÉRENCE** est un raisonnement explicité; **INCONNU** signifie que les sources disponibles ne tranchent pas. « Aucun cas public retrouvé » est toujours une limite de recherche, jamais une preuve d’absence.
