# Ejemplo de output · Tabla de KPIs Globales en Airtable

> Datos ficticios. Programa de 4 meses de finanzas personales para profesionales, vendido por llamada: USD 2.000 en un pago o 3 cuotas de USD 700 (USD 2.100), con reserva de USD 300. Canales: Instagram orgánico, Pauta y YouTube, con UTMs que llegan por Zapier desde la agenda. 2 closers.

**Lo que pegó la persona:** las tablas de su base (Agendas, Ventas, Reservas, Cuotas, Canales, Reporte), el export semanal de Meta y el pedido del founder: "quiero ver cada mes, por canal, agendas, asistencia, cierre, cuánta plata entró y cuánto me cuesta cada venta de pauta, sin que nadie lo cuente". La tabla Cuotas trae solo los pagos 2.° y 3.° (la 1.ª está en Ventas). Hay cuotas de alumnos de antes de las UTMs, sin canal. La base está en un plan pago.

---

# KPIs globales · Programa de finanzas personales (caso ficticio)

## Qué va a responder la tabla

Por mes y por canal: agendas, asistidas, no show, canceladas, cierres, facturación, cash nuevo (reservas + nuevos cierres), cuotas de ventas anteriores, cash total, asistencia, las dos tasas de cierre, cash nuevo por agenda y, para pauta, gasto y costo por venta.

Decisiones que habilita: dónde poner la pauta (costo por venta, no por agenda), si el mes creció por ventas nuevas o por cuotas viejas, y si el problema de un canal es de asistencia o de cierre.

## Las tres tablas núcleo

| Hoy | Pasa a |
|---|---|
| Agendas | **Agendas** (se queda) |
| Ventas + Reservas | **Deals y reservas** (una sola tabla con `Naturaleza`) |
| Cuotas | **Cuotas cobradas** (solo pagos 2.° y 3.°; la 1.ª cuota es el cierre) |
| Canales | Se oculta: el canal sale de la fórmula de UTMs |
| Reporte | Se oculta: lo reemplaza **KPIs globales** |
| (nueva) | **Gasto por anuncio**: una fila por semana y anuncio, importada del export de Meta |

Campos que se agregan:
- Agendas: separar el campo `Estado` en `Estado de la llamada` (Asistió · No show · Cancelada · Reprogramada) y `Estado del lead` (Seguimiento · Cierre ganado · Cierre perdido).
- Deals y reservas: `Naturaleza` (Reserva · Cierre), `Facturación USD` (vacío en reservas; 2.000 o 2.100 según el plan) y `Cash collected USD` (lo que entró hoy: 300, 700 o 2.000).
- Cuotas cobradas: `Canal (del deal)` como lookup. Como la tabla trae solo pagos posteriores al primero, el cash nuevo sale de Deals y no hay doble conteo (Paso 2b, primera fila).
- Agendas y Deals: canal de pauta con anuncio (`Pauta · VSL-1`, `Pauta · VSL-2`) para tener costo por venta por anuncio.

## La clave

| Tabla | Fórmula `Clave KPI` |
|---|---|
| Agendas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha de la llamada}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & IF({Canal}, {Canal}, "Sin canal")` |
| Deals y reservas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & IF({Canal}, {Canal}, "Sin canal")` |
| Cuotas cobradas | `DATETIME_FORMAT(SET_TIMEZONE({Fecha de pago}, 'America/Argentina/Buenos_Aires'), 'YYYY-MM') & " / " & IF(ARRAYJOIN({Canal (del deal)}, ""), ARRAYJOIN({Canal (del deal)}, ""), "Sin canal")` |
| Gasto por anuncio | `DATETIME_FORMAT({Inicio de la semana}, 'YYYY-MM') & " / " & {Canal}` |

Resultado esperado en todas: `2026-10 / Pauta · VSL-1`. Una cuota de un alumno de antes de las UTMs da `2026-10 / Sin canal` y **entra** al cash del mes. Probalo copiando la clave de un registro de cada tabla en un bloc de notas: tienen que ser idénticas.

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
| Gasto USD | Rollup | `SUM(values)` de Gasto USD |
| Costo por venta | Fórmula | `IF({Cierres}, {Gasto USD} / {Cierres}, IF({Gasto USD}, "Gasto sin ventas", ""))` |

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
| 7 | Crear una cuota cobrada de un deal sin canal | Va a `2026-10 / Sin canal` y suma en Cash total del mes |
| 8 | Importar una semana de gasto de VSL-1 | Gasto USD de `2026-10 / Pauta · VSL-1` sube en ese monto; Costo por venta se recalcula |
| 9 | Sumar el cash total del mes y compararlo con los pagos del mes en el banco o la pasarela | Coinciden (si da más, hay doble conteo) |

## Cómo se ve un mes (datos de prueba)

**Octubre 2026:**

| Clave | Agendas | Asistidas | No show | Canceladas | Cierres | Facturación | Reservas | Nuevos cierres | Cuotas | Cash total | Gasto |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10 / Instagram orgánico | 50 | 34 | 10 | 6 | 9 | 18.400 | 600 | 12.800 | 4.900 | 18.300 | — |
| 2026-10 / Pauta · VSL-1 | 30 | 17 | 9 | 4 | 4 | 8.300 | 300 | 4.100 | 1.400 | 5.800 | 1.600 |
| 2026-10 / Pauta · VSL-2 | 50 | 13 | 29 | 8 | 0 | 0 | 600 | 0 | 700 | 1.300 | 1.900 |
| 2026-10 / YouTube | 20 | 15 | 3 | 2 | 4 | 8.200 | 0 | 5.400 | 1.400 | 6.800 | — |
| 2026-10 / Sin canal | 6 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 2.100 | 2.100 | — |
| **Total del mes** | **156** | **81** | **54** | **21** | **17** | **34.900** | **1.500** | **22.300** | **10.500** | **34.300** | **3.500** |

De dónde salen los montos de prueba:
- Instagram: 5 cierres en un pago (5 × 2.000) + 4 en cuotas (primer pago 4 × 700) = 12.800 de nuevos cierres; facturación 5 × 2.000 + 4 × 2.100 = 18.400; 2 reservas × 300; 7 cuotas de ventas anteriores × 700 = 4.900.
- Pauta · VSL-1: 1 en un pago + 3 en cuotas = 2.000 + 2.100 = 4.100; facturación 2.000 + 3 × 2.100 = 8.300; 1 reserva × 300; 2 cuotas × 700.
- Pauta · VSL-2: 0 cierres; 2 reservas × 300; 1 cuota × 700.
- YouTube: 2 en un pago + 2 en cuotas = 4.000 + 1.400 = 5.400; facturación 4.000 + 2 × 2.100 = 8.200; 2 cuotas × 700.
- Sin canal: 3 cuotas × 700 de alumnos que compraron antes de las UTMs. Con la regla vieja ("sin canal no entra") estos 2.100 desaparecían del cash del mes.

| Clave | Asistencia | Cierre s/ asistidas | Cierre s/ agendas | Cash nuevo | Cash nuevo por agenda | Costo por agenda | Costo por venta |
|---|---|---|---|---|---|---|---|
| Instagram orgánico | 68,0 % | 26,5 % | 18,0 % | 13.400 | 268 | — | — |
| Pauta · VSL-1 | 56,7 % | 23,5 % | 13,3 % | 4.400 | 146,7 | 53,3 | **400** |
| Pauta · VSL-2 | 26,0 % | 0 % | 0 % | 600 | 12 | **38** | **Gasto sin ventas** |
| YouTube | 75,0 % | 26,7 % | 20,0 % | 5.400 | 270 | — | — |
| Sin canal | 33,3 % | 0 % | 0 % | 0 | 0 | — | — |
| **Total** | **51,9 %** | **21,0 %** | **10,9 %** | **23.800** | **152,6** | | |

## Cómo leer cada dato (para este negocio)

| Dato | Qué pregunta responde | A quién le sirve | Qué mirar este mes |
|---|---|---|---|
| Agendas por canal | ¿De dónde viene el volumen? | Marketing, founder | VSL-2 trae 50 agendas, la tercera parte del total |
| Asistencia | ¿Llegan a la llamada? | Líder comercial, operaciones | VSL-2: 26 %. Es ese anuncio, no los recordatorios (orgánico y YouTube están bien) |
| Cierre s/ asistidas vs s/ agendas | ¿Es el closer o es el canal? | Líder comercial, marketing | Los closers cierran 26 % en orgánico: el problema de pauta no es la llamada |
| Facturación vs cash total | ¿Entra lo vendido? | Founder, contador | Se facturó 34.900 y entró 34.300, pero 10.500 son cuotas viejas |
| Costo por agenda vs costo por venta | ¿Qué anuncio trae clientes? | Marketing | VSL-2 es el más barato por agenda (38) y no vendió nada |
| Sin canal | ¿Funciona el tracking? | Operaciones | 6 agendas nuevas sin canal: revisar el link de agenda |

**Tres casos de uso para este founder:**
1. **La decisión de pauta:** con 6 semanas de datos, pausar o rehacer VSL-2 en lugar de escalarlo. Llevale la fila de costo por venta.
2. **La reunión de los lunes con el tablero abierto:** cash del mes con cuotas separadas, agendas y asistencia por canal, y vencidas.
3. **"¿Crecimos o cobramos cuotas?":** el 30 % del cash fue de cuotas viejas. Si sube, la adquisición se está frenando.

Leer qué significan estos números (por ejemplo, que la pauta llena la agenda de gente que no asiste) es trabajo de la skill **Analista de KPIs**.

## Lo que queda afuera y por qué

- **Gastos y margen:** se suman al cierre de mes (skill **Cierre de Mes Financiero**), no a esta tabla, hasta que la carga de gastos esté ordenada.
- **Calificación del lead:** hoy los closers no la cargan. Cuando exista el campo (Alta · Media · Baja · No calificado), se agrega un conteo con condición.
- **Reprogramadas:** se cuentan en Agendas totales pero no en asistidas ni en no show. En este mes de prueba son 0.
- **Morosidad:** es un stock al corte, no un número de mes y canal. Va en la vista "Vencidas" de Cuotas y en un número de la interfaz.

## Para confirmar

- Que el gasto semanal de Meta se pueda exportar por día (con quien maneja la pauta), para que no haya semanas partidas entre meses.
