# Notas de desarrollo

Esto vivía como comentarios dentro de `Vistare Landing v5.dc.html`. Se movió acá porque
los crawlers de IA leen los comentarios del HTML, y el auditor GEO marcaba estas notas
como inyección de prompt: están escritas en imperativo ("pegá acá el ID") y a un modelo
le parecen instrucciones dirigidas a él.

Este archivo no se publica: `_recursos/` y los `.md` de raíz no están en `site_files()`
de deploy-landing.

---

## 1

```
Open Graph: sin esto, el link compartido por WhatsApp sale en blanco.
     Si mueves la landing a otro dominio, actualiza las URL absolutas de abajo.
```

---

## 2

```
── TOUR 360 REAL (demo en vivo) ──
         Parámetros de la URL:
           qs=1    entra directo a Inside View (se salta el fly-in desde Dollhouse)
           wh=0    la rueda del mouse scrollea la página en vez de quedar atrapada
                   haciendo zoom en el tour. Clave en una landing larga.
           brand=0 oculta "Presented By" y los datos de contacto del panel About.
           nozoom=1 fija el encuadre en 1.00x y el visitante no lo puede cerrar.
                   NOTA: 1.00x no es la apertura maxima. El rango real del zoom de
                   Matterport llega hasta 0.70x (probado: zoomTo(0.5) devuelve 0.7),
                   pero bajar de 1.00x solo se puede por SDK, y el SDK en dominio
                   propio exige plan pago + Developer Tools License.
         Sin play=1 a propósito: así Matterport muestra el póster y no arranca el
         motor WebGL hasta que el visitante hace clic.
```

---

## 3

```
══ REELS DE INSTAGRAM (dinamico) ══
     Trae los reels mas recientes de @lumen360.co y los pinta en la grilla de
     la seccion "Tours", con el diseño de la pagina.

     COMO ACTIVARLO (5 min, gratis):
       1. Entra a https://behold.so y crea una cuenta.
       2. "Connect an Instagram account" -> autoriza @lumen360.co por OAuth.
          Ojo: Instagram exige cuenta Business o Creator. Si la tuya es
          Personal, cambiala en Instagram > Configuracion > Tipo de cuenta.
       3. "+ Add Feed" -> tipo JSON -> en "Allowed post types" deja solo Reels.
       4. Copia el ID del feed y pegalo abajo en FEED_ID.

     Por que Behold y no la API de Instagram directo: Meta cerro la Basic
     Display API en diciembre de 2024. La Graph API que la reemplaza necesita
     un access token, y en una pagina estatica ese token quedaria visible en
     el codigo fuente para cualquiera. Behold guarda el token de su lado y
     expone solo un JSON publico de lectura, sin credenciales.

     Si FEED_ID esta vacio o la peticion falla, la seccion entera se oculta
     sola (y su link en el footer), para no dejar un hueco en la pagina.
```

---

## 4

```
══ VIDEOS: autoplay mudo que funcione en iOS ══
     Dos bugs que arregla esto:

     1. El runtime de la plantilla setea muted como PROPIEDAD de React, pero
        nunca escribe el ATRIBUTO muted en el HTML. iOS mira el atributo al
        parsear y por eso bloqueaba el autoplay: quedaba el recuadro gris.
        Aca se lo ponemos a mano, como atributo de verdad.

     2. Los videos cargaban aunque estuvieran fuera de pantalla. Ahora el src
        se asigna recien cuando entran al viewport, y se pausan al salir.

     En movil el video vertical del hero se elimina del todo (no solo se
     oculta): se le quita el src para que no gaste datos.
```
