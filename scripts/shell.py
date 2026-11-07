"""Shared HTML shell functions for www.groupchaton.com sub-pages."""

BRAND         = "https://assets.groupchaton.com/assets/brand"
CANONICAL_BASE = "https://www.groupchaton.com"
FONTS_URL     = ("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans"
                 ":wght@400;500;600;700&display=swap")

# Plain string — contains CSS braces, must NOT be embedded inside an f-string
PAGE_CSS = """\
:root{--gco:#5FB34C;--gco-dk:#469036;--bg:#fafafa;--sf:#fff;--tx:#111;--tx2:#555;\
--bd:rgba(0,0,0,.09);--bd2:rgba(0,0,0,.16);--sf2:rgba(0,0,0,.04);\
--r:10px;--sans:'Plus Jakarta Sans',system-ui,sans-serif}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){\
--bg:#111;--sf:#181818;--tx:#f0f0f0;--tx2:#8a8a8a;\
--bd:rgba(255,255,255,.08);--bd2:rgba(255,255,255,.18);--sf2:rgba(255,255,255,.06)}}
:root[data-theme="dark"]{--bg:#111;--sf:#181818;--tx:#f0f0f0;--tx2:#8a8a8a;\
--bd:rgba(255,255,255,.08);--bd2:rgba(255,255,255,.18);--sf2:rgba(255,255,255,.06)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);background:var(--bg);color:var(--tx);line-height:1.75;padding:0}
a{color:var(--gco);text-decoration:none}a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:200;background:var(--sf);border-bottom:1px solid var(--bd)}
.hdr-in{max-width:1120px;margin:0 auto;padding:0 24px;display:flex;align-items:center;\
justify-content:space-between;height:62px;gap:12px}
.logo{display:flex;align-items:center}
.logo img{height:44px;width:auto}
@media(max-width:480px){.logo img{height:36px}}
.logo .dk{display:none}
[data-theme="dark"] .logo .dk{display:block}[data-theme="dark"] .logo .lt{display:none}
@media(prefers-color-scheme:dark){\
:root:not([data-theme="light"]) .logo .dk{display:block}\
:root:not([data-theme="light"]) .logo .lt{display:none}}
.hdr-nav{display:flex;align-items:center;gap:5px}
.hdr-nav a{font-size:.78rem;font-weight:700;padding:5px 11px;border-radius:20px;\
background:rgba(var(--c),.1);color:rgb(var(--c));border:1px solid rgba(var(--c),.22);\
transition:background .18s,border-color .18s,transform .18s;white-space:nowrap}
.hdr-nav a:hover{background:rgba(var(--c),.2);border-color:rgba(var(--c),.4);\
transform:translateY(-1px);text-decoration:none}
#tbtn{width:36px;height:36px;display:flex;align-items:center;justify-content:center;\
border-radius:8px;border:1px solid var(--bd2);background:transparent;cursor:pointer;\
color:var(--tx2);transition:color .18s,background .18s,border-color .18s;flex-shrink:0}
#tbtn:hover{color:var(--tx);background:var(--sf2)}
@media(max-width:680px){.hdr-nav{display:none}}
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
    "var h=document.documentElement;"
    "function applyT(t){"
    "if(t)h.setAttribute('data-theme',t);else h.removeAttribute('data-theme');"
    "var dk=t==='dark'||(!t&&window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches);"
    "var sun=document.getElementById('i-sun'),moon=document.getElementById('i-moon');"
    "if(sun)sun.style.display=dk?'none':'';"
    "if(moon)moon.style.display=dk?'':'none';"
    "}"
    "applyT(localStorage.getItem('gco-theme'));"
    "document.addEventListener('DOMContentLoaded',function(){"
    "applyT(localStorage.getItem('gco-theme'));"
    "var btn=document.getElementById('tbtn');"
    "if(btn)btn.addEventListener('click',function(){"
    "var cur=h.getAttribute('data-theme');"
    "var dk=cur==='dark'||(!cur&&window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches);"
    "var n=dk?'light':'dark';"
    "applyT(n);localStorage.setItem('gco-theme',n);"
    "});"
    "});"
    "})();</script>"
)

_SUN_SVG = ('<svg id="i-sun" viewBox="0 0 24 24" width="17" height="17" stroke="currentColor"'
            ' fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="12" cy="12" r="5"/>'
            '<line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/>'
            '<line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>'
            '<line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>'
            '<line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/>'
            '<line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>'
            '<line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>')
_MOON_SVG = ('<svg id="i-moon" viewBox="0 0 24 24" width="17" height="17" stroke="currentColor"'
             ' fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
             '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>')

PAGE_HEADER_HTML = (
    "<header>\n"
    '  <div class="hdr-in">\n'
    '    <a href="/" class="logo" aria-label="GroupChatOn home">\n'
    f'      <img src="{BRAND}/gsc-light.png" alt="GroupChatOn" height="44" class="lt">\n'
    f'      <img src="{BRAND}/gsc-dark.png" alt="" height="44" class="dk">\n'
    "    </a>\n"
    '    <nav class="hdr-nav" aria-label="Services">\n'
    '      <a href="https://infinity.groupchaton.com/" style="--c:160,76,179">∞ Infinity</a>\n'
    '      <a href="https://www.groupchaton.com/" style="--c:95,179,76">\U0001f4d6 Novels</a>\n'
    '      <a href="https://share.groupchaton.com/" style="--c:37,211,102">\U0001f517 Share</a>\n'
    '      <a href="https://help.groupchaton.com/" style="--c:13,148,136">❓ Help</a>\n'
    '      <a href="https://toolkit.groupchaton.com/" style="--c:37,99,235">\U0001f5c2 Toolkit</a>\n'
    '      <a href="https://send.groupchaton.com/" style="--c:234,88,12">\U0001f4e4 Send</a>\n'
    "    </nav>\n"
    '    <button id="tbtn" aria-label="Toggle light/dark theme">\n'
    f'      {_SUN_SVG}\n'
    f'      {_MOON_SVG}\n'
    "    </button>\n"
    "  </div>\n"
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
