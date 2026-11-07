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

print("\nBuild complete.")
