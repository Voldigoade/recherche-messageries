---
title: Cifrado de extremo a extremo — E2EE
description: Los dispositivos de los participantes controlan las claves. El servidor
  de transporte no debería leer mensajes normales.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Cifrado de extremo a extremo — E2EE

## Definición breve

Los dispositivos de los participantes controlan las claves. El servidor de transporte no debería leer mensajes normales.


## Ejemplo concreto

Alice escribe a Bob. El relé transporta texto cifrado; Bob lo descifra en su teléfono.


## Qué protege

La confidencialidad del contenido en el protocolo y ruta documentados, con dispositivos íntegros.


## Qué no protege

No oculta automáticamente IP, horarios, cuenta o grafo social; tampoco copias de Bob ni spyware.


## Por qué importa

El contenido puede estar protegido y la relación seguir siendo identificable.


## Ejemplo de comportamiento

Signal protege normalmente mensajes y llamadas; el texto de Discord no usa E2EE.

<details class="technical-details"><summary>Detalles técnicos</summary><p>Autenticación de claves, dispositivos vinculados, copias e implementaciones determinan el alcance real. E2EE no significa anonimato.</p></details>


## Pruebas y lectura relacionada

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Fuente: e2ee — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Fuente: e2ee — report.limits">[2]</a><p><a href="/recherche-messageries/es/idees-recues/">Ideas equivocadas</a> · <a href="/recherche-messageries/es/comparer/">Comparador</a></p>
