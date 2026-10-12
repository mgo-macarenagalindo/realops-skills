# Casos de uso · Detective de Automatizaciones

Seis situaciones de infonegocio: cuatro donde una automatización que "andaba" deja de andar (modo diagnóstico), una donde nadie sabe qué corre (modo inventario) y una donde hay demasiadas piezas (modo simplificar). Negocios y nombres ficticios.

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

---

## 4. Leads asignados a alguien que ya no está, y nadie tiene la clave

**La situación.** En una mentoría grupal, un lead escribe que llenó la aplicación hace un mes y nadie le contestó. En la base figura asignado a una setter que se fue hace dos meses. Aparecen 9 así. La automatización que reparte está en la cuenta de esa ex setter: nadie del equipo puede ver el historial. Y a "¿está haciendo daño ahora?" o "¿qué cambió?", la respuesta es "no lo sé".

**Qué le pasás.** Solo el export de la tabla de leads y lo que dice el equipo ("reparte en rueda, nunca lo tocamos").

**Qué te devuelve.** El plan B en acción: con preguntas más chicas ("¿cuál es el lead mal asignado más nuevo?") se ve que la falla no se repite hace semanas, así que **no se apaga** (apagarla cortaría la entrada de aplicaciones). La rama F (personas y cuentas), el diagnóstico desde los datos de destino, lo confirmado separado de los supuestos rotulados "Supuesto a validar con <rol>", y un arreglo en dos partes: reasignar los 9 hoy y recuperar la cuenta. Más el checklist de baja de equipo como prevención.

**Por qué sirve.** Es la falla más común en equipos que rotan, y la más difícil: sin acceso, conseguir el acceso es el paso 1 del arreglo.

---

## 5. Heredaste el negocio y nadie sabe qué corre solo

**La situación.** Entrás como operativo estratégico a una escuela online. El founder dice "tenemos unos Zaps y algo en Airtable". Nadie tiene la lista. Los mails de error de Zapier le llegan a una ex coordinadora.

**Qué le pasás.** La lista de herramientas y accesos, y el acceso de lectura que tengas (o nada).

**Qué te devuelve.** El modo inventario: el prompt de solo lectura para que Cowork recorra Zapier, la pestaña de automatizaciones de Airtable y el resto, las preguntas por las automatizaciones escondidas (reparto de la agenda, recordatorios, mails de la pasarela de pago, flujos de ManyChat) y el informe: tabla resumen para el founder, una ficha en lenguaje de negocio por automatización, el mapa de cuentas (quién recibe los errores) y los hallazgos 🔴 🟡 🟢 con evidencia.

**Por qué sirve.** No se puede arreglar, migrar ni simplificar lo que no se conoce. Y es el entregable que más valora un founder que "no sabe qué tiene".

---

## 6. 23 Zaps, el plan excedido y avisos repetidos

**La situación.** Una mentoría con 23 Zaps: uno de onboarding por cada programa, uno de agenda por cada calendario, cinco de reportes de fin de día, dos que avisan lo mismo en el mismo canal y uno que se lleva el 44 % de las tareas porque se dispara con cualquier edición.

**Qué le pasás.** El inventario (o te lo arma primero).

**Qué te devuelve.** El modo simplificar: los grupos por patrón (duplicadas, variantes, consultas, cadenas, zombies, criterio repartido), la decisión de cada grupo con su porqué (incluido lo que **no** se junta), el antes y después en cantidad y consumo, la propuesta de reemplazar los cinco Zaps de reportes por un flujo con un resumen de IA, y el plan de corte en tandas: activar lo nuevo y apagar lo viejo en el mismo momento.

**Por qué sirve.** Pasar de 23 piezas a 9 baja el costo, pero sobre todo baja los lugares donde algo puede fallar sin que nadie se entere.

