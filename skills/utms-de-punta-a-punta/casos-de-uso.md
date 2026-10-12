# Casos de uso · UTMs de Punta a Punta

Cuatro situaciones de infonegocio donde saber de dónde viene cada lead cambia las decisiones. Negocios y nombres ficticios.

---

## 1. "¿De dónde vienen los que compran?"

**La situación.** Una mentoría vende por llamada con tráfico de Instagram, YouTube y pauta. En la base, el campo "Fuente" lo carga el setter a mano y está vacío en 4 de cada 10 agendas.

**Qué le pasás.** Las cuentas y canales, cuántos setters hay, la herramienta de agenda y cómo llega el dato a Airtable.

**Qué te devuelve.** La convención de macro a micro, el registro de links (uno por cuenta, uno por setter, uno por anuncio), los pasos para mapearlo en Zapier con la reserva de prueba y la fórmula que traduce los códigos a "Instagram orgánico", "Pauta" o "Setter". La carga manual de "Fuente" desaparece.

**Por qué sirve.** Sin canal no hay segmentación, y sin segmentación no hay diagnóstico. Clase 05/08.

---

## 2. "Hice todo y las UTMs no aparecen"

**La situación.** Armaste los links, creaste las columnas en Airtable, pero en Zapier no hay ningún parámetro para mapear.

**Qué le pasás.** Cómo probaste y a dónde apunta el link.

**Qué te devuelve.** El diagnóstico típico: la reserva de prueba se hizo con el link común (sin UTM), o el link apunta al widget de agenda y no a la landing. La secuencia correcta: reserva de prueba con el link con UTM, traer esa prueba al Zap, mapear. Y el checklist para validar que llegan.

**Por qué sirve.** Es la traba más repetida del tema. Clases 22/06 y 29/06.

---

## 3. Lanzamiento con 6 anuncios y una trafficker

**La situación.** Un programa va a lanzar una cohorte con 6 creativos en Meta, los publica una trafficker freelance, y quieren saber después cuál vendió, no cuál trajo más inscriptos.

**Qué le pasás.** Los creativos (formato y de qué habla cada uno), quién los publica, a dónde manda cada uno (formulario de inscripción en Tally a una clase en vivo).

**Qué te devuelve.** Un `utm_content` por creativo que se entiende sin diccionario (`vid-testimonio-psico-v1`, `car-error-4errores-v2`), el brief de una página para la trafficker con los parámetros dinámicos de Meta (nombre e ID de cada anuncio) y el checklist antes de publicar, los campos ocultos del Tally que guardan todo y cómo se va a cruzar después con las ventas. Con lo que no se va a poder medir (los anuncios de seguidores) dicho de antemano.

**Por qué sirve.** Medir cada anuncio pasa a ser parte de publicarlo, no una tarea que alguien hace (o no) después. Deja listo el dato que necesita la skill Rentabilidad por Anuncio. Clases 19/08 y 07/10.

---

## 4. "En la base dice AD-03 y nadie sabe qué es"

**La situación.** Los anuncios ya tienen UTM, pero el `utm_content` es un número (`AD-03`, `ad3`, `Ad 3`) y los referidos y los closers no aparecen por ningún lado.

**Qué le pasás.** Cinco o seis valores reales del histórico, quién publica los anuncios, cómo llegan los referidos y cómo se reparte la agenda de closers.

**Qué te devuelve.** La tabla de anuncios con el código viejo al lado del nombre nuevo, fórmulas que leen las dos formas sin reescribir el histórico, un link de referido por alumno con su ID y el closer asignado desde el anfitrión de la agenda, en el mismo Zap.

**Por qué sirve.** Arreglás hacia adelante sin romper lo que ya está cargado. Clases 01/06 y 27/04.
