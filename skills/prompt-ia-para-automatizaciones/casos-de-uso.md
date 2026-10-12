# Casos de uso · Prompt de IA para Automatizaciones

Tres situaciones de infonegocio donde un paso de IA tiene que correr solo y salir igual cada vez. Negocios y nombres ficticios.

---

## 1. El informe de llamada que se fue achicando

**La situación.** Un programa high ticket tiene un Zap que manda cada transcripción de venta a un paso de IA con el prompt "analizá esta llamada y hacé un informe". Las primeras semanas el informe era completo; ahora son tres líneas, y a veces dice que el lead "tiene presupuesto" cuando nunca se habló de plata.

**Qué le pasás.** El prompt actual, un informe bueno y uno malo, y qué datos del CRM existen (closer, programa, estado del lead).

**Qué te devuelve.** La plantilla de Google Doc con marcadores, el prompt en 5 bloques con un campo de salida por dato y la regla de `Sin dato`, el mapeo de cada salida a su marcador y el aviso de 4 líneas por el canal que ya usa el equipo (en este caso, Discord; si fuera un grupo de WhatsApp, mail por defecto y WhatsApp individual solo si el mail no se lee). Más la prueba con tres llamadas y una con texto después de que el lead se fue.

**Por qué sirve.** Pasás de "a veces sale bien" a un informe que el closer y su líder pueden comparar semana a semana. Clase 06/07.

---

## 2. Reportes de sesión 1 a 1 que el coach no tiene que escribir

**La situación.** En una mentoría de negocios, cada coach tarda 20 minutos en escribir el resumen de cada sesión. Son 60 sesiones por mes.

**Qué le pasás.** Cómo es hoy un buen resumen (uno escrito por el mejor coach), qué datos hay fuera de la grabación (número de sesión, objetivo del mes del alumno) y a dónde tiene que llegar.

**Qué te devuelve.** Plantilla de reporte para el alumno (qué se trabajó, acuerdos con fecha, tareas, próximo paso), el prompt con cada acuerdo pedido por separado (compromiso, cómo se mide, fecha límite) y el filtro para que solo pasen las sesiones 1 a 1.

**Por qué sirve.** Sube el valor percibido del servicio y le devuelve horas al equipo. Clases 25/05 y 20/08. Es la actividad 23.

---

## 3. Primer paso de IA sin pagar herramientas

**La situación.** Trabajás en un negocio chico que no quiere pagar más tareas de Zapier "hasta ver si sirve". Querés mostrar el valor del análisis de llamadas.

**Qué le pasás.** La tabla de Agendas de Airtable y qué querría ver el closer antes de la segunda llamada.

**Qué te devuelve.** El prompt para un agente de IA de Airtable: el closer pega la transcripción en un campo largo y el agente llena en la misma fila el perfil, el dolor principal, las objeciones con cita y el próximo paso. Con el mismo diseño de campos, el día que se pase a Zapier o n8n el prompt sirve igual.

**Por qué sirve.** Mostrás el resultado antes de pedir presupuesto. Clase 10/06.
