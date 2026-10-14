---
title: Summary of the findings
description: Main conclusions of the secure-messaging comparison, including Signal, SimpleX, Olvid, Session, Threema, Cwtch and Briar.
search:
  boost: 4
---

# Summary of the findings

## Main conclusions

1. **There is no universal winner.** The answer changes with the adversary, platform, identity model and need for calls or groups.
2. **E2EE is not anonymity.** A service may be unable to read message content while still observing account, IP, timing or traffic metadata.
3. **SimpleX is the strongest practical starting point for separating a new pseudonymous identity from a contact met on Discord.** It does not require a phone number, email address or global user identifier.
4. **Signal becomes much stronger in a pseudonymous configuration.** With number visibility and discovery set to `Nobody`, a fresh username and a neutral profile, the other participant does not need to receive the phone number. Signal still requires a number at registration.
5. **For iPhone + PC, Signal is the most practical secure option in this study.** SimpleX, Olvid and Threema are alternatives with different multi-device trade-offs.
6. **Olvid and Threema are good choices when the goal is not to give a phone number to the contact**, but they are not network-anonymity systems.
7. **Session is temporarily downgraded for high-assurance use** because of the 2026 WOOT research on Session Protocol V1 and the unresolved status of fixes/retesting in this report.
8. **Cwtch and Briar are specialised tools.** Their Tor-oriented designs are relevant to some network threats, but there is no official iOS client established here.
9. **Calls are a separate network path.** P2P may reveal IP addresses to the peer; TURN hides the peer IP but exposes metadata to the relay.
10. **No messenger in this study demonstrates general resistance to a global passive adversary.** Low-latency onion routing does not remove timing and volume correlation risks.
11. **Endpoints dominate after compromise.** An unlocked phone, spyware, notification database or malicious correspondent can expose plaintext regardless of the transport protocol.
12. **Public legal evidence is uneven.** Signal, Threema, Discord and Wire have concrete public examples of account metadata or messages being produced in specific cases; absence of a public case for another service is not proof that no disclosure exists.
13. **Open source is not the same thing as a verified distributed binary.** Version 1.0 did not rebuild every current APK, IPA or desktop package bit-for-bit.

## Practical starting points

| Situation | First options to examine |
|---|---|
| Everyday secure messaging | Signal |
| Pseudonymous contact met online | SimpleX; Signal with hardened privacy settings |
| No phone number shared with the peer | SimpleX, Threema, Olvid |
| Tor-oriented messaging | Cwtch, Briar |
| Teams / self-hosted collaboration | Matrix / Element |
| Mainstream adoption | Signal; WhatsApp when adoption is the overriding constraint |

Read the [quick guide](guide-rapide.md) before the [full comparison](comparatif.md) if you want the shortest path to a decision.
