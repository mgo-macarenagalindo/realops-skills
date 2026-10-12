# Casos de uso · Diseñador de Automatizaciones

Tres situaciones de infonegocio donde esta skill te evita armar el flujo equivocado. Negocios y nombres ficticios.

---

## 1. Tu primera automatización: agenda nueva → CRM → aviso

**La situación.** En un programa high ticket, cada vez que alguien agenda una llamada, el setter copia los datos de la agenda al CRM y le avisa al closer por WhatsApp. 25 agendas por semana, 4 minutos cada una.

**Qué le pasás.** Las herramientas (agenda, Airtable, Slack) y que van a usar n8n.

**Qué te devuelve.** La spec: evento nuevo en el calendario → buscar contacto por mail en Airtable → crear o actualizar → crear la oportunidad en etapa Agenda → avisar al closer en Slack. Con el mapeo de campos, qué pasa si el mail viene vacío y la guía nodo por nodo.

**Por qué sirve.** Es chica, se prueba en una tarde y ahorra más de 6 horas por mes. Es la Actividad 13 del programa.

---

## 2. Onboarding automatizado: de la venta al primer día adentro

**La situación.** Cuando se confirma una venta, alguien da accesos, manda la bienvenida y le avisa al equipo de servicio. A veces tarda 3 días. Los alumnos escriben "¿y ahora qué hago?".

**Qué le pasás.** El SOP del onboarding (si no lo tenés, la skill te frena y te manda primero a escribirlo) y las herramientas.

**Qué te devuelve.** La spec separando lo que se automatiza (alta en CRM de servicio, acceso a la comunidad, mail de bienvenida, aviso al coach) de lo que sigue siendo humano (la llamada de bienvenida). Plan de prueba con un cliente de prueba y medición del tiempo del pago al primer acceso.

**Por qué sirve.** Es el proceso que todo negocio de programas hace a mano y donde pierde gente. Es la Actividad 16.

---

## 3. Aviso de cuota y recordatorios de llamada

**La situación.** Una membresía con un programa premium en cuotas. La asistencia a las llamadas de venta está en 38 % y las cuotas se vencen sin aviso.

**Qué le pasás.** Que el negocio ya usa Zapier y no quiere sumar otra herramienta.

**Qué te devuelve.** Dos flujos en Zapier (respetando lo que el negocio ya usa): el aviso 3 días antes de cada vencimiento y la secuencia de 4 recordatorios de llamada (al agendar, 24 h antes con un recurso, a primera hora y 1 h antes). Con el filtro de "qué automatizar primero": empezar por los recordatorios, que mueven la asistencia.

**Por qué sirve.** Te enseña a decidir con criterio, no con la herramienta que te gusta. Y a ordenar por impacto.
