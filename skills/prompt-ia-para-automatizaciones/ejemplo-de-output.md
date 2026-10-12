# Ejemplo de output · Prompt de IA para Automatizaciones

> Datos ficticios. Programa de 4 meses para nutricionistas que quieren vender online, USD 2.000, vendido por llamada. Las llamadas se graban con la grabadora de la cuenta de la empresa, que se conecta directo a Zapier. CRM en Airtable, equipo en Discord. Unas 70 llamadas de venta por mes.

**Lo que pidió la persona:** "Quiero que cada llamada de venta genere un informe para el closer y para su líder, y que marketing tenga las frases de los leads. Hoy el prompt dice 'hacé un informe de esta llamada' y sale distinto cada vez."

---

# Paso de IA · Informe de llamada de venta · Zapier

## Para qué y quién lo lee

- **Closer:** prepara la segunda llamada y el seguimiento sin volver a escuchar la grabación.
- **Líder comercial:** feedback objetivo con evidencia, llamada por llamada.
- **Marketing:** dolores y frases textuales del lead para guiones y anuncios.

## Disparador y filtro

1. **Disparador:** transcripción nueva en la grabadora (cuenta de la empresa).
2. **Filtro:** seguir solo si el título de la reunión empieza con `Venta ·` (deja afuera reuniones internas y sesiones de alumnos).
3. **Buscar en Airtable** la agenda por mail del invitado, para traer closer, canal y estado del lead.
4. **Paso de IA** (este prompt).
5. **Crear documento** desde la plantilla, en la carpeta "Informes de venta".
6. **Actualizar** la agenda en Airtable con el link al informe y los campos `Interés` y `Objeción principal`.
7. **Aviso corto** en #ventas de Discord, que es el canal que ya usa el equipo.

## Plantilla del documento

```
INFORME DE LLAMADA · [[nombre_lead]] · [[fecha_llamada]]
Closer: [[closer]] · Canal: [[canal]] · Resultado: [[resultado]]

1. Quién es
[[perfil]]

2. Dónde está hoy (punto A)
[[situacion_actual]]

3. Qué quiere lograr (punto B)
[[deseo]]

4. Dolor principal, en sus palabras
[[dolor_principal]]

5. Objeciones
[[objeciones]]

6. Nivel de interés
[[interes]] · [[motivo_interes]]

7. Próximo paso acordado
[[proximo_paso]]

8. Feedback para el closer
[[feedback_closer]]

9. Frases para marketing
[[frases_marketing]]
```

## El prompt

```
# ROL
Sos analista comercial del equipo de ventas de un programa online para
nutricionistas. Escribís para el closer que hizo la llamada y para su líder.
No sos el closer: describís lo que pasó, con evidencia.

# OBJETIVO
Convertir la transcripción de una llamada de venta en un informe con
siempre la misma estructura, para preparar el seguimiento, dar feedback
al closer y darle a marketing el lenguaje real del lead.

# DATOS DE ENTRADA
- TRANSCRIPCION: el texto completo de la llamada.
- CLOSER: nombre del closer (viene del CRM).
- CANAL: de dónde vino el lead (viene del CRM).
- ESTADO_LEAD: estado actual en el CRM (viene del CRM).
- FECHA_LLAMADA: fecha de la llamada.
Usá los datos del CRM tal cual. No los deduzcas de la transcripción.

# CAMPOS DE SALIDA
Devolvé cada campo por separado, con estos nombres exactos.

nombre_lead: nombre del lead como se presenta en la llamada. Si no lo dice, Sin dato.

resultado: una de estas opciones, exacta: Venta · Seguimiento · No calificado · Perdida.
  Criterio: Venta solo si en la llamada confirma el pago o la reserva.

perfil: 2 líneas máximo. Profesión, años de experiencia, cómo trabaja hoy.
  Ejemplo: "Nutricionista hace 6 años, atiende en consultorio 3 días por semana."

situacion_actual: 2 líneas. Cómo consigue pacientes hoy y cuánto factura, solo si lo dice.

deseo: 2 líneas. Qué quiere lograr, con plazo si lo menciona.

dolor_principal: UNA frase textual del lead, entre comillas, sin corregir.
  Ejemplo: "Estoy cansada de depender de que me deriven pacientes."

objeciones: lista de hasta 3. Cada una con: tipo (Precio · Tiempo · Confianza ·
  Decisión compartida · Otra) + cita textual entre comillas + si el closer la
  respondió (Sí / No / A medias).
  Una objeción es algo que el lead dice que le impide comprar ahora. Una pregunta
  de información no es una objeción.

interes: una de estas opciones, exacta: Alto · Medio · Bajo.
motivo_interes: 1 línea con la evidencia (algo que dijo o preguntó).

proximo_paso: qué quedó acordado, con fecha si se dijo. Si no se acordó nada, Sin dato.

feedback_closer: 3 viñetas. Una cosa que hizo bien y dos para mejorar, cada una
  con el momento de la llamada en que pasó. Concretas, sin adjetivos.

frases_marketing: hasta 3 frases textuales del lead que describan su problema
  o su deseo, entre comillas. Solo frases del lead, nunca del closer.

manejo_del_precio (opcional, lo pidió el líder comercial): "Valor antes que
  precio: Sí" o "No" + minuto en que se dijo el precio + cita textual del closer.
  Sí = antes del precio el closer resumió el dolor y el objetivo del lead y cómo
  lo resuelve el programa. Marcá también si las cuotas se ofrecieron como
  respuesta a "es caro" y si se ofreció algo que no existe (descuento, beca).
  Ejemplo: "No · min 12 · 'ya te adelanto, el programa no es barato' · cuotas
  ofrecidas como respuesta al precio".

# REGLAS
1. No inventes. Si un dato no aparece en la transcripción ni en los datos de
   entrada, el campo dice exactamente: Sin dato
2. Las citas van textuales, entre comillas, sin corregir ni resumir.
3. No incluyas datos de tarjetas, documentos ni información de salud del lead.
4. Respetá los largos máximos.
5. Castellano neutro, claro, sin jerga de ventas.
6. Solo cuenta la conversación con el lead. Todo lo que se dice después de que
   el lead se va ("abandonó la reunión", la despedida final) o antes de que
   entre se ignora. No lo uses en ningún campo.
```

## Campos de entrada

| Campo | De dónde sale |
|---|---|
| TRANSCRIPCION | Grabadora, paso 1 |
| CLOSER | Airtable · Agendas · `Closer (nombre)` (lookup de texto, no el vínculo) |
| CANAL | Airtable · Agendas · `Canal` |
| ESTADO_LEAD | Airtable · Agendas · `Estado del lead` |
| FECHA_LLAMADA | Grabadora · fecha de la reunión |

## Mapeo de salidas

| Salida | Marcador | Campo de Airtable | ¿Va al aviso? |
|---|---|---|---|
| nombre_lead | [[nombre_lead]] | — | Sí |
| resultado | [[resultado]] | — (lo actualiza el closer en `Estado del lead`) | Sí |
| perfil | [[perfil]] | — | No |
| situacion_actual | [[situacion_actual]] | — | No |
| deseo | [[deseo]] | — | No |
| dolor_principal | [[dolor_principal]] | `Dolor principal` | Sí |
| objeciones | [[objeciones]] | `Objeción principal` (solo la primera) | No |
| interes + motivo_interes | [[interes]] · [[motivo_interes]] | `Interés` | Sí |
| proximo_paso | [[proximo_paso]] | `Próximo paso` | Sí |
| feedback_closer | [[feedback_closer]] | — | No |
| frases_marketing | [[frases_marketing]] | `Frases del lead` | No |
| manejo_del_precio | [[manejo_del_precio]] | `Valor antes que precio` (Sí/No) | No |
| (del CRM) closer, canal, fecha | [[closer]] [[canal]] [[fecha_llamada]] | — | — |

## Aviso corto (el canal del equipo: Discord · #ventas)

```
📞 {{nombre_lead}} · {{closer}} · {{resultado}}
Interés: {{interes}}
Dolor: {{dolor_principal}}
Próximo paso: {{proximo_paso}}
Informe completo: {{link_documento}}
```

Cuatro líneas de contenido + link. Sin objeciones ni feedback en el canal (el feedback es para el closer y su líder, no para todo el equipo).

## Plan de prueba

| # | Transcripción de prueba | Qué revisar |
|---|---|---|
| 1 | Llamada completa con venta (de práctica, armada por el equipo) | Los 11 campos llenos; resultado = Venta; citas textuales que existen en el texto |
| 2 | Llamada floja: el lead casi no habla de plata ni de plazos | `situacion_actual` y `proximo_paso` dicen Sin dato en vez de inventar |
| 3 | Llamada cortada a los 8 minutos | La estructura se mantiene igual; nada de "el lead parece interesado" sin evidencia |
| 4 | Llamada donde el closer sigue conectado después de que el lead se va y habla con otro closer | Nada de esa parte aparece en los campos del lead |

**Criterio para darlo por bueno:** en las 3, ningún campo contiene algo que no esté en la transcripción o en los datos de entrada, y el líder comercial puede leer el informe sin abrir la grabación. Después de una semana en producción, revisar 5 informes al azar contra su grabación.
