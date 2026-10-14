---
title: Network anonymity
description: Reduce the ability to link traffic to your network address or its destination.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Network anonymity

## Short definition

Reduce the ability to link traffic to your network address or its destination.


## Concrete example

TURN hides your IP from Bob, but the relay sees connection IPs.


## What it protects

Against some limited observers, depending on the actual path.


## What it does not protect

Not global timing / volume correlation, account identity, profile or voice.


## Why it matters

A call can take a different route from messages and reveal IP.


## Example messenger behaviour

Cwtch and Briar use Tor; Session exposes IP in beta P2P calls.

<details class="technical-details"><summary>Technical details</summary><p>Tor/onion and VPNs move visibility and trust. No studied service demonstrates general resistance to a global passive adversary.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L108" aria-label="Evidence: network-anonymity — report.threats">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Evidence: network-anonymity — report.comparison">[2]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: network-anonymity — report.limits">[3]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
