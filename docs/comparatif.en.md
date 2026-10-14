---
title: Messenger comparison
description: Qualitative comparison of secure messengers by identity, metadata, IP exposure, platform support and operational limits.
search:
  boost: 4
---

# Messenger comparison

This table is deliberately qualitative. It avoids pretending that privacy or security can be reduced to one numerical score.

| Messenger | Identity / pseudonymity | Content & metadata | Calls / IP | Practical reading |
|---|---|---|---|---|
| **Signal** | Phone number required by the service; contacts can use usernames without receiving the number | Mature E2EE; some account metadata remains | Calls can be relayed | Best practical secure default for many users, especially iPhone + PC |
| **SimpleX** | No mandatory phone, email or global user ID | Strong relationship separation; relays and push still observe transport metadata | TURN by default; direct mode can expose IP | Strongest practical option here for separate pseudonymous relationships |
| **Olvid** | No mandatory phone/email; cryptographic identity | E2EE, but server-side routing/timing metadata remains observable | TURN-only design documented | Good no-phone option; not a network-anonymity system |
| **Session** | Random identifier; no phone required | Onion routing for messages, but 2026 protocol findings reduce current assurance | Beta calls are P2P and may expose IP | Do not treat as the high-assurance winner until fixes/retests are clear |
| **Threema** | Random Threema ID; phone/email optional | E2EE with some account metadata and public transparency reporting | Call path depends on mode/configuration | Mature mobile option when phone-number sharing should be avoided |
| **Cwtch** | No phone/email; local profiles | Tor/onion architecture reduces central account metadata | No current calls established in the study | Specialised privacy tool; no official iOS client established here |
| **Briar** | Local identity | Tor plus local/Bluetooth/Wi-Fi modes on Android | No voice calls established | Useful for hostile-network/resilience cases; no iOS client and project in maintenance mode |
| **Matrix / Element** | MXID + homeserver | E2EE rooms protect content, but homeserver sees substantial metadata | TURN/SFU/WebRTC path matters | Strong for teams and self-hosting; not anonymous by default |
| **WhatsApp** | Phone-number-centric | E2EE for personal chats, rich Meta/account metadata | Relay options can hide peer IP | Excellent adoption, weak pseudonymity |
| **Telegram** | Phone-number-centric | Cloud Chats and groups are not E2EE; Secret Chats are separate | Direct/relay depends on setting | Great community product, not equivalent to an E2EE-by-default private messenger |
| **Discord** | Central account/community identity | Text/DMs are not E2EE; DAVE covers eligible voice/video media | Voice infrastructure sees network metadata | Collaboration/community platform, not a private-text messenger |

Other systems in the evidence register include Jami, Tox/qTox, XMPP/OMEMO, Wire, Delta Chat, Ricochet Refresh and Status/Waku. They are not omitted because they are “bad”; each has a different architecture and set of trade-offs.

## How to read this

- **Best encryption** is not the same as **best anonymity**.
- **No phone number** is not the same as **no metadata**.
- **Decentralised** is not the same as **private from peers**.
- **Tor** improves some network threat models but does not defeat a global observer.
- **Open source** improves auditability but does not prove the binary you installed matches the source.

For a decision rather than a taxonomy, use the [quick guide](guide-rapide.md) or [use-case guide](usages.md).
