# Leer una encuesta de satisfacción (Modo 3)

> Referencia de la skill **Analista de KPIs** (RealOps™). Se carga siempre que haya una encuesta o entrevistas de alumnos. Sale de las clases del 18/03 (datos de retención y encuesta), 29/04 (medir a mitad de camino y NPS) y 22/06 (alumnos en riesgo con contexto). Los umbrales marcados como **orientativos** son criterio de MG Operations, no estándar.

La encuesta dice **qué sienten**; la base, **qué hacen y qué deben**. Una encuesta leída sola casi siempre da mejor de lo que está el servicio: la contestan los más contentos y la lee quien la armó.

## Paso 1 · Cómo se hizo (antes de mirar un número)

| Pregunta | Por qué importa |
|---|---|
| ¿A cuántos se mandó y en qué fecha? | Sin eso no hay **tasa de respuesta** ni sesgo de no respuesta |
| ¿Por qué canal y con cuántos recordatorios? | Explica quién respondió |
| ¿Es anónima? ¿Pide un ID o solo el mail? | Si es anónima, no se cruza con conducta: se lee sola y se dice |
| ¿Deja responder más de una vez? | Si sí, buscá duplicados |
| ¿Dónde viven las respuestas? | En la cuenta personal de alguien es un riesgo (se va la persona, se va la encuesta) y un hallazgo de accesos |
| ¿Qué escala usa cada pregunta? | 0 a 10 para NPS; 1 a 5 o 1 a 10 para áreas. No mezcles escalas en un promedio |

## Paso 2 · Limpiar

1. **Duplicados:** misma persona (mismo mail o mismo ID) más de una vez. Quedate con la última respuesta y anotá cuál sacaste.
2. **Sin cruzar:** respuestas cuyo mail no está en la base (la persona usó otro mail). **No las adivines.** Se cuentan en el total de la encuesta, pero quedan fuera de los cruces con conducta. Si un mail sugiere a alguien (`consultorio.gq@` y hay un solo alumno con esas iniciales), anotalo como `[SUPUESTO: probablemente A-010, confirmalo con el CSM]` y no lo uses en el cálculo.
3. **Cruce por ID, no por mail.** Si la encuesta no pide ID, proponé sumarlo para la próxima. El mail distinto entre herramientas es el mismo problema que rompe accesos y automatizaciones: suele aparecer en las tres partes.
4. **Tasa de respuesta** = respuestas únicas ÷ enviadas. Como orientación (orientativo), arriba de 40 % ya permite leer cortes grandes; abajo de 20 %, leé la encuesta como pistas, no como medición.

## Paso 3 · Los números

- **NPS** = % promotores (9-10) − % detractores (0-6). Mostralo siempre con el conteo: "NPS 0 (16 promotores, 25 pasivos, 16 detractores de 57)". En cualquier corte con **menos de 20 respuestas**, solo conteo.
- **Cada área** (contenido, encuentros, soporte, comunidad, acceso…): promedio **y % que da 4 o 5** (o 9-10 en escala de 10). Ordenalas de peor a mejor.
- **Separá producto de operación.** Contenido y encuentros hablan del producto; soporte, acceso, cobros y comunicación hablan de la operación. La frase típica del caso real es "el producto gusta, la operación no".
- **Intención de seguir** ("¿pensás seguir cuando termine?"): Sí / No sé / No, cruzado con NPS y con la fecha en que termina cada cohorte. Es el primer número de renovación que tiene un negocio que no mide renovaciones.

## Paso 4 · Cortes que cambian la lectura

Hacé los que la base permita. Cada uno con conteo y, si n ≥ 20, NPS en porcentaje.

| Corte | Con qué dato de la base | Qué suele mostrar |
|---|---|---|
| Días de pago a acceso | Fecha de compra y de acceso | Si el onboarding tarda, el NPS cae con los días |
| Estado de cuotas **a la fecha de la respuesta** | Cuotas (vencimiento y fecha de pago) | Los que deben puntúan más bajo soporte y responden menos. Decí qué fecha de corte usaste: con el estado de hoy da otro número |
| Cohorte (mes de compra) | Alumnos | Qué cohorte está peor y si coincide con un cambio (de equipo, de herramienta, de oferta) |
| CSM o coach | Alumnos | Si hay uno solo, el corte no discrimina: el dato es la carga (alumnos por CSM) |
| Participación | Sesiones asistidas, última sesión | Quién se está yendo sin decirlo |

## Paso 5 · Quién no respondió

Compará la población que recibió la encuesta contra la que respondió: con deuda vs sin deuda, por cohorte, por participación. Si un grupo responde mucho menos (por ejemplo, los que deben: 36 % contra 57 %), **el NPS real es peor que el de la encuesta**. No lo corrijas con una cuenta inventada: decilo y nombrá el grupo.

## Paso 6 · Lo abierto

- Agrupá en temas, contá menciones y citá 2 o 3 frases por tema **por número de respuesta** (R-24), nunca por nombre.
- A cada tema, el área que lo resuelve: acceso → onboarding y automatización del alta; "no sé a quién escribir" → soporte y un canal único; "me atrasé y nadie me dijo" → cobros; "a otro le hicieron precio" → ventas y política de descuentos.
- Las respuestas abiertas suelen confirmar problemas que la base ya muestra. Cuando pase, juntalos: el número de la base + la frase del alumno es el argumento más fuerte para el founder.

## Paso 7 · Diagnóstico y decisiones

Igual que en el Modo 1: máximo 5 hallazgos, cada uno con área, causa (sistema / persona / mercado), evidencia y qué hacer con responsable, plazo y plan B. Decisiones típicas:

- Llamar esta semana a los detractores **con contexto** (qué deben, cuánto tardó su acceso, qué escribieron).
- Mover el NPS y la satisfacción por área al tablero de servicio, **cortados por acceso y por cuotas**.
- Oferta y métrica de continuidad antes de que termine la primera cohorte.
- Pasar la encuesta a una cuenta del negocio, una respuesta por alumno, con ID.

## Cómo mejorar la próxima encuesta

- En una cuenta del negocio, no personal.
- Una respuesta por persona; pide el **ID** o usa un link personalizado.
- A mitad del servicio y cerca del final (clase 29/04), siempre con las mismas preguntas para poder comparar.
- NPS + una nota por área + una abierta por área ("¿qué cambiarías?").
- Antes de mandarla, definí quién la lee, cuándo y qué decisión dispara cada número.
