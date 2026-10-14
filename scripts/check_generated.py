"""Verify the generator in an isolated copy; never replace working-tree pages."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix="messaging-generated-") as temporary:
        shadow = Path(temporary)
        for name in ("scripts", "research", "docs", "data", "content"):
            shutil.copytree(ROOT / name, shadow / name, ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy2(ROOT / "mkdocs.yml", shadow / "mkdocs.yml")
        subprocess.run([sys.executable, str(shadow / "scripts/structure_docs.py")], cwd=shadow, check=True)
        paths = {p.relative_to(shadow) for p in (shadow / "docs").rglob("*") if p.is_file()}
        paths |= {p.relative_to(ROOT) for p in (ROOT / "docs").rglob("*") if p.is_file()}
        paths |= {Path("mkdocs.yml"), Path("research/manifest.json")}
        differences = []
        for relative in sorted(paths):
            original, generated = ROOT / relative, shadow / relative
            if not original.exists() or not generated.exists():
                differences.append(str(relative))
            elif relative.suffix in (".md", ".yml", ".json"):
                if original.read_text(encoding="utf-8") != generated.read_text(encoding="utf-8"):
                    differences.append(str(relative))
            elif original.read_bytes() != generated.read_bytes():
                differences.append(str(relative))
        if differences:
            raise SystemExit("Generated content differs: " + ", ".join(differences))
    print("PASS: isolated generator matches versioned pages, configuration and manifest.")


if __name__ == "__main__":
    main()
