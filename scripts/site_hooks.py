"""Build hooks for source editing, crawler discovery and source annotations."""
import re
import json
import html as html_module
from pathlib import Path
from copy import copy
from bs4 import BeautifulSoup


def on_page_context(context, page, config, nav):
    if page.meta.get("editorial_source"):
        page.edit_url = config["repo_url"] + "/edit/main/" + page.meta["editorial_source"]
    elif page.meta.get("source_file"):
        page.edit_url = config["repo_url"] + "/edit/main/research/" + page.meta["source_file"]
    else:
        page.edit_url = config["repo_url"] + "/edit/main/docs/" + page.file.src_uri
    return context


def on_post_build(config):
    # Material 9.7.7 treats hreflang destinations as site roots and fetches a
    # sitemap relative to each page. static-i18n already supplies correct per-page
    # language links. Disable only that auto-rewriter, leaving native navigation,
    # semantic hreflang, search and the rest of Material intact. Dependency is
    # pinned; fail visibly on a future bundle change rather than silently drift.
    bundle = Path(config["site_dir"]) / "assets/javascripts/bundle.d7400e89.min.js"
    if config["theme"].get("language") == "fr" and not bundle.exists():
        raise RuntimeError("Pinned Material bundle missing; review static-i18n integration")
    if bundle.exists():
        original = bundle.read_text(encoding="utf-8")
        marker = "ui({document$:ct});"
        if original.count(marker) != 1:
            raise RuntimeError("Review Material / static-i18n compatibility before updating the pinned bundle")
        bundle.with_name("study.bundle.min.js").write_text(original.replace(marker, "/* Per-page language links are owned by static-i18n. */"), encoding="utf-8")
    if config["theme"].get("language") != "fr":
        return
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
- [Interactive decision guide]({base}/choisir/): Auditable rules, constraints and explicit caveats.
- [Compare messengers]({base}/comparer/): Source-linked properties for two to four applications.
- [Learn the concepts]({base}/concepts/): Definitions, examples, scope and evidence.
- [Common misconceptions]({base}/idees-recues/): Limits of encryption, anonymity and decentralisation.
- [Signal vs SimpleX]({base}/comparaisons/signal-vs-simplex/): A dedicated static comparison.
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


def on_post_page(output, page, config):
    output = output.replace("bundle.d7400e89.min.js", "study.bundle.min.js")
    # The language menu may lead to a language home when no translation exists.
    # That navigation fallback must not be advertised as an hreflang equivalent.
    available = set(getattr(page.file, "alternates", {"fr": page.file}))
    alternates = re.findall(r'<link\b[^>]*rel="alternate"[^>]*>', output)
    for tag in alternates:
        locale = re.search(r'hreflang="([^"]+)"', tag)
        if locale and locale[1] not in available:
            output = output.replace(tag, "", 1)
    return output


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
    soup = BeautifulSoup(html, "html.parser")
    for index, table in enumerate(soup.select("table")):
        heads = table.select("thead tr:first-child > th")
        if not heads: continue
        massive = len(heads) > 7
        table["class"] = ["study-matrix" if massive else "study-table"]
        table["role"] = "table"
        if massive:
            language = config["theme"].get("language", "fr")
            names = {"fr": "Matrice — défilement horizontal avec les flèches", "en": "Matrix — scroll horizontally with arrow keys", "es": "Matriz: desplazamiento horizontal con flechas"}
            region = soup.new_tag("div", attrs={"class": "md-typeset__scrollwrap", "role": "region", "tabindex": "0", "aria-label": names.get(language, names["fr"])})
            inner = soup.new_tag("div", attrs={"class": "md-typeset__table"})
            table.wrap(inner)
            inner.wrap(region)
        for col, head in enumerate(heads):
            head["scope"] = "col"
            head["id"] = f"study-{index}-col-{col}"
        for group in table.select("thead, tbody"): group["role"] = "rowgroup"
        for row_index, row in enumerate(table.select("tr")):
            row["role"] = "row"
            cells = row.find_all(["td", "th"], recursive=False)
            if row.find_parent("thead") or not cells: continue
            cells[0].name = "th"
            cells[0]["scope"] = "row"
            cells[0]["id"] = f"study-{index}-row-{row_index}"
            cells[0]["role"] = "rowheader"
            for col, cell in enumerate(cells[1:],1):
                cell["role"] = "cell"
                if col < len(heads):
                    cell["headers"] = f'{heads[col]["id"]} {cells[0]["id"]}'
                    if not massive:
                        label = soup.new_tag("span", attrs={"class":"study-cell-label"})
                        header_link = heads[col].find("a")
                        if header_link: label.append(copy(header_link))
                        else:
                            label["aria-hidden"] = "true"
                            label.string = heads[col].get("data-label", heads[col].get_text(" ",strip=True))
                        cell.insert(0,label)
    return str(soup)
