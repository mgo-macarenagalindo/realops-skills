# Ejemplo de output · UTMs de Punta a Punta

> Datos ficticios. Mentoría de 4 meses para psicólogos que quieren armar su consultorio online. Se vende por llamada desde una landing con agenda (Calendly incrustado, evento rotativo entre dos closers). Tráfico: dos cuentas de Instagram (la principal y la del cofundador), un canal de YouTube, pauta en Meta (tráfico frío con 3 creativos y retargeting con 1, los publica una trafficker freelance), newsletter quincenal, referidos de alumnos y una charla presencial con QR. Dos setters: Lucía y Joaquín. Zapier pasa cada agenda a Airtable.

**Lo que contó la persona:** "La fuente la carga el setter a mano en Airtable. En septiembre, 41 de 96 agendas quedaron sin fuente. Los anuncios tienen UTM, pero en la base dice `AD1`, `AD2`, `Ad3` y nadie sabe cuál es cuál. El founder quiere saber si YouTube vende o solo trae vistas, y cuánto venden los referidos."

---

# Convención de UTMs · Mentoría para psicólogos (caso ficticio)

## Qué queremos poder responder

1. ¿Cuántas agendas, asistencias y ventas trae cada canal? (orgánico de cada cuenta, YouTube, pauta, newsletter, referidos, evento)
2. ¿Qué anuncio específico vende, no solo cuál llena la agenda?
3. ¿Qué setter trae agendas que asisten y cierran? ¿Y qué closer cierra?
4. ¿Cuánto venden los referidos y quién refiere?

## La convención

| Parámetro | Valores permitidos | Significado |
|---|---|---|
| `utm_source` | `ig` · `yt` · `fb` · `nl` · `qr` · `ref` | Instagram · YouTube · Meta Ads · Newsletter · Evento presencial · Referido |
| `utm_medium` | `org` · `bio` · `ads` · `setter` · `evento` · `alumno` | Orgánico · Link de la bio · Pauta · Link de setter · Presencial · Link de alumno que refiere |
| `utm_campaign` | `cuenta-principal` · `cuenta-cofundador` · `canal` · `nl-quincenal` · `charla-oct26` · `referidos` · en pauta, el nombre de la campaña | Cuenta, campaña o tipo de tráfico |
| `utm_term` | Solo pauta: nombre del conjunto (`frio-intereses-psico`, `retarg-30d`) | Público |
| `utm_content` | Creativos según la regla de abajo · Setters: `lu`, `jo` · Videos: `yt-descripcion`, `yt-fijado` · Alumnos: su ID (`a0123`) | Pieza o persona |
| `ad_id` | Lo completa Meta | ID del anuncio |

Todo en minúsculas, sin acentos, con guiones. Un valor nuevo se agrega primero a esta tabla. **Fecha de corte: 20/10.** Desde ese día todo valor nuevo sigue esta convención; lo anterior se traduce, no se reescribe.

## Nomenclatura de `utm_content`

Regla: **`formato-angulo-gancho-version`**. Se lee y sabés qué pieza es sin abrir el administrador.

| Código viejo (histórico) | `utm_content` nuevo = nombre del anuncio en Meta | Formato | Ángulo | Qué es | Estado |
|---|---|---|---|---|---|
| `AD1` | `vid-testimonio-consultorio-v1` | Video | Testimonio | Psicóloga que llenó su agenda online | Activo |
| `AD2` | `car-error-5errores-v1` | Carrusel | Error | Los 5 errores al armar el consultorio online | Activo |
| `Ad3` | `img-mito-cobrarmenos-v1` | Imagen | Mito | "Online se cobra menos" | Pausado |
| `AD4` | `vid-oferta-retarg-v1` | Video | Oferta | Retargeting a quienes vieron la clase | Activo |

Cuando la trafficker haga dos versiones más del testimonio, son `vid-testimonio-consultorio-v2` y `-v3`, no `AD5` y `AD6`. El `ad_id` de cada una se suma a esta tabla cuando avisa que la publicó.

## Brief para la trafficker

> Para Carla (trafficker) · desde el 20/10
>
> **1. Nombres.** Campaña: `aplicacion-mentoria-oct26` (frío) y `retarg-mentoria-oct26`. Conjunto: `frio-intereses-psico`, `retarg-30d`. Anuncio: `formato-angulo-gancho-version`, como en la tabla. Minúsculas, guiones, sin acentos.
>
> **2. Parámetros de URL en cada anuncio** (campo "Parámetros de URL"):
> `utm_source=fb&utm_medium=ads&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&ad_id={{ad.id}}`
>
> **3. Antes de activar:** nombre con la convención, parámetros cargados, link a `https://ejemplo.com/diagnostico` (no al Calendly).
>
> **4. Después de activar:** aviso en #marketing con nombre e ID del anuncio.
>
> **5. Cada lunes:** export por anuncio con "Identificador del anuncio", gasto y agendas. Operaciones lo cruza con ventas y te devuelve el costo por venta de cada anuncio.
>
> Por qué: vas a poder mostrar qué anuncio tuyo vende, no solo cuál trae agendas baratas.

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
| Anuncios (todos) | fb | ads | `{{campaign.name}}` | `{{ad.name}}` (+ `ad_id`) | Trafficker |
| Newsletter | nl | org | nl-quincenal | — | Contenido |
| Referido del alumno A-0123 | ref | alumno | referidos | a0123 | Operaciones (va en el mail de referidos) |
| QR de la charla | qr | evento | charla-oct26 | — | Operaciones |

Ejemplo de link final (setter Lucía):
`https://ejemplo.com/diagnostico?utm_source=ig&utm_medium=setter&utm_campaign=cuenta-principal&utm_content=lu`

Link de referido: se genera con una fórmula en la tabla Alumnos y se manda en el mail de referidos a los 21 días del ingreso:
```airtable
"https://ejemplo.com/diagnostico?utm_source=ref&utm_medium=alumno&utm_campaign=referidos&utm_content=" & LOWER(SUBSTITUTE({ID}, "-", ""))
```

## Cómo llega a la base

**Con qué:** Zapier, porque el Zap "Calendly → Agendas" ya existe y lo mantiene alguien que no es técnico. Con unas 100 agendas por mes y un paso extra para el closer, hace falta un plan pago; si el costo pesa, Make hace lo mismo más barato por volumen. Si estuvieran en el plan gratis de Airtable, la alternativa es exportar las reservas de Calendly a CSV una vez por semana e importarlas (el anfitrión viene en el mismo archivo).

1. En Airtable, tabla Agendas: crear `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content` y `Anfitrión (mail)` (texto de una línea).
2. Abrir el link de Lucía en una ventana de incógnito y hacer **una reserva de prueba** con tu mail.
3. En el Zap "Calendly → Agendas", volver al disparador y traer esa reserva como prueba. Ahora aparecen los parámetros y el mail del anfitrión.
4. Mapear cada parámetro a su columna y el **mail del anfitrión** a `Anfitrión (mail)`. Publicar.
5. Repetir la prueba con el link de un anuncio (clic desde el anuncio publicado), con el de YouTube y con un link de referido, y verificar las filas en Airtable.
6. Calendly no guarda `ad_id`: como el `utm_content` es el nombre del anuncio y la tabla de anuncios tiene el ID, el cruce se hace por nombre. [Si más adelante pasan a un formulario de aplicación con campos ocultos, `ad_id` entra directo.]
7. Borrar o marcar las reservas de prueba.

## Fórmulas

Todas normalizan con `LOWER(TRIM())`, así `AD1` y `ad1` cuentan igual y el histórico se lee sin tocarlo.

**Canal:**

```airtable
IF(
  {utm_source} = "",
  "Sin dato",
  IF(
    LOWER(TRIM({utm_medium})) = "ads",
    "Pauta",
    SWITCH(
      LOWER(TRIM({utm_source})),
      "ig", "Instagram orgánico",
      "instagram", "Instagram orgánico",
      "yt", "YouTube",
      "nl", "Newsletter",
      "ref", "Referido",
      "qr", "Evento presencial",
      "Otro"
    )
  )
)
```

**Anuncio** (código viejo y nuevo al mismo nombre legible):

```airtable
IF(
  LOWER(TRIM({utm_medium})) != "ads", "",
  SWITCH(
    LOWER(TRIM({utm_content})),
    "ad1", "Testimonio consultorio v1",
    "vid-testimonio-consultorio-v1", "Testimonio consultorio v1",
    "ad2", "Carrusel 5 errores v1",
    "car-error-5errores-v1", "Carrusel 5 errores v1",
    "ad3", "Mito cobrar menos v1",
    "img-mito-cobrarmenos-v1", "Mito cobrar menos v1",
    "ad4", "Retargeting oferta v1",
    "vid-oferta-retarg-v1", "Retargeting oferta v1",
    "Anuncio sin registrar"
  )
)
```

Cuando haya más de 10 anuncios (referencia orientativa), reemplazá este `SWITCH` por un vínculo a la tabla Anuncios (con el código viejo y el nuevo como dos campos de búsqueda).

**Setter:**

```airtable
IF(
  LOWER(TRIM({utm_medium})) = "setter",
  SWITCH(LOWER(TRIM({utm_content})), "lu", "Lucía", "jo", "Joaquín", "Setter sin código"),
  "Sin setter"
)
```

**Closer** (desde el anfitrión de Calendly):

```airtable
SWITCH(
  LOWER(TRIM({Anfitrión (mail)})),
  "sofia@ejemplo.com", "Sofía",
  "diego@ejemplo.com", "Diego",
  "Sin closer"
)
```

**Alumno que refiere:** `IF(LOWER({utm_source}) = "ref", UPPER(LEFT({utm_content}, 1)) & "-" & MID({utm_content}, 2, 10), "")` devuelve `A-0123`, que se vincula a Alumnos.

**Respaldo sin UTM (código en el evento):** como cada setter también tiene su tipo de evento de calificación, `Llamada de diagnóstico (LU)` y `(JO)`:

```airtable
IF(
  {Setter} != "Sin setter",
  {Setter},
  IF(FIND("(LU)", {Nombre del evento}), "Lucía",
  IF(FIND("(JO)", {Nombre del evento}), "Joaquín", "Sin setter"))
)
```

## En la landing

Google Analytics (GA4) lee estas mismas UTMs y muestra cuántas visitas de cada link llegan a aplicar. Microsoft Clarity filtra grabaciones y mapas de calor por `utm_source`, `utm_medium` y `utm_campaign`: si la gente del anuncio de testimonio abandona en el primer bloque y la del carrusel no, el problema está en la promesa del anuncio, no en la página.

## Lo que no medimos con UTM y cómo se lee

| Qué | Por qué no | Cómo se lee |
|---|---|---|
| Anuncios para ganar seguidores | El lead no pasa por un link | Costo por seguidor en el administrador + evolución de agendas con `medium=bio` |
| Cada historia de Instagram | Costo de carga mayor que el valor del dato | Etiqueta por fecha en el calendario de contenidos, cruzada con las agendas de esa semana |
| Boca en boca sin link | No hay link | Pregunta en el formulario de agenda: "¿Cómo nos conociste?" (respaldo del link de referido) |

**Meta de tracking (orientativa):** que "Sin dato" baje de 41 de 96 agendas (43 %) a menos de 1 de cada 10 en noviembre, y que más de 9 de cada 10 agendas de pauta tengan anuncio reconocido.

## Checklist de prueba

- [ ] Prueba con cada tipo de link (bio, setter, YouTube, anuncio, newsletter, referido, QR): 7 filas con sus parámetros en Airtable.
- [ ] La fórmula `Canal` muestra el texto correcto en las 7.
- [ ] La fórmula `Anuncio` muestra el mismo nombre para `AD1` (histórico) y para `vid-testimonio-consultorio-v1`.
- [ ] La fórmula `Closer` muestra el nombre en la reserva de prueba (y "Sin closer" si el mail no está en la lista).
- [ ] Una reserva desde el link común (sin UTM) aparece como "Sin dato", no como un canal.
- [ ] La trafficker confirmó por escrito el brief y avisó el ID de cada anuncio activo.
- [ ] El campo manual "Fuente" se oculta (no se borra) cuando la fórmula lleva dos semanas funcionando.

## Para confirmar

| Supuesto | A quién |
|---|---|
| Cada closer tiene su propio usuario en Calendly (si comparten, no hay anfitrión) | Quien administra Calendly |
| La trafficker puede renombrar los anuncios activos sin reiniciar el aprendizaje | Trafficker |
| El mail de referidos sale a los 21 días | Coordinación de servicio |

---

**Mensaje para los setters (opcional):**

> Desde el lunes, cuando pasen el link de agenda, usen el suyo (está fijado en el canal). Así cada agenda que traen queda registrada a su nombre sin cargar nada, vemos qué conversaciones terminan en venta y las comisiones salen solas.
