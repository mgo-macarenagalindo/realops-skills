# Ejemplo de output · Diseñador de Automatizaciones

> Datos ficticios. Programa de 4 meses de coaching para abogados independientes, vendido por llamada. Agenda en Google Calendar, CRM en Airtable, equipo en Slack. Unas 22 agendas por semana.

---

# Automatización · Agenda nueva al CRM

**En una frase:** Cuando alguien agenda una llamada de venta en el calendario del equipo, se crea o actualiza el contacto y la oportunidad en Airtable y se avisa al closer en Slack, para que nadie copie datos a mano y el closer llegue a la llamada sabiendo de dónde vino el lead.

**Herramienta:** n8n (alternativa: Zapier, con la misma lógica) · **Dueño:** Operaciones · **Ahorro estimado:** 22 agendas × 4 min × 4 semanas ≈ **6 h por mes**, y cero oportunidades sin cargar.

## 1. Disparador

Evento nuevo en el calendario "Llamadas de venta" (Google Calendar). Sólo eventos cuyo título empiece con "Llamada ·" (así se excluyen reuniones internas).

## 2. Pasos

1. **Calendario** · Detectar evento nuevo en "Llamadas de venta".
2. **Filtro** · Seguir sólo si el título empieza con "Llamada ·" y tiene un invitado externo.
3. **Extraer datos** · Nombre, mail y respuestas del formulario de la agenda (vienen en la descripción del evento), fecha y hora, closer asignado (dueño del calendario o campo del formulario), canal de origen (el link de agenda usado: ver mapeo).
4. **Airtable · Buscar** en Contactos por mail.
   - Si existe → **actualizar** teléfono si cambió.
   - Si no existe → **crear** el contacto.
5. **Airtable · Crear** oportunidad vinculada al contacto, etapa = Agenda.
6. **Slack** · Mensaje al closer en #agendas: nombre, fecha y hora, canal de origen, respuesta a "¿qué te gustaría resolver?" y link a la oportunidad.

## 3. Mapeo de campos

| Origen (evento del calendario) | Destino (Airtable) | Transformación |
|---|---|---|
| Invitado · mail | Contactos · Mail | minúsculas, sin espacios |
| Invitado · nombre | Contactos · Nombre | |
| Descripción · "Teléfono" | Contactos · Teléfono | sólo números, con código de país |
| Inicio del evento | Oportunidades · Fecha de llamada | zona horaria del negocio |
| Descripción · "¿Qué te gustaría resolver?" | Oportunidades · Motivo de consulta | texto |
| Link de agenda usado (tipo de evento) | Oportunidades · Canal de origen | "Llamada · IG" → Instagram · "Llamada · Ads" → Pauta · "Llamada · Ref" → Referido · otro → Sin dato |
| Dueño del calendario | Oportunidades · Closer | buscar colaborador por mail |

## 4. Prompt de IA

No hace falta. (Si más adelante se quiere un resumen del formulario para el closer, se agrega un paso de IA con salida de máximo 3 líneas y la regla de no agregar nada que no esté en las respuestas.)

## 5. Si algo falla

| Falla | Qué hace el flujo | Quién se entera |
|---|---|---|
| El evento no tiene mail de invitado | No crea nada; manda aviso a #operaciones con el link del evento | Operaciones |
| Airtable no responde | Reintenta 3 veces cada 5 minutos; si sigue fallando, aviso a #operaciones | Operaciones |
| El contacto existe dos veces con el mismo mail | Usa el más reciente y avisa para limpiar el duplicado | Operaciones |
| El evento se reprograma | Este flujo no lo toma (es sólo para eventos nuevos). Se agrega un segundo flujo en una etapa 2 | — |

## 6. Plan de prueba

1. Crear una agenda de prueba con tu propio mail desde cada link (IG, Ads, Ref) y verificar el canal de origen en Airtable.
2. Agendar dos veces con el mismo mail: tiene que actualizar el contacto y crear **dos** oportunidades.
3. Crear un evento interno ("Reunión de equipo"): no tiene que pasar nada.
4. Agendar sin teléfono: el contacto se crea igual, con el teléfono vacío.
5. Verificar que el mensaje de Slack llegue al closer correcto.

## 7. Guía de armado (n8n, nodo por nodo)

1. **Disparador de Google Calendar** · evento creado · calendario "Llamadas de venta".
2. **IF** · título empieza con "Llamada ·" **y** hay invitado externo.
3. **Set / Edit fields** · arma los campos limpios (mail en minúsculas, canal de origen según el tipo de evento).
4. **Airtable · Search** · tabla Contactos · fórmula de búsqueda por mail.
5. **IF** · ¿encontró registro?
   - Sí → **Airtable · Update** (Contactos).
   - No → **Airtable · Create** (Contactos).
6. **Merge** · junta las dos ramas para seguir con el ID del contacto.
7. **Airtable · Create** · tabla Oportunidades, vinculada al contacto, etapa = Agenda.
8. **Slack · Send message** · canal #agendas, con mención al closer.
9. **Error workflow** · un flujo aparte que avisa a #operaciones si cualquier nodo falla.

Los nombres de los nodos pueden variar según la versión de n8n: si alguno no aparece así, buscá la función equivalente. Las credenciales de Google, Airtable y Slack se cargan en el gestor de credenciales de n8n, con el permiso mínimo (en Airtable, un token sólo para esta base).

## 8. Cómo apagarla

En n8n, abrir el flujo "Agenda nueva al CRM" y desactivarlo (interruptor de activo). Mientras esté apagada, los setters vuelven a cargar a mano con la plantilla de siempre.

---

¿La armamos juntos nodo por nodo? Cuando funcione, documentala con la skill Constructor de SOP de Infonegocio (modo automatización).
