---
title: Sécurité après compromission
description: Une session peut retrouver sa confidentialité après un vol temporaire
  de son état et une évolution sûre des clés.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Sécurité après compromission

## Définition courte

Une session peut retrouver sa confidentialité après un vol temporaire de son état et une évolution sûre des clés.


## Exemple concret

Un attaquant copie l’état de session puis perd l’accès ; de nouveaux échanges peuvent renouveler la protection.


## Ce que cela protège

Certains échanges futurs après la compromission temporaire, selon le protocole.


## Ce que cela ne protège pas

Ne répare pas un téléphone encore contrôlé par un spyware.


## Pourquoi cela compte

Distinguer récupération cryptographique et nettoyage d’un appareil.

<details class="technical-details"><summary>Détails techniques</summary><p>La propriété dépend des échanges de clés, des hypothèses et de l’implémentation ; elle n’est pas uniforme entre tous les clients.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: post-compromise — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: post-compromise — report.limits">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
