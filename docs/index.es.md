---
title: Mensajería segura, privacidad y seudonimato
description: Investigación independiente que compara mensajerías por cifrado, metadatos, seudonimato, IP, plataformas, auditorías y casos reales.
search:
  boost: 5
---

# Mensajería segura, privacidad y seudonimato

Este proyecto compara **18 sistemas de mensajería** mediante modelos de amenaza, no con una única puntuación de “app más segura”.

**Versión de referencia 1.0 · 14 de octubre de 2026.**

## Empieza aquí

- **Uso diario seguro en iPhone + PC:** Signal es el punto de partida más práctico.
- **Identidad seudónima separada para contactos conocidos en Internet:** SimpleX es el punto de partida práctico más fuerte de este estudio.
- **No compartir un número de teléfono:** SimpleX, Threema y Olvid son las opciones principales.
- **Mensajería orientada a Tor:** Cwtch y Briar son opciones especializadas, sin cliente iOS oficial establecido aquí.
- **Session:** arquitectura interesante, pero rebajada temporalmente para usos de alta garantía hasta aclarar los parches y retests posteriores a WOOT 2026.

[Guía rápida](guide-rapide.md) · [Resumen](resume.md) · [Comparación](comparatif.md) · [Elegir según el uso](usages.md)

## Qué compara realmente el estudio

Se separan **seguridad del contenido, metadatos, seudonimato, anonimato de red, unlinkability, exposición de IP, proveedor, solicitudes legales, seguridad del dispositivo y usabilidad**. No son la misma propiedad.

Una app puede tener E2EE excelente y seguir exponiendo metadatos. Una app basada en Tor puede reducir la exposición de red pero ser menos madura o más difícil de usar.

## Evidencia y límites

La base documental incluye documentación oficial, código público, auditorías independientes, investigación académica, advisories, informes de transparencia y documentos judiciales públicos cuando existen.

El registro completo de pruebas se mantiene en francés. Las páginas en español priorizan las conclusiones principales sin traducir automáticamente afirmaciones técnicas delicadas.

La versión 1.0 no incluyó un laboratorio de captura de tráfico para todas las apps, forense comercial de dispositivos actuales ni reconstrucción bit a bit de todos los binarios distribuidos.
