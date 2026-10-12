# Recetas · n8n

> Referencia del Diseñador de Automatizaciones (RealOps™). Cargala cuando la plataforma elegida sea n8n. Salen de flujos que armamos y pusimos en producción en infonegocios (anonimizados) y de la documentación y las plantillas públicas de n8n (n8n.io/workflows). Los nombres de los nodos pueden cambiar entre versiones: si alguno no aparece así, buscá la función equivalente.

## Reglas de casa para n8n

1. **Un flujo de errores para todos.** Armá un flujo "00 · Alertas" con el disparador de error que avise al canal de operaciones qué flujo falló y qué quedó sin hacer. **n8n no se lo asigna solo a los flujos nuevos:** en la configuración de cada flujo, elegí "00 · Alertas" como flujo de errores. Sin eso, el flujo falla en silencio.
2. **Webhook antes que horario.** Un disparador programado cada 15 minutos son unas 2.900 ejecuciones por mes, encuentre algo o no. En un caso real, dos flujos que "preguntaban" en vez de "esperar el aviso" se llevaban el 80 % del consumo. Si la herramienta manda webhooks, usalos.
3. **No repetir (idempotencia).** Antes de crear, buscá si ya existe (por mail, por ID de la agenda, por ID del pago). Guardá el ID externo en la base. Así, si el webhook llega dos veces, no se crea dos veces.
4. **Esperas largas, no.** Un nodo de espera de 12 o 24 horas deja la ejecución abierta y se pierde si la instancia se reinicia. Mejor: varios disparadores programados, o un programado diario que busca "lo que vence hoy".
5. **Zona horaria en el flujo y en el disparador.** Configurala en los dos. Si el negocio trabaja con varios países, mostrá la hora del lead al lado.
6. **Credenciales en el gestor de n8n**, con el permiso mínimo (en Airtable, un token solo para esa base). Nunca en un nodo de código ni en una captura.
7. **No renombres el nodo disparador** de un flujo activo, y no importes el JSON a mano encima de uno que ya existe: puede perder credenciales o duplicar nodos. Cambiá solo los parámetros.
8. **Nombres numerados** ("01 · Agenda → CRM", "02 · Venta → Onboarding") y una nota adhesiva en cada flujo con qué hace, dueño y de qué depende.

## Recetas

### 1 · Agenda nueva → CRM → aviso al closer
`Webhook (de la agenda)` → `Code / Edit fields` (limpiar mail, traducir el canal de origen desde la UTM con una tabla) → `Airtable · Search` (por mail) → `IF` existe → `Update` / `Create` → `Airtable · Create` (oportunidad, etapa Agenda, con el ID de la cita) → `IF` cancelada o reprogramada → actualizar la misma oportunidad en vez de crear otra → mensaje al closer.
- **Ojo:** el setter que agendó sale del link (código en la UTM), no del calendario: el calendario dice de quién es la agenda, no quién hizo el trabajo. Si se deduce mal, se pagan comisiones que nadie ganó.
- Las preguntas del formulario de agenda se buscan por un fragmento del texto, porque se editan.

### 2 · Venta cerrada → verificación humana → alta
`Webhook / Form trigger` (formulario del closer) → guardar la venta con estado "Pendiente de verificar" (si ya existe ese ID, no hacer nada) → mensaje a quien verifica el cobro con dos botones **[✅ Entró la plata] [❌ No entró]** → al tocar ✅: crear el alumno, las cuotas, dar los accesos y mandar la bienvenida (sub-flujo) → aviso al equipo.
- Sirve cuando el founder "quiere aprobar todo": la aprobación queda en un toque, no en una conversación.
- Botones: Telegram, Discord o Slack los permiten. Por WhatsApp hace falta un proveedor de la API oficial.

### 3 · Avisos de cobro diarios
`Schedule` (todos los días 9:00) → `Airtable · Search` (cuotas que vencen en 3 días, vencidas hoy, vencidas hace 7 y 15) → `Code` (armar un mensaje por persona) → `IF` hay algo → mail al alumno con link de pago + resumen a la persona responsable de cobros.
- Una sola ejecución por día cubre todos los avisos: 30 ejecuciones por mes.

### 4 · Llamadas sin resultado a las 24 horas
`Schedule` (cada mañana) → buscar llamadas de ayer con fecha pasada y resultado vacío → `IF` hay → aviso a cada closer con su lista.
- Es la forma de que el CRM no quede con agujeros.

### 5 · Checks de onboarding a las 48 horas y a los 7 días
`Schedule` diario → alumnos con 48 h desde la compra y sin acceso → aviso a operaciones. Alumnos con 7 días y sin primera actividad → aviso al CSM + mail al alumno.

### 6 · Reporte de fin de día por formulario → base → resumen
`Webhook` (Tally, Typeform o formulario de n8n) → guardar en la tabla de EOD → mensaje al canal del equipo. Un segundo flujo programado a la noche junta los reportes del día y manda el resumen al founder (con un paso de IA si se quiere un resumen en 5 líneas).

### 7 · Transferencia recibida → cobro sugerido
`Gmail trigger` (filtro: mails del banco con "transferencia recibida") → `Code` (sacar monto, fecha y nombre) → buscar cuotas pendientes con ese monto → mensaje a quien concilia: "Entró US$1.100 de 'J. Marenco'. ¿Es la cuota 2 de Juan Marenco? [Sí] [No]".
- No marca nada como pagado solo: sugiere y una persona confirma.

### 8 · Reporte semanal al founder
`Schedule` (domingo a la noche) → consultas a la base (cobrado, ventas, asistencia, vencidas) → `Code` (armar el mensaje con números y una comparación con la semana anterior) → Telegram, mail o WhatsApp.

### 9 · Paso de IA (análisis de llamada, clasificación de leads)
`Webhook` (transcripción nueva) → `Airtable · Get` (datos del CRM que no están en la llamada: closer, etapa, monto) → nodo de IA (o agente) con salida estructurada → guardar cada dato en su campo → aviso. El prompt se escribe con **Prompt de IA para Automatizaciones**.

## Un flujo con ramas en vez de cinco flujos

Si tenés un onboarding por programa, no hagas un flujo por programa: un **catálogo** (tabla o nodo de código) que dice qué accesos, qué mail y qué plazos lleva cada programa, y un solo flujo que lo lee. Agregar un programa es agregar una fila, no un flujo.

## Plan de prueba en n8n

- Probá con el botón de ejecutar y un evento de prueba, apuntando a un canal y una base de prueba.
- Para webhooks, usá la dirección de prueba hasta que funcione y recién después la de producción.
- Activá el flujo nuevo y **apagá el anterior en el mismo momento** (si reemplaza a un Zap o a otro flujo). Nunca los dos prendidos: se duplica todo.
- Mirá las ejecuciones todos los días durante la primera semana.

Fuentes: flujos en producción y borradores validados de infonegocios (anonimizados), plantillas públicas de n8n (n8n.io/workflows) y documentación de n8n (docs.n8n.io).
