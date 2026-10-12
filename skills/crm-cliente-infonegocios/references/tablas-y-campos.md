# Tablas y campos · estructura estándar del CRM de infonegocio

> Referencia de la skill CRM de Cliente para Infonegocios (RealOps™). Sale de las bases de muestra de MG Operations (BDD de muestra 1 y 2) y de lo que se corrigió en negocios reales. Adaptá los nombres al idioma del equipo; mantené la estructura.
>
> Tipos en español y, entre paréntesis, como aparecen en Airtable en inglés. "Obl." = obligatorio. Lo que dice "fórmula", "lookup", "rollup" o "conteo" no lo carga nadie.

---

## Módulo 1 · Setting

### 📲 Leads (setting)
**Una fila = una persona** que entró a conversación o aplicó. Si vuelve meses después, **no se crea otro lead**: se crea otra oportunidad.

| Campo | Tipo | Obl. | Quién lo carga | Notas |
|---|---|---|---|---|
| Nombre del lead | Texto (primario) | Sí | Formulario / integración | |
| WhatsApp · Instagram · Email | Teléfono · Texto · Email | Al menos uno | Formulario / setter | El mail y el teléfono se usan después para el onboarding automático: validarlos |
| Fecha de ingreso | Fecha de creación (Created time) | — | Automático | |
| Canal de entrada | Selección única | Sí | Formulario / setter | Lista cerrada: Inbound IG · Outbound · Anuncio (DM o formulario) · Aplicación · Lanzamiento · Referido · YouTube · Sin canal |
| Fuente cruda | Texto | No | Integración | Lo que llega tal cual (UTM, nombre del calendario). Sirve para auditar la normalización |
| UTM source · medium · campaign · content | Texto | Si viene de anuncio | Integración | Ver skill UTMs de Punta a Punta |
| Setter | Vínculo → Equipo (limitado a vista "Activos · Setters") | Sí | Asignación / setter | **Nunca** selección única |
| Estado de setting | Selección única | Sí | Setter | Nuevo · En conversación · Nutrición · Seguimiento · Link de agenda enviado · Agendó · No califica · No responde · Perdido |
| Respuestas de la aplicación | Texto largo o selecciones | Si hay formulario | Formulario | Ej.: facturación mensual, a qué se dedica, disponibilidad a invertir |
| Calificación del setter | Selección única | Sí antes de agendar con closer | Setter (o triage) | Cumple · No cumple. Criterio escrito en la descripción del campo |
| Motivo de no calificación | Selección única | Si No cumple | Setter | Sin negocio · Ingresos bajo el mínimo · Sin capacidad de inversión · Otro |
| Seguimientos hechos | Número | No | Setter | |
| Próximo seguimiento | Fecha | Sí si Estado = Seguimiento | Setter | Sin fecha no es seguimiento |
| Notas del setter (para el closer) | Texto largo | Sí antes de agendar | Setter | Se ve en la oportunidad por lookup |
| ID externo | Texto | Si hay CRM de mensajería | Integración | GoHighLevel, ManyChat: para no duplicar al reimportar |
| ☎️ Oportunidades | Vínculo → Oportunidades | — | Automático / setter | |
| Días sin contactar | Fórmula | — | — | `IF({Estado de setting} = "Nuevo", DATETIME_DIFF(TODAY(), {Fecha de ingreso}, 'days'), BLANK())` |

---

## Módulo 2 · Agendas

### ☎️ Oportunidades (agendas)
**Una fila = un intento de venta con llamada agendada.** La reagenda y la segunda llamada quedan en la misma fila. Si necesitás auditar cada llamada por separado (grabación, duración, closer distinto en cada una), sumá una tabla hija 📞 Llamadas.

| Campo | Tipo | Obl. | Quién lo carga | Notas |
|---|---|---|---|---|
| Nombre | Texto o fórmula (primario) | Sí | Integración | |
| Lead | Vínculo → Leads | Sí si hay tabla Leads | Integración / setter | |
| Fecha de agenda | Fecha de creación | — | Automático | Cuándo se agendó |
| Fecha de llamada | Fecha y hora | Sí | Integración del calendario | |
| Mes de llamada | Fórmula | — | — | `DATETIME_FORMAT({Fecha de llamada}, 'YYYY-MM')`. Si la fecha falta, la fórmula da error y la oportunidad no entra al reporte: vista de control "Sin fecha de llamada" |
| Calendario o evento de origen | Texto | No | Integración | |
| Canal | Selección única (o fórmula que normaliza la fuente cruda) | Sí | Formulario / setter | Misma lista cerrada que Leads. Si es fórmula, que el último caso sea "Sin canal", nunca vacío |
| 📌 Clave KPIs globales | Fórmula | — | — | `{Mes de llamada} & " \| " & {Canal}`. Se usa para vincular con 📈 KPIs globales |
| Setter | Lookup desde Lead (o vínculo → Equipo) | — | — | |
| Triage | Vínculo → Equipo | Si hay triage | Setter | |
| Closer | Vínculo → Equipo (vista "Activos · Closers") | **Sí antes de la llamada** | Setter / asignación | Sin closer no hay tasa de cierre por closer |
| Respuestas del formulario de agenda | Texto largo / selecciones | — | Formulario | Situación actual, objetivo, ingresos, disponibilidad a invertir, si decide solo |
| Notas del setter | Lookup desde Lead | — | — | Que el closer las vea antes de la llamada |
| Confirmó asistencia | Casilla | No | Setter / closer | |
| Estado de la llamada | Selección única | Sí | Closer, el mismo día | Esperando llamada · Asistida · No show · Cancelada por el lead · Cancelada por el equipo · Reagendada · Esperando 2da llamada |
| Fecha 2da llamada | Fecha | Si aplica | Closer | |
| Estado de la oportunidad | Selección única | Sí | Closer | Agendado · Seguimiento · Reserva · Cierre ganado · Perdido · Falso / duplicado |
| Calificación del closer | Selección única | Sí si Asistida | Closer | Alta · Media · Baja · No califica |
| Oferta hecha | Casilla | Sí si Asistida | Closer | Permite medir cierre sobre ofertas |
| Próximo seguimiento | Fecha | Sí si Estado = Seguimiento | Closer | |
| Motivo de pérdida | Selección única | Sí si Perdido | Closer | Precio · Tiempo · Socio o pareja · Confianza · No califica · No respondió · Otro |
| Link de grabación | URL | No | Closer / integración | Una por llamada |
| Notas del closer | Texto largo | No | Closer | |
| 💰 Deals | Vínculo → Deals + Reservas | — | Al cargar el deal | |
| Última modificación del estado | Última modificación (Last modified time) del campo Estado de la oportunidad | — | — | Para detectar oportunidades quietas |

---

## Módulo 3 · Ventas y cobros

### 💰 Deals + Reservas
**Una fila = un acuerdo de venta:** una reserva o un cierre (primer high ticket, upsell, renovación, downsell, evento vendido por llamada). Se carga con formulario, en el momento del pago.

| Campo | Tipo | Obl. | Quién lo carga | Notas |
|---|---|---|---|---|
| Nombre y apellido | Fórmula o lookup (primario) | — | — | |
| Oportunidad | Vínculo → Oportunidades | **Sí** | Closer | "Sin oportunidad no se cobra" |
| Origen | Selección única | Sí | Closer / migración | Base · Histórico (ventas traídas de planillas, sin oportunidad) |
| Cliente | Vínculo → Clientes | Sí en cierres | Automático o administración | **Un solo vínculo** entre Deals y Clientes (nunca dos pares paralelos) |
| Producto | Vínculo → Productos (o selección única) | Sí | Closer | |
| Tipo de venta | Selección única | Sí | Closer | Primer high ticket · Upsell · Renovación · Downsell · Evento |
| Naturaleza | Selección única | Sí | Closer | Reserva · Nuevo cierre · Recurrencia |
| Forma de pago | Selección única | Sí en cierres | Closer | Pago completo · Cuotas · Suscripción |
| Cantidad de cuotas | Número o selección | Si Cuotas | Closer | |
| Fecha del pago | Fecha | Sí | Closer | Fecha de esta operación (inicio del contrato si es cierre) |
| Facturación (USD) | Moneda | Sí en cierres | Closer | Valor total del ticket. **Vacía en reservas** |
| Cash collected (USD) | Moneda | Sí | Closer | Lo que entró en esta operación, dolarizado |
| Método de pago 1 · 2 · 3 | Selección única (o vínculo → Cuentas) | Al menos el 1 | Closer / administración | |
| Monto método 1 · 2 · 3 (moneda real) | Moneda (en la moneda del método) | Al menos el 1 | Closer / administración | Para conciliar con el banco |
| Quién recibió el efectivo | Vínculo → Equipo | Si efectivo | Closer | |
| Comprobante | Adjunto | Sí | Closer | Comprobante no es pago: administración confirma la acreditación |
| Acreditado | Casilla | Sí | Administración | Recién acá se da acceso y cuenta para comisiones |
| Pagó reserva | Casilla | Si hubo reserva | Closer | |
| Cash de reservas previas (USD) | Moneda o rollup | Si Pagó reserva | Closer | Evita que el saldo quede mal |
| Fecha para resolver la reserva | Fecha | Si Reserva | Closer | |
| Cash de cuotas (USD) | Rollup de Cuotas cobradas (SUM) | — | — | |
| Total pagado (USD) | Fórmula | — | — | `{Cash de reservas previas (USD)} + {Cash collected (USD)} + {Cash de cuotas (USD)}` |
| Saldo pendiente (USD) | Fórmula | — | — | `IF({Facturación (USD)}, {Facturación (USD)} - {Total pagado (USD)}, 0)` |
| Cuotas vencidas | Rollup de Cuotas programadas (COUNTALL con condición Estado = Vencida) | — | — | |
| Estado de pago | Fórmula | — | — | Reembolsado · Terminó de pagar · Con cuota vencida · Al día |
| Closer · Setter · Ejecutivo de éxito | Vínculos → Equipo (o lookups desde la oportunidad) | Según el tipo de venta | Closer | En upsells y renovaciones el que vende suele ser el ejecutivo de éxito |
| Canal | Lookup desde Oportunidad | — | — | |
| 📌 Clave KPIs globales | Fórmula | — | — | `DATETIME_FORMAT({Fecha del pago}, 'YYYY-MM') & " \| " & {Canal}` |
| Cerró por seguimiento | Casilla | No | Closer | |
| Reembolso | Selección única (No · Parcial · Total) | — | Administración | |
| Monto reembolsado (USD) · Fecha del reembolso | Moneda · Fecha | Si hubo | Administración | El egreso va también a Finanzas |
| Factura emitida | Casilla | — | Administración | **Distinto de Facturación**: es la factura fiscal |
| Comisión closer / setter / ejecutivo | Fórmula | — | — | `{Cash collected (USD)} * {% comisión closer (lookup desde Equipo)}` y 0 si Reembolso ≠ No. Sin nombres de personas en la fórmula |

**Estado de pago (fórmula de ejemplo):**
```
IF({Reembolso} = "Total", "Reembolsado",
  IF(AND({Facturación (USD)}, {Saldo pendiente (USD)} <= 0), "Terminó de pagar",
    IF({Cuotas vencidas} > 0, "Con cuota vencida", "Al día")))
```

### 🗓️ Cuotas programadas
**Una fila = una cuota que se espera cobrar**, de la 2 en adelante (la 1 entra con el deal). Se crean al cargar un cierre en cuotas (a mano o por automatización).

| Campo | Tipo | Obl. | Quién lo carga | Notas |
|---|---|---|---|---|
| Cuota | Fórmula (primario) | — | — | `{Nombre (lookup)} & " · cuota " & {N° de cuota}` |
| Deal | Vínculo → Deals + Reservas | Sí | Al crear | |
| N° de cuota | Número | Sí | Al crear | 2, 3, 4… |
| Monto esperado (USD) | Moneda | Sí | Al crear | |
| Vencimiento | Fecha | Sí | Al crear | Si el cliente renegocia, se cambia acá y queda nota |
| Cuota cobrada | Vínculo → Cuotas cobradas | — | Al cargar el pago | |
| Fecha de pago | Lookup desde Cuota cobrada | — | — | |
| Estado | Fórmula | — | — | Ver abajo |
| Días de atraso | Fórmula | — | — | Ver abajo |
| Mes de vencimiento | Fórmula | — | — | `DATETIME_FORMAT({Vencimiento}, 'YYYY-MM')`. Reemplaza las 12 fórmulas "Proyección de cuotas" por mes |
| Avisos enviados · Último aviso | Número · Fecha | Si Vencida | Responsable de cobro | |
| Responsable de cobro | Vínculo → Equipo | Sí si Vencida | Administración | Un solo rol dueño de cobrar |
| Nota de renegociación | Texto largo | No | Administración | |

```
// Estado
IF({Fecha de pago}, "Pagada",
  IF(IS_BEFORE({Vencimiento}, TODAY()), "Vencida",
    IF(DATETIME_DIFF({Vencimiento}, TODAY(), 'days') <= 7, "Por vencer", "Al día")))

// Días de atraso
IF(AND({Fecha de pago} = BLANK(), IS_BEFORE({Vencimiento}, TODAY())),
   DATETIME_DIFF(TODAY(), {Vencimiento}, 'days'), 0)
```

### 💵 Cuotas cobradas
**Una fila = un pago de cuota que entró** (cuota 2 en adelante, o una recurrencia). Se carga con su propio formulario.

| Campo | Tipo | Obl. | Notas |
|---|---|---|---|
| Nombre y apellido | Lookup / fórmula (primario) | — | |
| Deal | Vínculo → Deals + Reservas, **limitado a la vista "Cuotas pendientes"** | Sí | Así nadie carga una cuota a una reserva o a un pago completo |
| Cuota programada | Vínculo → Cuotas programadas | Sí si existe la tabla | |
| Fecha del pago | Fecha | Sí | |
| Cash collected (USD) | Moneda | Sí | |
| Método 1 · 2 · 3 + monto en moneda real | Selección + Moneda | Al menos el 1 | Igual que en Deals |
| Comprobante · Datos del comprobante | Adjunto · Texto largo | Sí | |
| Acreditado | Casilla | Sí | |
| Cumplimiento | Fórmula | — | Pagó adelantado · A tiempo · Con demora (compara Fecha del pago con Vencimiento) |
| Canal · Closer · Setter | Lookups desde Deal | — | |
| 📌 Clave KPIs globales | Fórmula | — | Mes **del pago** + canal **del deal** |
| Comisiones | Fórmula | — | Mismo criterio que en Deals |

### 🛒 Ventas directas (checkout)
**Una fila = una compra sin llamada** (low ticket, entrada a evento, producto digital). Suele llegar por integración desde la pasarela.

Campos: Cliente (texto o vínculo a Leads si después se lo trabaja) · Email · Fecha de compra · Producto · Cantidad · Monto en moneda real · Moneda · Monto USD · Método · Origen (UTM o canal) · Mes · ID de la transacción (para no duplicar).

### 🪙 Finanzas
**Una fila = un movimiento de plata por método, en su moneda real.** Ver `cobros-y-finanzas.md`.

Campos: ID movimiento (autonumérico, primario) · Tipo de movimiento (Ingreso · Egreso) · Categoría (Venta · Cuota · Venta directa · Sueldos · Comisiones · Herramientas · Publicidad · Impuestos · Reembolso · Retiro de socios · Otro) · Fecha · Monto (moneda real) · Moneda · Cuenta o método (vínculo → Cuentas) · Tipo de cambio del mes · Monto USD (fórmula) · Cliente o destinatario · Concepto · Origen (vínculo al deal, cuota o venta directa) · Comprobante · Conciliado (casilla) · Mes (fórmula) · Notas.

### 🏦 Cuentas y medios de cobro (opcional, muy recomendada si hay varias)
Una fila = una cuenta o pasarela. Campos: Nombre · Tipo (pasarela, banco, billetera, cripto, efectivo) · Moneda · Titular · **¿Es del negocio?** (casilla) · Quién tiene acceso. Una cuenta personal recibiendo cobros del negocio es un hallazgo.

### 📦 Productos (opcional)
Nombre · Tipo (high ticket, mid ticket, low ticket, membresía, evento) · Precio de lista USD · Duración en meses · Activo. Reemplaza las selecciones de "Programa" repetidas en varias tablas y permite agrupar cierres por producto sin un campo de conteo por producto.

---

## Módulo 4 · Clientes

### 👥 Clientes (CRM de servicio)
**Una fila = un cliente.** Se da de alta **desde su deal** (cuando el cierre se acredita).

| Campo | Tipo | Obl. | Quién lo carga | Notas |
|---|---|---|---|---|
| Nombre y apellido | Texto / fórmula (primario) | Sí | Automático | |
| Lead · Deals | Vínculos | Sí | Automático | Un solo par de vínculos con Deals |
| Productos adquiridos | Lookup desde Deals | — | — | |
| Coach o ejecutivo de éxito | Vínculo → Equipo (vista "Activos · tomando clientes") | Sí | Coordinación | |
| Estado | Selección única | Sí | Coordinación / coach | Onboarding pendiente · Activo · Suspendido por falta de pago · Pausado a pedido · Finalizó contrato · Baja |
| Fecha de acceso | Fecha | Sí al habilitar | Coordinación | |
| Días hasta el acceso | Fórmula | — | — | Entre el pago acreditado y el acceso |
| Fecha de onboarding · Fecha de inicio · Fecha fin de contrato | Fechas | Sí | Coordinación | |
| Días hasta el fin | Fórmula | — | — | `DATETIME_DIFF({Fecha fin de contrato}, TODAY(), 'days')` |
| Salud | Selección única | Sí | Coach | Excelente · Muy buena · Buena · Baja · En riesgo |
| Nota del cambio de salud | Texto largo | Sí si cambia | Coach | |
| Próxima acción · Fecha | Texto · Fecha | Sí si En riesgo | Coach | |
| Estado de pago · Saldo pendiente | Lookups desde Deals | — | — | El coach ve que debe, pero **no cobra** |
| Renovación | Selección única | Desde 60 días antes del fin | Coach | Apto · Ofrecida · Renovó · No renovó |
| Motivo de no renovación o baja | Selección única | Si aplica | Coach | |
| Caso de éxito (fecha · link) | Fecha · URL | No | Coach | |
| Sesiones | Vínculo → Sesiones | — | — | |
| Onboarding | Vínculo → Onboarding | — | Formulario | |

### 🤩 Onboarding (respuestas del formulario)
Una fila = un formulario de inicio respondido. Vinculado a Clientes. Objetivo principal, situación actual, situación deseada, obstáculos, expectativas, cómo nos conoció, por qué compró. Alimenta testimonios y el primer plan del coach.

### 🗣️ Sesiones / seguimientos
Una fila = una sesión o un contacto del coach. Cliente · Coach · Fecha · Tipo (1:1, grupal, seguimiento por mensaje) · Asistió · **Link de grabación propio** (uno por sesión, no todos los del día) · Notas · Próximo paso.

---

## Módulo 5 · Equipo y KPIs

### 👨🏻‍💻 Equipo
| Campo | Tipo | Notas |
|---|---|---|
| Nombre y apellido | Texto (primario) | |
| Roles | Selección múltiple (lista cerrada) | Setter · Triage · Closer · Ejecutivo de éxito / coach · Coordinación · Administración · Founder |
| Estado | Selección única | Activo · Activo sin tomar clientes · Inactivo |
| Fecha de ingreso · Fecha de egreso | Fecha | |
| Email | Email | Cuenta del negocio, no personal |
| % comisión closer · setter · ejecutivo | Porcentaje | Las fórmulas los leen por lookup. Regla escrita en la skill Esquema de Pago y Comisiones |
| Capacidad máxima de clientes | Número | Coaches |
| Clientes activos | Conteo con condición | |
| Vínculos | a Leads, Oportunidades, Deals, Clientes, EOD | |

Vistas: "Activos · Setters", "Activos · Closers", "Activos · tomando clientes". Los campos de persona de las otras tablas se limitan a estas vistas.

### 🌙 EOD (una tabla por rol)
Setters, closers y servicio reportan cosas distintas, por eso son tablas separadas. Cada fila: Persona (vínculo → Equipo) · Fecha · números del día · energía · feedback · 🔴 Clave persona | mes (fórmula). Qué pregunta cada EOD: skill **Centro de Comunicación y EOD**.

- **Setters:** conversaciones inbound y outbound · seguimientos · respuestas · links de agenda enviados · agendas por canal.
- **Closers:** agendadas · asistidas · calificadas · no show · canceladas · reagendadas · ofertas · cierres · reservas · seguimientos · links de llamadas.
- **Servicio:** sesiones agendadas y asistidas · seguimientos hechos · clientes en riesgo · clientes destacados (renovación, caso de éxito).

**El EOD no reemplaza al CRM:** los cierres y el cash se cuentan desde Deals; el EOD sirve para lo que no deja registro y para contrastar ("el closer dice 5 cierres, Deals dice 4").

### 📊 KPIs por persona (persona | mes) y 📈 KPIs globales (mes | canal)
Tablas de resumen, una fila por clave. Se vinculan solas con una automatización que busca o crea la fila por la clave. La receta completa está en la skill **Tabla de KPIs Globales en Airtable**. Lo que esta skill asegura es que cada tabla de origen tenga su clave:

| Tabla | Clave |
|---|---|
| Oportunidades | Mes de llamada \| Canal |
| Deals + Reservas | Mes del pago \| Canal |
| Cuotas cobradas | Mes del pago \| Canal del deal |
| EOD | Persona \| Mes |
