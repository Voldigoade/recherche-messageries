---
title: Chiffrement en transit
description: Protège le trajet entre deux points. Le serveur peut être l’un de ces
  points.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Chiffrement en transit

## Définition courte

Protège le trajet entre deux points. Le serveur peut être l’un de ces points.


## Exemple concret

Vous envoyez « rendez-vous à 18 h » via TLS. Le Wi-Fi ne lit pas le texte, mais le serveur qui termine TLS peut le recevoir.


## Ce que cela protège

Le contenu de la connexion contre un observateur du trajet, dans le modèle du protocole.


## Ce que cela ne protège pas

Pas nécessairement le contenu envers le serveur ; pas les IP, horaires ou appareils.


## Pourquoi cela compte

Un cadenas dans le navigateur n’établit pas qui peut lire les messages une fois reçus.

<details class="technical-details"><summary>Détails techniques</summary><p>TLS chiffre une liaison et authentifie son extrémité. Le chiffrement E2EE ajoute une protection du contenu entre les participants.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: transit — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: transit — report.limits">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
