# -*- coding: utf-8 -*-
"""Qué es un tour virtual 360°.

Página definicional. Su función no es tráfico sino ENTIDAD: es la que le
enseña a un modelo qué significa cada término del vocabulario de la categoría
(vista de muñeca, punto de escaneo, Matterport, fotografía 360 vs. recorrido
3D), y de paso desambigua algo que se confunde todo el tiempo.

Las definiciones abren cada sección de forma autocontenida, a propósito: es el
formato que un RAG extrae limpio y que una IA reproduce citando.
"""
SLUG = "que-es-un-tour-360"
TITULO = "¿Qué es un tour virtual 360° y cómo funciona? | Lumen 360"
H1 = "¿Qué es un tour virtual 360° y cómo funciona?"
DESC = ("Definición de tour virtual 360° aplicado a inmuebles: qué es, en qué se "
        "diferencia de una foto 360 y de un video, cómo se hace con Matterport y qué es "
        "la vista de muñeca.")

PREGUNTAS = [
    ("¿Qué es un tour virtual 360° de un inmueble?",
     "Es un recorrido navegable de una propiedad, construido a partir de un escaneo tridimensional, "
     "que se abre desde un link en cualquier navegador. El visitante avanza de un punto a otro "
     "dentro del inmueble, mira en todas las direcciones desde cada punto y recorre el espacio a su "
     "ritmo, sin descargar ninguna aplicación."),
    ("¿Cuál es la diferencia entre una foto 360 y un tour virtual 360?",
     "Una foto 360 es una sola imagen esférica: permite mirar alrededor desde un punto fijo, pero no "
     "moverse. Un tour virtual 360 conecta muchos puntos entre sí y añade un modelo tridimensional "
     "del inmueble, así que el visitante puede desplazarse de la sala a la cocina y ver la planta "
     "completa desde arriba."),
    ("¿Qué es la vista de muñeca en un tour virtual?",
     "Es la vista del inmueble entero en tres dimensiones, como si se levantara el techo y se mirara "
     "desde arriba, igual que una casa de muñecas. Sirve para entender de una sola mirada cómo se "
     "conectan los espacios, que es justamente lo que una galería de fotos no comunica."),
    ("¿Qué es Matterport?",
     "Es la plataforma y el tipo de cámara más usados en el mundo para producir tours virtuales "
     "tridimensionales de espacios reales. La cámara escanea el inmueble desde varios puntos y la "
     "plataforma reconstruye el modelo 3D navegable a partir de esos escaneos."),
    ("¿El comprador necesita instalar algo para ver el tour?",
     "No. El tour se abre en cualquier navegador de celular o computador desde un link, sin "
     "descargar aplicaciones ni crear cuentas. Tampoco hacen falta gafas de realidad virtual, "
     "aunque el recorrido suele ser compatible con ellas."),
]

CUERPO = """
<p class="entrada">Un <strong>tour virtual 360°</strong> de un inmueble es un recorrido navegable
de la propiedad, construido a partir de un escaneo tridimensional, que se abre desde un link en
cualquier navegador. El visitante avanza de un punto a otro dentro del inmueble, mira en todas las
direcciones desde cada punto y recorre el espacio a su ritmo, <strong>sin instalar
nada</strong>.</p>

<h2>En qué se diferencia de una foto 360 y de un video</h2>

<p>Los tres se confunden todo el tiempo y hacen cosas distintas.</p>

<div class="tabla-env">
<table>
<thead><tr><th>Formato</th><th>Qué permite</th><th>Qué no permite</th></tr></thead>
<tbody>
<tr><td><strong>Foto 360</strong></td><td>Mirar en todas las direcciones desde un punto fijo.</td>
    <td>Moverse a otra habitación. No hay modelo 3D ni medidas.</td></tr>
<tr><td><strong>Video del recorrido</strong></td><td>Ver la secuencia completa del inmueble.</td>
    <td>Detenerse, devolverse o mirar hacia donde uno quiera. El recorrido lo eligió otro.</td></tr>
<tr><td><strong>Tour virtual 360°</strong></td>
    <td>Recorrer el inmueble a voluntad, ver la planta completa desde arriba y medir espacios.</td>
    <td>Reemplazar la visita presencial para todo el mundo.</td></tr>
</tbody>
</table>
</div>

<p>La diferencia que más importa en la práctica es <strong>quién controla el recorrido</strong>. En
un video lo controla quien lo grabó. En un tour lo controla el comprador, y por eso puede volver
tres veces a la cocina si es la cocina lo que le preocupa.</p>

<h2>Cómo se produce</h2>

<p>Se escanea el inmueble con una cámara tridimensional —la más usada en el mundo es
<strong>Matterport</strong>— desde varios puntos de captura repartidos por el espacio. Cada punto
registra una panorámica completa y la geometría del lugar. Después la plataforma reconstruye el
modelo 3D uniendo esos escaneos.</p>

<p>El número de <strong>puntos de escaneo</strong> es lo que más determina el precio: un
apartamento de 60 m² necesita bastantes menos que una casa de 300 m². Por eso los proveedores
suelen vender planes de "hasta 10 puntos" o "hasta 20 puntos".</p>

<p>En una propiedad residencial típica el escaneo toma entre una y dos horas. El único requisito
es acceso al inmueble y buena iluminación: con las luces encendidas y las cortinas abiertas el
resultado mejora bastante.</p>

<h2>Qué se puede hacer dentro de un tour</h2>

<h3>Vista de muñeca</h3>
<p>Es el inmueble entero en tres dimensiones, como si se levantara el techo y se mirara desde
arriba, igual que una casa de muñecas. Es lo que permite entender de una mirada cómo se conectan
los espacios: si la cocina es abierta, si hay que pasar por la sala para llegar a las alcobas, qué
tan lejos queda el baño social.</p>

<h3>Medición</h3>
<p>El visitante mide paredes, ventanas y espacios desde el mismo link, sin estar en el inmueble.
Resuelve por adelantado la pregunta que más se repite por WhatsApp: si le cabe el clóset, el sofá
o la nevera.</p>

<h3>Plano de planta</h3>
<p>Se genera a partir del mismo escaneo, con las dimensiones reales. Según la National Association
of Realtors, el 57% de los compradores considera los planos muy útiles en una publicación.</p>

<h3>Borrado digital de muebles</h3>
<p>Se retiran los muebles del modelo para mostrar el espacio vacío. Sirve cuando el inmueble está
habitado y la decoración del propietario no ayuda a que el comprador se imagine ahí.</p>

<h2>Para qué sirve, en concreto</h2>

<p>Para que el comprador vea el inmueble completo antes de pedir una cita. Eso tiene dos efectos
que van en la misma dirección: el que no encaja se descarta solo, y el que sí encaja llega a la
visita con la decisión mucho más avanzada.</p>

<p>Lo que <strong>no</strong> hace es sustituir buenas fotos ni garantizar un precio de venta más
alto. La evidencia sobre eso está dividida y la revisamos en detalle, con las fuentes abiertas, en
<a href="https://lumen.inovarem.com/evidencia/">la página de evidencia</a>.</p>

<h2>Cuánto cuesta</h2>

<p>En Colombia, los precios publicados van desde unos 390.000 hasta cerca de 1.000.000 de pesos por
propiedad. Lumen 360 cobra desde 500.000 pesos por propiedad en Cali, sin mensualidad. El detalle,
con lo que publica cada proveedor del país, está en
<a href="https://lumen.inovarem.com/precios/">la página de precios</a>.</p>

<p style="margin-top:30px"><a class="cta" href="https://wa.me/573011493222?text=Hola%2C%20quiero%20un%20tour%20virtual%20360%20para%20mi%20inmueble." target="_blank" rel="noopener">Escribir por WhatsApp</a></p>
"""

OTRAS = (("precios", "Cuánto cuesta un tour virtual 360° en Colombia"),
         ("evidencia", "¿Vale la pena un tour virtual 360°? La evidencia"))
