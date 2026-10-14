---
title: Verificación de claves
description: Comprobar que la clave usada coincide con la esperada para el contacto.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Verificación de claves

## Definición breve

Comprobar que la clave usada coincide con la esperada para el contacto.


## Ejemplo concreto

Alice y Bob comparan una huella por un canal independiente de confianza.


## Qué protege

Reduce ciertos riesgos de sustitución de clave o suplantación.


## Qué no protege

Una clave coherente no certifica automáticamente la identidad civil.


## Por qué importa

Cifrar con la clave equivocada puede proteger el mensaje para la persona equivocada.


## Ejemplo de comportamiento

Con Signal solo mediante usuario y sin conocer el número del contacto, comparar Safety Number; AKV no acredita identidad.

<details class="technical-details"><summary>Detalles técnicos</summary><p>La transparencia de claves comprueba coherencia identificador–clave; autenticación humana y comprobaciones externas son distintas.</p></details>


## Pruebas y lectura relacionada

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Fuente: verification — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Fuente: verification — report.limits">[2]</a><p><a href="/recherche-messageries/es/idees-recues/">Ideas equivocadas</a> · <a href="/recherche-messageries/es/comparer/">Comparador</a></p>
