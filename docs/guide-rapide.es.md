---
title: Guía rápida — ¿qué mensajería elegir?
description: Guía práctica para elegir una mensajería según privacidad, seudonimato, metadatos, plataforma y exposición de IP.
search:
  boost: 4
---

# Guía rápida — ¿qué mensajería elegir?

Esta página está pensada para quien no quiere leer toda la investigación antes de tomar una decisión.

No existe una **mejor mensajería universal**. La elección depende de qué quieres proteger, qué dispositivos utilizas y frente a qué adversario.

## Respuesta corta

| Necesidad principal | Mirar primero | Por qué | Límite principal |
|---|---|---|---|
| Mensajería segura y práctica en iPhone + PC | **Signal** | E2EE maduro, clientes oficiales, buena usabilidad | El servicio sigue exigiendo un número de teléfono |
| Identidad seudónima separada para alguien conocido en Internet | **SimpleX** | Sin teléfono, email ni identificador global de usuario | Relés, push y dispositivos siguen exponiendo metadatos |
| No dar tu número a la otra persona | **SimpleX, Threema, Olvid** | Se pueden usar sin compartir el número | Esto no crea anonimato de red |
| Reducir la exposición directa de la IP al interlocutor | **SimpleX con TURN, Olvid, Signal con llamadas relay** | La llamada pasa por un relé | El relé ve metadatos de red |
| Mensajería orientada a Tor | **Cwtch o Briar** | Arquitectura onion/Tor | Sin cliente iOS oficial establecido en este estudio; herramientas especializadas |
| Equipos grandes / servidor elegido | **Matrix / Element** | Federación, grupos, multi-dispositivo | El homeserver sigue viendo bastantes metadatos |

## Cinco cosas que conviene entender

1. **E2EE no significa anonimato.** El servidor puede no leer el texto y aun así ver IP, horarios, cuentas o patrones de tráfico.
2. **El dispositivo importa tanto como el protocolo.** Un teléfono desbloqueado o comprometido puede revelar el contenido ya descifrado.
3. **Las llamadas usan otra ruta de red.** P2P/WebRTC puede revelar la IP al interlocutor; TURN la oculta al par pero entrega metadatos al relé.
4. **El seudonimato también depende del comportamiento.** Reutilizar usuario, avatar, fotos, documentos, estilo o horarios puede vincular identidades.
5. **Salir de Discord no borra Discord.** Las cuentas originales, el mensaje de invitación y los horarios ya pueden estar correlacionados.

## Signal o SimpleX

**Signal** suele ser más sencillo, maduro y práctico en iPhone + PC. Si la visibilidad y la búsqueda por número están en `Nobody`, y compartes únicamente un username nuevo, el interlocutor no necesita conocer tu número. Signal sí recibe un número válido durante el registro.

**SimpleX** es más interesante cuando la prioridad es separar relaciones seudónimas: no exige teléfono, email ni identificador global. A cambio, el modelo operativo de relés, push y multi-dispositivo es más complejo.

## ¿Y Session?

Session tiene un modelo de identidad y enrutamiento interesante, pero esta investigación no lo recomienda para usos de alta garantía mientras no esté claro el estado de los parches y retests independientes posteriores a los hallazgos WOOT 2026. Sus llamadas beta también son P2P y pueden revelar la IP al interlocutor.

## Si todavía quieres un punto de partida

- **Uso diario seguro:** Signal.
- **Separación seudónima fuerte:** SimpleX.
- **No compartir número:** SimpleX, Threema u Olvid.
- **Tor / red hostil:** Cwtch o Briar si tus plataformas lo permiten.

Son puntos de partida, no garantías. Consulta la [comparación](comparatif.md), el [resumen](resume.md) y la [guía por caso de uso](usages.md) para ver las condiciones.
