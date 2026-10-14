---
title: Anonymat réseau
description: Réduire la possibilité de relier un trafic à votre adresse réseau ou
  à son destinataire.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Anonymat réseau

## Définition courte

Réduire la possibilité de relier un trafic à votre adresse réseau ou à son destinataire.


## Exemple concret

TURN cache votre IP à Bob, mais le relais voit l’IP de vos connexions.


## Ce que cela protège

Contre certains observateurs limités, selon le chemin réellement pris.


## Ce que cela ne protège pas

Ni une corrélation globale des horaires et volumes, ni identité de compte, profil ou voix.


## Pourquoi cela compte

Un appel peut prendre une autre route que les messages et révéler une IP.


## Comportement d’une messagerie

Cwtch et Briar utilisent Tor ; Session expose l’IP dans ses appels bêta P2P.

<details class="technical-details"><summary>Détails techniques</summary><p>Tor/onion et VPN déplacent la visibilité et la confiance. Aucun service étudié ne démontre une résistance générale à l’adversaire passif global.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L108" aria-label="Source: network-anonymity — report.threats">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Source: network-anonymity — report.comparison">[2]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: network-anonymity — report.limits">[3]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
