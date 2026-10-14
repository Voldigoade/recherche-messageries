---
title: Idées reçues
description: Idées reçues
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Idées reçues



## « E2EE veut dire anonyme. »

Le contenu et l’identification sont deux propriétés différentes. Le compte, l’IP et les horaires peuvent rester observables.

<a href="/recherche-messageries/concepts/e2ee/">Chiffrement de bout en bout — E2EE</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L8" aria-label="Source: e2ee-anonymous — report.summary">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Source: e2ee-anonymous — report.metadata">[2]</a>


## « Le service ne lit pas mes messages, donc il ne sait rien. »

Des dates de compte, un numéro ou des connexions peuvent être utiles sans le texte. Distinguer capacité et remise réellement établie.

<a href="/recherche-messageries/concepts/metadata/">Métadonnées</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Source: no-data — report.metadata">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Source: no-data — report.legal">[2]</a>


## « Avec Tor, je ne peux pas être retrouvé. »

Tor réduit certaines observations locales ; pas les copies, l’identité du profil, les terminaux ou la corrélation globale.

<a href="/recherche-messageries/concepts/network-anonymity/">Anonymat réseau</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L108" aria-label="Source: tor — report.threats">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: tor — report.limits">[2]</a>


## « Décentralisé signifie privé. »

Les nœuds, bootstrap, DHT ou pairs peuvent voir leur portion de données. Il faut identifier les opérateurs réels.

<a href="/recherche-messageries/concepts/privacy/">Vie privée et minimisation des données</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Source: decentralised — report.comparison">[1]</a>


## « Open source signifie sûr. »

Le code public aide l’inspection, mais ne prouve pas qu’un binaire installé lui correspond. Aucun build courant n’a été reproduit bit à bit ici.

<a href="/recherche-messageries/concepts/security/">Sécurité</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Source: open-source — report.audits">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L46" aria-label="Source: open-source — report.methodology">[2]</a>


## « Pas de numéro signifie anonyme. »

Cela retire un identifiant, pas l’IP, les achats, les profils réutilisés ou les habitudes.

<a href="/recherche-messageries/concepts/pseudonymity/">Pseudonymat</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: no-phone — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Source: no-phone — report.opsec">[2]</a>


## « Un VPN rend la messagerie anonyme. »

Un VPN déplace la visibilité réseau et la confiance. Il n’efface ni le compte ni les autres canaux de corrélation. Vérifier le chemin réel.

<a href="/recherche-messageries/concepts/network-anonymity/">Anonymat réseau</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Source: vpn — report.opsec">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: vpn — report.limits">[2]</a>


## « Messages éphémères : rien ne sera récupérable. »

Le contact peut copier ou photographier. Notifications, bases, sauvegardes et versions comptent ; ne pas généraliser une ancienne extraction aux correctifs actuels.

<a href="/recherche-messageries/concepts/confidentiality/">Confidentialité</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Source: disappearing — report.opsec">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Source: disappearing — report.legal">[2]</a>


## « P2P est forcément plus privé. »

Moins de centralisation peut s’accompagner d’une IP révélée au pair. Le chemin des appels est distinct du chemin des messages.

<a href="/recherche-messageries/concepts/network-anonymity/">Anonymat réseau</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Source: p2p — report.comparison">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Source: p2p — report.metadata">[2]</a>


## « Un audit prouve que toute l’application est sûre. »

Un audit est borné par sa version, sa date, ses composants et ses exclusions. Vérifier corrections et retests sans étendre le scope.

<a href="/recherche-messageries/concepts/security/">Sécurité</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Source: audit — report.audits">[1]</a>


## « Sans le texte, une enquête ne peut rien apprendre. »

Les données de compte, le télécom, les stores, le FAI, les appareils et les correspondants sont des sources différentes. Un cas précis ne vaut pas pour tous.

<a href="/recherche-messageries/concepts/metadata/">Métadonnées</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Source: police — report.legal">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Source: police — report.metadata">[2]</a>
