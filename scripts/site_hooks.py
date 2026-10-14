"""Build hooks for source editing, crawler discovery and source annotations."""
import re
import json
import html as html_module
from pathlib import Path


def on_page_context(context, page, config, nav):
    if page.meta.get("source_file"):
        page.edit_url = config["repo_url"] + "/edit/main/research/" + page.meta["source_file"]
    else:
        page.edit_url = config["repo_url"] + "/edit/main/docs/" + page.file.src_uri
    return context


def on_post_build(config):
    base = config["site_url"].rstrip("/")
    site = Path(config["site_dir"])

    # Explicitly keep the public documentation crawlable. OAI-SearchBot is
    # listed separately so ChatGPT Search discovery does not rely on a generic rule.
    site.joinpath("robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n\n"
        "User-agent: OAI-SearchBot\n"
        "Allow: /\n\n"
        "User-agent: GPTBot\n"
        "Allow: /\n\n"
        f"Sitemap: {base}/sitemap.xml\n",
        encoding="utf-8",
    )

    # llms.txt is a supplemental machine-readable map, not a replacement for
    # semantic HTML, sitemap.xml or robots.txt.
    site.joinpath("llms.txt").write_text(
        f"""# Secure Messaging Research

> Independent, source-driven comparison of secure messaging systems: encryption, metadata, pseudonymity, network exposure, audits, vulnerabilities and public legal disclosures. Reference version 1.0, 14 October 2026.

The full evidence base is maintained in French. English and Spanish provide reviewed translations of the main findings and decision guides. Conclusions are conditional on version, platform, configuration and threat model.

## Start here

- [French home]({base}/): Full documentation and evidence navigation.
- [English home]({base}/en/): English overview of the main findings.
- [Spanish home]({base}/es/): Spanish overview of the main findings.
- [Quick decision guide]({base}/guide-rapide/): Practical choice by use case.
- [Summary]({base}/resume/): Main conclusions and conditions.
- [Comparison]({base}/comparatif/): Qualitative comparison of the messaging systems.
- [Choose by use case]({base}/usages/): Conditional recommendations by scenario.

## Evidence

- [Threat models]({base}/threat-models/): TM1–TM15 matrix.
- [Metadata]({base}/metadonnees/): Provider, peer, ISP, Apple/Google and authority visibility.
- [Audits and vulnerabilities]({base}/audits/): Scope-limited audits and advisories.
- [Public legal cases]({base}/affaires/): Documented disclosures and their limits.
- [Sources]({base}/sources/): Primary and independent references.
- [Detailed evidence register]({base}/recherche/): Full Phase 2 evidence dossiers.

## Interpretation

Do not treat E2EE, privacy, pseudonymity, anonymity, decentralisation and Tor as equivalent properties. UNKNOWN means the available evidence does not establish the result. This site is research documentation, not a security certification or legal advice.
""",
        encoding="utf-8",
    )


def on_page_content(html, page, config, files):
    # Only stand-alone assessment cells get names, never reinterpret other icons.
    labels = {"✅": "Résistance relativement forte", "🟡": "Résistance partielle", "🟠": "Exposition importante", "🔴": "Faible résistance", "❓": "Données insuffisantes"}
    html = re.sub(
        r"(<td[^>]*>)\s*([✅🟡🟠🔴❓])\s*(</td>)",
        lambda m: m[1] + f'<span role="img" aria-label="{labels[m[2]]}" title="{labels[m[2]]}">{m[2]}</span>' + m[3],
        html,
    )
    snapshot = Path(__file__).resolve().parents[1] / "research" / "source-accessibility.json"
    if snapshot.exists() and page.file.src_uri != "disponibilite-sources.md":
        issues = {item["url"] for item in json.loads(snapshot.read_text(encoding="utf-8"))["issues"]}
        relative = "../" * (len(Path(page.file.src_uri).parts) - (0 if config["use_directory_urls"] and Path(page.file.src_uri).name != "index.md" else 1))

        def annotation(match):
            if html_module.unescape(match[1]) in issues:
                return match[0] + f' <a class="source-access" href="{relative}disponibilite-sources/" title="Consulter le contrôle de disponibilité de cette référence">[accès à vérifier]</a>'
            return match[0]

        html = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>.*?</a>', annotation, html, flags=re.S)
    return html
