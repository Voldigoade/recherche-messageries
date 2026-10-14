---
title: Chiffrement de bout en bout — E2EE
description: Les terminaux des participants contrôlent les clés du contenu. Le serveur
  de transport ne devrait pas lire les messages normaux.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Chiffrement de bout en bout — E2EE

## Définition courte

Les terminaux des participants contrôlent les clés du contenu. Le serveur de transport ne devrait pas lire les messages normaux.


## Exemple concret

Alice écrit à Bob. Le relais transporte un texte chiffré ; Bob le déchiffre sur son téléphone.


## Ce que cela protège

La confidentialité du contenu dans le protocole et le chemin documentés, avec des terminaux intègres.


## Ce que cela ne protège pas

Ni IP, horaires, compte ou graphe social automatiquement ; ni copie par Bob ou spyware sur un terminal.


## Pourquoi cela compte

Le contenu peut être protégé alors que la relation reste identifiable.


## Comportement d’une messagerie

Signal protège normalement messages et appels ; Discord ne protège pas le texte en E2EE.

<details class="technical-details"><summary>Détails techniques</summary><p>Authentification des clés, appareils liés, sauvegardes et implémentations déterminent le périmètre réel. E2EE n’est pas un synonyme d’anonymat.</p></details>


## Preuves et lecture associée

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Source: e2ee — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Source: e2ee — report.limits">[2]</a><p><a href="/recherche-messageries/idees-recues/">Idées reçues</a> · <a href="/recherche-messageries/comparer/">Comparateur</a></p>
