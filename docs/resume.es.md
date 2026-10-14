---
title: Resumen de conclusiones
description: Principales conclusiones de la comparación de mensajerías seguras, con Signal, SimpleX, Olvid, Session, Threema, Cwtch y Briar.
search:
  boost: 4
---

# Resumen de conclusiones

## Conclusiones principales

1. **No existe un ganador universal.** La respuesta cambia según el adversario, la plataforma, el modelo de identidad y la necesidad de llamadas o grupos.
2. **E2EE no significa anonimato.** Un servicio puede no leer el contenido y aun así observar cuenta, IP, horarios o metadatos de tráfico.
3. **SimpleX es el punto de partida práctico más fuerte para separar una nueva identidad seudónima de un contacto conocido en Discord.** No exige teléfono, email ni identificador global.
4. **Signal mejora mucho con una configuración seudónima reforzada.** Con la visibilidad y búsqueda por número en `Nobody`, un username nuevo y un perfil neutro, el contacto no necesita recibir el número. Signal sigue exigiendo uno para registrar la cuenta.
5. **Para iPhone + PC, Signal es la opción segura más práctica de este estudio.** SimpleX, Olvid y Threema son alternativas con otras limitaciones de multi-dispositivo.
6. **Olvid y Threema son buenos cuando el objetivo es no dar el número al contacto**, pero no son sistemas de anonimato de red.
7. **Session queda temporalmente rebajado para usos de alta garantía** por la investigación WOOT 2026 sobre Session Protocol V1 y el estado no resuelto de parches/retests en este informe.
8. **Cwtch y Briar son herramientas especializadas.** Sus diseños orientados a Tor son útiles contra ciertas amenazas de red, pero no se estableció un cliente iOS oficial.
9. **Las llamadas tienen una ruta de red distinta.** P2P puede revelar la IP al interlocutor; TURN la oculta al par pero expone metadatos al relé.
10. **Ninguna mensajería estudiada demuestra resistencia general a un adversario pasivo global.**
11. **El dispositivo domina tras una compromisión.** Un teléfono desbloqueado, spyware, notificaciones o un corresponsal malicioso pueden exponer el texto ya descifrado.
12. **La evidencia legal pública es desigual.** Hay casos concretos para Signal, Threema, Discord y Wire; no encontrar un caso público para otro servicio no prueba que no exista.
13. **Código abierto no equivale a binario distribuido verificado.** La versión 1.0 no reconstruyó todos los APK, IPA o paquetes desktop bit a bit.

## Puntos de partida prácticos

| Situación | Opciones a mirar primero |
|---|---|
| Mensajería segura diaria | Signal |
| Contacto seudónimo conocido en Internet | SimpleX; Signal con privacidad del número reforzada |
| No compartir teléfono | SimpleX, Threema, Olvid |
| Mensajería orientada a Tor | Cwtch, Briar |
| Equipos / colaboración autoalojada | Matrix / Element |
| Adopción masiva | Signal; WhatsApp si la adopción es la restricción principal |

Para una decisión rápida, empieza por la [guía rápida](guide-rapide.md) antes de la [comparación](comparatif.md).
