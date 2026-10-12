# Ejemplo de output · Cierre de Mes Financiero

> Datos ficticios. Programa de 6 meses de inglés para profesionales de salud: USD 1.800 en un pago o 3 cuotas de USD 650 (USD 1.950); reserva de USD 250. Cobra por pasarela (USD), transferencia en dólares y transferencia en pesos. Tipo de cambio fijo de septiembre: 1 USD = 1.350 ARS (valor del caso). Equipo: 2 closers, 2 setters, 4 coaches pagados por alumno activo.

**Lo que dijo la persona:** "Hagamos el cierre de septiembre. Ya tengo todo: anuncios 4.200, alumnos activos al 30/09 son 120, agendas asistidas calificadas de los setters 46." Pegó el export de deals y cuotas cobradas de Airtable y los tres extractos.

---

# Cierre de septiembre 2026 · Programa de inglés (caso ficticio)

## Estado

**Cierre definitivo** (están los tres extractos). Pasos 0 a 4 hechos. **No escribí nada todavía.** Espero tu OK para el paso 5.

## Datos manuales

| Dato | A quién | Estado |
|---|---|---|
| Inversión en anuncios de septiembre | Dirección | ✅ USD 4.200 |
| Alumnos activos al 30/09 | Coordinación de servicio | ✅ 120 |
| Agendas asistidas calificadas por setter | Ventas | ✅ 46 (Setter 1: 25 · Setter 2: 21) |
| Factura del estudio contable | Administración | ⚠️ No llegó: se carga **proyectado** USD 400 |

## Prueba en seco (sin escribir)

**Antes de validar**, la base decía: cash collected USD 38.900 · facturación USD 35.700.

**Después de validar:**

| Concepto | Registros | USD |
|---|---|---|
| Reservas | 6 × 250 | 1.500 |
| Nuevos cierres en un pago | 8 × 1.800 | 14.400 |
| Nuevos cierres en cuotas (primer pago) | 10 × 650 | 6.500 |
| **Cash nuevo** | | **22.400** |
| Cuotas de ventas anteriores | 24 × 650 | 15.600 |
| **Cash collected total** | | **38.000** |
| Facturación (8 × 1.800 + 10 × 1.950) | 18 cierres | 33.900 |

## Validaciones

| N.° | Validación | Resultado |
|---|---|---|
| 1 | Comprobante no es pago | ⚠️ **2 registros sin acreditar:** una cuota de USD 650 (transferencia en pesos, comprobante del 28/09) y una reserva de USD 250 (pasarela, pago rechazado). Salen del cash: 38.900 → **38.000**. Quedan como alerta |
| 2 | Conciliación por método | ✅ Pasarela 21.400 + Transferencia USD 12.550 + Transferencia ARS 4.050 (5.467.500 ARS ÷ 1.350) = **38.000**. Coincide con los extractos |
| 3 | Facturación una vez, nunca en reservas | ⚠️ **1 reserva** tenía cargada facturación USD 1.800. Corregida en la prueba: 35.700 → **33.900** |
| 4 | Reserva previa descontada | ✅ Los 3 cierres que habían reservado tienen tildada la reserva previa |
| 5 | Primera cuota como cierre | ✅ |
| 6 | Todo en USD con tipo de cambio fijo | ✅ Los 7 pagos en pesos convertidos a 1.350; el monto en pesos está en su campo |
| 7 | Reembolsos como costo | ✅ 1 reembolso parcial de USD 900 cargado como egreso; la venta original sigue en la facturación de julio |
| 8 | Planes de cuotas modificados | ⚠️ 1 alumno pasó su cuota 3 de septiembre a octubre por chat; **el deal no está actualizado** (la proyección de octubre queda corta en USD 650) |
| 9 | Comisiones con responsable y regla | ✅ Closers 8 % del cash de nuevos cierres (regla vigente desde junio); setters USD 20 por agenda asistida calificada. La planilla de liquidación calcula sobre la misma base que el acuerdo (cash de nuevos cierres) y, cruzada registro por registro con la base, no tiene ventas duplicadas ni que falten |
| 10 | Gastos proyectados | ⚠️ 1 proyectado: estudio contable USD 400 |
| 11 | Consistencia entre tablas | ✅ Las 18 ventas del mes tienen el mismo medio de pago en deals y en cuotas, y la suma de cuotas de cada venta coincide con el monto contratado |

## Egresos del mes

| Concepto | Cálculo | USD | Estado |
|---|---|---|---|
| Equipo fijo | Según nómina vigente | 7.500 | Conciliado |
| Comisiones closers | 8 % × 20.900 (nuevos cierres) | 1.672 | Conciliado |
| Comisiones setters | 46 × 20 | 920 | Conciliado |
| Coaches | 120 alumnos activos × 25 | 3.000 | Conciliado |
| Pauta | Dato de dirección | 4.200 | Conciliado |
| Herramientas | Suscripciones del mes | 780 | Conciliado |
| Comisiones de pasarela y bancos | Según extractos | 1.140 | Conciliado |
| Reembolso parcial | 1 alumno | 900 | Conciliado |
| **Subtotal conciliado** | | **20.112** | |
| Estudio contable | Factura pendiente | 400 | **Proyectado** |
| **Total egresos** | | **20.512** | |

## Lo que se va a escribir (y espero tu OK)

1. En Deals: corregir la facturación de la reserva R-0912 (1.800 → vacío).
2. En Cuotas cobradas y Deals: marcar los 2 pagos sin acreditar como "No acreditado" (no se borran).
3. En Finanzas: los 8 egresos conciliados y el proyectado.
4. En la planilla de pagos al equipo: comisiones de closers (1.672), setters (920) y coaches (3.000), con el detalle por persona.
5. En el log: la línea del cierre de septiembre.

**No voy a tocar** el plan de cuotas del alumno que pasó la cuota (validación 8) hasta que el closer confirme la nueva fecha. ¿Corrijo las alertas antes o escribo así? **Necesito tu OK explícito.**

---

# Informe de cierre · septiembre 2026 (para el founder)

**En una frase:** entraron USD 38.000 y quedaron USD 17.488 (46 %): el margen está debajo del 50 % por la pauta y un reembolso, y el 41 % de lo que entró son cuotas de ventas anteriores, no ventas del mes.

## Ingresos

| | USD | % del cash |
|---|---|---|
| Reservas | 1.500 | 3,9 % |
| Nuevos cierres (primer pago) | 20.900 | 55,0 % |
| **Cash nuevo** | **22.400** | **58,9 %** |
| Cuotas de ventas anteriores | 15.600 | 41,1 % |
| **Cash collected** | **38.000** | 100 % |
| Facturación (18 cierres) | 33.900 | — |
| Primer pago de las ventas del mes sobre facturación del mes | 20.900 / 33.900 = **61,7 %** | — |

## Egresos

Conciliados USD 20.112 + proyectados USD 400 = **USD 20.512**. Lo que más pesa: equipo fijo (7.500), pauta (4.200) y coaches (3.000).

## Margen

| | USD | % sobre cash |
|---|---|---|
| Con proyectados | 38.000 − 20.512 = **17.488** | **46,0 %** |
| Sin proyectados | 38.000 − 20.112 = 17.888 | 47,1 % |

Referencia que se usa en el programa: arriba de 60 % es sano, alrededor de 50 % es mejorable. Este mes está debajo.

## Alertas y pendientes

1. **USD 900 sin acreditar** (una cuota y una reserva). Administración contacta hoy; si se acreditan, entran en octubre.
2. **Plan de cuotas desactualizado** de un alumno: la proyección de octubre queda corta en USD 650 hasta que se corrija.
3. **Reembolso de USD 900:** segundo en tres meses. Vale revisar el motivo con servicio.
4. **Factura contable pendiente** (USD 400 proyectados).

## Decisiones que necesito

1. ¿Seguimos con USD 4.200 de pauta en octubre? Antes de decidir, conviene ver qué anuncio vende (skill Rentabilidad por Anuncio).
2. ¿Escribimos la regla de tipo de cambio en los contratos nuevos? Hoy está solo en este cierre.

---

**Log del cierre (lo que se anota):**

```
2026-09 · Cash 38.000 (nuevo 22.400 · cuotas 15.600) · Facturación 33.900 · Egresos 20.512 (400 proyectados) · Margen 46,0 %
Trampas nuevas: reserva con facturación cargada (R-0912); cuota pasada de mes por chat sin actualizar el deal.
Decisión pendiente: pauta de octubre.
```
