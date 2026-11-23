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
    rnd = random.Random(seed)
    img = gradient(w, h, c1, c2)
    d = ImageDraw.Draw(img, "RGBA")
    if kind == "windows":
        cols, rows = 8, 5
        gw, gh = w / cols, h / rows
        for r in range(rows):
            for c in range(cols):
                a = rnd.randint(30, 120)
                d.rectangle([c * gw + 10, r * gh + 10, (c + 1) * gw - 10, (r + 1) * gh - 10], fill=(220, 240, 245, a))
    elif kind == "floor":
        horizon = int(h * 0.45)
        d.rectangle([0, horizon, w, h], fill=(230, 235, 235, 40))
        for i in range(-12, 13):
            d.line([(w / 2 + i * 40, horizon), (w / 2 + i * 190, h)], fill=(255, 255, 255, 60), width=3)
        for j in range(1, 8):
            y = horizon + (h - horizon) * (j / 8) ** 1.7
            d.line([(0, y), (w, y)], fill=(255, 255, 255, 50), width=3)
        d.ellipse([w * 0.2, h * 0.7, w * 0.8, h * 0.95], fill=(255, 255, 255, 35))
    elif kind == "office":
        for i in range(5):
            x = w * (0.08 + i * 0.18)
            d.rectangle([x, h * 0.55, x + w * 0.14, h * 0.58], fill=(240, 244, 245, 150))
            d.rectangle([x + w * 0.02, h * 0.58, x + w * 0.025, h * 0.85], fill=(240, 244, 245, 110))
            d.rectangle([x + w * 0.115, h * 0.58, x + w * 0.12, h * 0.85], fill=(240, 244, 245, 110))
            d.rectangle([x + w * 0.04, h * 0.42, x + w * 0.10, h * 0.54], fill=(200, 225, 230, 130))
        d.rectangle([0, h * 0.2, w, h * 0.24], fill=(255, 255, 255, 40))
    elif kind == "post":
        for i in range(9):
            x = rnd.randint(0, w); wd = rnd.randint(30, 90)
            d.polygon([(x, h), (x + wd, h), (x + wd + 160, 0), (x + 160, 0)], fill=(255, 255, 255, rnd.randint(18, 55)))
        d.rectangle([0, h * 0.82, w, h], fill=(0, 0, 0, 55))
    elif kind == "lobby":
        for i in range(6):
            x = w * (0.08 + i * 0.16)
            d.rectangle([x, 0, x + w * 0.05, h * 0.8], fill=(255, 255, 255, 45))
        d.rectangle([w * 0.3, h * 0.6, w * 0.7, h * 0.72], fill=(255, 255, 255, 120))
        d.rectangle([0, h * 0.8, w, h], fill=(255, 255, 255, 30))
    elif kind == "skyline":
        x = 0
        while x < w:
            bw = rnd.randint(int(w * 0.05), int(w * 0.13)); bh = rnd.randint(int(h * 0.25), int(h * 0.75))
            d.rectangle([x, h - bh, x + bw, h], fill=(255, 255, 255, rnd.randint(18, 40)))
            for wy in range(int(h - bh + 20), h - 20, 36):
                for wx in range(int(x + 12), int(x + bw - 14), 26):
                    if rnd.random() > 0.35:
                        d.rectangle([wx, wy, wx + 12, wy + 18], fill=(255, 220, 170, 90))
            x += bw + rnd.randint(6, 20)
    elif kind == "portrait":
        d.ellipse([w * 0.1, h * 0.1, w * 0.9, h * 0.7], fill=(255, 255, 255, 30))
        d.rectangle([w * 0.15, h * 0.55, w * 0.85, h * 0.9], fill=(255, 255, 255, 40))
        d.rectangle([w * 0.28, h * 0.25, w * 0.72, h * 0.55], fill=(255, 255, 255, 55))
    d.rectangle([0, h - 8, w, h], fill=ORANGE + (255,))
    img = img.filter(ImageFilter.GaussianBlur(1.2))
    img.save(OUT / f"{name}.jpg", quality=90)


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
