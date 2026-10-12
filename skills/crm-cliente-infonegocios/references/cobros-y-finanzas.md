# Cobros y finanzas · cómo se carga cada peso

> Referencia de la skill CRM de Cliente para Infonegocios (RealOps™). Modelo financiero de las bases de muestra de MG Operations.

## 1. Todos los tipos de cobro y dónde van

Cada plata que entra encaja en **un solo** caso.

| # | Tipo de cobro | Qué es | Da acceso | Tabla | Cómo se carga | Suma a |
|---|---|---|---|---|---|---|
| 1 | **Reserva** | Pago parcial para "guardar el lugar", bajo el mínimo de acceso | No | Deals + Reservas (Naturaleza = Reserva) | Formulario de deals | Cash nuevo. **No** suma facturación |
| 2 | **Pago completo** | Todo el ticket en una operación | Sí | Deals (Nuevo cierre · Pago completo) | Formulario de deals | Facturación y cash nuevo (iguales) |
| 3 | **Primera cuota** | Primer pago de un plan en cuotas; define el plan | Sí | Deals (Nuevo cierre · Cuotas) + crea las Cuotas programadas | Formulario de deals | Facturación (el ticket entero) y cash nuevo (solo lo que entró) |
| 4 | **Cuota siguiente** | Pago 2°, 3°… de un cierre existente | Ya tenía | Cuotas cobradas (vinculada a su cuota programada) | Formulario de cuotas | Cash de cuotas. **No** suma facturación ni cash nuevo |
| 5 | **Upsell / renovación / downsell** | Venta nueva a un cliente | Sí (al producto nuevo) | Deals (Tipo de venta = Upsell / Renovación / Downsell), con su oportunidad | Formulario de deals | Facturación y cash nuevo, separables por Tipo de venta |
| 6 | **Recurrencia** | Cobro mensual de una membresía o suscripción | Mantiene | Deals (Naturaleza = Recurrencia) el primer mes; Cuotas cobradas los siguientes | Integración de la pasarela | Cash de recurrencia (reportalo aparte del cash nuevo) |
| 7 | **Venta directa** | Checkout sin llamada: low ticket, entrada a evento | Sí | Ventas directas | Integración de la pasarela | Cash de ventas directas |
| 8 | **Reembolso** | Devolución total o parcial | Lo pierde | Se marca en el Deal (Reembolso + monto) y entra como **egreso** en Finanzas | Administración | Resta del resultado, **no** borra la venta |

**Errores que más se repiten**
1. Cargar la primera cuota en Cuotas cobradas: no se dispara el onboarding y el cierre no cuenta como venta. La 1ª va en Deals.
2. Cargar facturación en una reserva: infla el mes.
3. Cash collected igual a facturación en un cierre en cuotas: está mal cargado.
4. No tildar "Pagó reserva" cuando la reserva cierra: el saldo pendiente queda mal.
5. Contar comprobantes como pagos: hasta que administración marca "Acreditado", no es plata.

## 2. Dos bloques de dinero en cada cobro

| Bloque | En qué moneda | Para qué | Campos |
|---|---|---|---|
| **Comercial** | Siempre USD | KPIs, comisiones, tableros, comparar meses | Facturación (USD), Cash collected (USD) |
| **Financiero** | La moneda real de cada método | Conciliar con el extracto del banco o la pasarela | Método 1 · 2 · 3 y su monto en moneda real, quién recibió, comprobante |

**Hasta 3 métodos por operación** (caso real: parte por transferencia, parte por billetera, parte en efectivo). Si un cliente paga con más de tres, se carga una segunda operación.

**Tipo de cambio:** se fija **uno por mes y por moneda** (lo define administración en el cierre de mes) y se usa para pasar a USD. Nunca un tipo de cambio distinto por cada carga.

## 3. Finanzas: un movimiento por método

La tabla 🪙 Finanzas es la vista contable: **un registro por cada método de pago no vacío**, en su moneda real.

- **Ingresos:** no se cargan a mano. Una automatización, al crearse un registro en Deals, en Cuotas cobradas o en Ventas directas, crea 1, 2 o 3 movimientos (uno por método con monto). Así **no hay doble carga** y cada movimiento queda vinculado a su origen.
- **Egresos:** se cargan a mano o por formulario (sueldos, comisiones, herramientas, publicidad, impuestos, reembolsos, retiros).
- **Lo que ya estaba cargado** antes de la automatización se pasa con una carga masiva (filtrando solo registros con comprobante).

Receta de la automatización (nativa de Airtable, sin código):

```
Disparador: se crea un registro en Deals + Reservas (o en Cuotas cobradas)
Acción: lógica condicional
  Si Método 3 y Monto 3 tienen dato → crear 3 movimientos (MP1, MP2, MP3)
  Si no, si Método 2 y Monto 2 tienen dato → crear 2 movimientos
  Si no, si Método 1 y Monto 1 tienen dato → crear 1 movimiento
Cada movimiento: Tipo = Ingreso · Fecha = Fecha del pago · Monto = monto del método ·
  Método = método · Cliente = nombre · Concepto = producto y tipo de cobro ·
  Comprobante · Origen = vínculo al registro que lo disparó
```

Ojo con dos cosas: las automatizaciones nativas solo corren sobre registros nuevos, y cada corrida cuenta para el límite del plan.

## 4. Cuotas esperadas: dos formas

| | A · Columnas en el deal | B · Tabla Cuotas programadas (recomendada) |
|---|---|---|
| Cómo es | Campos "Fecha proyectada 2da cuota", "Monto 2da cuota"… hasta la 5ª en el deal | Una fila por cuota esperada, vinculada al deal |
| Sirve si | Planes de hasta 5 cuotas, fijos, poco volumen | Cualquier plan, renegociaciones, más de 5 cuotas |
| Morosidad | Fórmula larga de "próxima cuota" y un estado que se mueve a mano | Estado y días de atraso por fórmula, por cuota |
| Proyección de caja | Una fórmula por mes (y se rompe al cambiar de año si el año está fijo) | Una vista agrupada por "Mes de vencimiento" |
| Renegociar | Hay que reescribir varias columnas | Se cambia la fecha de la cuota y queda nota |

Si la base ya usa la forma A y funciona, no se rehace de golpe: se agrega la tabla B para los cierres nuevos y se migra lo abierto cuando haya tiempo. **Nunca** fórmulas de proyección con el año escrito adentro.

## 5. Esqueleto del protocolo de cuota vencida

Acá se define **qué registra la base**; los mensajes y el paso a paso van en la skill **Constructor de SOP**, y la conciliación del mes en **Cierre de Mes Financiero**.

| Día | Qué pasa | Quién | Qué se registra |
|---|---|---|---|
| −3 | Aviso previo con link de pago | Responsable de cobro | Último aviso |
| 1 | Primer aviso | Responsable de cobro | Avisos enviados = 1 |
| 7 | Segundo aviso; el coach se entera (no cobra) | Responsable de cobro | Avisos = 2 · Cliente pasa a "En riesgo" |
| 15 | Último aviso | Responsable de cobro | Avisos = 3 |
| 15 + | Decide: pausar acceso, plan de pago nuevo o baja | El founder o quien tenga la regla escrita | Estado del cliente · Nota de renegociación |

**Decisión del negocio, no de la base:** quién pausa el acceso y a los cuántos días. Si no está decidido, va a "Decisiones del negocio que la base no resuelve".
