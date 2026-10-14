---
title: Discord → messagerie privée
description: Gains et limites d’une migration depuis Discord vers SimpleX, Signal
  renforcé, Threema ou Olvid.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 349
---

# Discord → messagerie privée

Le passage de Discord à une messagerie privée améliore l’exposition du contenu seulement si la nouvelle messagerie E2EE protège effectivement ce contenu. Il ne supprime pas les traces déjà chez Discord : compte d’origine, heure du contact, message d’invitation, membres du serveur, IP de connexion et potentiellement historique de modération. Si la personne reçoit un lien depuis Discord, Discord peut savoir quel compte l’a envoyé à quel compte, même si le lien est aléatoire et le contenu ultérieur chiffré.

| Dimension | Discord | Après migration vers SimpleX / Signal renforcé / Threema / Olvid |
|---|---|---|
| Texte | Serveur Discord accessible/traitable; pas E2EE | E2EE pour les conversations ciblées; Discord conserve l’historique antérieur |
| Identité | Compte, serveur, username/historique social centralisés | Le contact reçoit seulement l’ID/lien/profil volontaire; risque de pseudo/avatar/langage réutilisé |
| IP | Discord voit IP de connexion; partenaire ne l’obtient pas généralement par les DMs | Le nouveau service/relay voit le chemin; un appel P2P peut transmettre l’IP au correspondant; un transfert d’invitation crée une jointure temporelle |
| Métadonnées | Compte, membership, messages et activité de service centralisés | Moins d’exposition chez le nouveau fournisseur selon architecture, mais push, FAI, stores, contacts et relais restent |
| Recours légal | Preuve U.S. v Bryant : messages et champs de compte effectivement remis dans une affaire | Réduction variable de ce que l’opérateur peut déchiffrer/remettre; le terminal et participant peuvent toujours fournir le contenu |

Pour une rencontre inconnue sur Discord, le choix de référence est **SimpleX** si les deux parties maîtrisent le profil par relation et peuvent accepter ses limites iOS/desktop. **Signal configuré comme ci-dessus** est une alternative très raisonnable si l’on privilégie l’ergonomie, l’adoption et PC, dès lors que le numéro est traité comme secret connu du fournisseur et que l’identité de l’autre partie est vérifiée. **Threema/Olvid** conviennent si la question principale est de ne pas révéler le numéro au contact; ni l’un ni l’autre ne fournit un anonymat réseau. Cwtch/Briar ne sont pas recommandés pour un utilisateur iPhone; Session n’est pas choix d’assurance maximale jusqu’à résolution et retest des findings WOOT.
