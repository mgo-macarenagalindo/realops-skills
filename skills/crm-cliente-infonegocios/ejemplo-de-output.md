# Ejemplo de output · CRM de Cliente para Infonegocios

> Datos ficticios. **Estudio Norte**: mentoría de 4 meses de marca personal para arquitectos. USD 2.400 en un pago o 4 cuotas de USD 650; reserva de USD 200 para congelar precio. Al terminar, se ofrece un mastermind de 6 meses (upsell). También vende un taller grabado de USD 27 por checkout. Cobra por Stripe (USD), transferencia en pesos argentinos y transferencia en pesos mexicanos. Equipo: 2 setters (DM de Instagram), 2 closers, 2 coaches, 1 persona de administración y la founder. Hoy: GoHighLevel para los DM, una planilla por closer y una planilla de cobros.

---

# CRM de Cliente · Estudio Norte
Herramienta: Airtable · Módulos: setting, agendas, ventas y cobros, clientes, equipo · Punto de partida: planillas + export de GoHighLevel

## 0. Qué queda, qué cambia, qué se suma

| Hoy | Qué pasa | Cómo |
|---|---|---|
| Contactos en GoHighLevel | Queda como herramienta de mensajes | Se importan a 📲 Leads con su ID externo para no duplicar |
| Planilla de cada closer | Se reemplaza | Sus columnas pasan a ☎️ Oportunidades y 💰 Deals. Se archivan el día que arranca la base |
| Planilla de cobros | Se reemplaza | Pagos de cierre → Deals; cuotas → 🗓️ Cuotas programadas y 💵 Cuotas cobradas |
| Mails de Stripe del taller | Se suma | 🛒 Ventas directas (por integración, después) |
| — | Se suma | 🪙 Finanzas y 🏦 Cuentas: hay tres monedas |

## 1. Mapa de módulos y tablas

```
📲 Leads ──< ☎️ Oportunidades ──< 💰 Deals + Reservas ──< 🗓️ Cuotas programadas ──1:1── 💵 Cuotas cobradas
                                         └── 👥 Clientes ──< 🗣️ Sesiones · 🤩 Onboarding
🛒 Ventas directas
Deals · Cuotas cobradas · Ventas directas ──> 🪙 Finanzas ──> 🏦 Cuentas
👨🏻‍💻 Equipo (vinculado en todo) · 🌙 EOD Setters · 🌙 EOD Closers   (KPIs: en una segunda etapa)
```

| Tabla | Una fila = |
|---|---|
| Leads | una persona que respondió un DM o comentó |
| Oportunidades | una llamada de venta agendada (con su reagenda) |
| Deals + Reservas | una reserva, un cierre o un upsell |
| Cuotas programadas | una cuota que se espera (de la 2ª a la 4ª) |
| Cuotas cobradas | un pago de cuota que entró |
| Ventas directas | una compra del taller |
| Finanzas | un movimiento de plata por método, en su moneda |
| Clientes | una arquitecta o arquitecto en la mentoría |
| Equipo | una persona del equipo |

## 2. Estados con criterio y responsable

**Setting (Leads)**

| Estado | Para avanzar | Responsable |
|---|---|---|
| Nuevo | Respondió el primer DM | Setter |
| En conversación | Contó a qué se dedica y qué quiere | Setter |
| Link de agenda enviado | Cumple el criterio (arquitecto/a con estudio propio o en marcha) | Setter |
| Agendó | Tiene oportunidad creada con closer asignado | Setter |
| No califica / No responde / Perdido | Motivo cargado | Setter |

**Llamada y oportunidad (Oportunidades)**: estado de la llamada (Esperando · Asistida · No show · Cancelada por el lead · Cancelada por el equipo · Reagendada) y estado de la oportunidad (Agendado · Seguimiento con fecha · Reserva · Cierre ganado · Perdido con motivo). Los mueve el closer el mismo día.

**Cobro (Cuotas programadas)**: Al día · Por vencer (7 días) · Vencida · Pagada, por fórmula.

**Cliente (Clientes)**

| Estado | Para avanzar | Responsable |
|---|---|---|
| Onboarding pendiente | Pago acreditado | Administración |
| Activo | Acceso dado y primera sesión hecha | Coach |
| Suspendido por falta de pago | Cuota con 15 días de atraso y decisión de la founder | Founder |
| Finalizó contrato | Pasaron los 4 meses | Coach |
| Baja | Motivo cargado | Coach |

**Renovación al mastermind:** Apto (desde 45 días antes del fin, si la salud es Buena o mejor) · Ofrecida · Renovó · No renovó.

## 3. Campos por tabla (los que cambian algo; el resto, estándar)

**Leads**: Nombre · Instagram · WhatsApp · Canal de entrada (Inbound IG · Outbound · Anuncio DM · Referido · Sin canal) · Setter (vínculo → Equipo, solo activos) · Estado de setting · Calificación del setter (Cumple · No cumple + motivo) · Próximo seguimiento · Notas para el closer · ID de GoHighLevel.

**Oportunidades**

| Campo | Tipo | Obl. | Quién |
|---|---|---|---|
| Lead | Vínculo → Leads | Sí | Setter |
| Fecha de llamada | Fecha y hora | Sí | Calendario |
| Closer | Vínculo → Equipo (activos) | Sí antes de la llamada | Setter |
| Canal | Lookup desde Lead | — | — |
| Estado de la llamada · Estado de la oportunidad | Selección única ×2 | Sí | Closer |
| Calificación del closer | Alta · Media · Baja · No califica | Sí si asistió | Closer |
| Próximo seguimiento | Fecha | Sí si Seguimiento | Closer |
| Motivo de pérdida | Selección única | Sí si Perdido | Closer |
| 📌 Clave KPIs | Fórmula `{Mes de llamada} & " \| " & {Canal}` | — | — |

**Deals + Reservas**

| Campo | Tipo | Ejemplo cierre en cuotas | Ejemplo reserva |
|---|---|---|---|
| Oportunidad | Vínculo | ✔ | ✔ |
| Tipo de venta | Selección | Primer high ticket | Primer high ticket |
| Naturaleza | Selección | Nuevo cierre | Reserva |
| Forma de pago | Selección | Cuotas (4) | — |
| Facturación (USD) | Moneda | 2.600 | vacío |
| Cash collected (USD) | Moneda | 650 | 200 |
| Método 1 · monto (moneda real) | Selección · Moneda | Transferencia MXN · 11.300 | Stripe USD · 200 |
| Pagó reserva · Cash de reservas previas | Casilla · Moneda | (si había reservado: ✔ · 200) | — |
| Total pagado · Saldo pendiente | Fórmulas | 650 · 1.950 | — |
| Acreditado | Casilla | Administración | Administración |
| Comisión closer | Fórmula | Cash collected × % del closer (desde Equipo) | ídem |

**Cuotas programadas**: Deal · N° · Monto esperado · Vencimiento · Cuota cobrada · Estado (fórmula) · Días de atraso (fórmula) · Mes de vencimiento · Avisos enviados · Responsable de cobro.

**Clientes**: Deals · Coach (vínculo, solo "tomando clientes") · Estado · Fecha de acceso · Días hasta el acceso · Fecha fin de contrato · Días hasta el fin · Salud · Próxima acción y fecha · Saldo pendiente (lookup) · Renovación · Motivo de baja.

**Equipo**: Nombre · Roles · Estado (Activo · Activo sin tomar clientes · Inactivo) · Fecha de egreso · % comisión closer / setter · Capacidad máxima (coaches: 25) · Clientes activos (conteo).

## 4. Tipos de cobro de Estudio Norte

| Cobro | Dónde | Facturación | Cash |
|---|---|---|---|
| Reserva USD 200 | Deals · Reserva | No | Cash nuevo |
| Pago completo USD 2.400 | Deals · Nuevo cierre · Pago completo | 2.400 | Cash nuevo 2.400 |
| Primera cuota USD 650 | Deals · Nuevo cierre · Cuotas + 3 Cuotas programadas | 2.600 | Cash nuevo 650 |
| Cuotas 2 a 4 | Cuotas cobradas | No | Cash de cuotas |
| Mastermind | Deals · Upsell (lo vende el coach, con oportunidad) | Sí | Cash nuevo, separado por Tipo de venta |
| Taller USD 27 | Ventas directas | — | Cash de ventas directas |
| Devolución | Reembolso en el deal + egreso en Finanzas | No se borra | Resta en el resultado |

Pesos argentinos y mexicanos: monto real en el bloque financiero; USD con el tipo de cambio del mes que fija administración.

## 5. Vistas por rol

| Rol | Vista | Tabla · filtro |
|---|---|---|
| Setter | Mis leads sin contactar | Leads · Setter = yo · Nuevo · más viejo primero |
| Setter | Mis seguimientos de hoy | Leads · Próximo seguimiento ≤ hoy |
| Closer | Mis llamadas de la semana | Oportunidades · Closer = yo · con notas del setter |
| Closer | Seguimientos vencidos | Oportunidades · Seguimiento · fecha < hoy |
| Administración | Comprobantes por acreditar | Deals y Cuotas cobradas · Acreditado vacío |
| Administración | Vencen en 7 días · Vencidas | Cuotas programadas · por días de atraso |
| Administración | Onboarding pendiente | Clientes · más días primero |
| Coach | Mis clientes en riesgo · Fin en 45 días | Clientes · Coach = yo |
| Founder | Tablero del mes (interface) | Cash del mes (nuevo + cuotas + directas), facturación, cierres por canal, vencido total |

## 6. Alertas y esqueleto de cuota vencida

- Lead nuevo sin contactar en 24 h → setter; si el setter está inactivo, coordinación.
- Oportunidad sin closer 24 h antes de la llamada → setter.
- Pago cargado sin acreditar en 48 h → administración.
- Cuota: aviso −3, día 1, día 7 (el coach se entera, no cobra), día 15; después decide la founder. Mensajes y paso a paso: skill Constructor de SOP.
- Cliente a 45 días del fin con salud Buena o mejor → coach (renovación).

## 7. Reglas de carga

- Ventas y cuotas, **solo por formulario** (uno de deals, uno de cuotas). El de cuotas solo deja elegir deals con cuotas pendientes.
- El closer carga estado, calificación y próximo paso el mismo día de la llamada.
- Administración acredita todos los días a las 10.
- Cuando alguien se va: inactivo en Equipo el mismo día y se reasignan sus leads, oportunidades y clientes.

## 8. Lo que se automatiza después

- Cierre en cuotas → crear las Cuotas programadas.
- Deal o cuota → movimientos en Finanzas (uno por método).
- Cierre acreditado → alta en Clientes y aviso al coach.
- Stripe del taller → Ventas directas.

## Decisiones del negocio que la base no resuelve

- ¿Comisión del closer sobre cash collected o sobre facturación? (La base calcula sobre cash; si se decide otra cosa, cambia la fórmula, no la estructura.)
- ¿Quién suspende el acceso por falta de pago y a los cuántos días?
- ¿El upsell al mastermind comisiona para el coach, para el closer o para los dos?

## Para confirmar

- [SUPUESTO: la reserva se descuenta del precio final, confirmalo con la founder]
- [SUPUESTO: el tipo de cambio del mes lo fija administración el día 1, confirmalo con administración]

---

¿Te lo bajo a pasos de construcción en Airtable? (Skill Arquitecto de Base en Airtable.) Para mostrarlo en tu portafolio, armá una copia con datos de prueba.
