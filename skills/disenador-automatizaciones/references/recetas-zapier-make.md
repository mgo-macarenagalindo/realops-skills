# Recetas · Zapier (y equivalencias en Make)

> Referencia del Diseñador de Automatizaciones (RealOps™). Cargala cuando el negocio ya use Zapier o Make. Salen de los Zaps que armamos y auditamos en clase y en negocios reales (anonimizados), y de la ayuda oficial de Zapier y Make. Los nombres de las opciones pueden cambiar: si algo no aparece así, buscá la función equivalente.

## Reglas de casa para Zapier

1. **Cuenta del negocio.** El Zap, sus conexiones y los mails de error tienen que estar a nombre de un mail del negocio. Si están a nombre de una persona, el día que se va nadie puede ver el historial ni arreglar nada.
2. **Carpetas y nombres numerados desde el día uno:** "01 · Agenda → CRM", "02 · Venta → Onboarding". Ayuda a auditar y a no duplicar.
3. **Buscar antes de crear.** En Airtable, usá "Find record" con la opción de crear si no existe. Así un reenvío no duplica.
4. **Registro de prueba completo.** Zapier solo reconoce los campos que vinieron con dato en la prueba. Si agregás una pregunta al formulario, cargá un registro con todo y volvé a traerlo.
5. **Rutas (Paths) con valores copiados**, no tipeados. Un acento distinto y la ruta nunca se cumple, y el Zap igual dice "éxito".
6. **Lookups de texto** para los campos vinculados de Airtable (si no, llega `rec…`).
7. **Delay al inicio si el registro se carga a mano** ("Delay for" 5 minutos), para que la persona termine de completar los campos.
8. **Mensajes a Discord de menos de 2.000 caracteres.** Si se pasa, el paso falla entero: partilo en dos pasos o mandá lo clave y dejá el resto en la base.
9. **Webhooks de Discord**: la dirección del webhook es una clave (quien la tiene puede publicar). No la pegues en capturas ni documentos.
10. **Programados de lunes a viernes**: "Every Week" con los días marcados, no "Every Day". Para probar, ponelo a pocos minutos.
11. **Calculá las tareas**: cada paso de acción que sale bien es una tarea. Filtros, rutas, Formatter y Delay no cuentan (confirmalo en tu historial).

## Recetas

### 1 · Formulario de aplicación → lead en Airtable con setter asignado
`Typeform / Tally / formulario de la landing · New entry` → `Formatter · Lookup table` (traducir la fuente o la UTM a un canal legible) → `Paths` por regla de asignación → `Airtable · Find or create record` (Leads, por mail) → aviso al setter.
- **La regla de asignación vive en una tabla de la base** ("Setters activos" con casilla Activo), no tipeada en el Zap. Si alguien se va, se destilda y listo.
- Si la regla es "en rueda", la forma sin código es un número en la base que se incrementa, o asignar en la base con una automatización nativa. Si es "por fuente", escribilo como regla, no como costumbre.

### 2 · Agenda de Calendly → llamada en Airtable → aviso al closer
`Calendly · Invitee Created` (a nivel organización si hay más de un closer o más de un tipo de evento) → `Filter` (no seguir si es una reprogramación: el campo de invitado anterior existe) → `Airtable · Find record` (Leads, por mail) → `Airtable · Create record` (Llamadas, vinculada al lead, con el ID del evento) → aviso al closer con las notas del setter.
- **Reprogramaciones:** Calendly las toma como evento nuevo. Con el filtro de arriba no se duplican; un segundo Zap ("Invitee Canceled" + nuevo evento) actualiza la llamada existente.
- **El closer:** sale del dueño del evento. Si la agenda es rotativa, verificá que el dato llega.

### 3 · Venta en Airtable → mail de bienvenida por programa
`Airtable · New record in view` (vista "🤖 Ventas para onboarding") → `Delay` 5 min → `Paths` por programa → `Gmail · Send email` (HTML armado con Claude) → `Airtable · Update` (Bienvenida enviada = ✓).

### 4 · Dos recordatorios de una clase en un solo Zap
`Schedule · Every Week` (la noche anterior) → `Webhook POST` a Discord con el aviso → `Delay for` 12 h → segundo `Webhook POST` con el link. Con un link de Zoom recurrente no se rompe. `@everyone` funciona; las menciones a roles, no siempre.

### 5 · Recordatorios de llamada para bajar el no-show
`Calendly · Invitee Created` → mensaje al lead al agendar (confirmación + un recurso) → `Delay until` 24 h antes → recordatorio → `Delay until` el día a primera hora → `Delay until` 1 h antes con el link.
- Si la agenda tiene recordatorios propios (Calendly, GoHighLevel), **usá esos primero**: no gastan tareas.
- Por WhatsApp hace falta un proveedor de la API oficial; si no hay, mail + SMS o el recordatorio nativo de la agenda.

### 6 · Paso de IA
`New record` (transcripción) → `AI by Zapier` o el paso de IA del proveedor → `Airtable · Update` (un campo por dato). El prompt se escribe con **Prompt de IA para Automatizaciones**, pasándole los datos del CRM que no están en la llamada.

### 7 · Sub-Zaps para no repetir pasos
Si cinco Zaps terminan con "avisar en el canal de ventas con este formato", hacé un Sub-Zap "Avisar a ventas" y llamalo desde los cinco. Cambiar el formato es cambiarlo una vez.

## Equivalencias en Make

| Zapier | Make |
|---|---|
| Zap | Escenario |
| Paths | Router (con filtros en cada ruta) |
| Filter | Filtro entre módulos |
| Formatter | Funciones de texto, fecha y número dentro del módulo |
| Delay | Sleep (corto) o un segundo escenario programado (largo) |
| Storage / Tables | Data store |
| Sub-Zap | Escenario llamado por webhook |
| Loop | Iterador + agregador |

En Make, **cada módulo que corre consume**, y un escenario programado consume aunque no haya datos nuevos. Si la app tiene disparador instantáneo (o manda webhooks a un "Custom webhook"), usalo. Configurá un manejador de errores en los módulos críticos (reintentar o ignorar y avisar).

## Cuándo pasar de Zapier a n8n

- Las tareas del mes superan el plan con frecuencia, o un solo Zap se lleva más de la mitad.
- Hay más de 10 Zaps que hacen variantes de lo mismo (uno por programa, uno por calendario).
- Hace falta código, IA con lógica o aprobaciones con botón.
- **La migración:** inventario primero (Detective de Automatizaciones), construir en n8n, probar con un canal de prueba, **activar n8n y apagar el Zap en el mismo momento**, y mirar la primera semana. Nunca los dos prendidos.

Fuentes: clases de RealOps™ (Zapier con Airtable y Discord, rutas, recordatorios, UTMs, reprogramaciones de Calendly), auditorías de cuentas de Zapier reales (anonimizadas), ayuda oficial de Zapier (help.zapier.com) y comunidad y ayuda de Make.
