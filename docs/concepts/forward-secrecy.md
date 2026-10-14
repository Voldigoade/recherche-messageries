---
title: Forward secrecy — PFS
description: Des clés compromises plus tard ne devraient pas dévoiler les anciens
  messages protégés par des clés éphémères supprimées.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Forward secrecy — PFS

## Définition courte

Des clés compromises plus tard ne devraient pas dévoiler les anciens messages protégés par des clés éphémères supprimées.


## Exemple concret

Une clé à long terme est volée aujourd’hui ; cela ne devrait pas suffire à déchiffrer l’ancien trafic enregistré.


## Ce que cela protège

La confidentialité de l’historique cryptographique dans le modèle du protocole.


## Ce que cela ne protège pas

Pas une base locale déjà déchiffrée, une capture du destinataire ou des clés jamais supprimées.


## Pourquoi cela compte

Les garanties peuvent différer entre le téléphone et un PC lié.


## Comportement d’une messagerie

Threema Desktop 2.0 bêta ne prend pas en charge la PFS dans le rapport.

<details class="technical-details"><summary>Détails techniques</summary><p>PFS dépend du protocole, de l’implémentation, de l’effacement et des appareils liés.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: forward-secrecy — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: forward-secrecy — report.limits">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
