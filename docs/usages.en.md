---
title: Choose by use case
description: Conditional recommendations by use case: everyday security, pseudonymity, no-phone identity, hostile contacts, Tor and team collaboration.
search:
  boost: 4
---

# Choose by use case

The right messenger depends on the job. These are **starting points**, not absolute rankings.

| Use case | Start with | Why | Main reservation |
|---|---|---|---|
| Secure everyday messaging | **Signal** | Mature E2EE, active maintenance, good desktop/mobile support | Registration still requires a phone number |
| New pseudonymous identity for a stranger met online | **SimpleX** | No phone/email/global user ID; relationship-specific invitations | Relays, push and endpoint metadata still exist |
| Same scenario, but usability on iPhone + PC matters more | **Signal with hardened number privacy** | Strong usability and content security; peer does not need the number | Signal and the telecom layer still know the registration number |
| No phone number shared with the peer | **SimpleX, Threema, Olvid** | All can avoid exposing a phone number to the contact | Different metadata and multi-device trade-offs |
| Malicious contact / avoid direct IP exposure during calls | **Olvid; SimpleX with TURN; Signal with relay enabled** | Relay prevents the peer from learning the direct IP | The relay sees network metadata |
| Tor-oriented messaging | **Cwtch, Briar** | Onion/Tor routing reduces some local/ISP visibility | No official iOS client established; specialised operational model |
| Large groups or chosen server | **Matrix / Element** | Strong ecosystem, federation and admin control | Homeserver and call infrastructure still observe metadata |
| Broad family/friend adoption | **Signal**; WhatsApp if adoption dominates | Easier migration | WhatsApp is tightly tied to the phone number and Meta ecosystem |
| Discord community | **Discord for community, another messenger for confidential text** | Discord is excellent for communities | Discord text/DMs are not end-to-end encrypted |

## Signal in a pseudonymous configuration

For the scenario studied here, Signal improves substantially when:

- `Who can see my number` is set to `Nobody`;
- `Who can find me by my number` is set to `Nobody`;
- a fresh username is shared instead of the number;
- profile name/avatar are not reused elsewhere;
- safety numbers are verified through a separate trusted channel when identity matters.

This protects the number **from the contact**, not from Signal or the phone-number ecosystem used for registration.

## When SimpleX is the better fit

SimpleX is preferable when the main objective is to avoid a global account identifier and keep relationships more compartmentalised. It does not make network activity invisible: relays, ISP/Wi-Fi, push providers and endpoints remain part of the threat model.

## When not to chase the “most private” app

A less familiar tool can create its own risk if users misconfigure calls, lose recovery material, fail to verify keys or abandon the app because it is too hard to use. For many ordinary users, a mature and correctly configured Signal deployment is safer in practice than a more exotic system they do not understand.
