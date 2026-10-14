---
title: Telemetry
description: Data an application sends about its operation, such as errors or usage.
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Telemetry

## Short definition

Data an application sends about its operation, such as errors or usage.


## Concrete example

A crash report may describe the device; a relay may see timing even without crash reports.


## What it protects

Disabling optional telemetry may reduce additional transmissions if the option is effective.


## What it does not protect

Does not remove transport metadata, notifications or other actors’ logs.


## Why it matters

“No analytics” and “no observed data” are different claims.

<details class="technical-details"><summary>Technical details</summary><p>Store labels and permissions are declarations / static clues; current SDK and push traffic was not comprehensively compared here.</p></details>


## Evidence and related reading

<a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Evidence: telemetry — report.audits">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L46" aria-label="Evidence: telemetry — report.methodology">[2]</a><p><a href="/recherche-messageries/en/idees-recues/">Common misconceptions</a> · <a href="/recherche-messageries/en/comparer/">Compare messengers</a></p>
