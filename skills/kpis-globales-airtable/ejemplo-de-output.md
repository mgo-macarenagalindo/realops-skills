# Ejemplo de output · Tabla de KPIs Globales en Airtable

> Datos ficticios. Programa de 4 meses de finanzas personales para profesionales, vendido por llamada: USD 2.000 en un pago o 3 cuotas de USD 700 (USD 2.100), con reserva de USD 300. Canales: Instagram orgánico, Pauta y YouTube, con UTMs que llegan por Zapier desde la agenda. 2 closers.

**Lo que pegó la persona:** las tablas de su base (Agendas, Ventas, Reservas, Cuotas, Canales, Reporte) y el pedido del founder: "quiero ver cada mes, por canal, agendas, asistencia, cierre y cuánta plata entró, sin que nadie lo cuente".

---

# KPIs globales · Programa de finanzas personales (caso ficticio)

## Qué va a responder la tabla

Por mes y por canal: agendas, asistidas, no show, canceladas, cierres, facturación, cash nuevo (reservas + nuevos cierres), cuotas de ventas anteriores, cash total, asistencia, las dos tasas de cierre y cash nuevo por agenda.

## Las tres tablas núcleo

| Hoy | Pasa a |
|---|---|
| Agendas | **Agendas** (se queda) |
| Ventas + Reservas | **Deals y reservas** (una sola tabla con `Naturaleza`) |
| Cuotas | **Cuotas cobradas** (solo pagos 2.° y 3.°; la 1.ª cuota es el cierre) |
| Canales | Se oculta: el canal sale de la fórmula de UTMs |
| Reporte | Se oculta: lo reemplaza **KPIs globales** |

Campos que se agregan:
- Agendas: separar el campo `Estado` en `Estado de la llamada` (Asistió · No show · Cancelada · Reprogramada) y `Estado del lead` (Seguimiento · Cierre ganado · Cierre perdido).
- Deals y reservas: `Naturaleza` (Reserva · Cierre), `Facturación USD` (vacío en reservas; 2.000 o 2.100 según el plan) y `Cash collected USD` (lo que entró hoy: 300, 700 o 2.000).
- Cuotas cobradas: `Canal (del deal)` como lookup.

## La clave

| Tabla | Fórmula `Clave KPI` |
|---|---|
| Agendas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha de la llamada}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & {Canal}` |
| Deals y reservas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & {Canal}` |
| Cuotas cobradas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha de pago}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & ARRAYJOIN({Canal (del deal)}, "")` |

Resultado esperado en las tres: `2026-10 / Pauta`. Probalo copiando la clave de un registro de cada tabla en un bloc de notas: tienen que ser idénticas.

## La tabla KPIs globales

| Campo | Tipo | Cálculo |
|---|---|---|
| Clave | Texto (primario) | Automatización |
| Agendas / Deals / Cuotas | Vínculos | Automatización |
| Agendas totales | Conteo | Agendas |
| Asistidas | Conteo con condición | Estado de la llamada = Asistió |
| No show | Conteo con condición | Estado de la llamada = No show |
| Canceladas | Conteo con condición | Estado de la llamada = Cancelada |
| Cierres | Rollup con condición | Naturaleza = Cierre · `COUNTALL(values)` |
| Facturación USD | Rollup | `SUM(values)` de Facturación USD |
| Reservas USD | Rollup con condición | Naturaleza = Reserva · `SUM(values)` de Cash collected USD |
| Nuevos cierres USD | Rollup con condición | Naturaleza = Cierre · `SUM(values)` de Cash collected USD |
| Cuotas USD | Rollup | `SUM(values)` de Monto USD |
| Cash nuevo USD | Fórmula | `{Reservas USD} + {Nuevos cierres USD}` |
| Cash total USD | Fórmula | `{Cash nuevo USD} + {Cuotas USD}` |
| Asistencia | Fórmula | `IF({Agendas totales}, {Asistidas} / {Agendas totales})` |
| Cierre sobre asistidas | Fórmula | `IF({Asistidas}, {Cierres} / {Asistidas})` |
| Cierre sobre agendas | Fórmula | `IF({Agendas totales}, {Cierres} / {Agendas totales})` |
| Cash nuevo por agenda | Fórmula | `IF({Agendas totales}, {Cash nuevo USD} / {Agendas totales})` |

## La automatización (una por tabla)

**"KPI · vincular agenda"** (igual para Deals y Cuotas, cambiando la tabla):

1. Disparador: cuando un registro de Agendas cumple condiciones → `Clave KPI` no está vacía.
2. Buscar registros → tabla KPIs globales → condición `Clave` es igual a `Clave KPI` (del paso 1).
3. Condición → si el paso 2 encontró registros:
   - Actualizar registro → Agendas → el registro del paso 1 → `KPIs globales` = IDs encontrados en el paso 2.
4. Si no:
   - Crear registro → KPIs globales → `Clave` = `Clave KPI` (del paso 1).
   - Actualizar registro → Agendas → el registro del paso 1 → `KPIs globales` = ID del registro creado.

## Plan de prueba

En una copia de la base, con datos inventados:

| # | Prueba | Resultado esperado |
|---|---|---|
| 1 | Crear una agenda de octubre con canal Pauta | Se crea la fila `2026-10 / Pauta` y la agenda queda vinculada |
| 2 | Crear otra agenda de octubre, Pauta | **No** se crea otra fila: se vincula a la misma |
| 3 | Crear una agenda sin canal y cargarle el canal 5 minutos después | Se vincula al cargar el canal |
| 4 | Crear una reserva de 300 en Pauta | Reservas USD = 300; Facturación USD no cambia |
| 5 | Crear una cuota cobrada de noviembre de un deal de octubre de Pauta | Va a `2026-11 / Pauta` (mes del pago, canal del deal) |
| 6 | Contar a mano las agendas asistidas de la fila y compararlas con el conteo | Coinciden |

## Cómo se ve un mes (datos de prueba)

**Octubre 2026:**

| Clave | Agendas | Asistidas | No show | Canceladas | Cierres | Facturación | Reservas | Nuevos cierres | Cuotas | Cash total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10 / Instagram orgánico | 50 | 34 | 10 | 6 | 9 | 18.400 | 600 | 12.800 | 4.900 | 18.300 |
| 2026-10 / Pauta | 80 | 30 | 38 | 12 | 4 | 8.300 | 900 | 4.100 | 2.100 | 7.100 |
| 2026-10 / YouTube | 20 | 15 | 3 | 2 | 4 | 8.200 | 0 | 5.400 | 1.400 | 6.800 |
| 2026-10 / Sin dato | 6 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total del mes** | **156** | **81** | **54** | **21** | **17** | **34.900** | **1.500** | **22.300** | **8.400** | **32.200** |

De dónde salen los montos de prueba:
- Instagram: 5 cierres en un pago (5 × 2.000) + 4 en cuotas (primer pago 4 × 700) = 12.800 de nuevos cierres; facturación 5 × 2.000 + 4 × 2.100 = 18.400; 2 reservas × 300; 7 cuotas de ventas anteriores × 700 = 4.900.
- Pauta: 1 en un pago + 3 en cuotas = 2.000 + 2.100 = 4.100; facturación 2.000 + 3 × 2.100 = 8.300; 3 reservas × 300; 3 cuotas × 700.
- YouTube: 2 en un pago + 2 en cuotas = 4.000 + 1.400 = 5.400; facturación 4.000 + 2 × 2.100 = 8.200; 2 cuotas × 700.

| Clave | Asistencia | Cierre s/ asistidas | Cierre s/ agendas | Cash nuevo | Cash nuevo por agenda |
|---|---|---|---|---|---|
| Instagram orgánico | 68,0 % | 26,5 % | 18,0 % | 13.400 | 268 |
| Pauta | 37,5 % | 13,3 % | 5,0 % | 5.000 | 62,5 |
| YouTube | 75,0 % | 26,7 % | 20,0 % | 5.400 | 270 |
| Sin dato | 33,3 % | 0 % | 0 % | 0 | 0 |
| **Total** | **51,9 %** | **21,0 %** | **10,9 %** | **23.800** | **152,6** |

(La fila "Sin dato" aparece porque esas 6 agendas tienen canal "Sin dato" desde la fórmula de UTMs. Es una señal de tracking, no un canal.)

Leer qué significan estos números (por ejemplo, que la pauta llena la agenda de gente que no asiste) es trabajo de la skill **Analista de KPIs**.

## Lo que queda afuera y por qué

- **Gastos y margen:** se suman al cierre de mes (skill **Cierre de Mes Financiero**), no a esta tabla, hasta que la carga de gastos esté ordenada.
- **Calificación del lead:** hoy los closers no la cargan. Cuando exista el campo (Alta · Media · Baja · No calificado), se agrega un conteo con condición.
- **Reprogramadas:** se cuentan en Agendas totales pero no en asistidas ni en no show. En este mes de prueba son 0.
