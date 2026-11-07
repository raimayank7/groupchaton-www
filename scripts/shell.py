"""Shared HTML shell functions for www.groupchaton.com sub-pages."""

BRAND         = "https://assets.groupchaton.com/assets/brand"
CANONICAL_BASE = "https://www.groupchaton.com"
FONTS_URL     = ("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans"
                 ":wght@400;500;600;700&display=swap")

# Plain string — contains CSS braces, must NOT be embedded inside an f-string
PAGE_CSS = """\
:root{--gco:#5FB34C;--gco-dk:#469036;--bg:#fafafa;--sf:#fff;--tx:#111;--tx2:#555;\
--bd:rgba(0,0,0,.09);--r:10px;--sans:'Plus Jakarta Sans',system-ui,sans-serif}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){\
--bg:#111;--sf:#181818;--tx:#f0f0f0;--tx2:#8a8a8a;--bd:rgba(255,255,255,.08)}}
:root[data-theme="dark"]{--bg:#111;--sf:#181818;--tx:#f0f0f0;--tx2:#8a8a8a;\
--bd:rgba(255,255,255,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);background:var(--bg);color:var(--tx);line-height:1.75;padding:0}
a{color:var(--gco);text-decoration:none}a:hover{text-decoration:underline}
header{background:var(--sf);border-bottom:1px solid var(--bd);padding:16px 24px;\
display:flex;align-items:center;gap:12px}
header a.home{font-weight:700;color:var(--tx);font-size:.9rem}
header a.home:hover{color:var(--gco);text-decoration:none}
.wrap{max-width:760px;margin:0 auto;padding:48px 24px 80px}
h1{font-size:1.9rem;font-weight:800;margin-bottom:8px}
.updated{font-size:.85rem;color:var(--tx2);margin-bottom:40px}
h2{font-size:1.1rem;font-weight:700;margin:36px 0 10px}
p,li{font-size:.95rem;color:var(--tx2);margin-bottom:12px}
ul{padding-left:20px}li{margin-bottom:6px}
footer{text-align:center;padding:24px;font-size:.8rem;color:var(--tx2);\
border-top:1px solid var(--bd)}
footer a{color:var(--tx2)}footer a:hover{color:var(--gco)}"""

THEME_SCRIPT = (
    "<script>(function(){"
    "var s=localStorage.getItem('gco-theme');"
    "if(s)document.documentElement.setAttribute('data-theme',s);"
    "})();</script>"
)

PAGE_HEADER_HTML = (
    "<header>\n"
    f'  <img src="{BRAND}/favicon.png" alt="" width="32" height="32">\n'
    '  <a href="/" class="home">GroupChatOn</a>\n'
    "</header>"
)

_FOOTER_ENTRIES = [
    ("home",        "/",                          "GroupChatOn"),
    ("privacy",     "/p/privacy-policy.html",     "Privacy Policy"),
    ("terms",       "/p/terms-of-use.html",       "Terms of Use"),
    ("disclaimer",  "/p/disclaimer.html",         "Disclaimer"),
    ("contact",     "/p/contact-us.html",         "Contact"),
]


def page_footer(omit=""):
    """Return <footer> HTML, omitting the link whose key == omit."""
    links = [
        f'<a href="{href}">{label}</a>'
        for key, href, label in _FOOTER_ENTRIES
        if key != omit
    ]
    sep = " &nbsp;·&nbsp;\n  "
    return f"<footer>\n  {sep.join(links)}\n</footer>"


def page_shell(title, desc, canonical, extra_css="", body="",
               omit_footer="", extra_script=""):
    """Render a complete sub-page HTML document."""
    css    = PAGE_CSS + ("\n" + extra_css if extra_css else "")
    footer = page_footer(omit_footer)
    # Build as string concatenation so CSS braces never enter an f-string
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{title}</title>\n"
        f'<meta name="description" content="{desc}">\n'
        f'<link rel="canonical" href="{CANONICAL_BASE}{canonical}">\n'
        f'<link rel="icon" type="image/png" href="{BRAND}/favicon.png">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        f'<link rel="stylesheet" href="{FONTS_URL}">\n'
        "<style>\n" + css + "\n</style>\n"
        "</head>\n"
        "<body>\n"
        + THEME_SCRIPT + "\n"
        + PAGE_HEADER_HTML + "\n"
        + body + "\n"
        + footer + "\n"
        + (extra_script + "\n" if extra_script else "")
        + "</body>\n"
        "</html>"
    )
