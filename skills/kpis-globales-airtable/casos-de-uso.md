# Casos de uso · Tabla de KPIs Globales en Airtable

Cinco situaciones de infonegocio donde los números del mes dejan de contarse a mano y empiezan a usarse para decidir. Negocios y nombres ficticios.

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

---

## 4. La tabla de pagos trae todo, y el cash da de más

**La situación.** La tabla de cuotas tiene una fila por cada pago esperado (pago único, cuota 1, 2 y 3, cobrados o no) y además el closer carga el primer pago en Ventas. El cash de septiembre da US$12.000 más que lo que entró al banco. Y las cuotas de alumnos viejos, sin canal, no aparecen.

**Qué le pasás.** Las dos tablas y cómo se carga cada una.

**Qué te devuelve.** La regla para no contar dos veces la primera cuota (todo el cash sale de Pagos, con un campo que separa "nuevo cierre" de "cuota anterior"), la fila "Sin canal" para que la plata vieja entre al mes, la validación contra el banco y, si la base está en el plan gratuito, la alternativa manual (pegar las claves una vez por semana desde una vista de control) y cuándo conviene pagar.

**Por qué sirve.** Un tablero que da distinto que el banco pierde la confianza del founder en una semana.

---

## 5. "Ya la armé. ¿Y ahora qué le digo al founder?"

**La situación.** La tabla funciona, el founder la abre una vez y no la vuelve a mirar.

**Qué le pasás.** Lo que el founder preguntó en la última reunión y la tabla del mes.

**Qué te devuelve.** Para qué sirve cada dato, a quién le sirve y cuándo prende una alarma (orientativa); el primer nivel de setters, servicio y operaciones si ellos también miran; tres casos de uso para ese negocio (por ejemplo, la reunión de los lunes con el tablero abierto, la decisión de pauta por costo por venta y la pregunta "¿crecimos o cobramos cuotas?"), y cómo presentárselo: una frase, tres números, una decisión.

**Por qué sirve.** El dueño no paga por un tablero: paga por las decisiones que toma con él. Construir, analizar, accionar.
