# ABC Midwest: sitio bilingüe (EN/ES)

Sitio estático generado con Python. La salida está en `public/` (ya generada y versionada).

## Regenerar
```bash
python3 tools/build.py      # genera public/
python3 tools/validate.py   # SEO, enlaces, imágenes, JSON-LD, sitemap
```
Requiere Python 3 y Pillow (`pip install pillow`).

## Dónde editar
- `tools/site.config.json`: nombre, dominio, teléfono, WhatsApp, correo, zonas, colores, `form_endpoint`.
- `tools/content.py`: servicios y textos en EN y ES, páginas legales.
- `tools/images_src/`: fotos (reemplace conservando el nombre: `hero-1.jpg`, `service-office.jpg`, …).
- `tools/assets_src/css|js`: estilos y scripts.

## Railway
`npm start` sirve `public/` con `serve` (incluye 404.html). `npm run build` no hace nada a propósito: Railway no necesita Python, porque `public/` va versionado. Regenere en local con `npm run site:build` y haga commit de `public/`. Configure el dominio en Railway y apunte el DNS.

## Formulario
Cree un endpoint (p. ej. Formspree) y péguelo en `form_endpoint`. Mientras tenga `REPLACE_ME`, el formulario abre el correo del usuario.
