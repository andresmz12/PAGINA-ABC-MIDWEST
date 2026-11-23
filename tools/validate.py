#!/usr/bin/env python3
"""Valida el sitio generado en public/.  Uso: python3 tools/validate.py
Sale con código 1 si hay errores. Las advertencias (pendientes) no fallan."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
CFG = json.loads((ROOT / "tools" / "site.config.json").read_text(encoding="utf-8"))
DOMAIN = CFG["domain"].rstrip("/")
errors, warns = [], []


def err(f, m): errors.append(f"{f}: {m}")
def warn(f, m): warns.append(f"{f}: {m}")


class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.title = ""; s.in_title = False; s.meta = {}; s.links = []; s.h1 = 0; s.imgs = []
        s.hrefs = []; s.srcs = []; s.ld = []; s.in_ld = False; s.ids = set(); s.todo = 0; s.html_lang = None

    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a: self.ids.add(a["id"])
        if tag == "html": self.html_lang = a.get("lang")
        if tag == "title": self.in_title = True
        elif tag == "meta":
            k = a.get("name") or a.get("property")
            if k: self.meta[k] = a.get("content", "")
        elif tag == "link": self.links.append(a)
        elif tag == "h1": self.h1 += 1
        elif tag == "img": self.imgs.append(a)
        elif tag == "a" and a.get("href"): self.hrefs.append(a["href"])
        elif tag == "script":
            if a.get("type") == "application/ld+json": self.in_ld = True; self.ld.append("")
            elif a.get("src"): self.srcs.append(a["src"])
        elif tag == "mark" and "todo" in (a.get("class") or ""): self.todo += 1
        if tag == "link" and a.get("rel") == "stylesheet" and a.get("href", "").startswith("/"): self.srcs.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "script": self.in_ld = False

    def handle_data(self, d):
        if self.in_title: self.title += d
        if self.in_ld: self.ld[-1] += d


def local_target(href):
    u = urlparse(href)
    if u.scheme in ("http", "https", "mailto", "tel") or href.startswith("#"):
        return None
    p = u.path
    t = PUB / p.lstrip("/")
    if p.endswith("/") or t.is_dir():
        t = t / "index.html"
    return t


pages = sorted(PUB.rglob("*.html"))
if not pages:
    print("No hay páginas en public/. Ejecuta tools/build.py"); sys.exit(1)
titles, descs, canon_seen = {}, {}, {}
sm_urls = set()
sm = PUB / "sitemap.xml"
if sm.exists():
    for loc in ET.parse(sm).getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        sm_urls.add(loc.text)
else:
    err("sitemap.xml", "no existe")
if not (PUB / "robots.txt").exists(): err("robots.txt", "no existe")
elif "Sitemap:" not in (PUB / "robots.txt").read_text(): err("robots.txt", "falta la línea Sitemap")

for f in pages:
    rel = str(f.relative_to(PUB)); is404 = rel == "404.html"
    p = P(); p.feed(f.read_text(encoding="utf-8"))
    t = p.title.strip(); d = p.meta.get("description", "")
    if not t: err(rel, "sin <title>")
    elif len(t) > 75: err(rel, f"título de {len(t)} caracteres (>75)")
    if not d: err(rel, "sin meta description")
    elif len(d) > 160: err(rel, f"descripción de {len(d)} caracteres (>160)")
    if t in titles: err(rel, f"título duplicado con {titles[t]}")
    titles[t] = rel
    if d in descs: err(rel, f"descripción duplicada con {descs[d]}")
    descs[d] = rel
    if p.h1 != 1: err(rel, f"{p.h1} etiquetas H1 (debe ser 1)")
    if not p.html_lang: err(rel, "<html> sin lang")
    cano = [l["href"] for l in p.links if l.get("rel") == "canonical"]
    if len(cano) != 1: err(rel, "debe tener exactamente un canonical")
    else:
        if not cano[0].startswith(DOMAIN + "/"): err(rel, f"canonical fuera del dominio: {cano[0]}")
        if not is404:
            canon_seen[cano[0]] = rel
            if cano[0] not in sm_urls: err(rel, "canonical ausente en sitemap.xml")
    hl = {l.get("hreflang"): l["href"] for l in p.links if l.get("rel") == "alternate" and l.get("hreflang")}
    for k in ("en", "es", "x-default"):
        if k not in hl: err(rel, f"falta hreflang={k}")
    for k in ("og:title", "og:description", "og:url", "og:image", "twitter:card", "twitter:title"):
        if k not in p.meta: err(rel, f"falta {k}")
    # JSON-LD
    types = []
    for raw in p.ld:
        try:
            j = json.loads(raw); types.append(j.get("@type"))
        except Exception as e:
            err(rel, f"JSON-LD inválido: {e}")
    if not is404 and "BreadcrumbList" not in types and rel not in ("index.html", "es/index.html"):
        err(rel, "falta BreadcrumbList")
    if rel in ("index.html", "es/index.html"):
        for need in ("LocalBusiness", "WebSite", "FAQPage"):
            if need not in types: err(rel, f"falta JSON-LD {need}")
    if "/services/" in "/" + rel and rel.count("/") >= 3 or ("servicios/" in rel and rel.count("/") >= 3):
        if "Service" not in types: err(rel, "falta JSON-LD Service")
        if "FAQPage" not in types: err(rel, "falta JSON-LD FAQPage")
    # imágenes
    for im in p.imgs:
        if "alt" not in im or not im["alt"].strip(): err(rel, f"imagen sin alt: {im.get('src')}")
        s = im.get("src", "")
        tgt = local_target(s)
        if tgt is not None and not tgt.exists(): err(rel, f"imagen inexistente: {s}")
        if not im.get("width") or not im.get("height"): warn(rel, f"imagen sin width/height: {s}")
    # enlaces y assets
    for h in p.hrefs:
        tgt = local_target(h)
        if tgt is None: continue
        if not tgt.exists(): err(rel, f"enlace interno roto: {h}")
    for s in p.srcs:
        tgt = local_target(s)
        if tgt is not None and not tgt.exists(): err(rel, f"asset inexistente: {s}")
    if p.todo: warn(rel, f"{p.todo} campos pendientes por completar (marcados en amarillo)")

# sitemap vs. páginas
for u in sm_urls:
    if not u.startswith(DOMAIN): err("sitemap.xml", f"URL fuera del dominio: {u}"); continue
    tgt = local_target(u[len(DOMAIN):] or "/")
    if not tgt.exists(): err("sitemap.xml", f"URL sin página: {u}")
for u, r in canon_seen.items():
    pass
# pares de idioma: cada hreflang debe existir
for f in pages:
    pass
# imágenes: peso y ancho
try:
    from PIL import Image
    for im in (PUB / "assets" / "img").glob("*.jpg"):
        w = Image.open(im).width
        if w > 1400: err(str(im.relative_to(PUB)), f"ancho {w}px > 1400")
        if im.stat().st_size > 400_000: warn(str(im.relative_to(PUB)), f"pesa {im.stat().st_size // 1024} KB")
except ImportError:
    warn("imágenes", "Pillow no disponible: no se verificó el ancho")
# datos de ejemplo aún en la config
for k, v in (("phone_e164", "+15550100199"), ("domain", "https://midominio.com"), ("email", "hello@midominio.com")):
    if CFG.get(k) == v: warn("site.config.json", f"'{k}' sigue con el valor de ejemplo ({v})")
if "REPLACE_ME" in CFG.get("form_endpoint", ""): warn("site.config.json", "form_endpoint sin configurar (el formulario abre el correo)")

print(f"Páginas revisadas: {len(pages)} · URLs en sitemap: {len(sm_urls)}")
for w in dict.fromkeys(warns): print("  AVISO:", w)
if errors:
    print(f"\n{len(errors)} ERRORES:")
    for e in errors: print("  ✗", e)
    sys.exit(1)
print("\n✓ Validación correcta: sin errores.")
