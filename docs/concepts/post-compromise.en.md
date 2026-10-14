---
title: Post-compromise security
description: A session can regain confidentiality after temporary state theft and
  safe key evolution.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Post-compromise security

## Short definition

A session can regain confidentiality after temporary state theft and safe key evolution.


## Concrete example

An attacker copies session state then loses access; fresh exchanges may renew protection.


## What it protects

Some future exchanges after temporary compromise, depending on protocol.


## What it does not protect

Does not repair a phone still controlled by spyware.


## Why it matters

Distinguish cryptographic recovery from cleaning a device.

<details class="technical-details"><summary>Technical details</summary><p>The property depends on key exchanges, assumptions and implementation; it is not uniform across all clients.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: post-compromise — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: post-compromise — report.limits">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
