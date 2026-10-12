# Fórmulas que siempre aparecen

> Referencia de la skill Arquitecto de Base en Airtable (RealOps™). Cambiá los nombres entre llaves por los de la base de la persona; confirmalos antes de dar la fórmula.

## Fechas y meses

```
// Mes (para agrupar y para claves). Siempre año + mes: nunca solo el mes
DATETIME_FORMAT({Fecha}, 'YYYY-MM')

// Días desde que entró (0 si ya se trabajó)
IF({Estado} = "Nuevo", DATETIME_DIFF(TODAY(), {Fecha de ingreso}, 'days'), 0)

// Días hasta el fin de un contrato (renovaciones)
DATETIME_DIFF({Fecha fin de contrato}, TODAY(), 'days')

// Ventana de renovación
IF(AND({Días hasta el fin} <= 60, {Días hasta el fin} >= 0), "En ventana", "")
```

## Cuotas y cobros

```
// Estado de una cuota
IF({Fecha de pago}, "Pagada",
  IF(IS_BEFORE({Vencimiento}, TODAY()), "Vencida",
    IF(DATETIME_DIFF({Vencimiento}, TODAY(), 'days') <= 7, "Por vencer", "Al día")))

// Días de atraso (0 si no está vencida)
IF(AND({Fecha de pago} = BLANK(), IS_BEFORE({Vencimiento}, TODAY())),
   DATETIME_DIFF(TODAY(), {Vencimiento}, 'days'), 0)

// Cumplimiento de un pago contra su vencimiento
IF({Fecha de pago},
  IF(IS_BEFORE({Fecha de pago}, {Vencimiento}), "Pagó adelantado",
    IF(IS_SAME({Fecha de pago}, {Vencimiento}, 'day'), "A tiempo", "Con demora")), "")

// Monto en USD desde la moneda real (tipo de cambio del mes, cargado como número)
IF({Moneda} = "USD", {Monto}, IF({Tipo de cambio}, ROUND({Monto} / {Tipo de cambio}, 2), BLANK()))

// Saldo pendiente
IF({Facturación (USD)}, {Facturación (USD)} - {Total pagado (USD)}, 0)
```

## Claves para tablas de resumen

```
// Mes | canal (KPIs por canal). El canal nunca vacío
DATETIME_FORMAT({Fecha}, 'YYYY-MM') & " | " & IF({Canal}, {Canal}, "Sin canal")

// Persona | mes (EOD y KPIs por persona). Persona como vínculo a Equipo
ARRAYJOIN({Persona}) & " | " & DATETIME_FORMAT({Fecha}, 'YYYY-MM')
```

La tabla de resumen tiene una fila por clave. Una automatización nativa, al crearse el registro de origen: **busca** la fila con esa clave (acción "Find records"), si no existe la **crea**, y **vincula** el registro de origen. Después, conteos y rollups con condición en la tabla de resumen.

## Personas y comisiones

```
// Comisión leyendo el porcentaje desde Equipo (lookup), sin nombres en la fórmula
IF(OR({Reembolso} = "Total", NOT({Acreditado})), 0,
   {Cash collected (USD)} * {% comisión closer (lookup)})
```

Si el lookup trae una lista, envolvelo: `VALUE(ARRAYJOIN({% comisión closer (lookup)}))` o usá un rollup con `MAX(values)`.

## Tasas (en tablas de resumen)

```
IF({Asistidas} > 0, {Cierres} / {Asistidas}, BLANK())          // campo en formato porcentaje
IF({Agendadas} > 0, {No show} / {Agendadas}, BLANK())
```

Usá `BLANK()` y no "sin dato" como texto: así el campo sigue siendo numérico y se puede graficar.

## Si una fórmula da error

1. Pedí el mensaje exacto y el tipo de cada campo que usa.
2. Errores típicos: el campo es un lookup (devuelve lista: usá `ARRAYJOIN` o un rollup); la fecha está vacía (envolvé en `IF({Fecha}, …)`); el nombre del campo cambió; hay un año escrito a mano.
3. Probá la fórmula con 3 registros cuyo resultado conocés.
