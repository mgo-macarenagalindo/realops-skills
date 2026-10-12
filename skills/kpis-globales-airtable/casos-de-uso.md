# Casos de uso · Tabla de KPIs Globales en Airtable

Tres situaciones de infonegocio donde los números del mes dejan de contarse a mano. Negocios y nombres ficticios.

---

## 1. Siete tablas y ningún número confiable

**La situación.** Una academia de marketing tiene en Airtable siete tablas (Agendas, Ventas, Reservas, Pagos proyectados, Canales, Cuotas, Reporte mensual). El reporte mensual lo arma la coordinadora contando registros con filtros. Tarda un día y cada mes da distinto.

**Qué le pasás.** La lista de tablas con sus campos y cómo entra el dato a cada una.

**Qué te devuelve.** La simplificación a tres tablas núcleo (lo demás pasa a vistas o se oculta), la fórmula de clave idéntica en las tres, la tabla KPIs globales con conteos y rollups con condición, la automatización de buscar o crear la fila y el plan de prueba con registros inventados.

**Por qué sirve.** El reporte del mes por canal se arma solo. Clase 10/06.

---

## 2. "La automatización encuentra cero registros"

**La situación.** Armaste la tabla de KPIs, pero la automatización siempre cae en "no encontró" y crea filas duplicadas para el mismo mes y canal.

**Qué le pasás.** Las fórmulas de clave de cada tabla y cómo se carga el canal.

**Qué te devuelve.** La diferencia carácter por carácter: en Agendas el mes sale como `2026-10` y en Deals como `Octubre 2026`; en Cuotas el canal viene de un lookup sin convertir. Las tres fórmulas unificadas, el disparador corregido ("cumple condiciones", porque el canal se carga después) y cómo unir las filas duplicadas sin borrar vínculos.

**Por qué sirve.** Es la falla más común de este sistema. Clase 15/06.

---

## 3. Del tablero en pesos y dólares a uno solo en dólares

**La situación.** Un programa cobra en tres monedas. El tablero suma pesos con dólares y el founder no le cree a ningún número.

**Qué le pasás.** Cómo cargan los montos hoy y en qué moneda piensa el founder.

**Qué te devuelve.** La regla de moneda (el closer carga en USD, o tipo de cambio fijo del mes), los campos de monto USD que alimentan la tabla de KPIs y el monto en moneda real que queda aparte para conciliar. Más la facturación real según el plan de cada cliente, no el precio de lista.

**Por qué sirve.** Un tablero con monedas mezcladas no se lee. Clase 07/10.
