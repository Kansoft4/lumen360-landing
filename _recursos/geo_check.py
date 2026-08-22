#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""¿Las IAs citan a Lumen 360? Marcador propio, vía la API de Perplexity.

    python3 _recursos/geo_check.py            # todas las preguntas
    python3 _recursos/geo_check.py --rapido   # solo las 3 decisivas

La clave se lee de /root/.config/lumen/perplexity.key (nunca del código ni de
un argumento, que quedaría en el historial del shell).

Qué mide y qué no. Mide lo único que no admite interpretación: si la respuesta
menciona la marca y si el dominio aparece entre las fuentes citadas. NO produce
el score 0-100 de la herramienta `geo` con la que se sacó el 32/100 de línea
base — para esa cifra hace falta esa herramienta. Acá el marcador es binario y
por eso es honesto: te cita o no te cita.
"""
import argparse, json, pathlib, sys, time, urllib.request, urllib.error

CLAVE = pathlib.Path("/root/.config/lumen/perplexity.key")
HIST = pathlib.Path(__file__).resolve().parent / "geo-history.json"
MARCA = "lumen 360"
DOMINIO = "lumen.inovarem.com"
API = "https://api.perplexity.ai/chat/completions"

# Las tres primeras son la prueba de fuego: preguntas de PROBLEMA DE NEGOCIO,
# no de producto. Ahí es donde hoy Lumen es invisible y donde está el mercado
# grande. Las demás son de categoría, más fáciles y menos valiosas.
PREGUNTAS = [
    ("negocio", "¿Cómo mejorar las ventas de mi inmobiliaria en Colombia?"),
    ("negocio", "¿Cómo vender un apartamento más rápido en Cali?"),
    ("negocio", "¿Cómo reducir las visitas a inmuebles que no terminan en compra?"),
    ("categoria", "¿Cuánto cuesta un tour virtual 360 inmobiliario en Colombia?"),
    ("categoria", "¿Vale la pena hacer un tour virtual 360 para vender un inmueble?"),
    ("categoria", "Mejores servicios de tours virtuales 360 para inmobiliarias en Colombia"),
    ("marca", "¿Qué es Lumen 360 y qué servicios ofrece?"),
]

COMPETIDORES = ["realstudio360.com", "finca360.com.co", "mentescreativas.com.co",
                "altamiradigital.com.co", "perspektiva360.com", "realvision360.com",
                "webpanorama360.com"]


def preguntar(clave, pregunta, modelo="sonar"):
    cuerpo = json.dumps({
        "model": modelo,
        "messages": [{"role": "user", "content": pregunta}],
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(API, data=cuerpo, headers={
        "Authorization": f"Bearer {clave}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rapido", action="store_true", help="solo las 3 preguntas de negocio")
    ap.add_argument("--modelo", default="sonar")
    a = ap.parse_args()

    if not CLAVE.exists() or not CLAVE.read_text().strip():
        print(f"Falta la clave de Perplexity en {CLAVE}\n")
        print("  mkdir -p /root/.config/lumen && chmod 700 /root/.config/lumen")
        print(f"  printf '%s' 'TU_CLAVE' > {CLAVE}")
        print(f"  chmod 600 {CLAVE}")
        return 2
    clave = CLAVE.read_text().strip()

    preguntas = [p for p in PREGUNTAS if not a.rapido or p[0] == "negocio"]
    corrida = {"fecha": time.strftime("%Y-%m-%d %H:%M"), "modelo": a.modelo, "resultados": []}
    citas_rivales = {}

    print(f"Marcador de citación · {corrida['fecha']} · modelo {a.modelo}\n")
    for tipo, q in preguntas:
        try:
            r = preguntar(clave, q, a.modelo)
        except urllib.error.HTTPError as e:
            detalle = e.read().decode()[:180]
            print(f"  ✗ error {e.code}: {detalle}")
            if e.code == 400:
                print(f"    (puede ser el nombre del modelo; probá --modelo sonar-pro)")
            return 1
        except Exception as e:
            print(f"  ✗ {type(e).__name__}: {e}")
            return 1

        texto = r["choices"][0]["message"]["content"]
        fuentes = r.get("citations") or r.get("search_results") or []
        fuentes = [f if isinstance(f, str) else f.get("url", "") for f in fuentes]
        blob = (texto + " " + " ".join(fuentes)).lower()

        mencion = MARCA in blob
        citado = DOMINIO in blob
        for c in COMPETIDORES:
            if c in blob:
                citas_rivales[c] = citas_rivales.get(c, 0) + 1

        marca_ok = "✓" if mencion else "·"
        dom_ok = "✓" if citado else "·"
        print(f"  [{tipo:9}] marca {marca_ok}  dominio {dom_ok}   {q[:58]}")
        corrida["resultados"].append({
            "tipo": tipo, "pregunta": q, "marca": mencion, "dominio": citado,
            "fuentes": fuentes[:8]})
        time.sleep(1.5)

    n = len(corrida["resultados"])
    nm = sum(1 for x in corrida["resultados"] if x["marca"])
    nd = sum(1 for x in corrida["resultados"] if x["dominio"])
    neg = [x for x in corrida["resultados"] if x["tipo"] == "negocio"]
    negm = sum(1 for x in neg if x["marca"] or x["dominio"])
    corrida["resumen"] = {"preguntas": n, "menciones": nm, "dominio_citado": nd,
                          "negocio_ganadas": negm, "negocio_total": len(neg)}

    print(f"\n  Marca mencionada : {nm}/{n}")
    print(f"  Dominio citado   : {nd}/{n}")
    print(f"  Preguntas de negocio ganadas: {negm}/{len(neg)}   ← la prueba de fuego")
    if citas_rivales:
        print("\n  Citados en su lugar:")
        for c, k in sorted(citas_rivales.items(), key=lambda x: -x[1]):
            print(f"     {k}× {c}")

    hist = json.loads(HIST.read_text()) if HIST.exists() else []
    if hist:
        p = hist[-1]["resumen"]
        print(f"\n  Corrida anterior ({hist[-1]['fecha']}): "
              f"marca {p['menciones']}/{p['preguntas']}, dominio {p['dominio_citado']}/{p['preguntas']}")
        d = nd - p["dominio_citado"]
        print(f"  Variación en dominio citado: {d:+d}")
    hist.append(corrida)
    HIST.write_text(json.dumps(hist, ensure_ascii=False, indent=2))
    print(f"\n  histórico → {HIST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
