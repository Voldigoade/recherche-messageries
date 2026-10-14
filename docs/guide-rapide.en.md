---
title: Quick guide — which messenger should you choose?
description: A practical guide to choosing a messenger by threat model, privacy needs, platform, metadata and IP exposure.
search:
  boost: 4
---

# Quick guide — which messenger should you choose?

This page is for readers who do not want to work through the full research first.

There is **no universal best messenger**. The right choice depends on what you are trying to protect, which devices you use and who the adversary is.

## Short answer

| Main need | Start with | Why | Main caveat |
|---|---|---|---|
| Secure everyday messaging on iPhone + PC | **Signal** | Mature E2EE, official desktop clients, good usability | A phone number is still required by the service |
| A separate pseudonymous identity for someone met online | **SimpleX** | No phone number, email or global user identifier | Relays, push services and endpoints still expose metadata |
| Do not give a phone number to the other person | **SimpleX, Threema, Olvid** | They can be used without sharing a phone number | This does not create network anonymity |
| Reduce direct IP exposure to the other participant | **SimpleX with TURN, Olvid, Signal with relayed calls** | Calls are relayed instead of direct | The relay then sees network metadata |
| Tor-oriented messaging | **Cwtch or Briar** | Onion/Tor architecture | No official iOS client established in this study; specialised tools |
| Large teams / chosen server | **Matrix / Element** | Federation, groups, multi-device | Homeservers still observe substantial metadata |

## Five things to understand first

1. **E2EE is not anonymity.** A server may be unable to read message text while still observing IP addresses, timestamps, accounts or traffic patterns.
2. **The endpoint matters as much as the protocol.** An unlocked or compromised phone can reveal plaintext after decryption.
3. **Calls use a separate network path.** P2P/WebRTC may reveal IP addresses to the peer; TURN hides the peer IP but exposes network metadata to the relay.
4. **Pseudonymity is behavioural too.** Reusing usernames, avatars, documents, photos, writing style or schedules can link identities.
5. **Moving away from Discord does not erase Discord.** The original accounts, invitation message and timing may already be correlated.

## Signal vs SimpleX

**Signal** is generally easier, more mature and more practical on iPhone + PC. With number visibility and discovery both set to `Nobody`, and a fresh username shared directly, the other participant does not need your number. Signal itself still receives a valid number during registration.

**SimpleX** is more attractive when relationship separation is the priority: no mandatory phone number, no mandatory email and no global user ID. The trade-off is a more complex operational model around relays, push and multi-device use.

## What about Session?

Session has an interesting identity and routing model, but this research does not recommend it for high-assurance use until the status of fixes and independent retesting after the 2026 WOOT findings is clear. Its beta calls are also P2P and can reveal the IP address to the peer.

## If you still want one practical starting point

- **Normal secure daily use:** Signal.
- **Strong pseudonymous separation:** SimpleX.
- **No phone number shared:** SimpleX, Threema or Olvid.
- **Tor / hostile network conditions:** Cwtch or Briar when your platforms support them.

These are starting points, not guarantees. Read the [comparison](comparatif.md), [summary](resume.md) and [use-case guide](usages.md) for the conditions behind them.
