---
title: Comparación de mensajerías
description: Comparación cualitativa de mensajerías seguras por identidad, metadatos, IP, plataformas y límites operativos.
search:
  boost: 4
---

# Comparación de mensajerías

Esta tabla es deliberadamente cualitativa. Evita fingir que privacidad y seguridad pueden reducirse a una única puntuación.

| Mensajería | Identidad / seudonimato | Contenido y metadatos | Llamadas / IP | Lectura práctica |
|---|---|---|---|---|
| **Signal** | Número obligatorio para el servicio; el contacto puede usar username sin recibirlo | E2EE maduro; quedan metadatos de cuenta | Las llamadas pueden ir por relay | Mejor opción práctica general para muchos usuarios, sobre todo iPhone + PC |
| **SimpleX** | Sin teléfono, email ni ID global obligatorio | Buena separación entre relaciones; relés y push ven metadatos de transporte | TURN por defecto; modo directo puede exponer IP | Opción práctica más fuerte aquí para relaciones seudónimas separadas |
| **Olvid** | Sin teléfono/email obligatorio; identidad criptográfica | E2EE, pero quedan visibles metadatos de routing/timing | Diseño TURN-only documentado | Buena opción sin número; no es anonimato de red |
| **Session** | ID aleatorio; sin teléfono | Onion routing para mensajes, pero los hallazgos 2026 reducen la confianza actual | Llamadas beta P2P pueden exponer IP | No tratar como ganador de alta garantía hasta aclarar parches/retests |
| **Threema** | ID aleatorio; teléfono/email opcionales | E2EE con algunos metadatos de cuenta | La ruta de llamada depende del modo | Opción móvil madura si no quieres compartir teléfono |
| **Cwtch** | Sin teléfono/email; perfiles locales | Arquitectura Tor/onion | Sin llamadas actuales establecidas | Herramienta especializada; sin iOS oficial establecido aquí |
| **Briar** | Identidad local | Tor + modos locales/Bluetooth/Wi-Fi en Android | Sin llamadas de voz establecidas | Útil en entornos hostiles; sin iOS y proyecto en modo mantenimiento |
| **Matrix / Element** | MXID + homeserver | E2EE protege contenido, pero el homeserver ve bastante metadata | TURN/SFU/WebRTC importa | Fuerte para equipos y self-hosting; no anónimo por defecto |
| **WhatsApp** | Centrado en número | E2EE para chats personales, muchos metadatos de Meta/cuenta | Opciones relay pueden ocultar IP al par | Adopción excelente, seudonimato débil |
| **Telegram** | Centrado en número | Cloud Chats y grupos no son E2EE; Secret Chats son aparte | Directo/relay según ajuste | Gran producto comunitario, no equivalente a E2EE por defecto |
| **Discord** | Identidad central de cuenta/comunidad | Texto/DM no E2EE; DAVE cubre audio/vídeo elegible | Infra de voz ve metadatos de red | Plataforma comunitaria, no mensajería privada de texto |

Otros sistemas del registro: Jami, Tox/qTox, XMPP/OMEMO, Wire, Delta Chat, Ricochet Refresh y Status/Waku.

## Cómo leer esto

- **Mejor cifrado** no significa **mejor anonimato**.
- **Sin número** no significa **sin metadatos**.
- **Descentralizado** no significa **privado frente a los peers**.
- **Tor** mejora ciertos modelos de amenaza, pero no derrota a un observador global.
- **Open source** mejora la auditabilidad, pero no demuestra que el binario instalado coincida con el código.

Para elegir, usa la [guía rápida](guide-rapide.md) o la [guía por caso de uso](usages.md).
