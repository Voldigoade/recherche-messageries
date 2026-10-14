---
title: Encryption in transit
description: Protects the connection between two points. The server may be one of
  those points.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Encryption in transit

## Short definition

Protects the connection between two points. The server may be one of those points.


## Concrete example

You send “meet at 6 pm” over TLS. The Wi-Fi cannot read it, but the server terminating TLS can receive it.


## What it protects

Connection content against an observer on the path, within the protocol model.


## What it does not protect

Not necessarily content from the server; not IP addresses, timing or devices.


## Why it matters

A browser padlock does not establish who can read messages after receipt.

<details class="technical-details"><summary>Technical details</summary><p>TLS encrypts a connection and authenticates its endpoint. E2EE adds content protection between participants.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: transit — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: transit — report.limits">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
