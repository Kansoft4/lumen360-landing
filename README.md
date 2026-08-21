# Lumen 360 · Landing

Landing de conversión para [Lumen 360](https://www.instagram.com/lumen360.co/), tours virtuales 360° con Matterport para inmobiliarias y asesores en Cali, Colombia.

Todos los CTA van a WhatsApp con un mensaje precargado distinto según la sección, para saber de qué parte de la página vino cada lead.

## Qué subir al servidor

Solo estos archivos van a la raíz del sitio:

```
index.html   (Vistare Landing v5.dc.html renombrado)
support.js
assets/
  hero-loft-hd.jpg
  og-image.jpg
  reel_loop_3.mp4
  tour-vista-muneca.mp4
  tour-quita-muebles.mp4
  tour-medicion.mp4
```

Son 14 MB. El resto del repo es material de trabajo.

## Estructura de la página

```
hero → tour 360 en vivo → por qué te sirve → qué hace
     → oferta → precio → reels de Instagram → FAQ
```

## Cómo está armado

Sin build ni dependencias. Es HTML con estilos en línea sobre un runtime de plantillas (`support.js`) que resuelve `{{ }}` y `<sc-for>`.

**Tour 360.** Un iframe a Matterport. Los parámetros de la URL importan:

| | |
|---|---|
| `wh=0` | La rueda del mouse scrollea la página en vez de quedar atrapada haciendo zoom |
| `nozoom=1` | Fija el encuadre. El visitante no lo puede cerrar |
| `qs=1` | Entra directo a Inside View, sin la animación desde Dollhouse |
| sin `play=1` | Muestra el póster y no arranca WebGL hasta que hacen clic |

**Reels de Instagram.** Se traen del feed JSON de [Behold](https://behold.so) en cada visita. Meta cerró la Basic Display API en diciembre de 2024, y la Graph API que la reemplaza pide un access token que en una página estática quedaría visible en el código fuente. Behold guarda el token de su lado y expone solo un JSON público de lectura.

Los videos se descargan y reproducen únicamente mientras están en pantalla (`IntersectionObserver`), en silencio. Si el feed falla o viene vacío, la sección se oculta sola junto con su enlace del footer.

**Copia responsive.** Cada texto largo tiene su versión corta. Bajo 760px el CSS intercambia una por otra: 44% menos caracteres en móvil, sin un segundo archivo que mantener.

## Antes de publicar en un dominio

**Las URL absolutas están escritas en el `<head>`.** Open Graph y el schema apuntan a `https://lumen360.inovarem.com/`. Tienen que ser absolutas para que WhatsApp encuentre la imagen de vista previa. Si el sitio va a otra dirección, hay que reemplazarla (aparece 7 veces, todas juntas).

**Behold: whitelist de dominio.** En el feed, agregar el dominio en *Domain whitelist*. Si queda vacío, cualquiera que lea el código fuente puede consumir el feed desde su propio sitio.

**Matterport SDK.** El tour por iframe funciona sin key. Solo hace falta si más adelante se controla la cámara por código, y en ese caso hay que agregar el dominio a la allow list de la key (sin comodines: `dominio.com` y `www.dominio.com` por separado).

## Carpetas

| | |
|---|---|
| `assets/` | Lo que usa la página |
| `uploads/` | Material de referencia y capturas del proceso de diseño |
| `archivo/` | Versiones anteriores (v1 a v5) y media descartada |
