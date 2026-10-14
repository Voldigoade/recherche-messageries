---
title: Secreto hacia adelante — PFS
description: Claves comprometidas después no deberían revelar mensajes antiguos protegidos
  con claves efímeras borradas.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Secreto hacia adelante — PFS

## Definición breve

Claves comprometidas después no deberían revelar mensajes antiguos protegidos con claves efímeras borradas.


## Ejemplo concreto

Hoy roban una clave duradera; no debería bastar para descifrar tráfico antiguo grabado.


## Qué protege

La confidencialidad del historial criptográfico dentro del modelo del protocolo.


## Qué no protege

No protege bases locales ya descifradas, capturas del destinatario ni claves nunca borradas.


## Por qué importa

Las garantías pueden variar entre teléfono y PC vinculado.


## Ejemplo de comportamiento

Threema Desktop 2.0 beta no admite PFS en el informe.

<details class="technical-details"><summary>Detalles técnicos</summary><p>PFS depende de protocolo, implementación, borrado y dispositivos vinculados.</p></details>


## Pruebas y lectura relacionada

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Fuente: forward-secrecy — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Fuente: forward-secrecy — report.limits">[2]</a><p><a href="/recherche-messageries/es/idees-recues/">Ideas equivocadas</a> · <a href="/recherche-messageries/es/comparer/">Comparador</a></p>
