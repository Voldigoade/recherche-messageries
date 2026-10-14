---
title: Secure messaging, privacy and pseudonymity
summary: Independent comparison of Signal, SimpleX, Olvid, Session, Threema, Cwtch, Briar and other messaging systems.
description: Independent research comparing secure messengers by encryption, metadata, pseudonymity, IP exposure, platform support, audits and real-world legal disclosures.
search:
  boost: 5
---

# Secure messaging, privacy and pseudonymity

This project compares **18 messaging systems** using threat models rather than a single “most secure app” score.

**Reference version 1.0 · 14 October 2026.**

## Start here

- **Secure everyday use on iPhone + PC:** Signal is the most practical starting point.
- **A separate pseudonymous identity for contacts met online:** SimpleX is the strongest practical starting point in this research.
- **No phone number shared with the other person:** SimpleX, Threema and Olvid are the main options to examine.
- **Tor-oriented messaging:** Cwtch and Briar are specialised options, but neither has an official iOS client established in this study.
- **Session:** interesting architecture, but temporarily downgraded for high-assurance use until the status of fixes and independent retesting after the 2026 WOOT findings is clear.

[Open the quick decision guide](guide-rapide.md) · [Read the summary](resume.md) · [Compare the messengers](comparatif.md) · [Choose by use case](usages.md)

## What this study actually compares

The research separates **content security, metadata privacy, pseudonymity, network anonymity, unlinkability, IP exposure, provider compromise, legal disclosure, endpoint security and usability**. Those properties are not interchangeable.

A messenger can have excellent E2EE while still exposing account, IP or social metadata. A Tor-based messenger can reduce network exposure while being less mature or harder to use. A decentralised system can still expose IP addresses to peers.

## Evidence

The source base includes official protocol documentation and source code, independent security audits, academic research, security advisories, transparency reports and public court material where available.

The detailed evidence register is maintained in French. English pages focus on the main findings and conditions without silently translating every technical claim.

## Important limits

Version 1.0 did **not** include a controlled packet-capture lab across all apps, commercial forensic acquisition of current devices or bit-for-bit reproduction of every distributed binary. Unknowns remain explicitly marked instead of being converted into scores.
