# Messageries : rapport final sécurité, vie privée et pseudonymat

**Version de référence : 1.0 — 14 octobre 2026**  
**Périmètre :** Signal, SimpleX, Olvid, Session, Threema, Cwtch, Briar, Jami, Tox/qTox, Matrix/Element, XMPP/OMEMO, Telegram, WhatsApp, Discord, Wire, Delta Chat, Ricochet Refresh et Status/Waku. Molly et Bitchat sont traités comme candidats complémentaires, pas comme réseaux distincts comparables à tous les autres.

Ce rapport remplace les classements numériques de l’ancienne Phase 3. Les notes entières sur 10 donnaient une précision non défendable au vu des écarts de périmètre, de version, de configuration et de preuve. Les anciens fichiers de recherche restent des pièces de travail : [dossier d’enquête Phase 2](enquete-messageries-progress.md) contient les fiches détaillées et le registre de preuves par produit; [ancienne Phase 3](enquete-messageries-phase3.md) est conservée comme trace historique, mais ses scores et verdicts ne doivent pas être repris comme conclusion actuelle.

## 1. Résumé lisible en deux minutes

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

## 2. Termes et lecture des preuves

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

## 3. Méthodologie et limites de cette version

Le rapport consolide le travail des Phases 1–3, les fiches de Phase 2, les audits, articles académiques, advisories, politiques, rapports de transparence, affaires judiciaires et vérifications web actualisées. Les sources de la Phase 2 restent la pièce principale pour les détails d’implémentation, les audits lus, les vulnérabilités, les observations d’infrastructure, les métadonnées par produit et les questions expérimentales.

Les conclusions sont conditionnelles à la date **14 octobre 2026**. Les produits changent; une conclusion sur une version ne vaut pas pour toutes les plateformes ni toutes les versions. Les politiques officielles décrivent les engagements de l’éditeur, pas nécessairement une observation indépendante des systèmes de production. Les études académiques sont limitées à leurs modèles, builds et protocoles examinés. Les décisions judiciaires décrivent un cas, une juridiction et un périmètre donnés.

**Travail effectivement réalisé :** recherches web et consultation de sources primaires; lecture des dossiers existants; lecture détaillée de plusieurs rapports PDF consignés en Phase 2; échantillons d’activité Git/release et manifests Android source; observations DNS/BGP passives limitées, datées et consignées pour quelques endpoints. Aucun scan de ports, accès non autorisé, compte de test, capture de paquets applicative, extraction Cellebrite/GrayKey/Magnet ni reconstruction bit-à-bit d’un binaire n’a été réalisé ici.

**Limite documentaire locale :** le répertoire `sources/` du miroir de projet était vide lors du contrôle. Le rapport cite donc des URL de sources externes et renvoie au dossier Phase 2, sans prétendre que des PDFs locaux absents ont été relus durant cette consolidation.

**Confiance globale :** moyenne pour les propriétés protocolaires bien documentées et les résultats judiciaires explicitement publiés; faible à moyenne pour les métadonnées en production, les appels par version, les builds distribués, la forensique mobile actuelle et la résistance à la censure par pays/opérateur. Les inconnues ne sont pas converties en échec certain ou en réussite certaine.

## 4. Candidats et compatibilité réelle

La comparaison distingue application, protocole, réseau et opérateur. Matrix est un protocole fédéré; Element est un ensemble de clients et de services. XMPP est un protocole, OMEMO une extension E2EE, et l’opérateur du serveur ainsi que le client choisi déterminent le résultat. Tox/qTox, Jami, Cwtch ou Ricochet Refresh ne partagent pas une infrastructure unique. Les architectures P2P réduisent parfois la visibilité centrale mais peuvent exposer l’IP aux pairs.

| Produit | Nature / architecture dominante | iPhone | PC | État pratique pertinent au 14-10-2026 |
|---|---|---:|---:|---|
| Signal | Service centralisé; E2EE Signal Protocol; téléphone à l’inscription | Oui | Windows/macOS/Linux | Desktop officiel appairé au téléphone. La disponibilité multiplateforme ne rend pas le compte anonyme. [Téléchargements](https://signal.org/download/) |
| SimpleX | Relais store-and-forward, pas d’identifiant global d’utilisateur | Oui | Windows/macOS/Linux | Profils locaux; appairage mobile–desktop documenté sur le même réseau local. Builds desktop actuels marqués bêta sur la page téléchargements. [Téléchargements](https://simplex.chat/downloads/) |
| Olvid | Service centralisé de rendez-vous/transport; identité cryptographique | Oui | Windows/macOS/Linux | Multi-device simultané sous licence après essai; historique antérieur non transféré automatiquement au nouvel appareil. [FAQ multi-appareil](https://olvid.io/faq/use-olvid-on-multiple-devices/) |
| Session | Réseau décentralisé de nœuds de service/onion routing pour messages | Oui | Windows/macOS/Linux | Appels audio/vidéo bêta, activés opt-in, P2P; statut des mitigations de l’étude WOOT 2026 non établi ici. [FAQ](https://getsession.org/faq) |
| Threema | Service centralisé et identifiant Threema aléatoire | Oui | Windows/macOS/Linux | Desktop 2.0 multi-device est bêta, jusqu’à deux ordinateurs, PFS non supportée; le client Web/Desktop ancien dépend du téléphone. [Limites bêta](https://threema.com/en/faq/md-limit) |
| Cwtch | Messages via services onion/Tor; profils locaux, pas de service central unique | Pas de client officiel établi | Windows/macOS/Linux, Android | Candidat de niche; mainteneurs et assurance moins étendus que les services grand public. L’absence d’iOS exclut l’usage iPhone natif. [Téléchargements](https://docs.cwtch.im/it/download/) |
| Briar | Android : store-and-forward chiffré via Tor, avec options locales Bluetooth/Wi-Fi; client desktop distinct en bêta | Non | Desktop Linux/Windows/macOS bêta | En maintenance depuis juillet 2026 : correctifs essentiels et de sécurité uniquement; desktop ne comble pas l’absence d’iOS. [Annonce maintenance](https://briarproject.org/news/2026-maintenance-mode/), [desktop](https://briarproject.org/download-briar-desktop/) |
| Jami | P2P distribué/DHT, appels et messages | Oui | Windows/macOS/Linux | Pas de serveur central unique, mais DHT, bootstrap, relais, NAT traversal et clients restent dans le modèle de confiance. |
| Tox/qTox | Protocole P2P et implémentations indépendantes | Dépend d’un client tiers; qTox n’est pas le client iOS | qTox surtout desktop | Les garanties varient fortement entre implémentations; IP directe lors de connexions/appels P2P possible. |
| Matrix / Element | Protocole fédéré + homeservers; Element clients/hosting | Oui | Windows/macOS/Linux/Web | Choix du homeserver, salons chiffrés, fédération, push, identité et SFU changent le threat model. [Spécification](https://spec.matrix.org/latest/) |
| XMPP / OMEMO | Protocole fédéré + extension E2EE + client/serveur choisis | Dépend du client | Dépend du client | Pas de verdict générique sans nommer serveur, client, version et réglages OMEMO. [XEP-0384](https://xmpp.org/extensions/xep-0384.html) |
| Telegram | Service centralisé cloud; Secret Chats séparés | Oui | Windows/macOS/Linux/Web | Cloud Chats et groupes ne sont pas E2EE; Secret Chats sont un mode distinct, généralement 1:1 et lié aux appareils. |
| WhatsApp | Service centralisé Meta; E2EE de contenu par défaut pour conversations personnelles | Oui | Windows/macOS/Web | Numéro et graphe d’usage restent identifiants importants; sauvegardes et comptes Meta/OS sont à considérer. |
| Discord | Plateforme centralisée de communautés/DM | Oui | Windows/macOS/Linux/Web | Texte non E2EE; DAVE chiffre l’audio/vidéo des appels éligibles, pas les messages texte. |
| Wire | Service centralisé orienté équipes, code client partiellement public | Oui | Windows/macOS/Linux/Web | Compte, configuration et services hébergés importent; un cas public établit la remise d’un e-mail d’inscription. |
| Delta Chat | Client de messagerie basé sur e-mail/chatmail; chiffrement Autocrypt selon conversation | Oui | Windows/macOS/Linux | La confidentialité et l’E2EE dépendent aussi du fournisseur e-mail, de la compatibilité du contact et du client. |
| Ricochet Refresh | Messagerie desktop 1:1 via Tor onion services | Non | Windows/macOS/Linux | Petit projet; mises à jour, assurance actuelle, groupes/appels et supply chain peu établis. Audit du Ricochet historique non transférable au Refresh actuel. |
| Status / Waku | Application et protocoles Waku/Logos, infrastructure de nœuds distribuée | Mobile selon versions | Client desktop stable non établi dans cette étude | À distinguer d’une messagerie centralisée; les nœuds gérés peuvent quand même observer IP/topics et métadonnées. |

**Candidats complémentaires.** Molly est un fork Android de Signal : il change certaines propriétés locales et de transport, mais conserve le réseau Signal et son exigence de numéro; ce n’est pas un réseau indépendant. Bitchat est un projet mesh Bluetooth/Nostr expérimental; son auditabilité, son modèle d’identité et son comportement selon les versions ne justifient pas de le classer au même niveau que les services matures. Les détails figurent dans la Phase 2.

## 5. Tableau comparatif final — capacités et limites structurantes

| Produit | Identité / découverte | Contenu et métadonnées | IP au correspondant et appels | Limite structurante / confiance |
|---|---|---|---|---|
| Signal | Numéro d’inscription obligatoire; username facultatif, sans annuaire public. Les réglages de visibilité et de recherche sont séparés. | E2EE mature pour messages/appels; le fournisseur ne voit pas le corps normal mais conserve des données de compte et peut remettre certaines métadonnées. | Appels relayables; vérifier le réglage et le chemin réel. | Très bon compromis sécurité/adoption, mais lien numéro–compte persiste côté service. AKV améliore la transparence des clés, pas l’identité civile. |
| SimpleX | Profil local sans ID global; lien/QR de connexion par relation. | E2EE Double Ratchet et padding déclaré pour les messages; files relais temporaires, métadonnées transport et push iOS restent des surfaces. | TURN par défaut masque l’IP au pair; le relais observe IP et durée; P2P révèle l’IP au correspondant. | Modèle d’identité/métadonnées distinctif, avec davantage de friction multi-device et de dépendance aux relais configurés. Les déclarations de non-logging restent des déclarations sans capture indépendante courante. |
| Olvid | Pas de téléphone/e-mail obligatoire; identité cryptographique. | Analyse indépendante 2026 du protocole sous hypothèses formelles; l’étude indique que le serveur voit des clés de routage, tailles et timings. | Documentation de calls TURN-only protège l’IP au pair mais pas au relay. | Métadonnées réseau et infrastructure demeurent; multi-device et appels payants après période d’essai. |
| Session | ID aléatoire, pas de numéro requis; routage onion pour messages selon réseau. | Les messages utilisent Session Protocol V1; l’étude WOOT 2026 trouve des défauts d’authentification et de compteurs. | Appels bêta P2P révèlent l’IP au correspondant et au STUN/TURN géré par STF. | Ne pas recommander pour assurance maximale avant preuve du correctif et retest sur version distribuée. Le réseau a évolué depuis Oxen, donc les résultats spécifiques à l’ancien consensus ne se transfèrent pas mécaniquement. |
| Threema | ID aléatoire; téléphone/e-mail facultatifs pour découverte. | E2EE; contrôle fournisseur moins riche en identité civile si aucun identifiant n’est lié, mais IP/timestamps/IDs existent. | Les modes d’appel et relais doivent être vérifiés par client/configuration. | Très établi côté mobile; Desktop 2.0 bêta sans PFS, deux PCs maximum et fonctionnalités incomplètes. |
| Cwtch | Profil sans téléphone/e-mail; contacts établis par échange d’invitations. | E2EE via Tor onion services et profil local selon conception annoncée. | Pas d’appels actuels établis dans le dossier. | Bon cloisonnement théorique vis-à-vis d’un service central, mais écosystème niche, maintenance et audits plus limités, pas d’iOS. |
| Briar | Identité locale; contact à proximité ou via invitation. | Chiffrement de bout en bout; Tor, réseau local, Bluetooth/stockage amovible sur Android. | Pas d’appels voix actuels établis. | Fort intérêt pour résilience hors Internet, mais UX, consommation et fonctionnalités limitées; projet désormais en maintenance essentielle, pas de client iOS. |
| Jami | Clé/identité; découverte DHT/P2P. | Chiffrement selon protocoles et fonctionnalités du client; métadonnées réparties entre pairs/services. | P2P peut exposer IP; relay/NAT traversals diffèrent par chemin. | Ne pas confondre « sans serveur central » avec protection contre le correspondant, les nœuds et la corrélation. |
| Tox/qTox | Clé publique/ID Tox; pas de numéro imposé par le protocole. | E2EE dans le protocole Tox, mais sécurité opérationnelle varie entre implémentations. | Connexions P2P/appels peuvent révéler les IP. | Couverture audits, maintenance et clients mobiles inégaux; il faut nommer précisément le client. |
| Matrix/Element | MXID `@nom:serveur`; serveur choisi; e-mail/téléphone facultatifs ou exigés par certains homeservers. | E2EE par salon, non automatique partout; serveur voit membership, événements de contrôle, comptes, appareils et IP. | WebRTC peut être direct ou via TURN/SFU; SFU voit IP et métadonnées même lorsque le média est chiffré. | Un homeserver auto-hébergé change l’opérateur mais ne supprime pas la fédération, les backups, push ou risques de salon non chiffré. |
| XMPP/OMEMO | JID sur domaine/serveur; adresse e-mail/nom peuvent être implicites ou corrélables. | OMEMO chiffre le contenu lorsque actif et compatible; serveur conserve JID, présence, roster/metadata et messages chiffrés selon config. | Jingle/ICE peut être direct; TURN masque pair mais voit IP. | Le résultat dépend principalement du serveur, client, version, gestion des appareils et configuration OMEMO. |
| Telegram | Numéro requis; username facultatif; lookup/réglages d’annuaire. | Cloud Chats par défaut côté serveur; Secret Chats E2EE distincts; groupes/channels cloud. | Appels relayables/directs selon réglage/réseau. | Très fonctionnel mais E2EE non universel; ne pas présenter « Telegram chiffré » sans préciser le mode. |
| WhatsApp | Numéro requis, carnet d’adresses et écosystème Meta. | E2EE par défaut messages/appels personnels; Meta traite beaucoup de métadonnées et la sauvegarde dépend du paramétrage. | Appels peuvent utiliser relay pour masquer IP au correspondant; service Meta demeure central. | Contenu protégé dans le périmètre E2EE, mais forte liaison au numéro, au graphe social, appareil et compte écosystème. |
| Discord | Compte avec identifiant/username, e-mail/téléphone parfois; serveurs/groupes identifiants. | Texte/DM lisibles par plateforme; DAVE E2EE pour médias d’appels éligibles uniquement. | Architecture d’appel relayée réduit généralement l’exposition directe pair-à-pair, mais révèle IP au service de voix. | À garder pour communautés/collaboration, pas comme canal confidentiel pour le texte. |
| Wire | Compte et découverte selon offre/configuration; e-mail téléphone selon inscription. | E2EE de contenu dans le produit; serveurs et comptes gardent de la métadonnée. | Appels relayés ou directs selon service et config. | Code et audits présents mais pas équivalents à une inspection intégrale de l’infrastructure et des builds. |
| Delta Chat | E-mail/chatmail comme adresse; profil local et liens d’invitation. | Autocrypt peut E2EE les échanges; le serveur mail voit les adresses et métadonnées SMTP/IMAP; chiffrement dépend du contact. | Appels WebRTC peuvent être P2P et exposer IP; TURN change le point de confiance. | Bonne portabilité et modèle familier; assurance E2EE non uniforme, messagerie et mail provider forment une seule chaîne. |
| Ricochet Refresh | Identité par onion service; sans compte central téléphone/e-mail. | Messages via canal Tor onion; manque de preuve contemporaine suffisante sur ratchet, audits et rétention locales. | Pas d’appels actuels établis. | Surface réseau intéressante mais maintenance, maturité et audits récents faibles/inconnus; ne pas transformer l’audit de Ricochet historique en audit Refresh. |
| Status/Waku | Profil wallet/clé et identifiants Status selon fonctionnalités. | Protocoles E2EE annoncés; nœuds Waku peuvent voir IP/topic/activité selon service. | Appels ne sont pas établis comme avantage actuel. | Le mot « décentralisé » ne dit pas combien d’opérateurs réels ni ce qu’un nœud voit; assurance et ergonomie évoluent. |

## 6. Matrice TM1–TM15

La matrice évalue une résistance relative et non la sécurité absolue. La cellule dépend du mode par défaut ou de la configuration courante documentée; un réglage explicite (par exemple TURN, salons E2EE ou visibilité du numéro) peut la déplacer. `✅` signifie une résistance relativement forte à cette menace, `🟡` partielle, `🟠` exposition importante, `🔴` faible résistance, `❓` données insuffisantes. Les cellules `❓` ne sont pas des notes négatives.

| Threat model | Signal | SimpleX | Olvid | Session | Threema | Cwtch | Briar | Jami | Tox/qTox | Matrix/Element | XMPP/OMEMO | Telegram | WhatsApp | Discord | Wire | Delta Chat | Ricochet | Status/Waku |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| TM1 Fournisseur curieux | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟠 | 🟡 | ✅ | 🟠 |
| TM2 Infrastructure compromise | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ✅ | ✅ | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM3 Opérateur malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | ✅ | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | 🔴 | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 |
| TM4 ISP / Wi-Fi / LAN | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM5 Observateur passif multipoint | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM6 Adversaire global passif | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 |
| TM7 Contact malveillant | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟠 | 🟡 | 🟠 |
| TM8 Harceleur / doxxer OSINT | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | 🟠 |
| TM9 Demande judiciaire classique | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | ✅ | ✅ | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM10 Enquête sophistiquée multi-source | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🟠 | 🟠 |
| TM11 Appareil verrouillé | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | 🟡 | 🟡 | 🟡 | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ | 🟡 | ❓ |
| TM12 Appareil déverrouillé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM13 Spyware / terminal contrôlé | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| TM14 Supply-chain compromise | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟠 |
| TM15 Censure étatique | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 |

### Justification courte des lignes

- **TM1–TM3 :** le chiffrement protège le contenu face à un serveur honnêtement curieux ou compromis, mais un opérateur peut voir les métadonnées qu’expose l’architecture et contrôler disponibilité, rendez-vous, distribution client et mises à jour. SimpleX/Cwtch/Briar/Ricochet réduisent l’identifiant central; ce n’est pas une preuve qu’aucun nœud ou client ne peut les corréler. Pour Session, le résultat WOOT 2026 pèse particulièrement sur TM2/TM3.
- **TM4–TM6 :** TLS/E2EE masque le contenu, pas l’IP du service, les horaires et le volume. Tor/onion peut masquer une IP de destination à certains observateurs locaux, mais ne prouve pas l’immunité à l’analyse de trafic. Aucun service ne démontre une résistance générale à TM6.
- **TM7–TM8 :** absence de numéro/annuaire et identités par contact aident contre un pair/doxxer, mais profil, pseudo réutilisé, fichiers, liens, voix, habitudes et appels P2P peuvent défaire la séparation. La relation Discord initiale demeure chez Discord si le lien d’invitation y est partagé.
- **TM9–TM10 :** la possibilité de remettre une donnée et une remise observée sont distinctes. Données fournisseurs, télécom, store, FAI, appareils, participants et OSINT s’additionnent. Les rangs ne sont pas une garantie juridique; voir §9.
- **TM11–TM13 :** la forensique d’appareil verrouillé est versionnée et les preuves contemporaines sont rares; les nombreuses cellules restent `❓`. Déverrouillé/compromis, l’app peut afficher le texte en clair, donc résistance faible pour tous.
- **TM14 :** le code public facilite l’inspection mais aucun build distribué de l’ensemble des clients n’a été reproduit dans cette mission. Le client fermé, pipeline d’update, dépendances, magasins et clés de signature restent des surfaces.
- **TM15 :** Briar dispose de Tor/bridges et transports locaux sur Android, mais l’état maintenance réduit la pérennité; fédération, P2P, Tor et auto-hébergement peuvent diversifier les points de panne, pas empêcher blocages de stores, DNS, IP, protocoles ou bootstrap.

Cette matrice reprend la grille consolidée de la Phase 2, après contrôle de configuration et d’actualité; chaque colonne renvoie au dossier individuel correspondant dans le [registre Phase 2](enquete-messageries-progress.md), où se trouvent les justifications courtes et les liens de preuve par menace. Elle n’ajoute pas une précision expérimentale : les symboles sont des appréciations qualitatives et restent conditionnels. Pour censure, forensique, supply chain et demandes judiciaires, le dossier individuel fait foi si le cas précis est plus nuancé.

## 7. Métadonnées : ce que chaque observateur peut réellement voir

Échelle : **CONFIRMÉ** = documentation/architecture/cas établit l’accès; **PROBABLE** = nécessaire ou fortement impliqué sans preuve de rétention; **POSSIBLE** = dépend de la configuration ou du fournisseur tiers; **NON ACCESSIBLE PAR DESIGN** = protégé dans le chemin documenté si code et terminaux intègres; **INCONNU** = la preuve ne tranche pas. Les autorités n’ont accès qu’aux données détenues par un acteur et remises ou saisies dans un cadre donné; une possibilité technique ne prouve pas une remise réelle.

| Service | Fournisseur / serveurs | Correspondant | ISP / réseau local | Apple / Google | Données autorités déjà documentées |
|---|---|---|---|---|---|
| Signal | CONFIRMÉ : numéro d’inscription et quelques dates de compte; contenu E2EE NON ACCESSIBLE PAR DESIGN côté service pour messages normaux | CONFIRMÉ : contenu/profil partagé; numéro masqué si configuration appliquée et non déjà connu | CONFIRMÉ : IP de connexion, destination/temps/volume | POSSIBLE : installation, compte store/push/device metadata; détails payload non testés | CONFIRMÉ 2026 : dates de création et dernière connexion pour six comptes; pas le contenu. |
| SimpleX | CONFIRMÉ : relais/queues/push et métadonnées transport; corps E2EE NON ACCESSIBLE PAR DESIGN. La société déclare que les relais presets ne loggent pas les IP ordinaires; pas vérifié indépendamment | CONFIRMÉ : contenu/profil transmis; ID de connexion propre à la relation | CONFIRMÉ : destinations relay, horaires/volume; IP visible au premier relais/à l’ISP | POSSIBLE : APNs token et fréquence; la politique décrit ce que le service push et Apple peuvent voir | Déclaration 2025 : 12 demandes sans données responsive communiquées, non vérifiée indépendamment; cas de production concret inconnu. |
| Olvid | CONFIRMÉ : serveurs voient des informations de routage, clés publiques, taille/horodatage selon analyse formelle; contenu E2EE selon modèle | CONFIRMÉ : profil et identité cryptographique présentés; téléphone/e-mail non obligatoires | CONFIRMÉ : IP, endpoints, temps, volume | POSSIBLE : push/store liés au terminal | Aucun cas public de remise individuelle établi dans cette recherche; données d’infrastructure possibles selon rétention inconnue. |
| Session | CONFIRMÉ : nœuds/relais voient le trafic/activité nécessaire; appels beta exposent IP à l’opérateur STUN/TURN | CONFIRMÉ : ID/session, contenu reçu; appels P2P peuvent révéler IP | CONFIRMÉ : IP des nœuds et timing; onion routing pour messages | POSSIBLE : store/push selon plateforme; détail exact inconnu | Aucun cas de remise concret identifié ici; la capacité des nœuds et les obligations exactes restent dépendantes du réseau/juridiction. |
| Threema | CONFIRMÉ : ID et dates de connexion; métadonnées de compte. Contenu chiffré par conception | CONFIRMÉ : ID, contenu, nom/photo rendus publics par l’utilisateur | CONFIRMÉ : IP destination/temps/volume | POSSIBLE : achat, installation, push/device; mapping public inconnu | Rapport agrégé 2025 et S1 2026 : remises de champs de compte pour des IDs; pas de preuve de contenu de message remis par Threema. |
| Cwtch | POSSIBLE : relais onion et disponibilité/activité; pas de profil global annoncé | CONFIRMÉ : identité choisie et messages reçus | CONFIRMÉ : accès Tor/Internet et volume; IP cible masquée à certains points selon Tor | POSSIBLE : magasin et OS; pas de client iOS | Pas de production concrète retrouvée; les pairs/terminaux restent des sources. |
| Briar | POSSIBLE : Tor ou échanges locaux; centralisation moindre | CONFIRMÉ : conversations locales et identité de contact | CONFIRMÉ : connexions Tor/locaux, timing/volume | POSSIBLE : Google Play si installé depuis Play; pas d’app iOS | Pas de cas de remise fournisseur documenté retrouvé; terminal, correspondants, store ou FAI restent hors du cœur Briar. |
| Jami | CONFIRMÉ/POSSIBLE : DHT, bootstrap et relais voient leur portion du réseau | CONFIRMÉ : peer et contenu reçu | CONFIRMÉ : P2P peut révéler IP et trafic | POSSIBLE : stores et push dépendant de la plateforme | Pas de cas concret établi dans cette recherche; dépend des nœuds/terminaux visés. |
| Tox/qTox | POSSIBLE : nœuds DHT/bootstrap et peers observent l’activité qu’ils relaient | CONFIRMÉ : clé/ID, contenu; IP probable en P2P | CONFIRMÉ : IP pair et volumes selon le chemin | POSSIBLE : app tierce/mobile; pas de correspondance universelle | Aucun cas produit identifié; diversité des clients et opérateurs empêche un tableau juridique unique. |
| Matrix/Element | CONFIRMÉ : homeserver voit compte, appareils, IP, membership/rooms, événements/temps; contenu clair hors E2EE, ciphertext dans salons E2EE | CONFIRMÉ : salons, identifiants et contenu accessible au client; membership visible | CONFIRMÉ : IP serveur, horaires/volume | POSSIBLE/PROBABLE : push token/room/event metadata, store identity | Guide matrix.org décrit la procédure; aucun cas public avec champs effectivement remis par Matrix.org établi ici. Autres homeservers distincts. |
| XMPP/OMEMO | CONFIRMÉ : serveur voit JID, présence, connexions et transport; contenu chiffré si OMEMO réellement actif | CONFIRMÉ : JID, contenu et empreinte/clé | CONFIRMÉ : IP serveur/timing; IP pair possible en appels | POSSIBLE : app/store/push selon client | Pas de résultat juridique générique possible sans serveur identifié; remise/cas réels inconnus. |
| Telegram | CONFIRMÉ : numéro, comptes, cloud messages/groupes et métadonnées; Secret Chats diffèrent | CONFIRMÉ : username/numéro visibles selon réglages, messages reçus | CONFIRMÉ : IP/serveurs/temps | PROBABLE : app/push/store/OS; détails de liaison variables | Production judiciaire civile indienne sous pli, comprenant catégories d’IP/noms rapportées; ce n’est pas preuve d’une remise policière de ces champs. |
| WhatsApp | CONFIRMÉ : numéro, graphe/horaires/infos de service; contenu E2EE pour chats personnels | CONFIRMÉ : numéro, profil, contenu, groupes | CONFIRMÉ : IP, destination/temps/volume | PROBABLE : APNs/FCM/store/compte OS; payload exact et liaison non entièrement testés | Des données de compte sont recherchables selon procédure; cas détaillés et champs concrets dans la Phase 2; ne pas extrapoler un cas sans dossier primaire. |
| Discord | CONFIRMÉ : identité de compte, membres/serveurs, messages texte et métadonnées | CONFIRMÉ : profil, messages, appels/groupes | CONFIRMÉ : IP, timing/volume/service voice | PROBABLE : compte OS/store, push, device IDs selon déclarations store | CONFIRMÉ : messages et données de compte remis dans U.S. v. Bryant (2020). |
| Wire | CONFIRMÉ : compte, IP/metadata de service et champs selon offre; contenu E2EE selon périmètre | CONFIRMÉ : messages/profil | CONFIRMÉ : IP/temps/volume | POSSIBLE : store/push | CONFIRMÉ : e-mail d’inscription remis dans le dossier Tsunami Democràtic; pas preuve de contenu Wire remis. |
| Delta Chat | CONFIRMÉ : fournisseur mail voit adresses, headers/horaires/volumes; E2EE dépend de la conversation | CONFIRMÉ : adresse e-mail/clé, contenu | CONFIRMÉ : connexions mail et IP destination; appels P2P éventuels | POSSIBLE : store/push tiers | Fournisseurs mail peuvent remettre leurs données; pas de cas Delta Chat spécifique établi. |
| Ricochet Refresh | POSSIBLE : points Tor et onion service; pas de fournisseur messagerie unique établi | CONFIRMÉ : contact onion, contenu reçu | CONFIRMÉ : FAI voit entrée Tor et activité volumétrique; destination masquée selon Tor | POSSIBLE : store du système d’exploitation desktop; non testé | Aucun cas Refresh documenté retrouvé; ne vaut pas absence de risque Tor/endpoint. |
| Status/Waku | CONFIRMÉ/POSSIBLE : certains nœuds voient IP/topic/activité; rétention varie selon service géré | CONFIRMÉ : profile/clé, messages/groupes | CONFIRMÉ : IP des nœuds, horaires/volumes | POSSIBLE : push/store selon app | Aucun cas de remise individualisé établi; fournisseur/nœud et wallet/clé peuvent permettre corrélations différentes. |

| Métadonnée | Fournisseur | Contact | ISP | Apple/Google | Autorités |
|---|---|---|---|---|---|
| IP | CONFIRMÉ pour services centralisés et points de connexion; dépend d’onion/P2P/relais | POSSIBLE ou CONFIRMÉ en P2P/appel; NON ACCESSIBLE PAR DESIGN au pair si TURN réellement utilisé | CONFIRMÉ au point d’accès; VPN/Tor change l’observateur, ne supprime pas toute observation | POSSIBLE via services push/store et compte OS; mapping à un profil de messagerie souvent INCONNU | PROBABLE si acteur détient logs; les remises constatées sont produit/cas spécifiques |
| Téléphone | CONFIRMÉ pour Signal/WhatsApp/Telegram; facultatif pour Threema; non requis dans SimpleX/Olvid/Cwtch/Briar/Ricochet | CONFIRMÉ si partagé/sauvegardé par le contact; masquage app ne fait pas oublier un numéro déjà connu | CONFIRMÉ par l’opérateur télécom; l’association à un profil dépend des autres données | PROBABLE comme donnée de compte Apple/Google, mais lien avec l’ID de messagerie variable | POSSIBLE via opérateur et fournisseur si conservé; ne pas supposer production automatique |
| E-mail | CONFIRMÉ sur produits/serveurs qui l’exigent ou si ajouté; dépend de l’offre | POSSIBLE si donné en profil ou en dehors du service | NON ACCESSIBLE PAR DESIGN sous TLS seul, mais fournisseur de mail distinct le voit | PROBABLE pour compte store; lien avec le compte messagerie non systématique | POSSIBLE si conservé; Wire fournit un exemple de remise d’e-mail d’inscription |
| Identifiant | CONFIRMÉ selon le modèle : numéro, MXID, JID, ID random, clé, queue ou compte | CONFIRMÉ pour chaque identité que le contact contacte | POSSIBLE par corrélation, non nécessairement lisible sous TLS | POSSIBLE via ID d’installation/push; correspondance avec identité sociale dépend du produit | POSSIBLE dans retour de service ou appareil; données concrètes variables |
| Graphe social / groupes | CONFIRMÉ dans systèmes centralisés/fédérés et groupes gérés; plus fragmenté via queues onion/P2P | CONFIRMÉ pour contacts et groupes auxquels il participe | POSSIBLE par timing multi-points; pas forcément les noms | POSSIBLE via push, carnet OS, interactions/labels | PROBABLE si serveur/participants/appareil détiennent l’état; remise réelle à établir cas par cas |
| Timestamps / fréquence / volume | CONFIRMÉ ou fortement probable pour serveurs et relais; padding/retention sont spécifiques | CONFIRMÉ pour messages reçus et statut vu; volume observable | CONFIRMÉ sur lien réseau | POSSIBLE par événements push et activité app; détail de liaison souvent inconnu | POSSIBLE si logs, sauvegardes, appareils ou participants obtenus |
| Appareils / push tokens | CONFIRMÉ au service lorsque multi-device/push les requièrent; payload varie | POSSIBLE via appareils vérifiés/listes selon app | POSSIBLE au niveau connexions, pas l’ID logique sous TLS | CONFIRMÉ pour token/install OS; contenu du payload dépend du produit et de l’OS | POSSIBLE via service push ou saisie; pas un synonyme de lecture du contenu |

Pour la matrice granulaire **service × IP/téléphone/e-mail/ID/graphe/timestamps/volumes/groupes/appareils/push × fournisseur/contact/ISP/Apple-Google/autorités**, consulter les matrices par service dans [le dossier Phase 2](enquete-messageries-progress.md). Elles incluent les colonnes statut et les liens de justification; aucune case « inconnu » ne doit être lue comme « aucune donnée ».

## 8. Audits, vulnérabilités, mobile et supply chain

Un audit est un résultat borné par date, version, commits et périmètre. La Phase 2 transcrit les éléments disponibles pour les audits lus et consigne les scopes, exclusions, findings, sévérités, corrections et retests lorsqu’ils sont publiés. Voici les éléments qui changent le plus la lecture comparative.

| Produit / preuve | Ce que la preuve couvre | Résultat / limite à retenir |
|---|---|---|
| Signal — analyses du protocole, source libsignal et Automatic Key Verification | Propriétés E2EE/gestion des clés et cohérence des associations identifiant–clé; AKV audité par Cloudflare/Trail of Bits dans son périmètre de transparency log | Pas un certificat d’identité réelle ni un audit de toute app, backend, iOS/Android, appels ou build distribué. Pour une relation initiée uniquement par username, la vérification automatique de l’autre personne ne s’applique pas sans connaître son numéro; utiliser le Safety Number par canal fiable. [Signal AKV](https://signal.org/blog/automatic-key-verification/) |
| SimpleX — Trail of Bits (oct. 2022), revue protocolaire (juil. 2024), nouvelle revue annoncée 2026 | Snapshot crypto/réseau et protocol design distincts | Correctifs importants publiés après revue 2022; ne couvre pas toutes releases courantes ni tous relais. Une revue 2026 mentionnée dans le dossier n’avait pas de rapport public exploitable à la date d’arrêt. [Politique/audits](https://simplex.chat/privacy/) |
| Olvid — CSPN/Synacktiv historiques; étude formelle 2026 | Versions mobiles historiques pour CSPN; papier 2026 formalise une portion du protocole sous un modèle symbolique | Preuves utiles mais pas validation des applications et services 2026 complets. Papier 2026 signale aussi la visibilité serveur de clés/routage, tailles et timing; pas un audit d’infrastructure entière. [Spécification](https://www.olvid.io/assets/documents/2024-10-07_Olvid-specifications.pdf), [papier 2026](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf) |
| Session — Quarkslab 2021; USENIX WOOT 2026 | Le premier concerne un état historique; le second analyse Session Protocol V1 en 1:1 et petits groupes fermés, avec contexte d’application réelle | WOOT rapporte absence d’authentification mutuelle de clé publique et absence d’authentification cryptographique de compteurs monotones, avec usurpation, forge de timestamps, suppression/rejeu. Version exacte, correctifs, retest et effet sur les versions installées restent à confirmer. [USENIX WOOT 2026](https://www.usenix.org/conference/woot26/presentation/urushigaki) |
| Threema — audits 2018–2024, dont Cure53 Desktop 2.0 Beta 26 (janv. 2024) | Audits de code/protocole et clients différents; Desktop Beta 26 (commit précis non publié dans résumé de Phase 2), 16 jours ouvrés, 5 seniors, white-box | Trois vulnérabilités et quatre faiblesses générales documentées; corrections mentionnées mais pas de retest public sur la bêta actuelle Beta 66 repéré. La bêta Desktop 2.0 ne prend pas en charge PFS, selon l’éditeur. [Limites Desktop](https://threema.com/en/faq/md-limit) |
| Briar — Cure53 (2017), ROS/OTF (2023) et retest (fév.–mars 2024) | Versions précises, scopes et retest sont développés en Phase 2 | Les résultats historiques ne valident pas les builds actuels. Projet en maintenance essentielle depuis juillet 2026; la pérennité opérationnelle devient un facteur de risque. [État du projet](https://briarproject.org/news/2026-maintenance-mode/) |
| Delta Chat — rapports 2019, 2020, Cure53/OTF Webxdc 2023; étude ETH Zürich/USENIX 2024 | Cibles particulières : client, Webxdc, SecureJoin/Autocrypt/rPGP | Plusieurs preuves indépendantes, mais pas une validation générique de tout client, fournisseur mail, appel ou build courant. E2EE varie par compatibilité et conversation. |
| Matrix/Element | Audits et advisories Matrix SDK; étude forensique Synapse 1.133.0 (2026) | Événements non chiffrés, membership et logs serveur peuvent être extraits; le papier ne teste pas l’extraction commerciale des clients actuels. Salons E2EE n’empêchent pas l’exposition de metadata. |
| Wire | Audits de composants et advisory iOS CVE-2026-35049 | Advisory: clients iOS <4.16.0 pouvaient boucler/crasher via payload Proteus malformé; corrigé en 4.16.0 selon l’avis; exploitation réelle non signalée par la source. Ce n’est pas une brèche générale de chiffrement. |
| Discord | Audits Trail of Bits de protocoles DAVE / libdave; advisory d’oct. 2026 | DAVE s’applique à audio/vidéo éligibles, non au texte. Un défaut de validation documenté en 2026 rappelle qu’un protocole audité reste versionné; déploiement complet du correctif multi-plateforme non confirmé dans cette consolidation. |
| WhatsApp | Audits spécifiques (Private Processing) et analyse académique 2026 de WhatsApp Web | L’audit Trail of Bits 2025 porte sur la fonctionnalité d’inférence privée/TEE, pas sur toute la messagerie ni le protocole Signal. L’étude 2026 observe des traces compatibles avec son modèle pour WhatsApp Web et relève des différences non documentées du fork libsignal, sans démontrer rupture E2EE globale. |
| Cwtch, Jami, Tox, Ricochet, Status, Telegram | Scopes, audits et limites par version dans le dossier Phase 2 | Pour plusieurs, l’absence d’audit public récent large, de retest ou de build vérifié est un inconnu important, pas un verdict de vulnérabilité. Ricochet Refresh ne doit pas hériter de l’audit de Ricochet antérieur. |

### Builds, permissions et télémétrie

- **Code public ≠ binaire vérifié.** Des dépôts, tags, CI et instructions de compilation sont disponibles pour plusieurs clients; dans cette étude, aucun APK/IPA/desktop courant n’a été reproduit bit-à-bit puis comparé à la distribution officielle. Le rapport Phase 2 examine aussi l’activité de dépôts, advisories, dépendances et mainteneurs à titre d’échantillon borné, non de recensement exhaustif.
- **SimpleX** publie des instructions pour vérifier/reproduire ses builds Linux et Android; cette procédure documentaire n’est pas un résultat de reproduction indépendante de notre part. [Builds](https://simplex.chat/downloads/).
- **Briar Desktop** publie des checksums par artefact; un checksum protège contre une altération pendant le transfert seulement si la valeur de référence est authentique, il ne prouve pas la correspondance source–binaire.
- **Cwtch** a documenté la reproductibilité des bindings Linux/Windows et un état Android partiel dans une publication historique; vérifier l’état courant et la version exacte avant d’en tirer une conclusion supply chain. [Article technique](https://docs.cwtch.im/blog/cwtch-bindings-reproducible/).
- **Manifests Android** Signal, SimpleX, Session et Threema ont été inspectés à des commits publics pinés en Phase 2. Les permissions déclarées ne prouvent ni accès runtime ni comportement du binaire Store; pour les autres clients, ce contrôle comparatif n’est pas complet.
- Les labels App Store et Play Data Safety sont des disclosures éditeur dépendantes du storefront/version et ne sont pas des captures réseau. Une divergence illustrée : le label Play de Session affirme une absence d’exposition IP générale alors que sa FAQ décrit la divulgation d’IP au pair et au STUN/TURN lors des appels bêta; la différence peut être liée au périmètre messages/appels, mais elle n’est pas explicitée de façon suffisante.
- Les permissions caméra/micro sont attendues pour appels; fichiers/photos pour pièces jointes; contacts seulement si la fonction correspondante est utilisée. Localisation, Bluetooth et push doivent être contrôlés client par client. Aucune comparaison complète des IPA/APK distribués et de leur trafic analytics/crash/SDK n’a été exécutée.

## 9. Demandes publiques, affaires et incidents

| Service / cas | Donnée effectivement obtenue ou remise établie | Ce que cela ne prouve pas |
|---|---|---|
| **Signal, D.C. subpoena, 6 mars 2026** | La réponse Signal indique 37 numéros ciblés : 7 sans compte, 30 comptes existants; dates de création/dernière connexion communiquées pour 6, rien de responsive pour 24 sur la période. [Réponse et documents](https://signal.org/bigbrother/district-of-columbia/) | Aucun contenu de message remis; ne couvre pas téléphone saisi, FAI, store ou participant. C’est la réponse fournisseur publiée, non une mesure universelle de rétention. |
| **Signal, extraction iOS rapportée en 2026** | Presse spécialisée rapporte qu’un témoignage FBI a montré des aperçus de messages entrants Signal, y compris messages expirés/suppression app, conservés dans la base des notifications iOS. [404 Media](https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database/) | Modèle iPhone, version iOS/app, état verrouillé et outil exact non disponibles dans la pièce publique consultée; Apple a documenté le correctif iOS/iPadOS 26.4.2 pour CVE-2026-28950. Ne pas présenter l’ancien résultat comme une capacité actuelle post-correctif. [Apple](https://support.apple.com/en-us/127002) |
| **SimpleX, transparence 2025** | L’opérateur déclare 12 demandes policières sans information responsive fournie. [Rapport](https://simplex.chat/transparency/) | Déclaration agrégée de fournisseur; pas de pièces judiciaires ni audit indépendant des données de chaque relais. |
| **Threema, transparency report 2025 et premier semestre 2026** | Le rapport indique 423 demandes en 2025, 402 affaires avec données pour 1 505 IDs; il décrit des données limitées (jours de création/dernière connexion et éléments facultatifs hash téléphone/e-mail ou push token). Pour le premier semestre 2026, 444 demandes et 438 affaires avec données pour 2 026 IDs sont rapportées. [Rapport](https://threema.com/en/transparency-report) | Chiffres et catégories agrégés auto-déclarés; ne démontrent pas de remise de contenus ou les champs d’un dossier précis. |
| **Threema, U.S. v. Wedding, 2025** | L’acte d’accusation relate conversations/groupes et un appel Threema. [DOJ](https://www.justice.gov/opa/media/1418931/dl?inline=) | Le document ne dit pas que Threema AG a remis ces messages; l’obtention peut passer par participant/témoin/appareil. |
| **Telegram, ordonnance Delhi High Court, 2022–2023** | Production de données à la Cour sous pli scellé; ordonnance décrit un tableau comportant des noms d’administrateurs, téléphones et IP de certains canaux. Une déclaration ultérieure des demandeurs parle de données plus limitées; valeurs sous scellés. [Ordonnance](https://indiankanoon.org/doc/119238688/), [suivi](https://indiankanoon.org/doc/2402568/) | Affaire civile de copyright, pas preuve que la police a effectivement reçu toutes les catégories; les pièces rendent la portée partiellement contradictoire. |
| **Discord, U.S. v. Bryant, 2020** | Opinion judiciaire décrit la remise à la police de données de compte, IP, device ID, e-mail, messages, images et données liées à VoIP sous mandat. [Décision](https://app.midpage.ai/document/united-states-v-bryant-1000161304572) | Cas particulier, juridiction et warrant précis; ne mesure pas tous les champs ni toute rétention actuelle. |
| **Wire, enquête Tsunami Democràtic, 2024** | Wire a confirmé avoir fourni des informations de compte de base, dont l’e-mail d’inscription, relayé dans une enquête ayant ensuite sollicité d’autres prestataires. [TechCrunch avec confirmation Wire](https://techcrunch.com/2024/05/08/encrypted-services-apple-proton-and-wire-helped-spanish-police-identify-activist/) | Pas de preuve de remise du corps des messages Wire. |
| **Matrix.org / autres** | Matrix.org publie un guide d’application de la loi; aucun dossier public consulté n’établit les données effectivement transmises par Matrix.org. Les autres homeservers sont des entités distinctes. | L’absence de cas trouvé n’établit pas une absence de demandes, d’ordres secrets ou de productions. Même limite pour Olvid, Briar, Cwtch, Jami, Tox, Ricochet Refresh, Status, Delta Chat et les autres services sans dossier concret retrouvé dans cette recherche. |

**Conclusion juridique :** la meilleure protection contre une réquisition d’un fournisseur est de minimiser ce que l’opérateur détient, mais cela ne couvre ni l’opérateur téléphonique, l’hébergeur/relay, Apple/Google, les sauvegardes, les appareils, les interlocuteurs ni les données d’un compte Discord d’origine. La juridiction du fournisseur n’efface pas une donnée effectivement détenue ou accessible ailleurs. Les mécanismes européens et nationaux varient et nécessiteraient une analyse juridique pays par pays; ce rapport ne donne pas de conseil juridique.

## 10. Dossiers synthétiques par produit

Ces fiches indiquent la conclusion de référence et la réserve qui doit accompagner toute recommandation. Les preuves/audits détaillés sont dans le [dossier d’enquête Phase 2](enquete-messageries-progress.md), organisé par produit.

### Signal

**À retenir :** E2EE mûr, réseau centralisé, forte adoption et clients officiels iPhone + Windows/macOS/Linux. Pour séparer un pseudo, créer un username unique non réutilisé, mettre la visibilité du numéro et la recherche par numéro sur « personne », ne pas synchroniser/importer les contacts si inutile, et partager uniquement le lien/username souhaité. **Limite :** le service exige toujours un numéro à l’inscription; une clé transparente garantit une association identifiant–clé cohérente, pas que la personne contrôle l’identité annoncée. L’autoverification du correspondant via le log ne fonctionne pas dans le scénario username seul si son numéro n’est pas connu; comparer un Safety Number via canal indépendant. Desktop reste un appareil lié au téléphone principal. Sources : [privacy phone/username](https://signal.org/blog/phone-number-privacy-usernames/), [AKV](https://signal.org/blog/automatic-key-verification/), [desktop](https://signal.org/download/).

### SimpleX

**À retenir :** le modèle sans identifiant global et les liens propres à chaque relation sont adaptés au cloisonnement; profils et historique restent locaux, les relais stockent temporairement des messages chiffrés. Les notifications instantanées iOS donnent au serveur push une partie des métadonnées de queues/fréquence selon la politique; Apple voit un nombre de notifications et des métadonnées chiffrées, pas le contenu selon la conception publiée. TURN masque l’IP au contact dans le réglage par défaut des appels, mais le relay voit IP/durée. Profil mobile–desktop via le même LAN est une contrainte concrète. Source de politique (éditeur) : [privacy policy](https://simplex.chat/privacy/); calls [guide](https://simplex.chat/docs/guide/audio-video-calls.html); [downloads](https://simplex.chat/downloads/).

### Olvid

**À retenir :** compte cryptographique sans téléphone/e-mail obligatoire, calls documentés via TURN-only et étude indépendante formelle récente. **Limites :** serveur voit des éléments de routage/timing/taille dans le modèle analysé; multi-device simultané et appels nécessitent licence après l’essai; discussion historique non synchronisé automatiquement. N’est pas une solution d’anonymat réseau. Sources : [specifications](https://www.olvid.io/assets/documents/2024-10-07_Olvid-specifications.pdf), [formal study](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf), [multi-device](https://olvid.io/faq/use-olvid-on-multiple-devices/).

### Session

**À retenir :** identifiant non téléphonique et routage onion des messages. **Réserves critiques :** étude WOOT 2026 sur Protocol V1 établit trois familles d’attaques dans les implémentations étudiées; aucun correctif/retest courant n’est établi dans cette consolidation. Appels bêta opt-in P2P révèlent IP au correspondant et au serveur STUN/TURN. Sources : [USENIX](https://www.usenix.org/conference/woot26/presentation/urushigaki), [FAQ appels](https://getsession.org/faq). Reclasser seulement après version corrective documentée et retest indépendant suffisant.

### Threema

**À retenir :** l’identifiant aléatoire et l’inscription sans téléphone/e-mail sont utiles au pseudonymat envers le contact. **Limites :** le fournisseur peut détenir des données d’ID/connexion et en publie des remises agrégées; l’achat via store peut créer une relation store; Desktop 2.0 bêta, PFS non supportée, fonctionnalité limitée et rétention de certaines propriétés dépend des clients. Sources : [privacy and reports](https://threema.com/en/transparency-report), [Desktop 2 beta limits](https://threema.com/en/faq/md-limit), [cryptography whitepaper](https://threema.com/assets/8-press/2026-04-20-threema-cryptography-whitepaper.pdf).

### Cwtch

**À retenir :** architecture onion et absence de serveur central unique réduisent la concentration de métadonnées de compte. **Limites :** modèle Tor ne masque pas contre le global passive adversary; pas d’iOS, pas d’appels établis, maturité/assurance et audits plus limités. Utilisable pour utilisateurs qui acceptent une application niche et une configuration particulière. Sources : [intro](https://docs.cwtch.im/docs/intro/), [downloads](https://docs.cwtch.im/it/download/).

### Briar

**À retenir :** utile pour contacts Android quand résilience hors réseau et Tor/transport local comptent; le client Desktop existe en bêta pour Linux/Windows/macOS. **Limites :** pas d’app iOS, coûts UX/fonctionnels, pas d’appels, versions de desktop et mobile séparées; projet désormais maintenance seulement (correctifs essentiels/sécurité). Ne pas en faire le choix pratique pour un utilisateur iPhone. Sources : [how it works](https://briarproject.org/how-it-works/), [desktop](https://briarproject.org/download-briar-desktop/), [maintenance](https://briarproject.org/news/2026-maintenance-mode/).

### Jami

P2P/DHT donne une indépendance à un opérateur central, avec risques de découverte, disponibilité, IP pair-à-pair, DHT/bootstrap, NAT traversal, et audits/mainteneurs par version moins homogènes. Le choix n’est favorable que si les utilisateurs comprennent les implications des appels et testent leurs chemins réseau.

### Tox / qTox

Identité par clé et protocole P2P, mais qTox n’est qu’une implémentation desktop. Clients mobiles, forks, maintenance et fonctions ne sont pas interchangeables. Les appels P2P et IP publique exposent le pair; un ID long terme peut être corrélé par réutilisation. Le protocole et chaque client doivent être évalués séparément.

### Matrix / Element

La fédération permet de choisir un homeserver ou de l’auto-héberger, mais les événements de membership, appareils, IP et timestamps restent visibles à l’opérateur correspondant. E2EE est activé par salon/client et n’efface pas metadata. Appels via SFU/TURN ont leur propre opérateur et visibilité IP. Source technique : [Matrix specification](https://spec.matrix.org/latest/), [Element privacy](https://element.io/en/legal/privacy), [matrix.org law enforcement guide](https://matrix.org/legal/law-enforcement-guidelines/).

### XMPP / OMEMO

Une pile à configurer, pas un produit unique. OMEMO protège le contenu seulement si client, appareils, contacts et extension sont compatibles et correctement vérifiés; serveur voit JID, présence, connexions et groupe/roster selon extension. Pour comparer, il faut fixer un client iOS, client PC, serveur précis et politique de logs. Source protocole : [XEP-0384](https://xmpp.org/extensions/xep-0384.html).

### Telegram

Les Cloud Chats et groupes sont côté serveur; les Secret Chats sont un mode E2EE distinct. Les channels et groupes ne sont donc pas privés de la plateforme au même sens. Numéro et user discovery ont une surface de corrélation. Usage de communauté grand public acceptable si l’objectif n’est pas la confidentialité de contenu vis-à-vis du service; ne jamais résumer comme « E2EE par défaut ».

### WhatsApp

E2EE par défaut pour messages et appels personnels; contenu chiffré ne rend pas le numéro, le graphe d’usage, l’IP, les infos de compte et les sauvegardes inconnus à Meta/OS. Les études 2025–2026 de l’enquête sont versionnées et certaines attaques de découverte de numéros ont été corrigées selon les auteurs; ne pas présenter un état historique comme faille actuelle.

### Discord

Excellent outil communautaire et de collaboration; texte, DM et historiques de serveurs restent lisibles/traitables par la plateforme. DAVE E2EE s’applique aux médias audio/vidéo éligibles, non au texte et non à toutes exceptions de canaux. Comme preuve de distinction entre capacité et pratique, un mandat a produit des messages et données de compte dans U.S. v. Bryant. Garder Discord comme point de départ ne peut pas être effacé par le changement d’app.

### Wire

E2EE et clients partiellement audités/ouvert sont utiles, mais compte, e-mail et métadonnées subsistent. L’affaire 2024 prouve que l’e-mail d’inscription peut relier un compte pseudonyme à d’autres fournisseurs; elle ne prouve pas la remise du contenu. Audit produit, backend et build distribué ne sont pas équivalents.

### Delta Chat

Modèle e-mail familier, client multiplateforme et plusieurs audits ciblés. L’adresse mail et ses opérateurs forment l’infrastructure d’identité/transport; les métadonnées mail restent visibles, et l’E2EE dépend de l’état de la conversation. Appel P2P peut divulguer l’IP. Favorable si portabilité/interopérabilité e-mail priment, moins si unlinkability réseau et simplicité cryptographique sont prioritaires.

### Ricochet Refresh

Le canal Tor onion évite un compte central et limite l’exposition IP dans son chemin normal, mais le projet est de faible maturité/activité et l’assurance actuelle est faible. L’audit NCC souvent cité vise Ricochet historique, pas Refresh 3.x. Desktop seulement, 1:1, pas de service multi-device/appels établi. Candidat de recherche, pas recommandation par défaut.

### Status / Waku

Réseau distribuable, mais les opérateurs de nœuds gérés peuvent observer IP/topics/activité selon le service; certaines rétentions annoncées doivent être distinguées du contenu chiffré. Profil wallet/clé peut être durable et corrélable. Appels, clients desktop, builds, gouvernance et opérateurs effectifs restent à vérifier pour le cas précis.

## 11. Classement par threat model et usage

Ce sont des paliers conditionnels, pas un ordre numérique ni un « score global ».

| Besoin | Choix à examiner en premier | Pourquoi / réserve principale |
|---|---|---|
| A — Sécurité générale pour usage normal | Signal; Threema; Olvid; WhatsApp si adoption prioritaire | Maturité, E2EE et maintenance (Signal); identité no-phone (Threema/Olvid); adoption énorme mais métadonnées (WhatsApp). Configuration et version comptent. |
| B — Minimisation des métadonnées de compte | SimpleX; Cwtch; Briar; Ricochet Refresh | Identifiants par relation ou onion; moins de compte global. Briar/Cwtch/Ricochet ont des limites de plateforme/maturité; SimpleX garde relais/push/transport. |
| C — Pseudonymat utilisable | SimpleX; Signal renforcé; Threema; Olvid | SimpleX n’associe pas de numéro obligatoire; Signal offre username privé au contact mais numéro nécessaire côté service; Threema/Olvid évitent numéro requis. |
| D — Réduction d’identification réseau contre observateur limité | Briar/Cwtch/Ricochet (Tor), SimpleX avec relais correctement configurés, Session pour messages uniquement après résolution des findings | Tor/onion déplace les observateurs; pas de protection globale. Pas de client iOS pour Briar/Cwtch/Ricochet. Session est rétrogradé en attente de correctifs/retest. |
| E — Minimisation des métadonnées sociales | SimpleX; Cwtch; Briar; Signal avec username discovery off | Le graphe est moins centralisé/identifiable; P2P peut exposer IP; Signal garde numéro côté fournisseur. |
| F — Résistance à un opérateur malveillant | Briar/Cwtch/Ricochet pour minimiser service central; Signal/Matrix/Threema avec vérification de clés selon cas | Distribution réduit un pouvoir central mais élargit la chaîne. Key transparency Matrix/Signal ne prouve pas l’identité réelle; aucun n’évite client/update ciblé. |
| G — Résistance à une demande fournisseur | Services détenant peu de données identifiantes (SimpleX/Cwtch/Briar/Ricochet), sous réserve de relais/tiers | Ne signifie pas immunité juridique : téléphone, FAI, store, serveur onion, destinataire et terminal restent des sources. Signal/Threema ont des divulgations de données de compte publiées. |
| H — Deux pseudonymes Internet sans téléphone partagé | SimpleX; Signal renforcé si numéro d’inscription non relié publiquement à l’identité; Cwtch si les deux participants peuvent l’utiliser | SimpleX lien par relation; Signal facilite l’adoption et le PC mais son fournisseur reçoit le numéro; Cwtch n’a pas iOS. |
| I — Contact malveillant / empêcher l’IP au pair | SimpleX avec TURN; Olvid (TURN-only documenté); Signal réglage relayé; Briar/Cwtch si appels inutiles | Relais cache l’IP au pair, la donne au relais. Désactiver P2P et ne cliquer aucun lien profilant. |
| J — Censure / coupure | Briar en Android; Cwtch; fédération Matrix/XMPP; options Tor/relays auto-hébergés | Résilience dépend des bridges, stores, bootstrap, domaine, ASN et pays. Briar est en maintenance; aucune campagne OONI actuelle complète n’a été réalisée ici. |
| K — Journaliste/source | Briar pour deux utilisateurs Android avec besoin hors réseau; Signal pour adoption et sécurité opérationnelle générale; SimpleX/Cwtch selon cloisonnement | Le canal ne remplace pas protocole éditorial, vérification d’identité, protection appareil, traitement de fichiers ou plan de secours. |
| L — Grandes équipes/groupes | Matrix/Element auto-hébergé et configuré; Wire; WhatsApp/Discord quand adoption prime | Matrix/Wire offrent des contrôles administratifs; Discord est mauvais pour confidentialité texte; vérifier gestion des appareils et historique de groupe. |
| M — Simplicité et migration de proches | Signal; WhatsApp si adoption avant tout | Signal permet E2EE sans changement d’usage majeur; WhatsApp a une base de contacts mais collecte de metadata et compte numéro. |

### Classement par configuration concrète

| Configuration | Niveau relatif | Choix plausibles | Ce que l’on gagne / ce qui reste |
|---|---|---|---|
| **Par défaut / sans réglages particuliers** | Dépend fortement des defaults, donc pas de classement unique | Signal, SimpleX, Threema, WhatsApp selon besoin | Signal cache généralement le numéro aux personnes qui ne l’ont pas déjà; découverte par numéro reste activée par défaut. SimpleX minimise l’ID, mais le push iOS par défaut peut augmenter metadata. WhatsApp protège le contenu des chats personnels mais pas numéro/metadata. Telegram/Discord ne protègent pas le texte E2EE. |
| **Renforcée** | Signal ou SimpleX selon priorité; Olvid/Threema si absence de numéro chez interlocuteur | Signal : visibilité numéro `Nobody`, découverte par numéro `Nobody`, username unique partagé; SimpleX : profil distinct, invitation unitaire, push iOS moins riche si acceptable, relais d’appel forcé; Olvid : calls TURN, profils/appareils vérifiés; Threema : aucune liaison téléphone/e-mail sauf besoin | Renforce cloisonnement/anti-contact/metadata ciblées; ne résout pas le service qui connaît le numéro (Signal), la visibilité des relais, les stores, un appareil compromis ou la divulgation du correspondant. |
| **Pseudonyme fort, mais non-anonyme** | SimpleX en premier; Signal renforcé sous préconditions; Cwtch si platform fit | Identité neuve par relation, pas de profil public, jamais de username/avatar réutilisé; appel sans P2P; vérifier l’identité hors bande | Réduit l’énumération et le lien direct vers identité civile. Le lien Discord initial, l’IP aux premiers relais/FAI, les habitudes et les appareils restent corrélables. |

### Signal en username-only : verdict réévalué

La configuration demandée améliore réellement la confidentialité vis-à-vis du contact :

1. `Who can see my number` → **Nobody**.
2. `Who can find me by my number` → **Nobody**.
3. Créer un username non réutilisé et le partager directement; le username n’est pas un handle public recherché et ne s’affiche pas automatiquement dans la conversation.
4. Utiliser un nom/photo/profil sans lien vers d’autres identités; ne pas supposer que l’avatar est caché au correspondant.
5. Vérifier les safety numbers manuellement via un canal indépendant lorsqu’on ne connaît pas le numéro du correspondant; AKV ne certifie pas une identité humaine et ne permet pas, dans le cas username-only, l’autovérification de l’autre compte sans connaître son numéro.

**Ce que cette configuration change :** un doxxer qui ne connaît que le numéro ne devrait pas retrouver le compte si le réglage de recherche est correctement activé; le contact initial n’a pas besoin de recevoir le numéro. **Ce qu’elle ne change pas :** Signal doit recevoir un numéro valide pour inscrire le compte; Signal peut relier le numéro à son compte. Si le numéro est connu des opérateurs, réutilisé, payé/activé par une identité réelle ou lié à d’autres services, le pseudonymat peut s’effondrer. Un numéro non publiquement relié à l’identité n’est pas automatiquement anonyme vis-à-vis de l’opérateur téléphonique ou de Signal. **Conclusion :** Signal remonte substantiellement dans le cas iPhone + PC et dans le pseudonymat envers le correspondant, mais ne rejoint pas SimpleX sur l’absence d’identifiant global obligatoire ni sur la séparation fournisseur–numéro.

### iPhone + PC

| Palier d’usage | Options | Motif déterminant |
|---|---|---|
| Le plus praticable sans perdre la sécurité de contenu | Signal | iPhone + clients Win/macOS/Linux officiels; l’iPhone reste primaire et appaire les desktops. Username privacy peut cacher le numéro du contact, mais pas du service. |
| Alternative sans numéro requis | SimpleX, Olvid, Threema | SimpleX nécessite appairage mobile–desktop sur même LAN et notifications/stockage à comprendre; Olvid multi-device simultané sous licence et ancien historique non transféré; Threema 2.0 Desktop bêta sans PFS. |
| Plateforme personnalisable / serveur choisi | Matrix/Element ou XMPP/OMEMO | iOS et PC possibles via clients précis; choisir et configurer homeserver, identité, encryption des salons, backups, push et appels. Ce n’est pas un résultat automatique du protocole. |
| À ne pas recommander comme solution pratique iPhone | Briar, Cwtch, Ricochet Refresh | Pas de client iOS officiel établi; Briar Desktop bêta ne remplace pas Briar sur iPhone. Cwtch peut connecter desktop/Android mais pas iOS; Ricochet est desktop. |

## 12. Discord → autre messagerie : gains et limites

Le passage de Discord à une messagerie privée améliore l’exposition du contenu seulement si la nouvelle messagerie E2EE protège effectivement ce contenu. Il ne supprime pas les traces déjà chez Discord : compte d’origine, heure du contact, message d’invitation, membres du serveur, IP de connexion et potentiellement historique de modération. Si la personne reçoit un lien depuis Discord, Discord peut savoir quel compte l’a envoyé à quel compte, même si le lien est aléatoire et le contenu ultérieur chiffré.

| Dimension | Discord | Après migration vers SimpleX / Signal renforcé / Threema / Olvid |
|---|---|---|
| Texte | Serveur Discord accessible/traitable; pas E2EE | E2EE pour les conversations ciblées; Discord conserve l’historique antérieur |
| Identité | Compte, serveur, username/historique social centralisés | Le contact reçoit seulement l’ID/lien/profil volontaire; risque de pseudo/avatar/langage réutilisé |
| IP | Discord voit IP de connexion; partenaire ne l’obtient pas généralement par les DMs | Le nouveau service/relay voit le chemin; un appel P2P peut transmettre l’IP au correspondant; un transfert d’invitation crée une jointure temporelle |
| Métadonnées | Compte, membership, messages et activité de service centralisés | Moins d’exposition chez le nouveau fournisseur selon architecture, mais push, FAI, stores, contacts et relais restent |
| Recours légal | Preuve U.S. v Bryant : messages et champs de compte effectivement remis dans une affaire | Réduction variable de ce que l’opérateur peut déchiffrer/remettre; le terminal et participant peuvent toujours fournir le contenu |

Pour une rencontre inconnue sur Discord, le choix de référence est **SimpleX** si les deux parties maîtrisent le profil par relation et peuvent accepter ses limites iOS/desktop. **Signal configuré comme ci-dessus** est une alternative très raisonnable si l’on privilégie l’ergonomie, l’adoption et PC, dès lors que le numéro est traité comme secret connu du fournisseur et que l’identité de l’autre partie est vérifiée. **Threema/Olvid** conviennent si la question principale est de ne pas révéler le numéro au contact; ni l’un ni l’autre ne fournit un anonymat réseau. Cwtch/Briar ne sont pas recommandés pour un utilisateur iPhone; Session n’est pas choix d’assurance maximale jusqu’à résolution et retest des findings WOOT.

## 13. Recommandations OPSEC proportionnées

### Pour SimpleX

- Créer un profil distinct et une invitation à usage unique par relation; ne pas utiliser de nom public `.simplex` pour un pseudonyme.
- Éviter de synchroniser des contacts qui ne sont pas nécessaires; ne pas injecter le profil dans un compte cloud/personnel.
- Sur iOS, choisir consciemment entre notification instantanée et moindre exposition des métadonnées; masquer le contenu des previews écran verrouillé.
- Garder TURN/relais imposé pour les appels si le contact ne doit pas voir l’IP; le relais verra l’adresse et la durée. Désactiver les appels si aucun besoin.
- Ne jamais envoyer originaux photo/documents sans inspecter EXIF, auteur, chemins, miniatures, noms de fichiers et historiques.

### Pour Signal en configuration pseudonyme

- Inscrire avec un numéro que l’utilisateur accepte d’exposer au service et à l’opérateur télécom; « non-public » n’est pas synonyme de « non-lié ».
- Mettre la visibilité ET la recherche par numéro sur `Nobody`; partager seulement un username neuf par canal choisi.
- Ne pas réutiliser profil, avatar, nom, groupe, lien public, sauvegarde ou carnet de contacts identifiant.
- Appairer uniquement ses propres PCs, contrôler les appareils liés et les retirer après usage; garder l’iPhone et le PC à jour.
- Vérifier les safety numbers par canal indépendant, surtout avec un nouveau correspondant; AKV n’atteste pas son identité civile.
- Limiter les notifications sur écran verrouillé; tenir compte du cas historique iOS de notifications, corrigé par Apple selon l’avis 26.4.2, sans extrapoler avant/après correctif.

### Pour Olvid / Threema

- Vérifier en personne/par canal séparé l’identité ou l’empreinte attendue; ne pas supposer que clé/profile de compte signifie personne vérifiée.
- Si PC nécessaire, considérer explicitement le coût et les propriétés de multi-device; sur Threema beta, accepter l’absence de PFS sur Desktop 2.0 ou éviter ce mode si PFS exigée.
- Régler les calls sur TURN/relais si l’IP au contact importe; distinguer l’IP exposée au relais.

### Pour tous

- Un terminal à jour, code robuste, chiffrement OS, verrouillage court et sauvegarde maîtrisée protègent souvent plus qu’un changement de messagerie.
- Réduire les comptes liés et permissions contacts/localisation/micro/caméra; activer micro/caméra seulement lors d’usage explicite.
- Couper previews de notifications, vérifier les appareils liés et les clés après migration ou ajout d’appareil.
- Ne pas choisir VPN/Tor mécaniquement : identifier l’observateur déplacé, tester le chemin réellement pris, éviter une fuite hors tunnel et considérer l’empreinte liée aux horaires.
- Séparer l’identité avant le premier contact : pseudo, image, signature linguistique, heures, e-mail, téléphone, cloud et partage de fichier peuvent reconstituer le lien.
- Ne jamais compter sur message éphémère pour empêcher sauvegarde, capture, caméra externe ou export par le destinataire.

## 14. Limites, inconnues et expériences qui changeraient le verdict

### Inconnues importantes

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

### Tests sûrs qui apporteraient le plus de preuve

1. Tester dans un laboratoire avec deux appareils contrôlés le username-only Signal, lookup par numéro désactivé, contacts déjà dans l’adresse et affichage du profil; comparer Android et iOS sans utiliser de comptes tiers.
2. Capturer DNS/connexions/ICE lors d’appels de test sur comptes propres, avec relay activé/désactivé, et vérifier l’IP vue par le pair et par le serveur STUN/TURN pour les versions exactes.
3. Comparer payloads de notifications iOS/Android et comportement avec contenu masqué, push instantané/retardé, comptes et appareils test dédiés.
4. Reconstruire les APK/desktop où une procédure reproductible est documentée, comparer aux artefacts officiels, vérifier signatures, dépendances et provenance; ne pas inférer IPA reproductible à partir d’Android.
5. Créer un jeu d’essai avec photos/docs et examiner localement EXIF, thumbnails, caches, clipboard, bases et notifications; état verrouillé/déverrouillé documenté par modèle/version/heure.
6. Tester l’état du correctif Session uniquement sur environnements et profils contrôlés, avec protocole d’étude et autorisation; faire confirmer les mitigations par les auteurs ou une évaluation indépendante. Pas d’attaque de nœuds réels ni d’utilisateurs.
7. Mesurer la censure uniquement à partir de mesures publiques et appareils autorisés, en enregistrant pays, opérateur, AS, date, DNS/transport et version; ne pas présenter une mesure passée comme état actuel.

### Ce qu’aucune messagerie ne peut complètement résoudre

Un endpoint compromis ou déverrouillé peut exposer l’écran, les bases, les clés, les fichiers et les notifications; un participant peut copier ou photographier le message; une personne peut être corrélée par pseudo, avatar, style, horaire, voix, EXIF ou liens. Un observateur global peut tenter une corrélation de trafic même quand l’IP du pair est masquée. Aucun paramètre d’application ne remplace la maîtrise des appareils, des sauvegardes, des identités et du comportement.

## 15. Sources et pièces de référence

Les sources ci-dessous sont les références primaires/indépendantes qui portent les conclusions de premier ordre. La bibliographie élargie, les audits détaillés (organisme, date, version, scope, exclusions, findings, corrections/retest), vulnérabilités et matrices par service sont dans le [dossier Phase 2](enquete-messageries-progress.md). Les références sont classées par rôle; l’éditeur établit ses déclarations, pas une preuve indépendante de leur application en production.

### Sources transversales et référentiels

- [Spécification Matrix](https://spec.matrix.org/latest/) — protocole/API, source primaire.
- [XEP-0384 OMEMO](https://xmpp.org/extensions/xep-0384.html) — extension XMPP E2EE, spécification.
- [USENIX WOOT 2026 — Practical Attacks on a Decentralized Secure Messenger Session](https://www.usenix.org/conference/woot26/presentation/urushigaki) — recherche indépendante, Session Protocol V1.
- [DFRWS / Forensic Science International 2026 — analyse forensique Matrix/Synapse](https://dfrws.org/wp-content/uploads/2026/03/DFRWS-down-the-Rabbit-Hole-A-forensic-analy_2026_Forensic-Science-Internati.pdf) — étude de serveur en environnement/version précisés; pas extraction Cellebrite mobile.
- [Apple Security Updates, CVE-2026-28950](https://support.apple.com/en-us/127002) — avis primaire sur correctif iOS/iPadOS 26.4.2.

### Signal

- [Phone Number Privacy and Usernames](https://signal.org/blog/phone-number-privacy-usernames/) — billet officiel, réglages d’identité et limites du username.
- [Automatic Key Verification](https://signal.org/blog/automatic-key-verification/) — billet officiel, key transparency et limites d’authentification humaine.
- [Signal download](https://signal.org/download/) et [support linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices) — plateformes et appairage.
- [Dossier de subpoena D.C. 2026](https://signal.org/bigbrother/district-of-columbia/) — documents et réponse fournisseur.

### SimpleX, Olvid, Session

- [SimpleX download](https://simplex.chat/downloads/), [policy](https://simplex.chat/privacy/), [calls guide](https://simplex.chat/docs/guide/audio-video-calls.html), [transparency](https://simplex.chat/transparency/) — sources officielles; les affirmations de logs ne sont pas indépendamment mesurées.
- [Olvid specifications](https://www.olvid.io/assets/documents/2024-10-07_Olvid-specifications.pdf), [formal analysis 2026](https://www.cryptojedi.org/papers/olvidgbu-20260805.pdf), [multi-device](https://olvid.io/faq/use-olvid-on-multiple-devices/) — protocol, étude et contraintes produit.
- [Session FAQ](https://getsession.org/faq), [USENIX WOOT 2026](https://www.usenix.org/conference/woot26/presentation/urushigaki) — calls et analyse indépendante, périmètres distincts.

### Threema, Briar, Cwtch, réseaux onion/P2P

- [Threema transparency report](https://threema.com/en/transparency-report), [Desktop beta limitations](https://threema.com/en/faq/md-limit), [2026 cryptography whitepaper](https://threema.com/assets/8-press/2026-04-20-threema-cryptography-whitepaper.pdf).
- [Briar how it works](https://briarproject.org/how-it-works/), [Briar Desktop downloads](https://briarproject.org/download-briar-desktop/), [maintenance mode notice, 9 July 2026](https://briarproject.org/news/2026-maintenance-mode/).
- [Cwtch overview](https://docs.cwtch.im/docs/intro/), [downloads](https://docs.cwtch.im/it/download/), [reproducible bindings report](https://docs.cwtch.im/blog/cwtch-bindings-reproducible/).
- Les sources de Jami, Tox/qTox et Ricochet Refresh sont inventoriées par dépôt/protocole et limite de client dans le dossier de Phase 2; ne pas généraliser un résultat d’un client à l’autre.

### Discord, Matrix, Wire, Telegram, WhatsApp, Delta Chat

- [Discord DAVE protocol and code](https://github.com/discord/libdave) — périmètre médias audio/vidéo, distinct du texte; voir aussi son advisory traité en Phase 2.
- [Matrix.org privacy notice](https://matrix.org/legal/privacy-notice/), [law enforcement guide](https://matrix.org/legal/law-enforcement-guidelines/), [Element privacy](https://element.io/en/legal/privacy) — sources de fournisseur sur matrix.org/Element, pas tous homeservers.
- [Wire iOS advisory CVE-2026-35049](https://github.com/wireapp/wire-ios/security/advisories/GHSA-v6wg-c7qc-x66g) — avis de sécurité avec versions et correction.
- [U.S. v. Bryant](https://app.midpage.ai/document/united-states-v-bryant-1000161304572) — opinion judiciaire concernant Discord et retour de mandat.
- [Telegram Delhi High Court order](https://indiankanoon.org/doc/119238688/) et [follow-up](https://indiankanoon.org/doc/2402568/) — production civile sous pli; champs/portée partiellement contradictoires.
- [Wire investigation reporting with company confirmation](https://techcrunch.com/2024/05/08/encrypted-services-apple-proton-and-wire-helped-spanish-police-identify-activist/) — remise d’e-mail de compte, sans preuve de remise de contenu Wire.
- Delta Chat : audits Cure53/OTF Webxdc, études ETH/USENIX et doc Autocrypt sont cités individuellement dans le [registre Phase 2](enquete-messageries-progress.md); chaque audit couvre un périmètre distinct.

### Repère de lecture final

Ne pas citer ce rapport comme certification de sécurité ni comme conseil juridique. Pour refaire une comparaison après une mise à jour majeure, la première tâche est de vérifier les versions et configurations, le statut de correctifs Session/Threema/Signal, les labels mobiles, les builds installés et les disclosures légales depuis les sources primaires. Le document canonique conserve les inconnues plutôt que de remplir les cases par supposition.
