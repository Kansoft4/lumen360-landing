# -*- coding: utf-8 -*-
"""Molde compartido de las páginas de recursos de Lumen 360.

La paleta y las tipografías salen de la landing viva (Hanken Grotesk +
Playfair Display sobre #EFF4F4), no del brief: una página de recursos que
parezca de otra marca es peor que no tenerla.

Reglas de escritura que este molde da por sentadas y que el contenido debe
respetar, porque son las que hacen que un modelo pueda citar la página:
  · la primera oración se sostiene sola y responde la pregunta del título;
  · el dato duro va arriba, con fuente y año, no en la conclusión;
  · las secciones rondan las 100-150 palabras, que es el trozo que un RAG
    extrae limpio;
  · toda cifra publicada se rastrea hasta una URL que abre.
"""

BASE = "https://lumen.inovarem.com"
WA = "https://wa.me/573011493222?text=Hola%2C%20quiero%20informaci%C3%B3n%20sobre%20Lumen%20360."
TEL = "+57 301 149 3222"

TINTA = "#172A3A"; CUERPO = "#3F5A66"; TENUE = "#7C919C"
FONDO = "#EFF4F4"; PAPEL = "#FFFFFF"; BORDE = "#DCE6E7"
SUAVE = "#E4EDEE"; VERDE = "#16785A"; VERDE_OSC = "#004346"

SERIF = "'Playfair Display',serif"
SANS = "'Hanken Grotesk',-apple-system,Segoe UI,sans-serif"


def _css():
    return f"""
*{{box-sizing:border-box}}
body{{margin:0;background:{FONDO};color:{CUERPO};font-family:{SANS};
  font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}}
a{{color:{VERDE};text-decoration:none}}
a:hover{{text-decoration:underline}}
.env{{width:100%;max-width:760px;margin:0 auto;padding:0 clamp(20px,4vw,40px)}}
.ancho{{max-width:1100px}}
h1{{font-size:clamp(30px,5vw,50px);line-height:1.1;letter-spacing:-.035em;
  font-weight:800;color:{TINTA};margin:0 0 20px}}
h2{{font-size:clamp(23px,3vw,31px);line-height:1.2;letter-spacing:-.025em;
  font-weight:700;color:{TINTA};margin:52px 0 14px}}
h3{{font-size:19px;font-weight:700;color:{TINTA};margin:32px 0 8px}}
p{{margin:0 0 17px}}
em.s{{font-family:{SERIF};font-style:italic;font-weight:500}}
.entrada{{font-size:20px;line-height:1.6;color:{TINTA}}}
.pildora{{display:inline-flex;align-items:center;padding:8px 15px;border-radius:999px;
  background:{SUAVE};border:1px solid #CBDCDE;font-size:13px;font-weight:600;color:{CUERPO}}}
.dato{{background:{PAPEL};border:1px solid {BORDE};border-radius:16px;
  padding:26px 28px;margin:26px 0}}
.dato .cifra{{font-size:clamp(30px,4.5vw,42px);font-weight:800;color:{TINTA};
  letter-spacing:-.03em;line-height:1.05;display:block}}
.dato .glosa{{font-size:15px;color:{TENUE};margin-top:9px;display:block}}
.aviso{{border-left:3px solid {VERDE};background:{PAPEL};border-radius:0 12px 12px 0;
  padding:18px 22px;margin:26px 0;font-size:16px}}
.tabla-env{{overflow-x:auto;margin:26px 0;-webkit-overflow-scrolling:touch}}
table{{border-collapse:collapse;width:100%;min-width:520px;font-size:15px;background:{PAPEL}}}
th,td{{text-align:left;padding:12px 14px;border-bottom:1px solid {BORDE};vertical-align:top}}
th{{font-weight:700;color:{TINTA};background:{SUAVE}}}
ul,ol{{margin:0 0 17px;padding-left:22px}}
li{{margin-bottom:7px}}
.fuentes{{font-size:14.5px;color:{TENUE};line-height:1.6}}
.fuentes li{{margin-bottom:12px}}
.cta{{display:inline-flex;align-items:center;gap:10px;background:{VERDE};color:#fff;
  padding:15px 26px;border-radius:999px;font-weight:700;font-size:16px;margin-top:8px}}
.cta:hover{{background:{VERDE_OSC};text-decoration:none}}
nav.migas{{font-size:14px;color:{TENUE};margin-bottom:22px}}
nav.migas a{{color:{TENUE}}}
header.barra{{border-bottom:1px solid {BORDE};background:rgba(239,244,244,.9);
  backdrop-filter:blur(8px);position:sticky;top:0;z-index:10}}
header.barra .env{{display:flex;align-items:center;justify-content:space-between;
  padding-top:15px;padding-bottom:15px}}
.marca{{font-weight:800;color:{TINTA};font-size:18px;letter-spacing:-.02em}}
footer.pie{{border-top:1px solid {BORDE};margin-top:72px;padding:38px 0 56px;font-size:15px}}
footer.pie .env{{display:flex;flex-wrap:wrap;gap:12px 26px;align-items:center}}
.otras{{background:{PAPEL};border:1px solid {BORDE};border-radius:16px;padding:24px 26px;margin:44px 0 0}}
.otras a{{display:block;padding:7px 0;font-weight:600}}
@media(max-width:600px){{body{{font-size:16.5px}}}}
"""


def pagina(slug, titulo, h1, descripcion, cuerpo, schema_extra=None,
           actualizado="2026-08-22", otras=()):
    """Devuelve el HTML completo de una página de recursos."""
    import json
    url = f"{BASE}/{slug}/"
    grafo = [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lumen 360", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": h1, "item": url}]},
        {"@type": "Article", "@id": f"{url}#articulo", "headline": h1,
         "description": descripcion, "url": url, "inLanguage": "es-CO",
         "datePublished": actualizado, "dateModified": actualizado,
         "author": {"@id": f"{BASE}/#organizacion"},
         "publisher": {"@id": f"{BASE}/#organizacion"},
         "isPartOf": {"@id": f"{BASE}/#sitio"},
         "mainEntityOfPage": url},
    ]
    if schema_extra:
        grafo.extend(schema_extra)
    ld = json.dumps({"@context": "https://schema.org", "@graph": grafo},
                    ensure_ascii=False, indent=2)

    enlaces = "".join(
        f'<a href="{BASE}/{s}/">{t} &rarr;</a>' for s, t in otras)
    bloque_otras = (f'<div class="otras"><strong style="color:{TINTA}">'
                    f'Seguir leyendo</strong>{enlaces}</div>') if otras else ""

    return f"""<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta name="last-modified" content="{actualizado}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Lumen 360">
<meta property="og:locale" content="es_CO">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@1,400;1,500&display=swap" rel="stylesheet">
<style>{_css()}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<header class="barra"><div class="env ancho">
  <a href="{BASE}/" class="marca">Lumen 360</a>
  <a href="{WA}" target="_blank" rel="noopener" style="font-weight:600;font-size:15px">WhatsApp {TEL}</a>
</div></header>

<main class="env" style="padding-top:44px">
  <nav class="migas"><a href="{BASE}/">Lumen 360</a> &rsaquo; {h1}</nav>
  <h1>{h1}</h1>
{cuerpo}
{bloque_otras}
</main>

<footer class="pie"><div class="env ancho">
  <span style="font-weight:800;color:{TINTA}">Lumen 360</span>
  <span style="color:{TENUE}">Tours virtuales 360&deg; en Cali</span>
  <a href="{WA}" target="_blank" rel="noopener">WhatsApp {TEL}</a>
  <a href="https://www.instagram.com/lumen360.co" target="_blank" rel="noopener">Instagram</a>
  <a href="{BASE}/">Inicio</a>
  <span style="color:{TENUE};width:100%;font-size:13.5px">Actualizado el {actualizado}. &copy; 2026 Lumen 360 &middot; Cali, Colombia.</span>
</div></footer>
</body>
</html>
"""
