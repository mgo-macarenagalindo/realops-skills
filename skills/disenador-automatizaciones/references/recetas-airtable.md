# Recetas · Automatizaciones nativas de Airtable

> Referencia del Diseñador de Automatizaciones (RealOps™). Cargala cuando la plataforma elegida sea Airtable. Salen de lo que armamos en clase y en negocios reales (anonimizados), más la documentación oficial de Airtable. Los nombres de los menús pueden cambiar: si algo no aparece así, buscá la función equivalente.

## Cómo está armada una automatización de Airtable

- **Disparador** (uno): cuando se crea un registro · cuando se actualiza · cuando entra en una vista · cuando cumple una condición · cuando se envía un formulario · a una hora programada · cuando llega un webhook · cuando se toca un botón · integraciones (Google, Outlook).
- **Acciones** (varias, en orden): crear registro · actualizar registro · buscar registros · enviar mail · ejecutar un script · mensajes a Slack, Teams, Google, Outlook y otras apps.
- **Grupos con condiciones**: un bloque de acciones que solo corre si se cumple algo ("si Programa = Premium…"). Es la forma de tener ramas sin hacer dos automatizaciones.
- **Repetir para cada registro**: después de "buscar registros", repetís una acción por cada uno (ej.: crear una sesión por cada alumno marcado).

## Siete trucos que evitan el 80 % de las fallas

1. **Una vista por automatización.** Si dispara con "entra en una vista", la vista se llama igual que la automatización ("🤖 Aviso cuota 3 días") y en la descripción dice "No tocar el filtro: la usa la automatización X".
2. **Esperar a que el registro esté completo.** Airtable no tiene una acción de espera. Si el registro lo carga una persona a mano, la automatización puede correr antes de que termine. Opciones: disparar con "cumple una condición" cuando el último campo obligatorio deja de estar vacío, o un paso de script con una espera corta al inicio (planes pagos).
3. **"Última modificación" con campos específicos.** Si usás un campo de última modificación como disparador (en Airtable o desde Zapier), configuralo para que mire **solo** el campo que importa. Si mira todos, cada edición dispara la automatización: en un caso real eso consumió el 44 % del plan de Zapier.
4. **Opciones cerradas, copiadas exactas.** Las condiciones comparan texto exacto: "Élite" no es "Elite". Copiá la opción desde el campo, no la tipees.
5. **Lookups para los mensajes.** Un campo vinculado manda el código del registro (`rec…`). Para un mail o un aviso, creá un lookup que traiga el nombre como texto y usá ese.
6. **Un campo de control para no repetir.** "Aviso enviado (fecha)" o una casilla "Procesado": la automatización lo completa y la vista lo excluye. Así nunca manda dos veces.
7. **El dueño, a la vista.** En la descripción de la automatización: qué hace, quién la mantiene y qué campos o vistas no se pueden renombrar.

## Recetas

### 1 · Venta → registro en Finanzas
**Cuándo:** el closer carga la venta y administración la vuelve a cargar en la tabla de ingresos.
- **Disparador:** registro creado en Ventas (o "cumple condición: Estado de pago = Confirmado", si se carga antes de cobrar).
- **Acciones:** crear registro en Finanzas con monto, fecha, medio de pago y vínculo a la venta. Actualizar la venta: "Pasado a finanzas = ✓".
- **Ojo:** si la venta se edita después (cambia el monto), esta automatización no se entera. Decidí si Finanzas toma el dato vinculado (lookup) en vez de copiarlo.

### 2 · Aviso de cuota 3 días antes del vencimiento
- **Vista:** "🤖 Vence en 3 días": Estado = Pendiente, Vencimiento = dentro de 3 días (o fórmula de días que faltan = 3), "Aviso previo enviado" vacío.
- **Disparador:** registro entra en la vista.
- **Acciones:** mandar el aviso por el canal que use el negocio (ver "Canal de aviso" abajo) con nombre, monto, fecha y link de pago. Actualizar "Aviso previo enviado" con la fecha.
- **Ojo:** en el plan gratis el mail solo llega a colaboradores de la base: no sirve para escribirle al alumno. Ahí el aviso va a la persona responsable de cobros, que lo manda por WhatsApp con un mensaje ya armado, o se hace desde Zapier o n8n.

### 3 · Cuota vencida → responsable y tarea
- **Disparador:** cumple condición: Estado = Vencida y Responsable vacío.
- **Acciones:** asignar el responsable de cobros (rol, desde una tabla de Roles, no un nombre tipeado). Crear tarea "Cobrar cuota X" con fecha a 1 día. Aviso a la persona.
- **Escalado:** dos vistas más, "Vencida hace 7 días" y "Vencida hace 15 días", cada una con su automatización (aviso al responsable y, a los 15, al founder).

### 4 · Lead sin contactar a las 24 horas
- **Campo fórmula:** horas desde el ingreso (`DATETIME_DIFF(NOW(), {Fecha de ingreso}, 'hours')`).
- **Vista:** "🤖 Sin contactar 24 h": Estado = Nuevo y horas ≥ 24.
- **Disparador:** registro entra en la vista. **Acción:** aviso al setter asignado y a quien coordina ventas.
- **Ojo:** las fórmulas con NOW() se recalculan cada cierto tiempo, no al segundo. Para "24 horas" alcanza.

### 5 · Formulario de reporte de fin de día → registros vinculados
**Cuándo:** el coach carga su reporte y marca a qué alumnos vio hoy; alguien después crea una sesión por alumno a mano.
- **Disparador:** formulario enviado (o registro creado en EOD).
- **Acciones:** buscar los alumnos marcados → repetir para cada uno → crear registro en Sesiones vinculado al alumno y al EOD.
- En un negocio real, esta automatización creó más de 1.000 sesiones en menos de 5 segundos cada una, sin que nadie las cargue.

### 6 · Formulario de inicio del alumno → ficha + aviso al coach
- **Disparador:** formulario enviado.
- **Acciones:** buscar al alumno por mail → actualizar su ficha con las respuestas → aviso al coach asignado con el resumen.
- **Ojo:** si el mail no coincide (el alumno usó otro), la búsqueda no encuentra nada. Agregá un grupo con condición "si no encontró" que avise a operaciones.

### 7 · Webhook entrante (agenda o pago desde otra app)
**Cuándo:** la agenda o la pasarela pueden mandar un aviso (webhook) y querés evitar Zapier.
- **Disparador:** cuando llega un webhook. Airtable te da una dirección; esa dirección se pega en la otra herramienta.
- **Acciones:** buscar el contacto por mail → crear o actualizar → crear la oportunidad.
- **Ojo:** necesitás que la otra herramienta mande webhooks (verificalo) y el formato que llega. Probá con un evento real de prueba antes de mapear.

### 8 · Paso de IA dentro de Airtable
Para resumir, clasificar o analizar un texto (transcripción, respuesta de formulario), Airtable tiene campos y agentes de IA según el plan. El prompt lo escribís con la skill **Prompt de IA para Automatizaciones**: datos de entrada, un campo de salida por dato y la regla de no inventar.

## Canal de aviso (no asumas Slack)

| El negocio usa… | Desde Airtable nativa |
|---|---|
| Slack o Teams | Acción nativa de mensaje |
| Mail | Acción "Enviar un mail" (en el plan gratis, solo a colaboradores) |
| WhatsApp | Airtable no lo manda solo. Opciones: mail a la persona responsable con el mensaje listo para copiar y pegar, una interfaz con botón "Abrir WhatsApp" (link `wa.me` con el texto armado), o sumar Zapier, Make o n8n con un proveedor de WhatsApp |
| Discord o Telegram | Con script y webhook (planes pagos) o desde Zapier, Make o n8n |

## Cuándo NO usar Airtable nativa

- El volumen supera las corridas del plan (calculalo: un formulario con 50 leads por semana son unas 215 corridas por mes, más del doble del plan gratis).
- Hace falta escribirle a personas de afuera desde el plan gratis.
- El flujo une 3 o más herramientas externas, o necesita IA con lógica, aprobaciones con botón o reintentos.

Fuentes: clases de RealOps™ (Airtable vs. Notion, automatización financiera en vivo, campos de IA, vistas y disparadores), auditorías de bases reales (anonimizadas) y la documentación de automatizaciones de Airtable (support.airtable.com).
