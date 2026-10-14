---
title: Télémétrie
description: Données qu’une application transmet sur son fonctionnement, par exemple
  des erreurs ou l’usage.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Télémétrie

## Définition courte

Données qu’une application transmet sur son fonctionnement, par exemple des erreurs ou l’usage.


## Exemple concret

Un rapport de crash peut décrire l’appareil ; un relais peut voir des horaires même sans rapport de crash.


## Ce que cela protège

Désactiver une télémétrie optionnelle peut réduire des envois supplémentaires, si cette option est effective.


## Ce que cela ne protège pas

Ne supprime pas les métadonnées nécessaires au transport, les notifications ou les logs d’autres acteurs.


## Pourquoi cela compte

« Pas d’analytics » et « aucune donnée observée » sont deux affirmations différentes.

<details class="technical-details"><summary>Détails techniques</summary><p>Labels de magasin et permissions sont des déclarations / indices statiques ; le trafic SDK et push courant n’a pas été comparé complètement ici.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Source: telemetry — report.audits">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L46" aria-label="Source: telemetry — report.methodology">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
