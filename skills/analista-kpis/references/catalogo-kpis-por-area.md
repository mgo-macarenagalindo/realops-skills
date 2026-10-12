# Catálogo de KPIs por área · infonegocios

> Referencia de la skill **Analista de KPIs** (RealOps™). No es para medir todo: es el menú del que elegís. Para cada área, empezá por la fila marcada **★** (la mínima) y sumá las demás sólo si hay dato y alguien va a decidir con ellas. Los valores de alarma de las fichas son **orientativos** (criterio de MG Operations), salvo asistencia y los dos cierres, que salen de clase: ajustalos a la tendencia de cada negocio.

Cada KPI trae: **qué pregunta responde · cómo se calcula · de dónde sale · qué decisión dispara.** Si un número no dispara ninguna decisión, no va al tablero.

---

## 1 · Marketing y canal o fuente de adquisición

Todo se corta **por canal** (pauta, Instagram orgánico, YouTube, referidos, WhatsApp, lanzamiento) y, en pauta, **por anuncio** (UTM `utm_content`).

| KPI | Pregunta | Cálculo | Fuente | Decisión que dispara |
|---|---|---|---|---|
| Leads por canal | ¿De dónde entra la gente? | Conteo de leads por canal y mes | CRM / base | Dónde poner energía de contenido |
| Costo por lead | ¿Cuánto cuesta que alguien aplique? | Inversión ÷ leads (del anuncio) | Plataforma de anuncios + base | Cambiar creativo o segmentación |
| Costo por agenda | ¿Cuánto cuesta una llamada? | Inversión ÷ agendas. **Aclarar qué agenda** (con setter o con closer) | Plataforma o base | Solo alarma temprana: no decide escalar |
| ★ **Costo por venta (CAC por anuncio)** | ¿Cuánto cuesta un cliente que paga? | Inversión del anuncio ÷ ventas con esa UTM | Plataforma (gasto) + base (ventas) | Pausar, mantener o escalar cada anuncio |
| Cash por agenda | ¿Cuánta plata trae cada llamada del canal? | Cash nuevo del canal ÷ agendas del canal | Base | Comparar canales con tickets distintos |
| Retorno (ROAS) sobre cash | ¿Cuánto vuelve por dólar? | Cash collected del canal ÷ inversión. Mostrar también sobre facturado | Base + plataforma | Repartir presupuesto entre canales |
| Calificación por canal | ¿El canal trae gente que puede comprar? | Leads que cumplen el criterio ÷ leads del canal | Formulario / setter | Cambiar preguntas del formulario o el público |
| Leads sin canal | ¿Funciona el tracking? | Leads con canal vacío ÷ total | Base | Arreglar UTMs (skill **UTMs de Punta a Punta**) |
| Retención de video / VSL | ¿Lo miran? | % que llega al minuto clave | Plataforma de video | Rehacer el arranque del video |

**Cuidados.** La atribución por UTM es del último link: hay gente que vio la campaña y entró por otro lado. Separá "de dónde vino el lead" de "de dónde agendó". Si la pauta compra seguidores o comunidad (no agendas directas), su retorno está repartido entre canales orgánicos: compará con esa salvedad.

---

## 2 · Setters (calificación y agenda)

| KPI | Pregunta | Cálculo | Fuente | Decisión |
|---|---|---|---|---|
| Conversaciones / mensajes enviados | ¿Cuánto trabaja el embudo de entrada? | Conteo diario, **inbound y outbound separados** | EOD del setter | Carga y reparto entre setters |
| Ofertas o links de agenda enviados | ¿Dónde se cae el lead antes de agendar? | Conteo diario | EOD del setter | Guion de DM o de calificación |
| Agendas con closer | ¿Cuántas llamadas genera? | Conteo por setter | Base (llamadas) | — (no decide solo: ver la de abajo) |
| ★ **Agendas que se presentan y califican** | ¿Agenda gente que compra? | Llamadas realizadas que cumplen criterio ÷ agendas del setter | Base | Coaching del setter; revisar incentivo |
| Cierre de las agendas del setter | ¿Lo que agenda termina en venta? | Ventas ÷ llamadas que agendó | Base | Comparar setters con el mismo público |
| Tiempo de primera respuesta | ¿Se enfría el lead? | Horas entre aplicación y primer contacto | CRM | Turnos, avisos, reasignación |
| Leads sin contactar | ¿Se pierde gente en la cola? | Leads en "Nuevo" con más de 48 h | CRM | Reasignar (por ejemplo, de quien se fue) |
| Completitud del campo de calificación | ¿Se puede confiar en el filtro? | Llamadas con calificación cargada ÷ total | Base | Campo obligatorio |

**Cuidado con el incentivo.** Si el setter cobra por agenda, este bloque es el primero que hay que mirar. Pagar por llamada calificada que se presenta, o por venta, alinea el número con la plata.

---

## 3 · Closers

| KPI | Pregunta | Cálculo | Fuente | Decisión |
|---|---|---|---|---|
| Llamadas asignadas | ¿Cuánta carga tiene? | Conteo por closer | Base | Reparto (no según huecos de agenda) |
| Asistencia de sus llamadas | ¿Le llega gente? | Realizadas ÷ agendadas | Base | Es del sistema (recordatorios, setter), no del closer |
| ★ **Cierre sobre asistidas** | ¿Cierra cuando tiene a la persona enfrente? | Ventas ÷ realizadas, **por closer y por canal** | Base | Coaching, escucha de llamadas |
| Cierre sin el canal problemático | ¿Es el closer o son sus leads? | Mismo cálculo, sacando el anuncio o canal que no califica | Base | Separar efecto del lead y del closer |
| Ticket promedio / % contado | ¿Cómo vende? | Facturado ÷ ventas; ventas de contado ÷ ventas | Base | Política de cuotas |
| Descuentos fuera de política | ¿Respeta el precio? | Ventas con monto distinto al de lista | Base + llamadas | Política escrita de descuentos |
| Seguimientos vencidos | ¿Cierra el ciclo? | Leads en "Seguimiento" sin tocar hace más de 7 días | CRM | Rutina de seguimiento |
| Cuota 2 cobrada de sus ventas | ¿Vende a quien paga? | Ventas del closer con cuota 2 paga ÷ con cuota 2 vencida | Base | Revisar calificación en la llamada |

**Cuidado.** Llamadas sin closer cargado vuelven aproximada la tasa por persona: declaralo antes de comparar.

---

## 4 · Área comercial (todo el embudo)

| KPI | Cálculo | Para qué |
|---|---|---|
| ★ Agendas · asistencia · calificación · cierre total | Las 4 mínimas | Salud del embudo de un vistazo |
| Los dos cierres | Sobre asistidas y sobre agendas | Si se abren como tijera, cambió algo en el equipo |
| Ciclo de venta | Días entre aplicación y venta | Seguimiento, urgencia de la oferta |
| Pipeline estancado | Oportunidades sin tocar hace más de 30 días ÷ abiertas | Limpieza del CRM, seguimientos |
| Estados sin cerrar | No-shows que siguen "Agendado", reservas sin marcar | Disciplina de carga |
| Ventas por canal y por closer | Conteo y facturado | Dónde se gana |

---

## 5 · Cobros y caja

| KPI | Pregunta | Cálculo | Decisión |
|---|---|---|---|
| ★ **Cobrado del mes en 3 cubetas** | ¿Cuánta plata entró de verdad y de dónde? | Reservas · nuevos cierres (primer pago) · cuotas de ventas anteriores | No leer el total como éxito comercial |
| Facturado del mes | ¿Cuánto se vendió? | Monto contratado de las ventas del mes | Comparar con cobrado, nunca reemplazarlo |
| ★ **Morosidad** | ¿Se cobran las cuotas? | Cuotas vencidas impagas ÷ cuotas que ya debían estar pagas (**al corte**) | Dueño de cobros, protocolo a 1, 7 y 15 días |
| Monto vencido y días de atraso | ¿Cuánto y desde cuándo? | Suma y mediana | Priorizar a quién llamar |
| Vencidas sin aviso / sin responsable | ¿Alguien está cobrando? | Conteo | Asignar responsable |
| Con cuota vencida y acceso activo | ¿Se aplica la regla? | Conteo | Política de suspensión |
| % del cash de clientes existentes | ¿Vivimos de adquisición o de cartera? | (Cuotas viejas + renovaciones) ÷ cash total | Si pasa del 50 % varios meses, la adquisición está frenada |
| Vence en los próximos 7 días | ¿Qué explota esta semana? | Cuotas con vencimiento en la semana | Aviso antes del vencimiento |

**Morosidad es un stock:** se calcula al corte (por ejemplo, cada domingo) sobre todo lo que ya debía estar pago, no sobre "lo que venció esta semana".

---

## 6 · Servicio y satisfacción

### Lo que sale de encuestas y entrevistas

| KPI | Cómo se obtiene | Cuándo | Decisión |
|---|---|---|---|
| ★ **NPS** | "Del 0 al 10, ¿qué tan probable es que recomiendes el programa?" → % promotores (9-10) − % detractores (0-6) | A mitad del servicio y cerca del final | Detractores: llamada del CSM esa semana |
| Nota por entregable o fase | 1 a 10 por cada entregable o fase + "¿por qué?" | Al terminar cada fase | Rehacer la fase con nota baja |
| Cumplimiento de la promesa | "¿Lograste [micro-objetivo de la fase]?" Sí / en parte / no | Por fase | Ajustar el journey o la promesa de venta |
| Temas de lo abierto | Agrupar respuestas y contar menciones | Cada encuesta | Mejoras de producto; lenguaje para marketing |
| Testimonios disponibles | Promotores que aceptan dar testimonio | Al cierre | Material de venta |
| Satisfacción con el onboarding | 1 a 10 + qué faltó | Al terminar la primera semana | Corregir bienvenida y accesos |
| Satisfacción por área (contenido, soporte, acceso…) | Promedio **y** % que da 4-5; producto y operación por separado | Con cada encuesta | Atacar el área operativa más baja |
| Intención de seguir | "¿Pensás seguir cuando termine?" Sí / No sé / No, por cohorte | A mitad y antes del final | Oferta de continuidad antes de que termine la cohorte |
| Tasa de respuesta y sesgo | Respuestas únicas ÷ enviadas; tasa de los que deben vs los que no | Con cada encuesta | Si los que deben no responden, el NPS real es peor |

Las entrevistas (de offboarding, de mitad de camino, con el founder) se leen igual: temas, menciones y frases textuales, cruzadas con conducta.

### Lo que sale de la conducta (proxies cuando no hay encuesta)

| KPI | Cálculo | Decisión |
|---|---|---|
| Tiempo a primer acceso | Días entre pago y acceso habilitado | Automatizar el alta |
| Participación | Sesiones asistidas por alumno; última sesión | Detectar al que se está yendo |
| Alumnos en riesgo | Sin sesión hace más de 14 o 21 días, o micro-objetivo atrasado | Contacto del CSM con contexto |
| Bajas y reembolsos | Conteo y motivo | Si no se registran, ese es el hallazgo |
| Renovaciones y upsells | Renovados ÷ los que terminan | Oferta de continuidad |
| Referidos | Ventas con fuente "referido" | Programa de referidos; marketing de casos |
| Duración promedio | Meses activos por alumno | Valor de vida del cliente |

**Cruce clave:** nota baja + sin sesiones + cuota vencida es el mismo alumno más veces de lo que parece. Mostralo. El paso a paso para leer una encuesta (limpieza, cortes, sesgo de no respuesta) está en `leer-encuestas.md`.

---

## 7 · Operaciones (carga, cambio de contexto, automatizaciones)

| KPI | Pregunta | Cálculo | Fuente | Decisión |
|---|---|---|---|---|
| ★ **Horas perdidas en fricción** | ¿Dónde se va el tiempo? | Minutos anotados por semana, por área y por persona | Registro de fricción (skill **Mapa de Fricción Invisible**) | Qué proceso arreglar primero |
| Cambio de contexto | ¿Cuántas veces se interrumpe a cada persona? | Interrupciones o pedidos por persona por día (preguntas en el grupo, "¿me aprobás?", "¿alguien sabe…?") | Registro de fricción, grupo del equipo | Canales y reglas de urgencia (skill **Centro de Comunicación y EOD**); wiki para lo que se pregunta dos veces |
| Preguntas repetidas | ¿Qué se pregunta dos veces? | Conteo de la misma pregunta en la semana | Grupo del equipo | Va a la wiki o a una vista |
| Carga por persona | ¿Alguien está al límite? | Horas trabajadas y nivel de energía declarados en el EOD; tareas abiertas por persona | EOD, gestor de tareas | Redistribuir o delegar (skill **Matriz de Delegación**) |
| Cuellos de botella del founder | ¿Qué espera al dueño? | Tareas o aprobaciones que sólo puede hacer el founder; días de espera | Gestor de tareas, registro | Pasar la regla a un rol |
| Tareas manuales repetitivas | ¿Qué se podría automatizar? | Minutos por semana × frecuencia | Registro de fricción | Prioridad de automatización |
| ★ **Automatizaciones activas y horas recuperadas** | ¿Lo que se automatizó devuelve tiempo? | Por automatización: minutos antes − minutos después, por semana; sumado al mes | Registro antes/después | Seguir automatizando o arreglar la que falla |
| Fallas de automatización | ¿Fallan en silencio? | Ejecuciones con error ÷ total; registros que no llegaron | Historial de la herramienta | Avisos de error al rol correcto |
| Completitud de datos | ¿Se puede confiar en el tablero? | % de registros con los campos clave; % de días con EOD cargado | Base, formularios | "Sin registro no se liquida" |
| Tiempo de ciclo de procesos | ¿Cuánto tarda lo que importa? | Por ejemplo, pago → acceso; venta → comisión liquidada | Base | SOP y automatización |

**Cómo se mide "tiempo ganado" sin inventarlo:** registro de una semana **antes** (minutos y frecuencia), la automatización o el cambio, y registro de una semana **después**. La diferencia por semana × 4 es el tiempo recuperado al mes. Si no hay "después", es una estimación y se dice.

---

## Fichas de ejemplo (para el Modo 2)

| KPI | Pregunta | Cálculo | Fuente | Frecuencia | Responsable | Alarma | Decisión |
|---|---|---|---|---|---|---|---|
| Cobrado del mes (3 cubetas) | ¿Cuánta plata entró? | Suma de pagos con fecha de pago en el mes, separados | Tabla de pagos | Semanal | Coordinación de servicio | Nuevos cierres bajan 2 meses seguidos | Revisar embudo antes de subir pauta |
| Morosidad | ¿Se cobran las cuotas? | Vencidas impagas ÷ cuotas que debían estar pagas, al domingo | Tabla de cuotas | Semanal | Dueño de cobros | Sube 2 semanas seguidas | Aplicar protocolo, revisar quién cobra |
| Costo por venta por anuncio | ¿Qué anuncio trae clientes? | Gasto ÷ ventas por UTM | Meta + base | Semanal (6 semanas móviles) | Marketing | Un anuncio con gasto y 0 ventas en 4 semanas | Pausar o rehacer |
| Agendas que se presentan y califican, por setter | ¿El setter filtra? | Realizadas que califican ÷ agendas | Base | Semanal | Líder comercial | Debajo de 50 % | Coaching; revisar incentivo |
| NPS de mitad de servicio | ¿Nos recomendarían? | Promotores − detractores | Encuesta | Por cohorte | CSM | Negativo | Llamar a detractores esa semana |
| Horas recuperadas por automatización | ¿Valió la pena? | Minutos antes − después, × 4 | Registro | Mensual | Operaciones | Menos de lo esperado | Arreglar o apagar |
