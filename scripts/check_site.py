"""Check the built site, including every internal destination and fragment."""
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import hashlib
import json
import sys
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CONFIG = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
BASE = CONFIG["site_url"]
BASE_PATH = urlparse(BASE).path
ERRORS = []
CACHE = {}


def soup(path):
    if path not in CACHE:
        CACHE[path] = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    return CACHE[path]


def resolve(url):
    parsed = urlparse(url)
    if parsed.netloc != urlparse(BASE).netloc or not parsed.path.startswith(BASE_PATH):
        return None
    relative = unquote(parsed.path[len(BASE_PATH):])
    target = SITE / relative
    if parsed.path.endswith("/") or target.is_dir():
        target /= "index.html"
    return target


def main():
    pages = list(SITE.rglob("*.html"))
    checked = 0
    for path in pages:
        html = soup(path)
        relative = path.relative_to(SITE).as_posix()
        page_url = urljoin(BASE, relative.removesuffix("index.html"))
        if not html.title or not html.title.get_text(strip=True):
            ERRORS.append(f"{relative}: missing title")
        if path.name != "404.html":
            if not html.select_one('meta[name="description"][content]'):
                ERRORS.append(f"{relative}: missing description")
            canonical = html.select_one('link[rel="canonical"]')
            if not canonical or canonical.get("href") != page_url:
                ERRORS.append(f"{relative}: incorrect canonical")
            if len(html.select("article h1")) != 1:
                ERRORS.append(f"{relative}: expected one article h1")
            lang = 'en' if relative.startswith('en/') else 'es' if relative.startswith('es/') else 'fr'
            if html.html.get('lang') != lang:
                ERRORS.append(f"{relative}: incorrect document language")
            article_data = html.select_one('script[type="application/ld+json"]')
            if not article_data or json.loads(article_data.string)['inLanguage'] != lang:
                ERRORS.append(f"{relative}: incorrect JSON-LD language")
            alternates = {n['hreflang']: urljoin(page_url, n['href']) for n in html.select('link[rel="alternate"][hreflang]')}
            if not alternates or alternates.get(lang) != page_url:
                ERRORS.append(f"{relative}: missing self hreflang")
            for alternate_lang, alternate_url in alternates.items():
                target = resolve(alternate_url)
                if target and target.is_file():
                    other = soup(target)
                    back = other.select_one(f'link[rel="alternate"][hreflang="{lang}"]')
                    if not back or urljoin(alternate_url, back['href']) != page_url:
                        ERRORS.append(f"{relative}: hreflang not reciprocal for {alternate_lang}")
        for node in html.select("a[href], link[href], script[src], img[src]"):
            href = node.get("href", node.get("src", ""))
            if not href or href.startswith(("mailto:", "data:", "javascript:")):
                continue
            full = urljoin(page_url, href)
            target = resolve(full)
            if target is None:
                continue
            checked += 1
            if not target.is_file():
                ERRORS.append(f"{relative}: missing destination {href}")
                continue
            fragment = unquote(urlparse(full).fragment)
            if fragment and target.suffix == ".html" and not soup(target).find(id=fragment):
                ERRORS.append(f"{relative}: missing fragment {href}")
        ids = [node["id"] for node in html.select("[id]")]
        if len(ids) != len(set(ids)):
            ERRORS.append(f"{relative}: duplicate ids")
        for th in html.select("th"):
            if not th.get_text(strip=True):
                ERRORS.append(f"{relative}: empty table heading")
    sitemap = SITE / "sitemap.xml"
    if not sitemap.is_file():
        ERRORS.append("missing sitemap")
    else:
        for node in ET.parse(sitemap).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            target = resolve(node.text)
            if not target or not target.is_file():
                ERRORS.append(f"sitemap: missing target {node.text}")
    if f"Sitemap: {BASE.rstrip('/')}/sitemap.xml" not in (SITE / "robots.txt").read_text(encoding="utf-8"):
        ERRORS.append("robots.txt: incorrect sitemap URL")
    if 'User-agent: OAI-SearchBot\nAllow: /' not in (SITE / 'robots.txt').read_text(encoding='utf-8'):
        ERRORS.append('OAI-SearchBot must remain allowed')
    index = json.loads((SITE / "search" / "search_index.json").read_text(encoding="utf-8"))
    if len(index["docs"]) < 60:
        ERRORS.append("incomplete search index")
    manifest = json.loads((ROOT / "research" / "manifest.json").read_text(encoding="utf-8"))
    required = ['index','guide-rapide','choisir','comparer','comparatif','usages','idees-recues','opsec','methodologie','limites','audits','affaires','metadonnees','threat-models','resume']
    for lang in ('fr','en','es'):
        prefix = '' if lang == 'fr' else lang+'/'
        for name in required:
            target = SITE / (prefix+('index.html' if name=='index' else name+'/index.html'))
            if not target.is_file(): ERRORS.append(f'missing V2 translation: {lang} {name}')
        for m in json.loads((ROOT/'data/messengers.json').read_text(encoding='utf-8'))['messengers']:
            if not (SITE/(prefix+'messageries/'+m['id']+'/index.html')).is_file(): ERRORS.append(f'missing profile: {lang} {m["id"]}')
    for name, digest in manifest["sha256"].items():
        if hashlib.sha256((ROOT / "research" / name).read_bytes()).hexdigest() != digest:
            ERRORS.append(f"source checksum mismatch: {name}")
        if (ROOT / "research" / name).read_bytes() != (SITE / "downloads" / Path(name).with_suffix(".txt")).read_bytes():
            ERRORS.append(f"download differs from original: {name}")
    if ERRORS:
        print("\n".join(ERRORS))
        sys.exit(1)
    print(f"PASS: {len(pages)} HTML pages, {checked} internal links/assets/fragments, titles, descriptions, canonical URLs, sitemap, robots, search and original checksums.")


if __name__ == "__main__":
    main()
