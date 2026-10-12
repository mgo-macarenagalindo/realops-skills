# Formularios y agendas · cómo guarda cada herramienta los parámetros

> Referencia de la skill UTMs de Punta a Punta. Cargala cuando la entrada del lead sea un formulario o una agenda y haya que configurar la captura.

La regla en todas: **el nombre del parámetro en el link y el nombre del campo tienen que ser idénticos** (`utm_content` no es `UTM_content` ni `utm content`). Y siempre se prueba con el link con UTM.

| Herramienta | Cómo captura | Qué tenés que hacer |
|---|---|---|
| **Calendly** | Toma `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` y `utm_term` de la URL de la página donde está | Que el link apunte a la landing con el widget. En Zapier aparecen en el disparador después de una reserva de prueba con el link con UTM. Parámetros propios (como `ad_id`) no los guarda: pasalo en `utm_term` o capturalo antes, en el formulario |
| **GoHighLevel** | Guarda los parámetros de la URL en el contacto (atribución) | Verificá en el contacto de prueba que aparezcan; mapealos a campos personalizados si los querés mandar a otra base |
| **Typeform** | Campos ocultos (*hidden fields*) | En el formulario: Lógica → campos ocultos, uno por parámetro con el nombre exacto. Link directo: `...form/abc?utm_source=ig&utm_content=...`. **Incrustado en una landing:** activá que tome los parámetros de la página (`data-tf-transitive-search-params` con la lista de nombres) y no les pongas un valor fijo en el código del embed, porque pisa el de la URL |
| **Tally** | Campos ocultos | Agregá el bloque de campos ocultos con los nombres exactos (distingue mayúsculas). Incrustado con el código de Tally, toma los parámetros de la página que lo contiene |
| **Formulario de Airtable** | Prellenado por link | Link con `prefill_utm_source=ig&hide_utm_source=true` para cada campo. Armá el link una vez por canal |
| **Google Forms** | No tiene campos ocultos | Link prellenado con la pregunta de origen (visible). Si el tracking importa, pasá a un formulario que los tenga |
| **Checkout (Hotmart, Stripe, Kajabi)** | Varía: algunos guardan `src`/`sck` o metadatos | Confirmá en una compra de prueba qué llega. Si no llega, el cruce con la venta se hace por mail contra el lead que sí tiene UTM |

## Formulario y después agenda

Cuando el lead llena una aplicación (Typeform, Tally) y después agenda (Calendly):
- **La UTM se guarda en la aplicación**, que es donde nace el lead. La agenda se vincula por mail.
- Si querés que la agenda también la tenga, en la redirección final del formulario agregá los campos ocultos al link de Calendly (`?utm_source={utm_source}&...` usando la opción de "recall" de la herramienta).

## El closer desde el anfitrión

En Calendly con evento rotativo o colectivo, el disparador de Zapier trae el **mail del anfitrión** asignado. Mapealo a una columna `Anfitrión (mail)` y traducilo:

```airtable
SWITCH(
  LOWER(TRIM({Anfitrión (mail)})),
  "closer1@negocio.com", "Nombre Closer 1",
  "closer2@negocio.com", "Nombre Closer 2",
  "Sin closer"
)
```

Mejor todavía: vinculá la llamada a la tabla Closers buscando por mail (paso "Find record" en Zapier) para tener rollups de llamadas y ventas por closer. Requisito: cada closer con su propio usuario en Calendly (si comparten cuenta, no hay anfitrión distinguible).
