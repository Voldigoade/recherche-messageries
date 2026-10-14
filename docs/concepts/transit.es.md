---
title: Cifrado en tránsito
description: Protege la conexión entre dos puntos. El servidor puede ser uno de ellos.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Cifrado en tránsito

## Definición breve

Protege la conexión entre dos puntos. El servidor puede ser uno de ellos.


## Ejemplo concreto

Envía «nos vemos a las 18» por TLS. El Wi-Fi no lee el texto, pero el servidor que termina TLS puede recibirlo.


## Qué protege

El contenido de la conexión frente a un observador en la ruta, dentro del modelo del protocolo.


## Qué no protege

No necesariamente el contenido frente al servidor; no IP, horarios ni dispositivos.


## Por qué importa

El candado del navegador no establece quién puede leer los mensajes al recibirlos.

<details class="technical-details"><summary>Detalles técnicos</summary><p>TLS cifra una conexión y autentica su extremo. E2EE añade protección del contenido entre participantes.</p></details>


## Pruebas y lectura relacionada

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Fuente: transit — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Fuente: transit — report.limits">[2]</a><p><a href="/recherche-messageries/es/idees-recues/">Ideas equivocadas</a> · <a href="/recherche-messageries/es/comparer/">Comparador</a></p>
