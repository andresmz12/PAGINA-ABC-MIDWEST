#!/usr/bin/env python3
"""Generador del sitio estático bilingüe (EN / ES).

Uso:  python3 tools/build.py
Lee:  tools/site.config.json, tools/content.py, tools/assets_src/, tools/images_src/
Crea: public/  (listo para cualquier hosting estático)
"""
import hashlib
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
PUB = ROOT / "public"
sys.path.insert(0, str(TOOLS))

from content import SERVICES, UI, LEGAL  # noqa: E402
import make_placeholders  # noqa: E402

CFG = json.loads((TOOLS / "site.config.json").read_text(encoding="utf-8"))
DOMAIN = CFG["domain"].rstrip("/")
LANGS = ["en", "es"]
TODAY = date.today().isoformat()
PAGES = []  # [{lang,key,path,title,desc,...}] para el sitemap


def esc(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------------------ rutas
SECTION = {"en": {"services": "services", "about": "about", "contact": "contact", "privacy": "privacy", "terms": "terms"},
           "es": {"services": "servicios", "about": "nosotros", "contact": "contacto", "privacy": "privacidad", "terms": "terminos"}}


def svc_by_id(sid):
    return next(s for s in SERVICES if s["id"] == sid)


def path(key, lang, sid=None):
    pre = "/" if lang == "en" else "/es/"
    if key == "home":
        return pre
    if key == "service":
        return f"{pre}{SECTION[lang]['services']}/{svc_by_id(sid)['slug'][lang]}/"
    return f"{pre}{SECTION[lang][key]}/"


def abs_url(p):
    return DOMAIN + p


def other(lang):
    return "es" if lang == "en" else "en"


# ------------------------------------------------------------------ assets
def file_hash(p):
    return hashlib.md5(p.read_bytes()).hexdigest()[:8]


def build_theme_css():
    c = CFG["colors"]
    css = (":root{\n"
           f"  --primary:{c['primary']};\n  --primary-dark:{c['primary_dark']};\n"
           f"  --accent:{c['accent']};\n  --accent-hover:{c['accent_hover']};\n"
           f"  --light:{c['light']};\n  --text:{c['text']};\n  --muted:{c['muted']};\n}}\n")
    return css


def optimize_images():
    from PIL import Image
    out = PUB / "assets" / "img"
    out.mkdir(parents=True, exist_ok=True)
    for src in sorted((TOOLS / "images_src").glob("*")):
        if src.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        im = Image.open(src).convert("RGB")
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
        im.save(out / (src.stem + ".jpg"), "JPEG", quality=76, optimize=True, progressive=True)


LOGO_MARK = ('<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
             '<rect width="40" height="40" rx="10" fill="{bg}"/>'
             '<path d="M10 28 20 10l10 18" fill="none" stroke="{fg}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
             '<path d="M14.5 22h11" stroke="{fg}" stroke-width="3.4" stroke-linecap="round"/>'
             '<circle cx="31" cy="9" r="2.6" fill="{ac}"/></svg>')


def logo_html(light=False):
    c = CFG["colors"]
    bg, fg = (("#FFFFFF", c["primary"]) if light else (c["primary"], "#FFFFFF"))
    mark = LOGO_MARK.format(bg=bg, fg=fg, ac="#F59E5B" if light else c["accent"])
    cls = "logo logo-light" if light else "logo"
    return (f'<span class="{cls}-inner">{mark}<span class="logo-text"><strong>ABC</strong><span>Midwest</span></span></span>')


def write_static_assets():
    c = CFG["colors"]
    a = PUB / "assets"
    (a / "css").mkdir(parents=True, exist_ok=True)
    (a / "js").mkdir(parents=True, exist_ok=True)
    (a / "css" / "theme.css").write_text(build_theme_css(), encoding="utf-8")
    shutil.copy(TOOLS / "assets_src" / "css" / "styles.css", a / "css" / "styles.css")
    shutil.copy(TOOLS / "assets_src" / "js" / "main.js", a / "js" / "main.js")
    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="%s"/>'
           '<path d="M10 28 20 10l10 18M14.5 22h11" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
           '<circle cx="31" cy="9" r="2.6" fill="#F59E5B"/></svg>') % c["primary"]
    (a / "favicon.svg").write_text(fav, encoding="utf-8")


ASSET_V = {}


def asset_url(rel):
    return f"/assets/{rel}?v={ASSET_V[rel]}"


# ------------------------------------------------------------------ iconos
def _svg(inner, cls="icon", fill="none", stroke=True):
    s = ' stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"' if stroke else ""
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="{fill}"{s} aria-hidden="true" focusable="false">{inner}</svg>'


ICON = {
    "phone": _svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>'),
    "mail": _svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>'),
    "check": _svg('<path d="M20 6 9 17l-5-5"/>'),
    "arrow": _svg('<path d="M5 12h14M12 5l7 7-7 7"/>'),
    "down": _svg('<path d="m6 9 6 6 6-6"/>'),
    "left": _svg('<path d="m15 18-6-6 6-6"/>'),
    "right": _svg('<path d="m9 18 6-6-6-6"/>'),
    "menu": _svg('<path d="M3 12h18M3 6h18M3 18h18"/>'),
    "x": _svg('<path d="M18 6 6 18M6 6l12 12"/>'),
    "pause": _svg('<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>'),
    "play": _svg('<polygon points="6 3 20 12 6 21 6 3"/>'),
    "wa": _svg('<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'),
    "pin": _svg('<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
}

FLAG = {
    "en": '<svg class="flag" viewBox="0 0 24 16" aria-hidden="true" focusable="false"><rect width="24" height="16" rx="2" fill="#fff"/>'
          + "".join(f'<rect y="{i * 2.46:.2f}" width="24" height="1.23" fill="#B22234"/>' for i in range(7))
          + '<rect width="11" height="8.6" rx="1" fill="#3C3B6E"/></svg>',
    "es": '<svg class="flag" viewBox="0 0 24 16" aria-hidden="true" focusable="false"><rect width="24" height="16" rx="2" fill="#fff"/>'
          '<rect width="8" height="16" rx="2" fill="#006847"/><rect x="16" width="8" height="16" rx="2" fill="#CE1126"/>'
          '<circle cx="12" cy="8" r="2" fill="#9C7A2B"/></svg>',
}


# ------------------------------------------------------------------ JSON-LD
def jsonld(objs):
    out = []
    for o in objs:
        out.append('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>")
    return "\n".join(out)


def business_node(lang):
    t = UI[lang]
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": DOMAIN + "/#business",
        "name": CFG["name"],
        "url": DOMAIN + path("home", lang),
        "telephone": CFG["phone_e164"],
        "email": CFG["email"],
        "image": abs_url("/assets/img/og-default.jpg"),
        "description": t["home_meta_desc"],
        "areaServed": [{"@type": "State", "name": a["en"]} for a in CFG["service_areas"]],
        "knowsLanguage": ["en", "es"],
        "contactPoint": {"@type": "ContactPoint", "telephone": CFG["phone_e164"], "email": CFG["email"],
                         "contactType": "customer service", "availableLanguage": ["English", "Spanish"]},
    }


def website_node(lang):
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": DOMAIN + "/#website",
            "url": DOMAIN + "/", "name": CFG["name"], "inLanguage": UI[lang]["html_lang"],
            "publisher": {"@id": DOMAIN + "/#business"}}


def faq_node(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def breadcrumb_node(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(p)}
                                for i, (n, p) in enumerate(items)]}


def service_node(svc, lang):
    s = svc[lang]
    return {"@context": "https://schema.org", "@type": "Service",
            "name": s["name"], "description": s["meta_desc"],
            "url": abs_url(path("service", lang, svc["id"])),
            "serviceType": s["name"],
            "provider": {"@id": DOMAIN + "/#business"},
            "areaServed": [{"@type": "State", "name": a["en"]} for a in CFG["service_areas"]],
            "image": abs_url(f"/assets/img/{svc['img']}.jpg")}


# ------------------------------------------------------------------ layout
def head(lang, key, title, desc, p, alt_paths, ld, sid=None):
    t = UI[lang]
    canon = abs_url(p)
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{abs_url(alt_paths[l])}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{abs_url(alt_paths["en"])}">'
    img = abs_url("/assets/img/og-default.jpg")
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta name="theme-color" content="{CFG['colors']['primary']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(CFG['name'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:locale:alternate" content="{UI[other(lang)]['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap">
<link rel="stylesheet" href="{asset_url('css/theme.css')}">
<link rel="stylesheet" href="{asset_url('css/styles.css')}">
{jsonld(ld)}
</head>"""


def header(lang, key, alt_paths):
    t = UI[lang]
    svc_items = "".join(
        f'<li><a href="{path("service", lang, s["id"])}">{esc(s[lang]["name"])}</a></li>' for s in SERVICES)
    svc_items += f'<li class="dd-all"><a href="{path("services", lang)}">{esc(t["all_services"])}</a></li>'

    def cur(k):
        return ' aria-current="page"' if key == k else ""
    sect = "services" if key in ("services", "service") else key
    return f"""<a class="skip" href="#main">{esc(t['skip'])}</a>
<header class="site-header">
<div class="container header-in">
<a class="logo" href="{path('home', lang)}" aria-label="{esc(CFG['name'])}">{logo_html()}</a>
<button class="burger" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="{esc(t['menu'])}"><span class="i-open">{ICON['menu']}</span><span class="i-close">{ICON['x']}</span></button>
<nav id="primary-nav" class="primary-nav" aria-label="{esc(t['primary_nav'])}">
<ul>
<li><a href="{path('home', lang)}"{cur('home')}>{esc(t['nav_home'])}</a></li>
<li class="has-dd"><a href="{path('services', lang)}"{' aria-current="true"' if sect == 'services' else ''}>{esc(t['nav_services'])}</a><button class="dd-toggle" type="button" aria-expanded="false" aria-label="{esc(t['nav_services'])}">{ICON['down']}</button><ul class="dd">{svc_items}</ul></li>
<li><a href="{path('about', lang)}"{cur('about')}>{esc(t['nav_about'])}</a></li>
<li><a href="{path('contact', lang)}"{cur('contact')}>{esc(t['nav_contact'])}</a></li>
</ul>
</nav>
<div class="header-actions">
<a class="header-phone" href="tel:{CFG['phone_e164']}">{ICON['phone']}<span>{esc(CFG['phone_display'])}</span></a>
<a class="btn btn-accent btn-sm header-quote" href="{path('contact', lang)}">{esc(t['cta_quote'])}</a>
<a class="lang-switch" href="{alt_paths[other(lang)]}" hreflang="{other(lang)}" lang="{other(lang)}" title="{esc(UI[other(lang)]['lang_name'])}">{FLAG[other(lang)]}<span>{UI[other(lang)]['lang_code']}</span></a>
</div>
</div>
</header>"""


def footer(lang, alt_paths):
    t = UI[lang]
    svc = "".join(f'<li><a href="{path("service", lang, s["id"])}">{esc(s[lang]["name"])}</a></li>' for s in SERVICES)
    langs = "".join(
        f'<a class="lang-chip" href="{alt_paths[l]}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{FLAG[l]}<span>{UI[l]["lang_name"]}</span></a>'
        for l in LANGS)
    areas = ", ".join(a[lang] for a in CFG["service_areas"])
    wa = f'https://wa.me/{CFG["whatsapp"]}?text=' + html.escape(UI[lang]["wa_text"].replace(" ", "%20"))
    return f"""<footer class="site-footer">
<div class="container footer-grid">
<div class="f-brand">
<a class="logo logo-light" href="{path('home', lang)}" aria-label="{esc(CFG['name'])}">{logo_html(True)}</a>
<p>{esc(t['footer_blurb'])}</p>
<div class="lang-chips" role="group" aria-label="{esc(t['language'])}">{langs}</div>
</div>
<div><h2 class="f-title">{esc(t['footer_links'])}</h2><ul>
<li><a href="{path('home', lang)}">{esc(t['nav_home'])}</a></li>
<li><a href="{path('about', lang)}">{esc(t['nav_about'])}</a></li>
<li><a href="{path('contact', lang)}">{esc(t['nav_contact'])}</a></li>
<li><a href="{path('privacy', lang)}">{esc(t['privacy'])}</a></li>
<li><a href="{path('terms', lang)}">{esc(t['terms'])}</a></li></ul></div>
<div><h2 class="f-title">{esc(t['footer_services'])}</h2><ul>{svc}</ul></div>
<div><h2 class="f-title">{esc(t['footer_contact'])}</h2><ul class="f-contact">
<li><a href="tel:{CFG['phone_e164']}">{ICON['phone']}{esc(CFG['phone_display'])}</a></li>
<li><a href="mailto:{CFG['email']}">{ICON['mail']}{esc(CFG['email'])}</a></li>
<li><a href="{wa}" rel="noopener" target="_blank">{ICON['wa']}WhatsApp</a></li>
<li class="f-areas">{ICON['pin']}<span>{esc(areas)}</span></li></ul></div>
</div>
<div class="container f-bottom"><p>© {date.today().year} {esc(CFG['name'])}. {esc(t['rights'])}</p>
<p><a href="{path('privacy', lang)}">{esc(t['privacy'])}</a> · <a href="{path('terms', lang)}">{esc(t['terms'])}</a></p></div>
</footer>"""


def floating(lang):
    t = UI[lang]
    wa = f'https://wa.me/{CFG["whatsapp"]}?text=' + html.escape(t["wa_text"].replace(" ", "%20"))
    return f"""<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="{esc(t['cta_whatsapp'])}">{ICON['wa']}</a>
<nav class="mobile-bar" aria-label="{esc(t['mobile_bar'])}">
<a class="mb-call" href="tel:{CFG['phone_e164']}">{ICON['phone']}<span>{esc(t['cta_call'])}</span></a>
<a class="mb-quote" href="{path('contact', lang)}">{esc(t['cta_quote'])}</a>
</nav>"""


def page(lang, key, title, desc, body, ld, alt_paths, sid=None, p=None):
    p = p or path(key, lang, sid)
    html_doc = (head(lang, key, title, desc, p, alt_paths, ld, sid) + "\n<body>\n" + header(lang, key, alt_paths)
                + f'\n<main id="main">\n{body}\n</main>\n' + footer(lang, alt_paths) + "\n" + floating(lang)
                + f'\n<script src="{asset_url("js/main.js")}" defer></script>\n</body>\n</html>\n')
    out = PUB / p.strip("/") / "index.html" if p != "/" else PUB / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_doc, encoding="utf-8")
    PAGES.append({"lang": lang, "key": key, "sid": sid, "path": p, "alt": alt_paths})


# ------------------------------------------------------------------ bloques
def breadcrumbs(lang, trail):
    """trail: [(nombre, ruta|None)] — el último es la página actual."""
    t = UI[lang]
    parts = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            parts.append(f'<li><a href="{p}">{esc(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="{esc(t["breadcrumb"])}"><ol>{"".join(parts)}</ol></nav>'


def cta_banner(lang):
    t = UI[lang]
    return f"""<section class="section banner dark"><div class="container banner-in reveal">
<div><h2>{esc(t['banner_title'])}</h2><p>{esc(t['banner_text'])}</p></div>
<div class="banner-actions"><a class="btn btn-accent btn-lg" href="{path('contact', lang)}">{esc(t['cta_quote'])}</a>
<a class="btn btn-ghost btn-lg" href="tel:{CFG['phone_e164']}">{ICON['phone']}{esc(CFG['phone_display'])}</a></div></div></section>"""


def faq_list(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{esc(q)}{ICON["down"]}</summary><div class="faq-a"><p>{esc(a)}</p></div></details>' for q, a in items) + "</div>"


def service_cards(lang, exclude=None):
    t = UI[lang]
    out = []
    for s in SERVICES:
        if s["id"] == exclude:
            continue
        d = s[lang]
        out.append(f"""<article class="card svc-card reveal">
<div class="card-img"><img src="/assets/img/{s['img']}.jpg" alt="{esc(d['img_alt'])}" width="1400" height="933" loading="lazy" decoding="async"></div>
<div class="card-body"><h3><a class="stretched" href="{path('service', lang, s['id'])}">{esc(d['name'])}</a></h3>
<p>{esc(d['short'])}</p><span class="link-arrow">{esc(t['learn_more'])}{ICON['arrow']}</span></div></article>""")
    return '<div class="grid grid-svc">' + "".join(out) + "</div>"


def steps(items):
    return '<ol class="steps">' + "".join(
        f'<li class="step reveal"><span class="step-n">{i + 1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></li>'
        for i, (a, b) in enumerate(items)) + "</ol>"


def areas_list(lang):
    return '<ul class="chips">' + "".join(f'<li>{ICON["pin"]}{esc(a[lang])}</li>' for a in CFG["service_areas"]) + "</ul>"


def quote_card(lang, sid=None):
    t = UI[lang]
    href = path("contact", lang) + (f"?service={sid}" if sid else "")
    return f"""<aside class="quote-card"><h3>{esc(t['quote_card_title'])}</h3><p>{esc(t['quote_card_text'])}</p>
<a class="btn btn-accent btn-block" href="{href}">{esc(t['cta_quote'])}</a>
<a class="btn btn-outline-light btn-block" href="tel:{CFG['phone_e164']}">{ICON['phone']}{esc(CFG['phone_display'])}</a></aside>"""


# ------------------------------------------------------------------ páginas
def alt_map(key, sid=None):
    return {l: path(key, l, sid) for l in LANGS}


def build_home(lang):
    t = UI[lang]
    alt = alt_map("home")
    slides = []
    dots = []
    for i, (h, sub, img, alt_txt) in enumerate(t["slides"]):
        first = i == 0
        slides.append(f"""<div class="slide{' is-active' if first else ''}" role="group" aria-roledescription="slide" aria-label="{i + 1} / {len(t['slides'])}"{'' if first else ' aria-hidden="true"'}>
<img src="/assets/img/{img}.jpg" alt="{esc(alt_txt)}" width="1400" height="788"{' fetchpriority="high"' if first else ' loading="lazy"'} decoding="async">
<div class="slide-shade"></div>
<div class="container slide-copy"><h2 class="slide-title">{esc(h)}</h2><p>{esc(sub)}</p>
<div class="slide-actions"><a class="btn btn-accent btn-lg" href="{path('contact', lang)}">{esc(t['cta_quote'])}</a>
<a class="btn btn-ghost btn-lg" href="{path('services', lang)}">{esc(t['nav_services'])}</a></div></div></div>""")
        dots.append(f'<button type="button" class="dot{" is-active" if first else ""}" aria-label="{esc(t["go_slide"])} {i + 1}"{" aria-current=\"true\"" if first else ""}></button>')
    hero = f"""<section class="hero" aria-roledescription="carousel" aria-label="{esc(t['home_h1'])}">
<div class="hero-kicker container"><h1>{esc(t['home_h1'])}</h1></div>
<div class="slides" aria-live="off">{''.join(slides)}</div>
<div class="hero-ctrl container"><div class="dots">{''.join(dots)}</div>
<div class="arrows"><button type="button" class="ctrl prev" aria-label="{esc(t['prev'])}">{ICON['left']}</button>
<button type="button" class="ctrl toggle" aria-label="{esc(t['pause'])}" data-pause="{esc(t['pause'])}" data-play="{esc(t['play'])}"><span class="i-pause">{ICON['pause']}</span><span class="i-play">{ICON['play']}</span></button>
<button type="button" class="ctrl next" aria-label="{esc(t['next'])}">{ICON['right']}</button></div></div>
</section>"""
    facts = '<section class="facts dark"><div class="container facts-grid">' + "".join(
        f'<div class="fact reveal"><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in t["facts"]) + "</div></section>"
    services = f"""<section class="section"><div class="container"><div class="sec-head reveal"><p class="eyebrow">{esc(t['services_eyebrow'])}</p>
<h2>{esc(t['services_title'])}</h2><p class="lead">{esc(t['services_lead'])}</p></div>{service_cards(lang)}</div></section>"""
    process = f"""<section class="section dark"><div class="container"><div class="sec-head reveal"><p class="eyebrow">{esc(t['process_eyebrow'])}</p>
<h2>{esc(t['process_title'])}</h2></div>{steps(t['process'])}</div></section>"""
    about = f"""<section class="section gray"><div class="container split">
<div class="split-img reveal"><img src="/assets/img/about.jpg" alt="{esc(t['about_img_alt'])}" width="1100" height="1300" loading="lazy" decoding="async"></div>
<div class="split-copy reveal"><p class="eyebrow">{esc(t['about_eyebrow'])}</p><h2>{esc(t['about_title'])}</h2>
{''.join(f'<p>{esc(x)}</p>' for x in t['about_text'])}
<h3 class="mini">{esc(t['areas_title'])}</h3>{areas_list(lang)}
<a class="btn btn-primary" href="{path('about', lang)}">{esc(t['about_cta'])}</a></div></div></section>"""
    faqs = t["faq_home"]
    faq = f"""<section class="section"><div class="container narrow"><div class="sec-head reveal"><p class="eyebrow">{esc(t['faq_eyebrow'])}</p>
<h2>{esc(t['faq_title'])}</h2></div>{faq_list(faqs)}</div></section>"""
    body = hero + facts + services + process + about + faq + cta_banner(lang)
    ld = [business_node(lang), website_node(lang), faq_node(faqs)]
    page(lang, "home", t["home_meta_title"], t["home_meta_desc"], body, ld, alt)


def hero_simple(lang, crumbs, h1, lead, img=None, alt_txt="", extra=""):
    bg = (f'<img class="ph-img" src="/assets/img/{img}.jpg" alt="{esc(alt_txt)}" width="1400" height="933" decoding="async" fetchpriority="high">'
          if img else "")
    return f"""<section class="page-hero{' has-img' if img else ''}">{bg}<div class="ph-shade"></div>
<div class="container ph-in">{breadcrumbs(lang, crumbs)}<h1>{esc(h1)}</h1><p class="lead">{esc(lead)}</p>{extra}</div></section>"""


def build_services_index(lang):
    t = UI[lang]
    alt = alt_map("services")
    crumbs = [(t["nav_home"], path("home", lang)), (t["nav_services"], None)]
    body = hero_simple(lang, crumbs, t["services_page_h1"], t["services_page_lead"])
    body += f'<section class="section"><div class="container">{service_cards(lang)}</div></section>'
    body += f"""<section class="section gray"><div class="container"><div class="sec-head reveal"><p class="eyebrow">{esc(t['process_eyebrow'])}</p>
<h2>{esc(t['process_title'])}</h2></div>{steps(t['process'])}</div></section>""" + cta_banner(lang)
    ld = [breadcrumb_node([(t["nav_home"], path("home", lang)), (t["nav_services"], path("services", lang))])]
    page(lang, "services", t["services_meta_title"], t["services_meta_desc"], body.replace('class="section gray"', 'class="section gray"'), ld, alt)


def build_service(lang, svc):
    t = UI[lang]
    d = svc[lang]
    sid = svc["id"]
    alt = alt_map("service", sid)
    crumbs = [(t["nav_home"], path("home", lang)), (t["nav_services"], path("services", lang)), (d["name"], None)]
    extra = (f'<div class="ph-actions"><a class="btn btn-accent btn-lg" href="{path("contact", lang)}?service={sid}">{esc(t["cta_quote"])}</a>'
             f'<a class="btn btn-ghost btn-lg" href="tel:{CFG["phone_e164"]}">{ICON["phone"]}{esc(CFG["phone_display"])}</a></div>')
    body = hero_simple(lang, crumbs, d["name"], d["tagline"], svc["img"], d["img_alt"], extra)
    body += '<section class="trust"><div class="container trust-in">' + "".join(
        f'<span>{ICON["check"]}{esc(x)}</span>' for x in t["trust"]) + "</div></section>"
    body += f"""<section class="section"><div class="container split">
<div class="split-copy reveal"><h2>{esc(d['name'])}</h2>{''.join(f'<p>{esc(x)}</p>' for x in d['summary'])}
<p><a class="btn btn-primary" href="{path('contact', lang)}?service={sid}">{esc(t['cta_quote'])}</a></p></div>
<div class="split-img reveal"><img src="/assets/img/{svc['img']}.jpg" alt="{esc(d['img_alt'])}" width="1400" height="933" loading="lazy" decoding="async"></div></div></section>"""
    cards = "".join(f'<article class="card inc-card reveal"><span class="inc-ico">{ICON["check"]}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>'
                    for a, b in d["includes"])
    body += f"""<section class="section gray"><div class="container"><div class="sec-head reveal"><h2>{esc(t['includes_title'])}</h2>
<p class="lead">{esc(t['includes_lead'])}</p></div><div class="grid grid-4">{cards}</div></div></section>"""
    body += f"""<section class="section dark"><div class="container"><div class="sec-head reveal"><p class="eyebrow">{esc(t['process_eyebrow'])}</p>
<h2>{esc(t['process_service_title'])}</h2></div>{steps(t['process'])}</div></section>"""
    body += f"""<section class="section"><div class="container faq-wrap"><div><div class="sec-head reveal"><h2>{esc(t['faq_service_title'])}</h2></div>
{faq_list(d['faqs'])}</div>{quote_card(lang, sid)}</div></section>"""
    body += f"""<section class="section gray"><div class="container"><div class="sec-head reveal"><h2>{esc(t['other_services'])}</h2></div>
{service_cards(lang, exclude=sid)}</div></section>"""
    ld = [service_node(svc, lang), faq_node(d["faqs"]),
          breadcrumb_node([(t["nav_home"], path("home", lang)), (t["nav_services"], path("services", lang)),
                           (d["name"], path("service", lang, sid))])]
    page(lang, "service", d["meta_title"], d["meta_desc"], body, ld, alt, sid=sid)


def build_about(lang):
    t = UI[lang]
    alt = alt_map("about")
    crumbs = [(t["nav_home"], path("home", lang)), (t["nav_about"], None)]
    body = hero_simple(lang, crumbs, t["about_h1"], t["about_lead"])
    body += f"""<section class="section"><div class="container split">
<div class="split-img reveal"><img src="/assets/img/about.jpg" alt="{esc(t['about_img_alt'])}" width="1100" height="1300" loading="lazy" decoding="async"></div>
<div class="split-copy reveal">{''.join(f'<p>{esc(x)}</p>' for x in t['about_body'])}
<h3 class="mini">{esc(t['areas_title'])}</h3><p>{esc(t['areas_lead'])}</p>{areas_list(lang)}</div></div></section>"""
    vals = "".join(f'<article class="card inc-card reveal"><span class="inc-ico">{ICON["check"]}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in t["values"])
    body += f"""<section class="section gray"><div class="container"><div class="sec-head reveal"><h2>{esc(t['values_title'])}</h2></div>
<div class="grid grid-4">{vals}</div></div></section>""" + cta_banner(lang)
    ld = [business_node(lang), breadcrumb_node([(t["nav_home"], path("home", lang)), (t["nav_about"], path("about", lang))])]
    page(lang, "about", t["about_meta_title"], t["about_meta_desc"], body, ld, alt)


def build_contact(lang):
    t = UI[lang]
    alt = alt_map("contact")
    crumbs = [(t["nav_home"], path("home", lang)), (t["nav_contact"], None)]
    body = hero_simple(lang, crumbs, t["contact_h1"], t["contact_lead"])
    props = "".join(f'<option value="{esc(p)}">{esc(p)}</option>' for p in t["properties"])
    svcs = "".join(f'<option value="{s["id"]}">{esc(s[lang]["name"])}</option>' for s in SERVICES)
    svcs += f'<option value="other">{esc(t["f_service_other"])}</option>'
    req = f'<span class="req" aria-hidden="true">*</span>'
    form = f"""<form class="form" id="quote-form" method="post" action="{esc(CFG['form_endpoint'])}" novalidate
 data-endpoint="{esc(CFG['form_endpoint'])}" data-email="{esc(CFG['email'])}" data-lang="{lang}"
 data-sending="{esc(t['f_sending'])}" data-send="{esc(t['f_send'])}" data-success="{esc(t['f_success'])}"
 data-error="{esc(t['f_error'])}" data-mailto="{esc(t['f_mailto'])}" data-invalid="{esc(t['f_invalid'])}" data-required="{esc(t['f_required'])}">
<div class="f-row"><div class="f-field"><label for="f-name">{esc(t['f_name'])} {req}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="f-field"><label for="f-email">{esc(t['f_email'])} {req}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
<div class="f-row"><div class="f-field"><label for="f-phone">{esc(t['f_phone'])} <small>({esc(t['f_optional'])})</small></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="f-field"><label for="f-company">{esc(t['f_company'])} <small>({esc(t['f_optional'])})</small></label><input id="f-company" name="company" type="text" autocomplete="organization"></div></div>
<div class="f-row"><div class="f-field"><label for="f-prop">{esc(t['f_property'])} {req}</label><select id="f-prop" name="property_type" required><option value="">{esc(t['f_select'])}</option>{props}</select></div>
<div class="f-field"><label for="f-service">{esc(t['f_service'])}</label><select id="f-service" name="service"><option value="">{esc(t['f_select'])}</option>{svcs}</select></div></div>
<div class="f-field"><label for="f-msg">{esc(t['f_message'])} {req}</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
<div class="hp" aria-hidden="true"><label for="f-web">{esc(t['f_honeypot'])}</label><input id="f-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<input type="hidden" name="language" value="{lang}">
<p class="f-note">{esc(t['f_privacy'])} <a href="{path('privacy', lang)}">{esc(t['privacy_link'])}</a>.</p>
<button class="btn btn-accent btn-lg" type="submit">{esc(t['f_send'])}</button>
<div class="f-status" role="status" aria-live="polite" hidden></div>
</form>"""
    wa = f'https://wa.me/{CFG["whatsapp"]}?text=' + html.escape(t["wa_text"].replace(" ", "%20"))
    side = f"""<aside class="side-card reveal"><h2>{esc(t['contact_direct'])}</h2><ul class="contact-list">
<li><a href="tel:{CFG['phone_e164']}">{ICON['phone']}<span><small>{esc(t['call_us'])}</small>{esc(CFG['phone_display'])}</span></a></li>
<li><a href="mailto:{CFG['email']}">{ICON['mail']}<span><small>{esc(t['email_us'])}</small>{esc(CFG['email'])}</span></a></li>
<li><a href="{wa}" target="_blank" rel="noopener">{ICON['wa']}<span><small>WhatsApp</small>{esc(t['cta_whatsapp'])}</span></a></li></ul>
<h3 class="mini">{esc(t['areas_title'])}</h3>{areas_list(lang)}</aside>"""
    body += f'<section class="section"><div class="container contact-grid"><div class="reveal">{form}</div>{side}</div></section>'
    ld = [business_node(lang), breadcrumb_node([(t["nav_home"], path("home", lang)), (t["nav_contact"], path("contact", lang))])]
    page(lang, "contact", t["contact_meta_title"], t["contact_meta_desc"], body, ld, alt)


def todo(text):
    return re.sub(r"\{\{(.+?)\}\}", lambda m: f'<mark class="todo">[{esc(m.group(1))}]</mark>', esc(text).replace("&quot;", '"').replace("&#x27;", "'"))


def build_legal(lang, key):
    t = UI[lang]
    alt = alt_map(key)
    L = LEGAL[key][lang]
    crumbs = [(t["nav_home"], path("home", lang)), (L["h1"], None)]
    body = hero_simple(lang, crumbs, L["h1"], t["updated"] + ": " + "{{DATE}}".replace("{{DATE}}", TODAY))
    notice = f'<p class="draft-notice" role="note">{esc(t["draft_notice"])}</p>' if CFG.get("legal_draft_notice") else ""
    secs = "".join(f'<h2>{i + 1}. {esc(h)}</h2>' + "".join(f"<p>{todo(p)}</p>" for p in ps) for i, (h, ps) in enumerate(L["sections"]))
    body += f'<section class="section"><div class="container narrow legal">{notice}{secs}</div></section>'
    ld = [breadcrumb_node([(t["nav_home"], path("home", lang)), (L["h1"], path(key, lang))])]
    page(lang, key, t[f"{key}_meta_title"], t[f"{key}_meta_desc"], body, ld, alt)


def build_404():
    lang = "en"
    t, e = UI["en"], UI["es"]
    alt = {"en": "/404.html", "es": "/404.html"}
    body = f"""<section class="section nf"><div class="container narrow center">
<p class="nf-code" aria-hidden="true">404</p><h1>{esc(t['nf_title'])} · {esc(e['nf_title'])}</h1>
<p class="lead">{esc(t['nf_text'])}<br>{esc(e['nf_text'])}</p>
<p><a class="btn btn-primary btn-lg" href="/">{esc(t['nf_home'])}</a> <a class="btn btn-outline btn-lg" href="/es/">{esc(e['nf_home'])}</a></p></div></section>"""
    doc = (head(lang, "404", t["nf_meta_title"], t["nf_meta_desc"], "/404.html", alt, []).replace(
        '<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"', 1)
        + "\n<body>\n" + header(lang, "404", {"en": "/", "es": "/es/"}) + f'\n<main id="main">\n{body}\n</main>\n'
        + footer(lang, {"en": "/", "es": "/es/"}) + "\n" + floating(lang)
        + f'\n<script src="{asset_url("js/main.js")}" defer></script>\n</body>\n</html>\n')
    (PUB / "404.html").write_text(doc, encoding="utf-8")


def build_seo_files():
    urls = []
    for pg in PAGES:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(pg["alt"][l])}"/>' for l in LANGS)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(pg["alt"]["en"])}"/>'
        pri = "1.0" if pg["key"] == "home" else ("0.8" if pg["key"] in ("services", "service", "contact") else "0.5")
        urls.append(f'<url><loc>{abs_url(pg["path"])}</loc><lastmod>{TODAY}</lastmod><priority>{pri}</priority>{alts}</url>')
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    (PUB / "sitemap.xml").write_text(sm, encoding="utf-8")
    (PUB / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")


def main():
    make_placeholders_ok = True  # genera solo las fotos que falten
    for name, w, h, kind, seed, c1, c2 in make_placeholders.JOBS:
        if not (make_placeholders.OUT / f"{name}.jpg").exists():
            make_placeholders.scene(name, w, h, kind, seed, c1, c2)
    if PUB.exists():
        shutil.rmtree(PUB)
    PUB.mkdir()
    write_static_assets()
    optimize_images()
    for rel in ("css/theme.css", "css/styles.css", "js/main.js"):
        ASSET_V[rel] = file_hash(PUB / "assets" / rel)
    for lang in LANGS:
        build_home(lang)
        build_services_index(lang)
        for s in SERVICES:
            build_service(lang, s)
        build_about(lang)
        build_contact(lang)
        build_legal(lang, "privacy")
        build_legal(lang, "terms")
    build_404()
    build_seo_files()
    print(f"OK: {len(PAGES)} páginas + 404 en {PUB}")


if __name__ == "__main__":
    main()
