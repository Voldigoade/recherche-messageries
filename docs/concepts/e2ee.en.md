---
title: End-to-end encryption — E2EE
description: Participants’ devices control content keys. The transport server should
  not read ordinary messages.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# End-to-end encryption — E2EE

## Short definition

Participants’ devices control content keys. The transport server should not read ordinary messages.


## Concrete example

Alice messages Bob. The relay carries ciphertext; Bob decrypts it on his phone.


## What it protects

Content confidentiality within the documented protocol and path, with uncompromised devices.


## What it does not protect

Not automatically IP, timing, account or social graph; not Bob’s copy or endpoint spyware.


## Why it matters

Content can be protected while the relationship remains identifiable.


## Example messenger behaviour

Signal normally protects messages and calls; Discord text is not E2EE.

<details class="technical-details"><summary>Technical details</summary><p>Key authentication, linked devices, backups and implementations determine the actual scope. E2EE is not a synonym for anonymity.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: e2ee — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: e2ee — report.limits">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
