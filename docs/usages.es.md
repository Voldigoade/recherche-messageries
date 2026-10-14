---
title: Elegir según el caso de uso
description: Recomendaciones condicionales según seguridad diaria, seudonimato, no compartir teléfono, contacto malicioso, Tor y colaboración.
search:
  boost: 4
---

# Elegir según el caso de uso

La mensajería correcta depende del trabajo. Estos son **puntos de partida**, no rankings absolutos.

| Caso de uso | Empezar por | Por qué | Reserva principal |
|---|---|---|---|
| Mensajería segura diaria | **Signal** | E2EE maduro, mantenimiento activo, buen soporte móvil/desktop | El registro sigue exigiendo teléfono |
| Nueva identidad seudónima para alguien conocido en Internet | **SimpleX** | Sin teléfono/email/ID global; invitaciones por relación | Relés, push y endpoints siguen teniendo metadatos |
| Mismo escenario, priorizando iPhone + PC | **Signal con privacidad del número reforzada** | Muy usable y fuerte en seguridad de contenido | Signal y la capa telefónica siguen conociendo el número de registro |
| No compartir teléfono con el contacto | **SimpleX, Threema, Olvid** | Evitan exponer el número al interlocutor | Diferentes compromisos de metadata y multi-dispositivo |
| Contacto malicioso / evitar IP directa en llamadas | **Olvid; SimpleX con TURN; Signal con relay** | El relay impide que el peer vea la IP directa | El relay ve metadatos de red |
| Mensajería orientada a Tor | **Cwtch, Briar** | Onion/Tor reduce parte de la visibilidad local/ISP | Sin iOS oficial establecido; modelo operativo especializado |
| Grupos grandes o servidor elegido | **Matrix / Element** | Ecosistema, federación y administración | Homeserver e infraestructura de llamadas siguen viendo metadata |
| Familia/amigos y adopción fácil | **Signal**; WhatsApp si la adopción domina | Migración sencilla | WhatsApp liga mucho la cuenta al número y a Meta |
| Comunidad Discord | **Discord para comunidad, otra app para texto confidencial** | Discord es excelente para comunidades | Texto y DMs de Discord no son E2EE |

## Signal en configuración seudónima

Para el escenario estudiado, Signal mejora claramente cuando:

- `Who can see my number` = `Nobody`;
- `Who can find me by my number` = `Nobody`;
- se comparte un username nuevo en vez del número;
- nombre/avatar no se reutilizan en otros sitios;
- se verifican los safety numbers por otro canal cuando la identidad importa.

Esto protege el número **frente al contacto**, no frente a Signal o al ecosistema telefónico utilizado para el registro.

## Cuándo SimpleX encaja mejor

SimpleX es preferible cuando la prioridad es evitar un identificador global y compartimentar mejor las relaciones. No vuelve invisible la actividad de red: relés, ISP/Wi-Fi, push providers y dispositivos siguen formando parte del threat model.

## No persigas una app “más privada” que nadie entiende

Una herramienta más exótica puede crear riesgos nuevos si se configuran mal las llamadas, se pierde material de recuperación, no se verifican claves o los usuarios la abandonan porque es demasiado complicada. Para mucha gente, Signal bien configurado será más seguro en la práctica que una solución más rara mal utilizada.
