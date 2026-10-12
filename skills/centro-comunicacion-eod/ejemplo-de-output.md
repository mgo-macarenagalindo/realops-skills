# Ejemplo de output · Centro de Comunicación y Reporte de Fin de Día

> Datos ficticios. Mentoría de 4 meses de oratoria para profesionales, USD 1.900 en 3 cuotas, vendida por llamada. Equipo de 9: founder, 3 setters (2 outbound, 1 inbound), 2 closers, 2 coaches y 1 coordinadora de operaciones. Hoy trabajan en tres grupos de WhatsApp. Van a usar Slack. El CRM está en Airtable.

---

# Centro de comunicación · Mentoría de oratoria

## Mapa de canales

| Canal | Para qué | Qué no va acá | Quién lee |
|---|---|---|---|
| #anuncios | Decisiones y novedades. Solo escriben founder y coordinación | Conversaciones: se responde en hilo | Todos |
| #operaciones | Procesos, herramientas, accesos, pedidos internos | Temas de un cliente puntual | Todos |
| #ventas | Leads, llamadas, cierres y traspaso a servicio | Datos de tarjeta o de pago completos | Setters, closers, founder |
| #leads-del-dia | Un mensaje corto por agenda: quién es, de dónde viene, qué dijo | Conversación: se responde en hilo | Setters, closers |
| #servicio | Alumnos, alertas, bajas | Charlas personales con alumnos | Coaches, coordinación |
| #reportes-diarios | Solo los EOD y el resumen | Cualquier otra cosa | Coordinación, founder |
| #random | Lo que no es trabajo | Pedidos de trabajo | Todos |

## Reglas de urgencia

| Tipo | Por dónde | Respuesta esperada | Horario |
|---|---|---|---|
| Pedido de trabajo que puede esperar | Canal del área | Antes de las 24 h hábiles | Lunes a viernes, 9 a 18 |
| Algo trabado que frena una venta o a un alumno hoy | Canal del área con @mención | Menos de 2 h | Horario laboral |
| Urgente de verdad (se cae algo que no puede esperar a mañana: la plataforma no funciona, una clase en vivo sin link) | WhatsApp a coordinación | Lo antes posible | Cualquier horario |
| Doblemente urgente (un pago masivo rechazado, un problema público con un alumno) | Llamada a coordinación o founder | Inmediata | Cualquier horario |

Notificaciones de Slack apagadas fuera de horario para todo el equipo.

## EOD por rol

**Bloque común** (todos, 2 minutos):

1. ✅ ¿Qué hiciste hoy? (lo terminado, con resultado)
2. 🧱 ¿Qué quedó trabado y qué necesitás? (o "nada")
3. ➡️ ¿Qué hacés mañana? (1 a 3 cosas)
4. ¿Actualizaste el CRM? Sí / No → si es no, ¿por qué?
5. Horas trabajadas hoy
6. Energía del 1 al 5
7. Feedback del día: algo que mejorarías o que te trabó (opcional pero siempre visible)

**Setter**

| Campo | Outbound | Inbound |
|---|---|---|
| Mensajes nuevos | número | número |
| Ofertas enviadas | número | número |
| Links de agenda enviados | número | número |
| Agendas | número | número |

Más: objeciones que más escuchaste hoy (texto corto).

**Closer:** llamadas agendadas · asistidas · no-show · calificadas · cierres · reservas · links a las grabaciones · notas de traspaso cargadas (sí/no).

**Coach:** sesiones dadas · alumnos en riesgo detectados (y si se avisó a coordinación) · pausas o bajas pedidas.

**Coordinación de operaciones:** altas · bajas · cuotas vencidas avisadas · pedidos pendientes de otros.

## Cómo se junta solo

- **Herramienta:** Workflow Builder de Slack, disparador programado de lunes a viernes a las 18:00.
- **Pasos:** mensaje con botón a cada persona → formulario según su rol → publica la respuesta en #reportes-diarios.
- **Dónde se guarda:** además de publicarse, cada reporte se guarda en la tabla **EOD** de Airtable (un registro por persona por día, vinculado al rol). Para construir este paso, skill Diseñador de Automatizaciones.
- **Leads del día:** cuando el setter agenda, publica en #leads-del-dia: nombre de pila, canal de origen, qué le duele en una línea y si es outbound o inbound. Los closers no necesitan abrir el CRM de setters.

## Quién lo lee y qué recibe el founder

- **Coordinación** lee los EOD crudos a las 18:30 y destraba lo que puede.
- **El founder** recibe a las 19:00 en #reportes-diarios un resumen de un minuto. Prompt para armarlo con Claude (o automatizarlo más adelante):

```
Te paso los reportes de fin de día del equipo de hoy.
Armame un resumen para el founder que se lea en 1 minuto:
1. TRABADO: todo lo que está bloqueado, quién lo reportó y qué necesita. Va primero.
2. NÚMEROS: agendas por canal (outbound / inbound), llamadas asistidas, cierres.
3. HECHO: lo más importante, en 3 a 5 líneas.
4. OJO: quién no reportó, quién respondió "no" a la pregunta del CRM,
   energía de 2 o menos, y si dos personas dicen cosas que se contradicen.
Usá roles, no nombres. Sin adornos.
[pegá los reportes]
```

Ejemplo de resumen:

> **Trabado (1):** closer 2 espera que el founder confirme si puede ofrecer 4 cuotas a un lead que decide mañana.
> **Números:** 7 agendas (5 outbound, 2 inbound) · 6 llamadas asistidas · 2 cierres · 1 reserva.
> **Hecho:** 3 onboardings nuevos · 11 avisos de cuota enviados · clase grupal del jueves con 34 asistentes.
> **Ojo:** setter inbound respondió "no" al CRM ("se cayó la conexión del formulario") · coach 1 con energía 2 por tercer día seguido.

## Mantenimiento mensual

Primer lunes del mes, coordinación cruza la tabla EOD contra el CRM:
- Agendas reportadas por setters vs. agendas en el calendario.
- Sesiones reportadas por coaches vs. sesiones agendadas (de ahí sale el pago por sesión, si lo hay).
- Personas con "no" al CRM más de 3 veces en el mes: se habla en el 1 a 1.

## Anuncio al equipo

> 📌 Desde el lunes 26/10, el trabajo se habla en Slack.
> - Pedidos internos → #operaciones · Ventas → #ventas · Alumnos → #servicio · Novedades → #anuncios
> - Todos los días a las 18:00 llega el pedido de reporte: dos o tres minutos.
> - WhatsApp queda solo para urgencias de verdad (lo que se cae y no puede esperar a mañana).
> Las reglas de cada canal están en su descripción.

---

¿Querés la spec de la automatización para que el EOD se guarde solo en la base? Para construirla, usá la skill Diseñador de Automatizaciones. Y sostenelo dos semanas: si algo de trabajo llega por WhatsApp, respondé "¿lo pasás a #canal?". Si lo respondés ahí, WhatsApp sigue valiendo.
