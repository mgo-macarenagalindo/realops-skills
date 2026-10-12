# Ejemplo de output · UTMs de Punta a Punta

> Datos ficticios. Mentoría de 4 meses para psicólogos que quieren armar su consultorio online. Se vende por llamada desde una landing con agenda (Calendly incrustado). Tráfico: dos cuentas de Instagram (la principal y la del cofundador), un canal de YouTube, pauta en Meta (tráfico frío con 3 creativos y retargeting con 1), newsletter quincenal y una charla presencial con QR. Dos setters: Lucía y Joaquín. Zapier pasa cada agenda a Airtable.

**Lo que contó la persona:** "La fuente la carga el setter a mano en Airtable. En septiembre, 41 de 96 agendas quedaron sin fuente. El founder quiere saber si YouTube vende o solo trae vistas."

---

# Convención de UTMs · Mentoría para psicólogos (caso ficticio)

## Qué queremos poder responder

1. ¿Cuántas agendas, asistencias y ventas trae cada canal? (orgánico de cada cuenta, YouTube, pauta, newsletter, evento)
2. ¿Qué setter trae agendas que asisten y cierran?
3. ¿Qué creativo de pauta vende, no solo cuál llena la agenda?

## La convención

| Parámetro | Valores permitidos | Significado |
|---|---|---|
| `utm_source` | `ig` · `yt` · `fb` · `nl` · `qr` | Instagram · YouTube · Facebook/Instagram Ads · Newsletter · Evento presencial |
| `utm_medium` | `org` · `bio` · `ads` · `setter` · `evento` | Contenido orgánico · Link de la bio · Pauta · Link que pasa un setter · Presencial |
| `utm_campaign` | `cuenta-principal` · `cuenta-cofundador` · `frio` · `retarg` · `canal` · `nl-quincenal` · `charla-oct26` | Cuenta o tipo de tráfico |
| `utm_content` | Creativos: `ad-testimonio-01` · `ad-errores-02` · `ad-mito-03` · `ad-retarg-01` · Setters: `lu` · `jo` · Videos: `yt-descripcion` · `yt-fijado` | Pieza o persona |

Todo en minúsculas, sin acentos, con guiones. Un valor nuevo se agrega primero a esta tabla.

## Registro de links

Landing: `https://ejemplo.com/diagnostico` (el link apunta a la página, nunca al widget de agenda).

| Uso | source | medium | campaign | content | Responsable |
|---|---|---|---|---|---|
| Bio cuenta principal | ig | bio | cuenta-principal | — | Contenido |
| Bio cuenta del cofundador | ig | bio | cuenta-cofundador | — | Contenido |
| Respuesta de setter Lucía | ig | setter | cuenta-principal | lu | Lucía |
| Respuesta de setter Joaquín | ig | setter | cuenta-principal | jo | Joaquín |
| Descripción de videos de YouTube | yt | org | canal | yt-descripcion | Contenido |
| Comentario fijado en YouTube | yt | org | canal | yt-fijado | Contenido |
| Anuncio testimonio (frío) | fb | ads | frio | ad-testimonio-01 | Tráfico |
| Anuncio errores (frío) | fb | ads | frio | ad-errores-02 | Tráfico |
| Anuncio mito (frío) | fb | ads | frio | ad-mito-03 | Tráfico |
| Anuncio retargeting | fb | ads | retarg | ad-retarg-01 | Tráfico |
| Newsletter | nl | org | nl-quincenal | — | Contenido |
| QR de la charla | qr | evento | charla-oct26 | — | Operaciones |

Ejemplo de link final (setter Lucía):
`https://ejemplo.com/diagnostico?utm_source=ig&utm_medium=setter&utm_campaign=cuenta-principal&utm_content=lu`

Los anuncios llevan en `utm_content` **el mismo nombre que el anuncio en el administrador**, así se cruzan sin traducir.

## Cómo llega a la base

1. En Airtable, tabla Agendas: crear `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` (texto de una línea).
2. Abrir el link de Lucía en una ventana de incógnito y hacer **una reserva de prueba** con tu mail.
3. En el Zap "Calendly → Agendas", volver al disparador y traer esa reserva como prueba. Ahora aparecen los cuatro parámetros.
4. Mapear cada uno a su columna. Publicar.
5. Repetir la reserva de prueba con el link de un anuncio y con el de YouTube, y verificar las tres filas en Airtable.
6. Borrar o marcar las reservas de prueba.

## Fórmulas

**Canal** (en Agendas; la misma lógica se usa en Deals):

```airtable
IF(
  {utm_source} = "",
  "Sin dato",
  IF(
    {utm_medium} = "ads",
    "Pauta",
    SWITCH(
      {utm_source},
      "ig", "Instagram orgánico",
      "yt", "YouTube",
      "nl", "Newsletter",
      "qr", "Evento presencial",
      "Otro"
    )
  )
)
```

Con esto, las agendas de setters cuentan como "Instagram orgánico" (el canal) y el setter se lee aparte:

**Setter:**

```airtable
IF(
  {utm_medium} = "setter",
  SWITCH({utm_content}, "lu", "Lucía", "jo", "Joaquín", "Setter sin código"),
  "Sin setter"
)
```

**Cuenta** (para separar las dos cuentas de Instagram):

```airtable
SWITCH({utm_campaign}, "cuenta-principal", "Principal", "cuenta-cofundador", "Cofundador", "")
```

**Respaldo sin UTM (código en el evento):** como cada setter también tiene su tipo de evento en Calendly, `Llamada de diagnóstico (LU)` y `Llamada de diagnóstico (JO)`, se agrega un respaldo para cuando el lead llega sin parámetros:

```airtable
IF(
  {Setter} != "Sin setter",
  {Setter},
  IF(FIND("(LU)", {Nombre del evento}), "Lucía",
  IF(FIND("(JO)", {Nombre del evento}), "Joaquín", "Sin setter"))
)
```

## Lo que no medimos con UTM y cómo se lee

| Qué | Por qué no | Cómo se lee |
|---|---|---|
| Anuncios para ganar seguidores | El lead no pasa por un link | Costo por seguidor en el administrador + evolución de agendas con `medium=bio` |
| Cada historia de Instagram | Costo de carga mayor que el valor del dato | Etiqueta por fecha en el calendario de contenidos, cruzada con las agendas de esa semana |
| Recomendaciones de boca en boca | No hay link | Pregunta obligatoria en el formulario de agenda: "¿Cómo nos conociste?" |

**Meta de tracking:** que "Sin dato" baje de 41 de 96 agendas (43 %) a menos de 1 de cada 10 en octubre. Si no baja, revisar qué link se está usando sin UTM.

## Checklist de prueba

- [ ] Reserva de prueba con cada tipo de link (bio, setter, YouTube, anuncio, newsletter, QR): 6 filas con sus 4 parámetros en Airtable.
- [ ] La fórmula `Canal` muestra el texto correcto en las 6.
- [ ] La fórmula `Setter` muestra el nombre en las de setter y "Sin setter" en el resto.
- [ ] Una reserva desde el link común (sin UTM) aparece como "Sin dato", no como un canal.
- [ ] El equipo de tráfico confirmó por escrito que cada anuncio nuevo lleva su `utm_content`.
- [ ] El campo manual "Fuente" se oculta (no se borra) cuando la fórmula lleva dos semanas funcionando.

---

**Mensaje para los setters (opcional):**

> Desde el lunes, cuando pasen el link de agenda, usen el suyo (está fijado en el canal). Así cada agenda que traen queda registrada a su nombre sin cargar nada, vemos qué conversaciones terminan en venta y las comisiones salen solas.
