# Ejemplo de output · Constructor de Landing con 21st.dev

> Datos ficticios. Caso práctico: **Programa Libertad Freelance** (finanzas y precios para freelancers, vendido por llamada). El copy final, la oferta, el avatar y el brief de marca salieron de la skill Arquitecto de Landing de Alto Ticket. El negocio usa GoHighLevel para el calendario y los mails, y quiere pegar la página ahí. La persona usa Claude en la app y nunca usó Node.js.

---

# Construcción · Página de agenda · Programa Libertad Freelance · Camino B

## Los inputs

| Input | Qué se usó |
|---|---|
| Copy final | El entregable del Arquitecto, 7 secciones + gracias |
| Oferta y avatar | Del mismo entregable: freelancers de diseño y desarrollo con clientes recurrentes; punto A "cobro lo mismo hace dos años" |
| Referencias visuales | Captura de una landing de un estudio contable (fondo crema, serif grande, un solo acento) + el Instagram del programa |
| Referencias de estructura | Tablero del Investigador: hero en dos columnas con video y calendario, mecanismo en 3 pasos, grilla de 4 testimonios |
| Links reales | Calendario de GoHighLevel y WhatsApp sí; logo `[PENDIENTE]` |

## Por qué camino B

La página va **adentro del constructor que ya paga el negocio** (elemento Custom Code de GoHighLevel) y la persona no maneja un proyecto React. 21st.dev se usa **como referencia visual**: Claude escribe sus versiones en HTML y CSS.

## El plan

| Sección | Referencia de 21st.dev | Qué tomamos |
|---|---|---|
| Hero (video + calendario) | [Heroes](https://21st.dev/community/components/s/hero) · [Backgrounds](https://21st.dev/community/components/s/background), por ejemplo `@kokonutd/background-paths` | Líneas suaves en movimiento detrás del título, en el verde de la marca, muy tenues |
| Problema | `@jahed/spotlight-card` | Las 3 frases en tarjetas que se iluminan donde pasa el mouse (en el celular, quietas) |
| Mecanismo | `@ibrandify/scroll-timeline` | Línea vertical que se llena al hacer scroll y enciende cada paso |
| Prueba | [Testimonials](https://21st.dev/community/components/s/testimonials) | Grilla de 2 × 2 con video y frase corta, sin carrusel |
| Para quién es / no | [Comparisons](https://21st.dev/community/components/s/comparison) | Dos columnas lado a lado, mismo peso visual |
| FAQ | `@ln-dev7/faqs-01` | Acordeón centrado, un "+" que gira |
| CTA final | [Calls to Action](https://21st.dev/community/components/s/cta) | Botón con un brillo que lo recorre cada pocos segundos |

**Momentos de movimiento (3):** la línea del mecanismo, las tarjetas del problema y el brillo del botón. Todo lo demás aparece con un fade corto al hacer scroll. Con "reducir movimiento" activado en el celular, la página queda quieta y se ve entera.

## Paso 1 · El prompt inicial

```
Vamos a construir la landing de agenda del Programa Libertad Freelance.
Te paso: el copy final (no lo cambies), la oferta y el avatar, la captura de referencia
visual, el tablero de estructura y estas referencias de 21st.dev por sección: [la tabla].

Camino: HTML autocontenido para pegar en un Custom Code de GoHighLevel.
- Un solo archivo con estilos y script. Estilos bajo la clase .lf.
- Fraunces (títulos) e Inter (texto). Colores #1F3D2B, #F6F1E7, #141414 y #D9A441 solo en botones.
- Un solo CTA (el calendario). Sin menú ni redes. Mobile-first (390 px).
- Los efectos de 21st, en tu propia versión con CSS y JS sin librerías. Respetá prefers-reduced-motion.
- Todo lo editable en un objeto CONFIG al final. Lo que no existe va como [PENDIENTE] visible.

Primero el plan. Después armala como artefacto para verla.
```

## Paso 2 · El artefacto

Claude muestra la página en un artefacto al costado del chat. Ahí se ve y se ajusta, sin tocar GoHighLevel.

| Ronda | Qué mirás | Ejemplo de pedido |
|---|---|---|
| 1 · Celular | ¿En el primer pantallazo se entiende qué es, para quién y qué hacer? ¿El fondo distrae del título? | "Las líneas del fondo, la mitad de intensas" |
| 2 · Compu | ¿El calendario se ve entero al lado del video? ¿La línea del mecanismo se llena a buen ritmo? | "La línea que termine de llenarse en el paso 3, no antes" |
| 3 · Detalle | Pendientes visibles, acordeón, botón de WhatsApp en gracias, la página con "reducir movimiento" | "En gracias, el botón tiene que abrir WhatsApp con el mensaje del CONFIG" |

El calendario no carga dentro del artefacto (la vista previa no deja traer páginas de afuera): se prueba en el paso 4.

## El CONFIG

```js
const CONFIG = {
  marca: { nombre: "Libertad Freelance", colorPrincipal: "#1F3D2B", colorAcento: "#D9A441", logoUrl: "" }, // [PENDIENTE] logo
  ctaTexto: "Agendá tu llamada de diagnóstico",
  calendario: "https://[tu-calendario-de-ghl]",   // la persona agenda directo desde la página
  precargarDatos: true,              // nombre, mail y UTM viajan en el link si el calendario los acepta
  webhookUrl: "",                    // no hay formulario propio: el calendario ya registra
  whatsapp: { numero: "5490000000000", mensaje: "Hola, agendé la llamada de diagnóstico. Me dedico a ___ y lo que más me preocupa de mis precios es ___." },
  videoUrl: "",                      // [PENDIENTE] link directo del video del founder
  movimiento: true,
  utm: ["utm_source", "utm_medium", "utm_campaign", "utm_content"], // se pasan al calendario
  noCalifica: { campo: "", valores: [], destinoUrl: "" }             // no aplica: el negocio no tiene criterio escrito
};
```

## El archivo completo

En camino B la skill entrega el `index.html` **entero** (en el artefacto y en un bloque para copiar). Acá, por largo, el esqueleto:

```html
<style>
.lf{ /* variables de color desde el CONFIG */ }
.lf [hidden]{display:none!important}
@media (prefers-reduced-motion: reduce){ .lf *{animation:none!important;transition:none!important} }
/* hero con líneas · tarjetas con luz · línea de tiempo · grilla · acordeón · botón con brillo */
</style>
<div class="lf"> <!-- las 7 secciones --> </div>
<script>
const CONFIG = { /* el de arriba */ };
/* un IntersectionObserver para el fade y la línea; la luz de las tarjetas solo con mouse */
</script>
```

## Paso 3 · Cómo migrarlo a GoHighLevel

1. En el funnel, una sección de ancho completo y sin padding, una fila, una columna, un elemento **Custom Code**.
2. Pegá desde `<style>` hasta el último `</script>`.
3. En la configuración de la página: título, descripción y *noindex* mientras sea borrador.
4. Videos: subí cada MP4 a la biblioteca de medios de GoHighLevel y pegá su link directo en el CONFIG.

**Si GoHighLevel limpia el script** y la línea o el acordeón no funcionan: subí la carpeta a **Netlify Drop** (app.netlify.com/drop) en una cuenta del negocio, conectá un subdominio y que el botón del funnel lleve ahí.

## Créditos

`CREDITOS.md`: los componentes de 21st.dev mirados como referencia (`@kokonutd/background-paths`, `@jahed/spotlight-card`, `@ibrandify/scroll-timeline`, `@ln-dev7/faqs-01`), con su link. No se copió código.

## Lo que queda pendiente antes de publicar

- URL pública del logo.
- Video del founder y los 4 testimonios con permiso.
- Probar en la página publicada el calendario con una reserva de prueba y `?utm_source=instagram` en la URL.

## Supuestos a validar

| Supuesto | Con quién | Cómo |
|---|---|---|
| El Custom Code de GoHighLevel corre `<script>` en el plan del negocio | Quien administra GoHighLevel | Pegar el archivo en una página de prueba sin publicar |

---

¿La pasamos por **Revisor de Landing y Publicación** antes de publicarla?
