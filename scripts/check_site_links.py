"""Check local links and assets in the built Jekyll site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import sys


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
errors = []


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.refs.append(attrs[key])


pages = {}
for file in ROOT.rglob("*.html"):
    parser = Links()
    parser.feed(file.read_text(encoding="utf-8"))
    pages[file] = parser

for file, parser in pages.items():
    for ref in parser.refs:
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc or ref.startswith(("mailto:", "//")):
            continue
        target = (ROOT / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (file.parent / unquote(parsed.path))
        if not parsed.path:
            target = file
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{file.relative_to(ROOT)}: missing {ref}")
        elif parsed.fragment and target.suffix == ".html" and parsed.fragment not in pages.get(target, Links()).ids:
            errors.append(f"{file.relative_to(ROOT)}: missing fragment {ref}")

manifest = ROOT / "assets/icons/site.webmanifest"
if manifest.exists():
    for icon in json.loads(manifest.read_text(encoding="utf-8"))["icons"]:
        target = ROOT / icon["src"].lstrip("/")
        if not target.is_file():
            errors.append(f"manifest: missing {icon['src']}")

print("\n".join(errors) if errors else f"Checked {len(pages)} HTML pages and manifest links: OK")
sys.exit(bool(errors))
