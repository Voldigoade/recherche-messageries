"""Small build hooks: correct source editing and site_url-derived robots."""
import re
import json
import html as html_module
from pathlib import Path


def on_page_context(context, page, config, nav):
    if page.meta.get("source_file"):
        page.edit_url = config["repo_url"] + "/edit/main/research/" + page.meta["source_file"]
    else:
        page.edit_url = config["repo_url"] + "/edit/main/scripts/structure_docs.py"
    return context


def on_post_build(config):
    base = config["site_url"].rstrip("/")
    Path(config["site_dir"], "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: " + base + "/sitemap.xml\n", encoding="utf-8")


def on_page_content(html, page, config, files):
    # Only stand-alone assessment cells get names, never reinterpret other icons.
    labels = {"✅": "Résistance relativement forte", "🟡": "Résistance partielle", "🟠": "Exposition importante", "🔴": "Faible résistance", "❓": "Données insuffisantes"}
    html = re.sub(r"(<td[^>]*>)\s*([✅🟡🟠🔴❓])\s*(</td>)",
                  lambda m: m[1] + f'<span role="img" aria-label="{labels[m[2]]}" title="{labels[m[2]]}">{m[2]}</span>' + m[3], html)
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
