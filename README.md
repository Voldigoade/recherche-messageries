# Secure Messaging Research

I built this project to answer a question that is usually oversimplified: **which messaging app is actually the right choice for a given threat model?**

It compares 18 messaging systems across content security, metadata, pseudonymity, network exposure, calls, device support, public audits, known vulnerabilities and real-world legal disclosures.

**[Read the website](https://voldigoade.github.io/recherche-messageries/)** · [Quick chooser](https://voldigoade.github.io/recherche-messageries/guide-rapide/) · [English](https://voldigoade.github.io/recherche-messageries/en/) · [Español](https://voldigoade.github.io/recherche-messageries/es/)

## Quick take

There is no universal winner.

| If you mainly need… | Start with… | Main caveat |
|---|---|---|
| A practical secure messenger on iPhone + PC | **Signal** | A phone number is still required by the service, even if hidden from contacts. |
| A separate pseudonymous identity for people met online | **SimpleX** | Relays, push notifications and endpoints still expose metadata. |
| No phone number shared with the other person | **SimpleX, Threema or Olvid** | They solve different identity and network problems; none makes the device anonymous. |
| Tor-oriented messaging / reduced direct network exposure | **Cwtch or Briar** | No official iOS client in the scope of this study; both are specialised tools. |
| Large teams or self-hosted collaboration | **Matrix / Element** | The homeserver still sees substantial metadata even with E2EE rooms. |

Discord text and Telegram Cloud Chats are **not** equivalent to an end-to-end encrypted private messenger.

## What is in the research

The public documentation includes:

- an interactive decision guide with auditable rules and explicit limits;
- a two-to-four messenger comparator with 39 source-linked properties;
- 18 messenger profiles, 16 concepts, 11 misconceptions and five reading paths;
- a TM1–TM15 threat-model matrix;
- metadata visibility by provider, contact, ISP, Apple/Google and authorities;
- call/IP exposure and TURN/P2P distinctions;
- audits, vulnerabilities and version limits;
- public law-enforcement and court cases;
- OPSEC recommendations;
- the full evidence register for readers who want to verify the details.

The conclusions are dated **14 October 2026** and are conditional on the version, platform, configuration and adversary. Unknowns are kept as unknowns instead of being turned into scores.

## Evidence and limitations

This is a source-driven research project, not a security certification. It includes primary documentation, public source code, independent audits, academic work, advisories, transparency reports and court material where available.

No controlled network lab, commercial mobile-forensics acquisition or bit-for-bit rebuild of every distributed binary was performed for version 1.0. Those gaps are stated explicitly in the site.

The reference report is [`research/rapport-final-messageries.md`](research/rapport-final-messageries.md). The detailed evidence register is [`research/enquete-messageries-progress.md`](research/enquete-messageries-progress.md).

## Languages

The full evidence base is maintained in French. **English** and **Spanish** cover all 18 profiles, the learning pages, comparison tools and important methodological, audit and legal summaries. Translated summaries link explicitly to French evidence; the original dossiers retain their wording and scope.

## Local verification

Install Python dependencies with `python -m pip install -r requirements.txt`, then `npm ci` and `npx playwright install chromium`. Run `python scripts/check_catalog.py`, `python scripts/check_generated.py`, `npm test`, `python -m mkdocs build --strict`, `python scripts/check_site.py` and `npm run test:browser`. The generator check works in a temporary copy and does not overwrite edited pages. CI runs the same checks before publication.

## Contributing

If a claim is outdated, a source disappeared, or a newer audit / advisory / court record changes a conclusion, [open an issue](https://github.com/Voldigoade/recherche-messageries/issues/new/choose) with the product, version, date and source.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing a change.

Research and documentation: **CC BY-SA 4.0**. Scripts and configuration: **MIT**.
