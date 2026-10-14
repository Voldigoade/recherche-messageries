---
title: Anonimato de red
description: Reducir la capacidad de vincular tráfico con su dirección de red o destino.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Anonimato de red

## Definición breve

Reducir la capacidad de vincular tráfico con su dirección de red o destino.


## Ejemplo concreto

TURN oculta su IP a Bob, pero el relé ve las IP de las conexiones.


## Qué protege

Frente a ciertos observadores limitados, según la ruta real.


## Qué no protege

No evita correlación global de horarios / volumen, identidad de cuenta, perfil ni voz.


## Por qué importa

Una llamada puede usar otra ruta que los mensajes y revelar IP.


## Ejemplo de comportamiento

Cwtch y Briar usan Tor; Session expone IP en llamadas P2P beta.

<details class="technical-details"><summary>Detalles técnicos</summary><p>Tor/onion y VPN desplazan visibilidad y confianza. Ningún servicio estudiado demuestra resistencia general al adversario pasivo global.</p></details>


## Pruebas y lectura relacionada

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L108" aria-label="Fuente: network-anonymity — report.threats">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Fuente: network-anonymity — report.comparison">[2]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Fuente: network-anonymity — report.limits">[3]</a><p><a href="/recherche-messageries/es/idees-recues/">Ideas equivocadas</a> · <a href="/recherche-messageries/es/comparer/">Comparador</a></p>
