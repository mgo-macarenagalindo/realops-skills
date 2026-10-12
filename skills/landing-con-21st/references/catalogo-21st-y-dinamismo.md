# Catálogo de 21st.dev por sección y dinamismo con criterio

> Referencia de **Constructor de Landing con 21st.dev** (RealOps™). Categorías y componentes verificados en 21st.dev el **12/10/2026** (los 6 componentes de ejemplo y las categorías abrían bien ese día). 21st es una comunidad: los componentes cambian, se renombran o se borran. Antes de pasar un link, abrilo; si no está, buscá en la categoría.
>
> **Cuándo se revisa** *(criterio orientativo)*: al empezar cada ciclo de 4 semanas del programa. Si la fecha de arriba tiene más de 2 meses, verificá cada link concreto antes de pasarlo y, si alguno ya no existe, pasá la categoría.

## Por qué siempre se pasan referencias de 21st

"Hacelo moderno" no se puede construir. Un link a un componente sí: Claude ve qué hace, cómo se mueve y cómo se ordena, y lo construye igual (camino A) o escribe su propia versión (camino B). Por eso **cada sección del plan lleva al menos un link de 21st** (la categoría y, si se puede, uno o dos componentes concretos), y la persona elige.

En el **camino B** (HTML para pegar en GoHighLevel, Kajabi, WordPress o Hostinger) los componentes de 21st no se pegan: son React + Tailwind y esos constructores no los corren. Se usan como **referencia visual** y Claude reescribe el efecto en HTML, CSS y JavaScript sin librerías. Muchas veces sale más liviano (por ejemplo, un "cierre cortina" se hace con `position: sticky`, sin la librería de animación del original).

## Sección de la landing → categoría de 21st

| Sección | Categoría en 21st.dev | Ejemplos para abrir y mirar |
|---|---|---|
| Hero | [Heroes](https://21st.dev/community/components/s/hero) · [Backgrounds](https://21st.dev/community/components/s/background) · [Shaders](https://21st.dev/community/shaders) | `@arunachalam/scroll-expansion-hero` (el video crece al hacer scroll) · `@kokonutd/background-paths` (fondo con líneas en movimiento) |
| Problema | [Texts](https://21st.dev/community/components/s/text) · [Cards](https://21st.dev/community/components/s/card) | `@jahed/spotlight-card` (la tarjeta se ilumina donde pasa el mouse) |
| Mecanismo (el método en pasos) | [Timelines](https://21st.dev/community/components/s/timeline) · [Steppers](https://21st.dev/community/components/s/steps) | `@ibrandify/scroll-timeline` (la línea se llena al hacer scroll) · `@ln-dev7/how-it-works-02` (cómo funciona, vertical) |
| Prueba | [Testimonials](https://21st.dev/community/components/s/testimonials) · [Stats & KPIs](https://21st.dev/community/components/s/stat) · [Videos](https://21st.dev/community/components/s/video) | Grilla de testimonios con video; números que cuentan al entrar (solo con números reales) |
| Oferta y para quién es | [Features](https://21st.dev/community/components/s/features) · [Comparisons](https://21st.dev/community/components/s/comparison) · [Grids & Bento](https://21st.dev/community/components/s/grid) | Bento de "qué incluye"; dos columnas "es para vos / no es para vos" |
| FAQ | [FAQs](https://21st.dev/community/components/s/faq) · [Accordions](https://21st.dev/community/components/s/accordion) | `@ln-dev7/faqs-01` (acordeón centrado) · `@ln-dev7/faqs-02` (dos columnas) |
| CTA y formulario | [Calls to Action](https://21st.dev/community/components/s/cta) · [Forms](https://21st.dev/community/components/s/form) · [Buttons](https://21st.dev/community/components/s/button) | Botón con brillo o "magnético"; formulario en pasos |
| Cierre | [Footers](https://21st.dev/community/components/s/footer) | Cierre "cortina" (el contenido se levanta y descubre el cierre fijo detrás) |

Los links de ejemplo van como `https://21st.dev/@<autor>/components/<componente>`. Para ver todo: [21st.dev/community/components](https://21st.dev/community/components).

**No uses** de 21st, en una landing de un solo CTA: menús de navegación, docks, carruseles de logos que el negocio no tiene ni "clients" inventados.

## Dinamismo: qué se recomienda siempre

Una landing quieta se siente plantilla. Una con diez efectos tarda en cargar y distrae del botón. La regla *(criterio orientativo)*: **2 o 3 momentos de movimiento por página, cada uno con un para qué.**

| Efecto | Para qué sirve en la venta | Dónde va | Categoría de referencia |
|---|---|---|---|
| **Aparecer al hacer scroll** (fade + subida corta, escalonado) | Ritmo de lectura: cada bloque llega cuando lo mirás | Toda la página, sutil | Texts · Features |
| **Línea de tiempo que se llena** | Hace visible el método: del punto A al B | Mecanismo | Timelines |
| **Tarjeta con luz o inclinación 3D** al pasar el mouse | Invita a leer los dolores o lo que incluye | Problema · Oferta (solo en compu) | Cards |
| **Números que cuentan** al entrar | Le da peso a un dato real | Prueba (solo con datos con fuente) | Stats & KPIs · Numbers |
| **Hero con fondo en movimiento** (aurora, malla, líneas) | Primera impresión "pro" sin sumar texto | Hero | Backgrounds · Shaders |
| **Botón magnético o con brillo** | Lleva la vista al único CTA | CTA del hero y final | Buttons · Calls to Action |
| **Barra fija con el CTA en el celular** | El botón siempre a mano sin repetir secciones | Celular | Calls to Action |
| **Cierre cortina** | Un final memorable que repite el CTA | Cierre | Footers |

**Reglas de performance y accesibilidad (siempre):**

- Respetar `prefers-reduced-motion`: quien lo tiene activado ve todo, sin animaciones.
- Inclinación 3D y botón magnético **solo con mouse**: en el celular no se activan.
- Las animaciones que no están en pantalla se pausan.
- Sin JavaScript o si algo falla, el contenido se ve igual (lo oculto para animar solo se oculta si el script arrancó).
- Sin librerías pesadas en el camino B. Un `IntersectionObserver` alcanza para casi todo.
- Nada de movimiento en el texto del formulario ni en el precio.

## Cómo se pasa una referencia en el chat

> Para el mecanismo quiero algo como esto: https://21st.dev/@ibrandify/components/scroll-timeline — la línea que se llena al hacer scroll. No copies el código: hacé tu versión en HTML y CSS, con nuestros colores.

En el camino A, en cambio, se instala (`npx @21st-dev/cli@latest add <autor>/<componente>`, con la sesión o la key cargada) y va a `CREDITOS.md` con su link.
