---
title: Vérification des clés
description: Vérifier que la clé utilisée correspond à celle attendue pour votre contact.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Vérification des clés

## Définition courte

Vérifier que la clé utilisée correspond à celle attendue pour votre contact.


## Exemple concret

Alice et Bob comparent une empreinte par un canal distinct qu’ils jugent fiable.


## Ce que cela protège

Réduit certains risques de substitution de clé ou d’usurpation.


## Ce que cela ne protège pas

Une clé cohérente ne certifie pas automatiquement une identité civile.


## Pourquoi cela compte

Chiffrer vers la mauvaise clé peut protéger le message pour la mauvaise personne.


## Comportement d’une messagerie

En Signal username-only sans numéro du pair connu, comparer le Safety Number ; AKV n’atteste pas son identité.

<details class="technical-details"><summary>Détails techniques</summary><p>Key transparency vérifie la cohérence identifiant–clé ; l’authentification humaine et les contrôles hors bande sont distincts.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: verification — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: verification — report.limits">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
