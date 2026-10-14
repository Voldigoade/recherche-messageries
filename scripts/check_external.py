"""Check source URL availability without changing research conclusions.

Results are local QA evidence, not evidence about messenger security.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import sys
import requests

ROOT = Path(__file__).resolve().parents[1]


def check(url):
    try:
        with requests.get(url, timeout=(8, 15), stream=True, headers={"User-Agent": "Mozilla/5.0 (compatible; DocumentationLinkCheck/1.0)"}) as response:
            return {"url": url, "status": response.status_code, "destination": response.url}
    except requests.RequestException as exc:
        return {"url": url, "status": "unverified", "error": type(exc).__name__}


def main():
    source = "\n".join(path.read_text(encoding="utf-8-sig") for path in (ROOT / "research").glob("*.md"))
    urls = sorted({u.rstrip(".,;:") for u in re.findall(r"https?://[^\s<>\)\]\|`\"\}]+", source) if "{" not in u})
    with ThreadPoolExecutor(max_workers=16) as executor:
        results = list(executor.map(check, urls))
    out = ROOT / ".qa"
    out.mkdir(exist_ok=True)
    (out / "external-links.json").write_text(json.dumps({"checked_at": datetime.now(timezone.utc).isoformat(), "results": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for result in results:
        code = str(result["status"])
        counts[code] = counts.get(code, 0) + 1
    print(f"Checked {len(results)} distinct cited URLs: {json.dumps(counts)}. Details in .qa/external-links.json.")
    if "--publish" in sys.argv:
        snapshot = {"date_fr": datetime.now(timezone.utc).astimezone(__import__('zoneinfo').ZoneInfo('Europe/Paris')).strftime('%d/%m/%Y'), "checked_at": datetime.now(timezone.utc).isoformat(), "total": len(results), "available": sum(r["status"] in (200, 202) for r in results), "issues": [r for r in results if r["status"] not in (200, 202)]}
        (ROOT / "research" / "source-accessibility.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
