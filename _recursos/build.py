#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las páginas de recursos y actualiza el sitemap.

    python3 _recursos/build.py

Escribe <slug>/index.html en la raíz del repo. El directorio _recursos NO se
publica: no está en site_files() de deploy-landing, así que el generador vive
versionado pero nunca llega al servidor web.
"""
import importlib, json, pathlib, sys, datetime

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
        html = chrome.pagina(
            slug=m.SLUG, titulo=m.TITULO, h1=m.H1, descripcion=m.DESC,
            cuerpo=m.CUERPO, schema_extra=extra or None,
            otras=getattr(m, "OTRAS", ()))
        d = RAIZ / m.SLUG
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(html, encoding="utf-8")
        # el JSON-LD tiene que ser válido o la página no sirve para nada
        import re
        ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        json.loads(ld.group(1))
        pal = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ",
                                                 html, flags=re.S | re.I)).split())
        hechas.append((m.SLUG, pal))
        print(f"  ✓ /{m.SLUG}/  {pal} palabras")

    # sitemap con la home + todas las páginas generadas
    hoy = datetime.date.today().isoformat()
    urls = [("", "1.0", "weekly")] + [(s, "0.8", "monthly") for s, _ in hechas]
    cuerpo = "\n".join(
        f"  <url>\n    <loc>{chrome.BASE}/{s + '/' if s else ''}</loc>\n"
        f"    <lastmod>{hoy}</lastmod>\n    <changefreq>{cf}</changefreq>\n"
        f"    <priority>{p}</priority>\n  </url>" for s, p, cf in urls)
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{cuerpo}\n</urlset>\n", encoding="utf-8")
    print(f"\n  ✓ sitemap.xml con {len(urls)} URLs")
    print(f"  → recordá que cada slug nuevo va también en site_files() de deploy-landing")
    return [s for s, _ in hechas]


if __name__ == "__main__":
    main()
