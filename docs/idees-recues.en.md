---
title: Common misconceptions
description: Common misconceptions
generated_v2: true
editorial_source: content/learning.json
search:
  boost: 3
---

# Common misconceptions



## “E2EE means anonymous.”

Content secrecy and identification are different properties. Account, IP and timing can remain observable.

<a href="/recherche-messageries/en/concepts/e2ee/">End-to-end encryption — E2EE</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L8" aria-label="Evidence: e2ee-anonymous — report.summary">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Evidence: e2ee-anonymous — report.metadata">[2]</a>


## “The service cannot read my messages, so it knows nothing.”

Account dates, a number or connections can be useful without text. Distinguish capability from actually established disclosure.

<a href="/recherche-messageries/en/concepts/metadata/">Metadata</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Evidence: no-data — report.metadata">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Evidence: no-data — report.legal">[2]</a>


## “With Tor, I cannot be traced.”

Tor reduces some local observations; not copies, profile identity, endpoints or global correlation.

<a href="/recherche-messageries/en/concepts/network-anonymity/">Network anonymity</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L108" aria-label="Evidence: tor — report.threats">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: tor — report.limits">[2]</a>


## “Decentralised means private.”

Nodes, bootstrap, DHT or peers can see their portion of data. Actual operators must be identified.

<a href="/recherche-messageries/en/concepts/privacy/">Privacy and data minimisation</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Evidence: decentralised — report.comparison">[1]</a>


## “Open source means secure.”

Public code helps inspection but does not prove the installed binary matches it. No current build was reproduced bit-for-bit here.

<a href="/recherche-messageries/en/concepts/security/">Security</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Evidence: open-source — report.audits">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L46" aria-label="Evidence: open-source — report.methodology">[2]</a>


## “No phone number means anonymous.”

It removes one identifier, not IP, purchases, reused profiles or habits.

<a href="/recherche-messageries/en/concepts/pseudonymity/">Pseudonymity</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L25" aria-label="Evidence: no-phone — report.definitions">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Evidence: no-phone — report.opsec">[2]</a>


## “A VPN makes a messenger anonymous.”

A VPN moves network visibility and trust. It removes neither the account nor other linkage channels. Check the actual path.

<a href="/recherche-messageries/en/concepts/network-anonymity/">Network anonymity</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Evidence: vpn — report.opsec">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L397" aria-label="Evidence: vpn — report.limits">[2]</a>


## “Disappearing messages mean nothing can be recovered.”

The contact can copy or photograph. Notifications, databases, backups and versions matter; do not generalise an old extraction to current fixes.

<a href="/recherche-messageries/en/concepts/confidentiality/">Confidentiality</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L363" aria-label="Evidence: disappearing — report.opsec">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Evidence: disappearing — report.legal">[2]</a>


## “P2P is necessarily more private.”

Less centralisation can come with IP disclosure to the peer. Calling and messaging paths are separate.

<a href="/recherche-messageries/en/concepts/network-anonymity/">Network anonymity</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L85" aria-label="Evidence: p2p — report.comparison">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Evidence: p2p — report.metadata">[2]</a>


## “An audit proves the whole application is safe.”

An audit is bounded by version, date, components and exclusions. Check fixes and retests without extending scope.

<a href="/recherche-messageries/en/concepts/security/">Security</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L179" aria-label="Evidence: audit — report.audits">[1]</a>


## “Without the text, an investigation learns nothing.”

Account data, telecom, stores, ISP, devices and correspondents are different sources. One case does not generalise to all.

<a href="/recherche-messageries/en/concepts/metadata/">Metadata</a> · <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L208" aria-label="Evidence: police — report.legal">[1]</a> <a class="fact-source" href="https://github.com/Voldigoade/recherche-messageries/blob/main/research/rapport-final-messageries.md#L142" aria-label="Evidence: police — report.metadata">[2]</a>
