"""Build www.groupchaton.com into docs/."""

import os
import shutil
import sys

# Allow `import shell` from this same directory
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Allow `import content.*` from the project root
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from shell import page_shell

import content.disclaimer as disclaimer
import content.terms      as terms
import content.privacy    as privacy
import content.contact    as contact

# ---------------------------------------------------------------------------
# Output directories
# ---------------------------------------------------------------------------
DOCS   = os.path.join(ROOT, "docs")
DOCS_P = os.path.join(DOCS, "p")

os.makedirs(DOCS_P, exist_ok=True)

# ---------------------------------------------------------------------------
# Sub-pages
# ---------------------------------------------------------------------------
PAGES = [
    ("disclaimer.html", disclaimer),
    ("terms-of-use.html", terms),
    ("privacy-policy.html", privacy),
    ("contact-us.html", contact),
]

for filename, mod in PAGES:
    html = page_shell(
        title       = mod.TITLE,
        desc        = mod.DESC,
        canonical   = mod.CANONICAL,
        extra_css   = getattr(mod, "EXTRA_CSS", ""),
        body        = mod.BODY,
        omit_footer = getattr(mod, "OMIT_FOOTER", ""),
        extra_script= getattr(mod, "SCRIPT", ""),
    )
    out = os.path.join(DOCS_P, filename)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"  built  docs/p/{filename}")

# ---------------------------------------------------------------------------
# Static files copied to docs/
# ---------------------------------------------------------------------------
STATIC = [
    "index.html",
    "changelog.json",
    "CNAME",
    "robots.txt",
    "ads.txt",
    "gco-dark.png",
    "gco-light.png",
    "404.html",
]

for name in STATIC:
    src = os.path.join(ROOT, name)
    dst = os.path.join(DOCS, name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  copied docs/{name}")
    else:
        print(f"  SKIP   {name} (not found)")

# ---------------------------------------------------------------------------
# sitemap.xml
# ---------------------------------------------------------------------------
CANONICAL_BASE = "https://www.groupchaton.com"

URLS = [
    ("/",                        "weekly", "1.0"),
    ("/p/privacy-policy.html",   "yearly", "0.3"),
    ("/p/terms-of-use.html",     "yearly", "0.3"),
    ("/p/disclaimer.html",       "yearly", "0.3"),
    ("/p/contact-us.html",       "monthly","0.5"),
]

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, freq, pri in URLS:
    lines.append(f"  <url>")
    lines.append(f"    <loc>{CANONICAL_BASE}{path}</loc>")
    lines.append(f"    <changefreq>{freq}</changefreq>")
    lines.append(f"    <priority>{pri}</priority>")
    lines.append(f"  </url>")
lines.append("</urlset>")

sitemap_path = os.path.join(DOCS, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")
print("  built  docs/sitemap.xml")

# ---------------------------------------------------------------------------
# Old novel addresses from the Blogger years (/2024/11/v2c1.html, /2024/11/lcf.html):
# the novels moved to novel.groupchaton.com, and these were 404 in Search Console.
# One small page each that redirects (meta refresh 0 + canonical) to the same
# chapter or novel there. The list comes from the reading app's own data.
# ---------------------------------------------------------------------------
import json, html as _h, urllib.request
NOVEL = "https://novel.groupchaton.com"

def _moved(rel, to):
    f = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(f), exist_ok=True)
    t = _h.escape(to, quote=True)
    with open(f, "w", encoding="utf-8", newline="\n") as o:
        o.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved to novel.groupchaton.com</title>'
                f'<link rel="canonical" href="{t}"><meta name="robots" content="noindex">'
                f'<meta http-equiv="refresh" content="0; url={t}"><script>location.replace({json.dumps(to)}+location.hash)</script>'
                f'</head><body><p>This page moved: <a href="{t}">{t}</a></p></body></html>\n')

try:
    data = json.load(urllib.request.urlopen(NOVEL + "/data/novels.json", timeout=60))
    made = 0
    for n in data["novels"]:
        if n.get("index"):
            _moved(n["index"].lstrip("/"), f"{NOVEL}/novel/{n['id']}/"); made += 1
        for c in n["chapters"]:
            _moved(c[0] + ".html", f"{NOVEL}/read/{c[0]}/"); made += 1
    # Blogger's own list and feed addresses
    for rel in ("search/index.html", "search/label/index.html", "feeds/posts/default.html", "default.html"):
        _moved(rel, "https://www.groupchaton.com/")
    print(f"  built  {made} old novel address redirects")
except Exception as e:
    print(f"  SKIP   old novel redirects ({e})")

print("\nBuild complete.")
