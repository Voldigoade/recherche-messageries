---
title: Key verification
description: Check that the key used matches the key expected for your contact.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Key verification

## Short definition

Check that the key used matches the key expected for your contact.


## Concrete example

Alice and Bob compare a fingerprint through a separate channel they trust.


## What it protects

Reduces some key-substitution or impersonation risks.


## What it does not protect

A consistent key does not automatically certify civil identity.


## Why it matters

Encrypting to the wrong key can protect the message for the wrong person.


## Example messenger behaviour

For Signal username-only without knowing the peer’s number, compare the Safety Number; AKV does not attest identity.

<details class="technical-details"><summary>Technical details</summary><p>Key transparency checks identifier–key consistency; human authentication and out-of-band checks are separate.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: verification — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: verification — report.limits">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
