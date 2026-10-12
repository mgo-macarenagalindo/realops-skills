# Ejemplo de output · Centro de Comunicación y Reporte de Fin de Día

> Datos ficticios. Mentoría de 4 meses de oratoria para profesionales, USD 1.900 en 3 cuotas, vendida por llamada. Equipo de 10: founder (que también da las clases grupales), 3 setters (2 outbound, 1 inbound), 2 closers (no cobran: el link de pago lo manda coordinación), 2 coaches, 1 coordinadora de operaciones y cobros, y 1 editora freelance por pieza. Hoy trabajan en tres grupos de WhatsApp. Van a usar Slack. El CRM está en Airtable, en una cuenta del negocio. Objetivo del trimestre: pasar de 9 a 14 ventas por mes sin sumar closers.

---

# Centro de comunicación · Mentoría de oratoria

**Herramienta: Slack (plan gratis), como reemplazo de los tres grupos.** El founder lo aceptó porque se archivan los grupos y no suma costo. Antes de anunciarlo, verificá en la página de precios de Slack que el plan gratis incluya el Workflow Builder.

## Paso 0 · Lo que se resuelve antes

- El espacio de Slack se crea con **operaciones@mentoriaoratoria.example** (cuenta del negocio), no con el mail de nadie. Admins: coordinación y founder.
- El formulario de la editora y la planilla de EOD también van en esa cuenta.

## EOD por rol

Estándares para todos: todos los días hábiles a la hora de cierre de cada rol, energía del 1 al 10, feedback que aporte criterio (no "día tranqui"). Big Rock en los roles que manejan su agenda.

**🌙 EOD Setter** (los 3, a las 18:30)

```
🌙 EOD Setter
👤 Nombre:
📅 Fecha:
🧲 Mensajes inbound:
📲 Mensajes outbound:
🟠 Seguimientos enviados:
🟢 Respuestas a seguimientos:
🟢 Ofertas enviadas:
🔴 Links de agenda enviados:
☎️ Agendas inbound:
☎️ Agendas outbound:
📋 ¿Actualizaste el CRM? Sí / No (si es no, por qué):
🔋 Nivel de energía (1–10):
🗣️ Feedback del día:
```

| Cambio vs. el modelo | Por qué | Quién lo mira |
|---|---|---|
| + ¿Actualizaste el CRM? | Los setters cargan cada lead en Airtable | Coordinación |
| La setter inbound deja en 0 las líneas outbound | Un solo formulario para los tres, sin campos vacíos que confundan | — |

**🌙 EOD Closer** (al terminar su última llamada, antes de las 21)

```
🌙 EOD Closer
👤 Nombre:
📅 Fecha:
☎️ Agendadas:
✅ Asistidas:
🔴 No show:
🟡 Reagendadas:
🟠 Canceladas:
🟢 Llamadas calificadas:
🔁 Seguimientos realizados hoy:
💸 Cierres:
📋 ¿Cargaste el resultado de cada llamada en el CRM? Sí / No (si es no, por qué):
🔋 Nivel de energía (1–10):
🗣️ Feedback del día:
💻 Links de llamadas:
```

| Cambio vs. el modelo | Por qué |
|---|---|
| − Reservas | En este negocio no existen |
| − Recolectado hoy | El closer no cobra: lo reporta coordinación |

**🌙 EOD Coach** (los 2, a las 18:30)

```
🌙 EOD Coach
👤 Nombre:
📅 Fecha:
🙋 Sesiones asistidas hoy:
📲 Seguimientos fuera de sesión:
⚠️ Alumnos en riesgo detectados (y a quién se avisó):
🪨 Big Rock del día:
✅ Tareas realizadas:
⏱️ Horas trabajadas:
🔋 Nivel de energía (1–10):
🗣️ Feedback del día:
```

+ Alumnos en riesgo: hay semáforo en el CRM y los coaches son los primeros en verlo. Lo mira coordinación.

**🌙 EOD Coordinación** (extensión, a las 18:30)

```
🌙 EOD Coordinación
👤 Nombre:
📅 Fecha:
🆕 Altas del día (pagos acreditados):
🔑 Accesos habilitados hoy / pendientes (con días de espera):
💵 Cuotas cobradas hoy:
📨 Avisos de cuota vencida enviados:
🪨 Big Rock del día:
🚧 Pendiente de otros (qué y de quién):
📋 ¿Actualizaste el CRM? Sí / No (si es no, por qué):
⏱️ Horas trabajadas:
🔋 Nivel de energía (1–10):
🗣️ Feedback del día:
```

**Founder:** no lleva EOD de ventas ni de servicio. Si quiere dar el ejemplo, el de Operaciones (Big Rock, tareas, bloqueos, energía, feedback).

**📦 Editora (por entrega, sin EOD diario):** reporta cada pieza en #contenido con la plantilla de entrega (qué entregó, link en la carpeta del negocio, qué falta, qué necesita).

Ejemplo de Big Rock bien escrito (coach): *"Llamar a los 3 alumnos en rojo del mes 2 y dejar fecha de sesión de recuperación"*. Atado al objetivo del trimestre: menos bajas, más renovaciones. Mal escrito: *"Avanzar con alumnos"*.

## Mapa de canales

| Canal | Para qué | Qué no va acá | Quién está |
|---|---|---|---|
| #anuncios | Decisiones y novedades. Solo escriben founder y coordinación | Conversaciones | Todos |
| #operaciones | Procesos, herramientas, accesos, pedidos internos | Temas de un alumno puntual | Todos menos la editora |
| #ventas | Cierres, dudas de calificación, objeciones que se repiten | Datos de tarjeta | Setters, closers, founder, coordinación |
| #leads-del-dia | Un mensaje por agenda, formato fijo | Conversación fuera del hilo | Setters, closers |
| #servicio | Alumnos, alertas, bajas | Temas de pago | Coaches, coordinación, founder |
| #cobros-y-accesos | Cuotas, pagos rechazados, altas a la plataforma | Discutir con un alumno por qué no pagó | Coordinación, founder |
| #contenido | Pedidos y entregas a la editora | Claves | Founder, editora, coordinación |
| #reportes-diarios | Solo EOD y resumen | Cualquier otra cosa | Todos publican; leen coordinación y founder |
| #random | Lo que no es trabajo | Pedidos | Todos |

## Leads del día

Formato fijo, un mensaje por agenda, y la charla en hilo:

```
📞 Jue 18 h · Laura · IG orgánico · factura USD 3-5k · ¿calificada? Sí · "me trabo cuando presento a clientes" · setter: M
```

## Reglas de urgencia

| Tipo | Por dónde | Respuesta esperada | Horario |
|---|---|---|---|
| Pedido que puede esperar | Canal del área | 24 h hábiles | Lunes a viernes, 9 a 18 |
| Algo trabado que frena una venta o a un alumno hoy | Canal del área con @mención | Menos de 2 h | Horario laboral |
| Urgente de verdad (no anda el link de la clase en vivo) | WhatsApp por privado a coordinación | Lo antes posible | Cualquier horario |
| Doblemente urgente (pagos rechazados en masa, un problema público con un alumno) | Llamada a coordinación o founder | Inmediata | Cualquier horario |

## Cómo se junta solo

- **Workflow Builder**, lunes a viernes: 18:30 para setters, coaches y coordinación; 20:45 para closers. Cada workflow abre el formulario de su rol y publica en #reportes-diarios.
- **Dónde se guarda:** además de publicarse, un registro por persona por día en la tabla **EOD** de Airtable, vinculado a la persona. Para construir ese paso: **Diseñador de Automatizaciones**.

## Quién lo lee y qué recibe el founder

Coordinación lee los EOD a las 9:00 del día siguiente (así entran los de los closers) y destraba lo que puede. El founder recibe a las 9:30 un resumen de un minuto. Prompt:

```
Te paso los EOD de ayer del equipo de la mentoría de oratoria.
Armame un resumen para el founder que se lea en 1 minuto:
1. TRABADO: lo bloqueado, quién lo reportó y qué necesita. Primero.
   Si espera una decisión del founder, marcalo "DECIDE FOUNDER".
2. NÚMEROS: agendas (outbound / inbound), asistidas, no show, cierres;
   sesiones dadas; cuotas cobradas y avisos de vencida.
3. BIG ROCKS: cuáles se cumplieron y cuáles no (y por qué, si lo dijeron).
4. OJO: quién no reportó, "no" al CRM, energía de 4 o menos,
   y números que no coinciden entre roles (agendas del setter vs. del closer).
Usá roles, no nombres de alumnos. No inventes números que no estén en los EOD.
[pegá los EOD]
```

> **Trabado (1):** closer 2 espera que el founder confirme si puede ofrecer 4 cuotas a un lead que decide hoy — DECIDE FOUNDER.
> **Números:** 7 agendas (5 outbound, 2 inbound) · 6 asistidas · 1 no show · 2 cierres · 14 sesiones · 3 cuotas cobradas, 4 avisos de vencida.
> **Big Rocks:** coach 1 llamó a los 3 alumnos en rojo ✅ · coordinación no terminó la conciliación de septiembre (se cayó Stripe) ❌.
> **Ojo:** setter inbound respondió "no" al CRM · coach 2 con energía 3 por tercer día seguido · setters reportan 7 agendas y closers 6 agendadas: revisar cuál no llegó.

## Mantenimiento mensual

Primer lunes del mes, coordinación cruza la tabla EOD con el CRM: agendas de setters contra el calendario de closers, sesiones de coaches contra las agendadas (de ahí sale su pago), cierres contra ventas. Personas con "no" al CRM más de 3 veces: se habla en el 1 a 1. Cada trimestre: campo que nadie miró, se saca.

## Anuncio al equipo

> 📌 Desde el lunes 26/10, el trabajo se habla en Slack.
> - Pedidos internos → #operaciones · Ventas → #ventas · Alumnos → #servicio · Pagos y accesos → #cobros-y-accesos · Novedades → #anuncios
> - Cada día te llega el pedido de tu reporte, según tu rol: dos o tres minutos.
> - WhatsApp queda solo para urgencias de verdad, por privado a coordinación.
> Los grupos de WhatsApp de trabajo se archivan el viernes 30/10.

## Para confirmar

Nada para confirmar: la persona dio roles, herramienta, CRM, tipo de setters y quién cobra. Antes de anunciarlo, verificá que el plan gratis de Slack incluya el Workflow Builder.

---

¿Querés la spec de la automatización para que el EOD se guarde solo en la base? Para construirla, usá la skill Diseñador de Automatizaciones. Y sostenelo dos semanas: si algo de trabajo llega por el grupo viejo, respondé "¿lo pasás a #canal?". Si lo respondés ahí, el grupo viejo sigue valiendo.
