#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las páginas de recursos y actualiza el sitemap.

    python3 _recursos/build.py

Escribe <slug>/index.html en la raíz del repo. El directorio _recursos NO se
publica: no está en site_files() de deploy-landing, así que el generador vive
versionado pero nunca llega al servidor web.
"""
import importlib, json, pathlib, re, sys

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
sys.path.insert(0, str(AQUI))
import chrome

PAGINAS = ["p_evidencia", "p_precios", "p_menos_visitas", "p_vender_mas_rapido",
           "p_propietario_exterior", "p_que_es_tour_360", "p_lumen_360"]


def faq_schema(preguntas):
    if not preguntas:
        return None
    return {"@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in preguntas]}


def main():
    hechas = []
    for nombre in PAGINAS:
        try:
            m = importlib.import_module(nombre)
        except ModuleNotFoundError:
            print(f"  · {nombre}: todavía no existe, salto")
            continue
        extra = []
        f = faq_schema(getattr(m, "PREGUNTAS", None))
        if f:
            extra.append(f)
        extra.extend(getattr(m, "SCHEMA_EXTRA", []))
        fecha = getattr(m, "ACTUALIZADO", chrome.ACTUALIZADO)
        html = chrome.pagina(
            slug=m.SLUG, titulo=m.TITULO, h1=m.H1, descripcion=m.DESC,
            cuerpo=m.CUERPO, schema_extra=extra or None,
            actualizado=fecha, otras=getattr(m, "OTRAS", ()))
        d = RAIZ / m.SLUG
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(html, encoding="utf-8")
        # el JSON-LD tiene que ser válido o la página no sirve para nada
        import re
        ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        json.loads(ld.group(1))
        pal = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ",
                                                 html, flags=re.S | re.I)).split())
        hechas.append((m.SLUG, pal, fecha))
        print(f"  ✓ /{m.SLUG}/  {pal} palabras  ({fecha})")

    # Sitemap. La fecha de cada URL sale de la propia página, no de hoy: si usara
    # date.today() el <lastmod> se separaría del <meta last-modified> y del
    # dateModified del schema cada vez que se regenera sin tocar contenido.
    fecha_home = chrome.ACTUALIZADO
    portada = RAIZ / "Vistare Landing v5.dc.html"
    if portada.exists():
        mm = re.search(r'name="last-modified" content="([0-9-]+)"',
                       portada.read_text(encoding="utf-8"))
        if mm:
            fecha_home = mm.group(1)
    urls = [("", "1.0", "weekly", fecha_home)] + [(s, "0.8", "monthly", f) for s, _, f in hechas]
    cuerpo = "\n".join(
        f"  <url>\n    <loc>{chrome.BASE}/{s + '/' if s else ''}</loc>\n"
        f"    <lastmod>{fch}</lastmod>\n    <changefreq>{cf}</changefreq>\n"
        f"    <priority>{p}</priority>\n  </url>" for s, p, cf, fch in urls)
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{cuerpo}\n</urlset>\n", encoding="utf-8")
    print(f"\n  ✓ sitemap.xml con {len(urls)} URLs")
    print(f"  → recordá que cada slug nuevo va también en site_files() de deploy-landing")
    return [s for s, _, _ in hechas]


if __name__ == "__main__":
    main()
