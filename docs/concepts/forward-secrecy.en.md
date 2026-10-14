---
title: Forward secrecy — PFS
description: Keys compromised later should not reveal old messages protected by deleted
  ephemeral keys.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Forward secrecy — PFS

## Short definition

Keys compromised later should not reveal old messages protected by deleted ephemeral keys.


## Concrete example

A long-term key is stolen today; that should not be enough to decrypt previously recorded traffic.


## What it protects

Confidentiality of cryptographic history within the protocol model.


## What it does not protect

Not already decrypted local databases, recipient screenshots or keys never erased.


## Why it matters

Guarantees may differ between a phone and a linked desktop.


## Example messenger behaviour

Threema Desktop 2.0 beta does not support PFS in the report.

<details class="technical-details"><summary>Technical details</summary><p>PFS depends on protocol, implementation, erasure and linked devices.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: forward-secrecy — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: forward-secrecy — report.limits">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
