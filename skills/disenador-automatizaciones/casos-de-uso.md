# Casos de uso · Diseñador de Automatizaciones

Cuatro situaciones de infonegocio donde esta skill te evita armar el flujo equivocado, o en la herramienta equivocada. Negocios y nombres ficticios.

---

## 1. Tu primera automatización: agenda nueva → CRM → aviso

**La situación.** En un programa high ticket, cada vez que alguien agenda una llamada, el setter copia los datos de la agenda al CRM y le avisa al closer por WhatsApp. 25 agendas por semana, 4 minutos cada una. El proceso no está escrito, pero es un pasaje de datos sin criterio.

**Qué le pasás.** Las herramientas (agenda, Airtable, WhatsApp), que van a usar n8n y a nombre de quién está cada cuenta.

**Qué te devuelve.** La spec en n8n (la spec hace de SOP): webhook de la agenda → buscar contacto por mail → crear o actualizar → oportunidad en etapa Agenda con el ID de la cita (así una reprogramación no duplica) → aviso al closer por el canal que ya usan. Con el flujo de errores asignado, el costo en ejecuciones y la guía nodo por nodo.

**Por qué sirve.** Es chica, se prueba en una tarde y ahorra más de 6 horas por mes. Es la Actividad 13 del programa.

---

## 2. Cuotas: ¿Airtable sola, Zapier o n8n?

**La situación.** Las cuotas viven en Airtable. Hay 30 vencidas y nadie sabe a quién le toca cobrar. La coordinadora pregunta si hace falta pagar Zapier.

**Qué le pasás.** El plan de Airtable, cuántas cuotas vencen por mes y por dónde se avisa el equipo.

**Qué te devuelve.** La decisión con números: el responsable, la tarea y el escalado a 7 y 15 días van con **automatizaciones nativas de Airtable** (todo pasa adentro de la base). El aviso al alumno por mail depende del plan (en el gratis, el mail solo llega a colaboradores), así que te muestra las dos salidas: mensaje listo para WhatsApp desde una interfaz, o un flujo diario en n8n que gasta 30 ejecuciones por mes.

**Por qué sirve.** Te enseña a no sumar una herramienta cuando la base ya alcanza, y a ver el límite del plan antes de que te frene.

---

## 3. Onboarding automatizado: de la venta al primer día adentro

**La situación.** Cuando se confirma una venta, alguien da accesos, manda la bienvenida y le avisa al equipo de servicio. A veces tarda 4 días, porque el founder quiere aprobar cada alta.

**Qué le pasás.** El SOP del onboarding (si no lo tenés y el proceso tiene criterio, la skill te manda primero a escribirlo) y las herramientas.

**Qué te devuelve.** Un solo flujo en n8n con un catálogo por programa (no un flujo por programa), la aprobación del founder convertida en un botón de "✅ Entró la plata" y la medición del tiempo del pago al primer acceso. Para el diseño completo, deriva a **Onboarding de Cliente Automatizado**.

**Por qué sirve.** Es el proceso que todo negocio de programas hace a mano y donde pierde gente. Es la Actividad 16.

---

## 4. Recordatorios de llamada en un negocio que ya paga Zapier

**La situación.** La asistencia a las llamadas de venta está en 62 %. El negocio ya paga Zapier y no quiere sumar otra herramienta.

**Qué le pasás.** La agenda que usan y el plan de Zapier.

**Qué te devuelve.** Primero, revisar los recordatorios nativos de la agenda (no gastan tareas). Si no alcanzan, la secuencia en Zapier (al agendar con un recurso, 24 h antes, a primera hora y 1 h antes) con el cálculo de tareas por mes. Y la siguiente por impacto: la alerta de "llamada sin resultado a las 24 horas".

**Por qué sirve.** Te enseña a decidir con criterio, no con la herramienta que te gusta, y a ordenar por impacto.
