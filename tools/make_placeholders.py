#!/usr/bin/env python3
"""Genera fotos PLACEHOLDER abstractas en tools/images_src/ (solo si faltan).

Para usar fotos reales: reemplaza los archivos de tools/images_src/ conservando
el nombre (hero-1.jpg, service-office.jpg, ...) y ejecuta `python3 tools/build.py`.
"""
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

OUT = Path(__file__).resolve().parent / "images_src"
OUT.mkdir(exist_ok=True)

TEAL = (15, 76, 92); DEEP = (10, 47, 58); ORANGE = (184, 67, 11)


def gradient(w, h, c1, c2, vertical=True):
    img = Image.new("RGB", (w, h), c1)
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (y / h) if vertical else (x / w)
            px[x, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return img


def tint(c, k):
    return tuple(max(0, min(255, int(v * k))) for v in c)


def scene(name, w, h, kind, seed, c1=TEAL, c2=DEEP):
    """Bloque plano neutro: marca claramente que falta la foto real (sin pseudo-arte)."""
    tones = {"hero-1": (38, 58, 50), "hero-2": (52, 70, 62), "hero-3": (30, 48, 42)}
    base = tones.get(name, (214, 208, 196) if name.startswith(("service", "about")) else (20, 52, 43))
    Image.new("RGB", (w, h), base).save(OUT / f"{name}.jpg", quality=90)


JOBS = [
    ("hero-1", 1600, 900, "office", 1, TEAL, DEEP),
    ("hero-2", 1600, 900, "floor", 2, (18, 92, 108), DEEP),
    ("hero-3", 1600, 900, "skyline", 3, (12, 62, 78), (6, 30, 40)),
    ("service-office", 1400, 933, "office", 4, TEAL, DEEP),
    ("service-post", 1400, 933, "post", 5, (40, 70, 80), DEEP),
    ("service-floors", 1400, 933, "floor", 6, TEAL, DEEP),
    ("service-windows", 1400, 933, "windows", 7, (22, 100, 120), DEEP),
    ("service-daily", 1400, 933, "lobby", 8, TEAL, DEEP),
    ("about", 1100, 1300, "portrait", 9, TEAL, DEEP),
    ("og-default", 1200, 630, "skyline", 10, TEAL, DEEP),
]

if __name__ == "__main__":
    for name, w, h, kind, seed, c1, c2 in JOBS:
        if not (OUT / f"{name}.jpg").exists():
            scene(name, w, h, kind, seed, c1, c2)
            print("placeholder:", name)
