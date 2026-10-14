---
title: Résumé
description: Les conclusions du rapport sur la sécurité, la vie privée et le pseudonymat
  des messageries, avec leurs limites.
search:
  boost: 2
source_file: rapport-final-messageries.md
source_line: 8
---

# Résumé

1. **Il n’existe pas de gagnant universel.** Le meilleur choix dépend surtout de l’adversaire, de l’identité que l’on accepte de révéler, du besoin d’appels, du terminal et de la capacité à maintenir une configuration correcte.
2. **E2EE n’est pas anonymat.** Un fournisseur peut ne pas lire le texte et néanmoins connaître l’adresse IP, l’heure, le compte, l’appareil, les destinataires ou l’appartenance à des groupes.
3. **Pour passer d’un contact Discord à une identité séparée, SimpleX est le choix le plus cohérent si le correspondant l’accepte.** Il ne demande pas de numéro, d’e-mail ni d’identifiant global; l’invitation est propre à la relation. Le premier relais, les notifications iOS, Discord et les terminaux restent des observateurs distincts.
4. **Signal mérite une réévaluation favorable en configuration pseudonyme renforcée.** Avec `Who can see my number = Nobody`, `Who can find me by my number = Nobody`, username non réutilisé partagé directement, profil neutre et vérification de clé, le correspondant n’a pas à recevoir le numéro. Signal conserve toutefois un numéro nécessaire à l’inscription : « caché au contact » ne signifie pas « inconnu du fournisseur » ni « non lié à l’identité civile ».
5. **Pour iPhone + PC, Signal est un compromis très praticable** : clients officiels desktop Windows/macOS/Linux, mais le téléphone reste l’appareil principal et sert à l’appairage. SimpleX fonctionne aussi sur ces plateformes, mais l’appairage mobile–desktop documenté exige le même réseau local; l’usage du profil sur plusieurs appareils est moins transparent.
6. **Olvid et Threema répondent bien au besoin “ne pas donner mon numéro au contact”**, mais pas à une exigence d’anonymat réseau. Olvid multi-appareil et appels nécessitent une licence après l’essai. Threema Desktop 2.0 est encore bêta; sa PFS n’est pas prise en charge dans cette bêta.
7. **Session est rétrogradé provisoirement pour les scénarios d’assurance élevée.** Un article USENIX WOOT 2026 décrit des attaques pratiques contre Session Protocol V1 (substitution de clé/usurpation, falsification de timestamps, suppression/rejeu). Le statut exact de correction et de retest des versions utilisées doit être vérifié avant tout retour à un niveau de confiance supérieur. Ses appels bêta exposent en outre l’IP au correspondant et au STUN/TURN géré.
8. **Cwtch et Briar sont des options spécialisées, pas des choix pratiques pour un utilisateur iPhone.** Les deux n’ont pas de client iOS officiel établi dans le dossier. Briar Desktop existe en bêta, mais le projet annonce depuis juillet 2026 ne faire que des correctifs essentiels et des mises à jour de sécurité.
9. **Les appels sont un chemin réseau distinct des messages.** TURN protège généralement l’IP vis-à-vis du correspondant mais révèle l’IP et la durée au relais. P2P/WebRTC peut révéler directement l’IP au pair. Un appel E2EE peut donc cacher la voix au relais tout en lui donnant des métadonnées réseau.
10. **Les preuves judiciaires réelles sont inégales.** Signal rapporte en 2026 avoir remis dates de création et dernière connexion pour six comptes, pas le contenu. Threema publie des totaux de demandes et de remises de données de compte. Discord a remis messages et données de compte dans une affaire pénale américaine documentée. Pour plusieurs autres services, aucun cas concret n’a été identifié ici : cela ne prouve pas qu’il n’en existe aucun.
11. **Les appareils dominent face à une saisie déverrouillée ou un spyware.** Aucun chiffrement de transport ne protège des messages après déchiffrement sur le terminal, d’une notification affichée, d’un destinataire qui fait une capture, ou d’un appareil compromis.
12. **Les builds distribués n’ont pas été reconstruits bit à bit dans cette enquête.** Code public, tags signés, procédure de build ou manifest source ne prouvent pas à eux seuls que l’APK/IPA installé correspond au code publié.
13. **Le choix pratique pour “inconnu rencontré sur Discord” :** SimpleX si l’acceptation et la configuration sont réalistes; Signal renforcé si l’adoption, l’ergonomie et iPhone + PC priment et si le numéro d’inscription n’est pas publiquement relié à l’identité; Threema/Olvid si la priorité est l’absence de numéro transmis au pair, avec les limites de multi-device indiquées.
14. **Aucun service évalué ne démontre une résistance générale à un adversaire passif global.** Les réseaux à faible latence, y compris les réseaux onion, laissent des possibilités de corrélation temporelle/volumétrique si l’adversaire observe assez de points.
