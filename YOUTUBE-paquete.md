# Paquete para YouTube

## Por qué esto

En la consulta *"cómo vendo apartamentos más rápido siendo agente inmobiliario en Cali"*,
Perplexity citó **16 fuentes. Ocho eran videos de YouTube.**

Lumen produce video todas las semanas y no tiene un solo video en YouTube. Ese es el hueco.

Instagram no sirve para esto: las IAs no indexan reels de Instagram como fuente citable.
YouTube sí, porque tiene transcripción automática y página pública indexable por video.

**Regla para todos:** en la descripción, el enlace a lumen.inovarem.com va en las primeras
dos líneas, antes del "ver más". Ahí es donde el crawler lo lee sin desplegar nada.

---

## Los 6 reels que ya existen

Se suben tal cual, sin reeditar. Son verticales: van como **Shorts**.

### 1 · "Tu mejor comprador puede estar a tres horas de vuelo"
- **Título:** Cómo vender un apartamento en Cali a un comprador que vive en otra ciudad
- **Descripción (primeras líneas):**
  > Si tu comprador está en Bogotá, Miami o Madrid, no va a comprar un tiquete para
  > averiguar si el apartamento le gusta. Con un tour virtual lo recorre completo desde
  > donde esté: https://lumen.inovarem.com/propietario-en-el-exterior/
- **Etiquetas:** vender apartamento Cali, comprador en el exterior, tour virtual 360, inmobiliaria Cali, Matterport Colombia
- **Fijar comentario:** enlace a un tour de ejemplo

### 2 · "Su propiedad estaba trabajando. Usted estaba dormido."
- **Título:** Tu apartamento se puede mostrar solo a las 2 de la mañana
- **Descripción:**
  > Un tour virtual no tiene horario de atención. El comprador entra cuando quiere,
  > recorre lo que quiere y vuelve las veces que necesite:
  > https://lumen.inovarem.com/vender-mas-rapido/
- **Etiquetas:** tour virtual inmobiliaria, vender más rápido, propiedad 24 horas, asesor inmobiliario Cali

### 3 · "Un propietario no se va con otro agente porque no vendiste"
- **Título:** Por qué pierdes exclusivas aunque estés haciendo bien el trabajo
- **Descripción:**
  > El propietario casi nunca se va por el resultado. Se va porque no supo qué estabas
  > haciendo entre un mes y el siguiente: https://lumen.inovarem.com/menos-visitas/
- **Etiquetas:** exclusiva inmobiliaria, captación propiedades, reporte al propietario, asesor inmobiliario

### 4 · "Mil publicaciones iguales. La tuya entre ellas."
- **Título:** Tu publicación se ve igual a las otras mil del portal
- **Descripción:**
  > Veinte fotos y una ficha técnica es lo mismo que publica todo el mundo. Un recorrido
  > que se puede caminar no: https://lumen.inovarem.com/que-es-un-tour-360/
- **Etiquetas:** marketing inmobiliario, publicar propiedad, diferenciar anuncio, tour 360

### 5 · "Dentro de un año esto va a ser lo normal"
- **Título:** El tour virtual va a ser obligatorio. Hoy todavía es ventaja.
- **Descripción:**
  > Toda ventaja dura hasta que la competencia la copia:
  > https://lumen.inovarem.com/vender-mas-rapido/
- **Etiquetas:** tendencias inmobiliarias, tecnología inmobiliaria, ventaja competitiva

### 6 · "Hay un argumento de venta que tenés gratis"
- **Título:** El argumento de venta de Cali que casi ningún asesor usa
- **Descripción:**
  > Antes de publicar esto, confirmar la cifra de valorización con fuente citable
  > (Camacol, DANE o Galería Inmobiliaria) y ponerla en la descripción con el enlace.
- **Etiquetas:** invertir en Cali, valorización, mercado inmobiliario Valle del Cauca
- ⚠️ **No subir sin verificar el dato.** Es el único de los seis que afirma una cifra de mercado.

---

## Los 3 demos de producto

Duran entre 4 y 9 segundos: muy cortos para YouTube por separado.

**Recomendación:** un solo video de 60 a 90 segundos que encadene los tres, con voz en off
o texto en pantalla explicando qué hace cada uno. Los archivos están en `assets/`.

- **Título:** Qué puede hacer tu comprador dentro de un tour virtual 360 (vista de muñeca, medición y quita muebles)
- **Descripción:** las tres descripciones que ya están en el `VideoObject` del sitio sirven
  tal cual. Están en el JSON-LD de index.html.

Este es el que más importa: es el único de formato largo, el que gana transcripción
automática completa y el que responde una pregunta que la gente sí escribe.

---

## Orden sugerido

1. El video largo de los 3 demos (el de mayor retorno)
2. Reels 1, 2 y 3 (mapean a las consultas objetivo)
3. Reels 4 y 5
4. Reel 6, solo después de verificar el dato

## Cómo medir si funcionó

```
geo citations --brand "Lumen 360" --domain lumen.inovarem.com \
  --query "cómo vendo apartamentos más rápido siendo agente inmobiliario en Cali"
```

Hoy da 0% en marca y 0% en dominio. Ese es el baseline.
Vale la pena volver a correrlo a las dos y a las cuatro semanas.
