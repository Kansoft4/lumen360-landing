Actualizá la landing de Lumen 360 con los cambios que están en GitHub.

## Origen

    https://github.com/Kansoft4/lumen360-landing
    rama main · commit 8a83a60

Si el repo de `/srv/landing/lumen360/` ya tiene ese remoto, un `git pull origin main`
alcanza. Si no lo tiene, agregalo o traé los cambios como bundle. **Antes de pisar nada,
verificá que no haya trabajo local sin commitear en el servidor** y avisame si lo hay.

Este repo ya incluye tus tres commits de GEO (schema completo, centro de recursos,
archivos de citación). Están fusionados, no los vas a perder. Si ves conflicto en
`Vistare Landing v5.dc.html`, pará y contame antes de resolver.

## Qué cambió

**Videos recomprimidos.** Venían en 1920x1080 a 7300 kbps para mostrarse en cajas de
150 px de alto. Ahora están a 960 px. Mismos nombres de archivo, mucho menos peso:

    reel_loop_3.mp4          5.4 MB -> 709 KB
    tour-vista-muneca.mp4    2.9 MB -> 250 KB
    tour-quita-muebles.mp4   2.7 MB -> 124 KB
    tour-medicion.mp4        2.7 MB -> 118 KB

**Tres archivos NUEVOS** que antes no existían:

    assets/tour-vista-muneca-poster.jpg
    assets/tour-quita-muebles-poster.jpg
    assets/tour-medicion-poster.jpg

**Si subís solo el HTML y te olvidás de estos tres, las tarjetas de "qué hace" vuelven
a verse como recuadros grises vacíos en iPhone.** Es el bug que esto justamente arregla.

**Arreglo de autoplay en iOS.** El runtime de la plantilla setea `muted` como propiedad
de React pero nunca escribe el atributo en el HTML. iOS mira el atributo al parsear, así
que bloqueaba el autoplay y sin poster quedaba el recuadro gris. Hay un script al final
del `<body>` que ahora escribe el atributo a mano.

**Ajustes de móvil.** Velo del hero vertical, pila de testimonios oculta bajo 760 px,
reels a dos columnas y caption recortado a dos líneas, video del hero sin descargarse
en teléfono.

**VideoObject completado.** Los cuatro nodos ahora traen `duration`, `thumbnailUrl`,
`inLanguage` y una `description` larga. El JSON-LD está validado.

## El despliegue

El archivo fuente es **`Vistare Landing v5.dc.html`** (con espacios en el nombre) y en
producción se sirve como **`index.html`**. Si tu proceso lo copia y renombra, respetalo.

Lo que va a la raíz del sitio:

    index.html            (renombrado desde Vistare Landing v5.dc.html)
    support.js
    assets/               9 archivos
    robots.txt  llms.txt  sitemap.xml
    ai/summary.json  ai/faq.json
    las 7 carpetas de recursos, sin cambios

`assets/_orig/` está en .gitignore y no se publica: son los videos originales, guardados
por si hay que regenerar algo.

## Verificá después de subir

    curl -sI https://lumen.inovarem.com/assets/tour-medicion-poster.jpg   # 200
    curl -s https://lumen.inovarem.com/ | grep -c 'data-loop'             # 5
    curl -s https://lumen.inovarem.com/ | grep -c 'lumen360.inovarem'     # 0

Y que el canonical siga en `https://lumen.inovarem.com/`. Si aparece `lumen360.inovarem.com`
en algún lado, algo se revirtió: ese subdominio hace 301 y romperlo fue el bug original.

Cuando termines, corré `geo audit --url https://lumen.inovarem.com --format text` y
pasame el score. El baseline de hoy es 72/100.

## Contame al terminar

1. Cómo se despliega exactamente (¿nginx sirve el checkout directo, o hay copia o build?)
2. Si `_recursos/build.py` genera las 7 páginas de recursos, o si ya son HTML estático
3. Si quedó algo sin commitear en el servidor antes de mi pull
