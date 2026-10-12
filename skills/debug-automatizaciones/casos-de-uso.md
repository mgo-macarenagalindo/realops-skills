# Casos de uso · Detective de Automatizaciones

Tres situaciones de infonegocio donde una automatización que "andaba" deja de andar. Negocios y nombres ficticios.

---

## 1. El onboarding que funciona para un programa y no para el otro

**La situación.** Un Zap de onboarding manda el mail de bienvenida y el acceso a la comunidad según el programa vendido. Con el Programa Esencial anda; con el Programa Élite, nada. Y en Discord, el campo del coach llega como `recA8fK2…`.

**Qué le pasás.** Captura del paso de rutas (PATH), el historial de las últimas ejecuciones y un registro de venta de ejemplo con nombres reemplazados.

**Qué te devuelve.** Dos causas con evidencia: la ruta compara "Programa Elite" y en la base dice "Programa Élite" (con acento), y el coach es un campo vinculado, así que llega su ID. El arreglo (copiar el valor exacto, lookup de texto para el coach), la prueba con un registro de prueba por programa y el registro del incidente.

**Por qué sirve.** Son las dos fallas más repetidas del grupo (clases 07/05 y 29/07). Con el árbol las encontrás en 10 minutos y no en una tarde.

---

## 2. "Zapier dice que salió bien, pero en Notion no está"

**La situación.** Un flujo que crea la tarjeta del cliente nuevo en Notion muestra "Success" en todas las ejecuciones. Las tarjetas no aparecen desde hace una semana.

**Qué le pasás.** El historial de una ejecución exitosa y qué cambió esa semana (alguien duplicó la base de clientes para "ordenarla").

**Qué te devuelve.** La rama C del árbol: el paso sigue escribiendo en la base vieja. Cómo reapuntarlo, la espera de unos minutos si Notion no reconoce la conexión nueva y la prueba. Más la prevención: antes de duplicar o mover una base, listar qué automatizaciones escriben en ella.

**Por qué sirve.** "Éxito sin dato" es la falla que más confianza le saca al founder. Clase 14/05.

---

## 3. Mails repetidos a los alumnos

**La situación.** En GoHighLevel, un workflow de recordatorio de cuota le mandó el mismo mail cuatro veces a 30 alumnos en una mañana.

**Qué le pasás.** El workflow (disparador, condiciones, acciones) y la hora de los envíos.

**Qué te devuelve.** Primero: "apagalo ya". Después, la rama E: el workflow actualiza el campo que lo dispara, así que se vuelve a disparar (bucle). El arreglo con una condición de "ya enviado", la prueba con un contacto nuevo de prueba y el mensaje para el equipo de servicio por si algún alumno escribe.

**Por qué sirve.** Te ordena la urgencia: frenar el daño antes de entenderlo. Clase 25/06.
