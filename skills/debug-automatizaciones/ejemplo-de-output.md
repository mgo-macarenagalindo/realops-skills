# Ejemplo de output · Detective de Automatizaciones

Dos ejemplos: **1 · Diagnóstico** de una automatización que falla y **2 · Inventario y simplificación** de todas las automatizaciones de un negocio.

## Ejemplo 1 · Diagnóstico

> Datos ficticios. Escuela online de diseño de interiores con dos programas: Programa Esencial y Programa Élite. El closer completa un formulario de Airtable al cerrar la venta; un Zap con rutas (PATH) manda el mail de bienvenida del programa, invita a la comunidad y avisa al equipo en Discord.

**Lo que contó la persona:** "En septiembre entraron 14 ventas. Las 9 del Esencial recibieron todo. Las 5 del Élite no recibieron ni el mail ni el acceso, y dos ya escribieron a soporte. Además, en Discord el coach aparece como un código raro. La semana pasada agregamos al formulario la pregunta 'Fecha de inicio' y en el mail llega vacía". Pegó captura del PATH, del paso de Discord y el historial.

---

# Diagnóstico · Onboarding por programa (Zap) · 06/10/2026

## Síntoma

- **Debería pasar:** venta registrada → ruta según el programa → mail de bienvenida de ese programa + invitación a la comunidad + aviso en Discord con nombre, programa y coach.
- **Pasa:** 9 de 14 ventas (Esencial) completas. 5 de 14 (Élite) sin mail ni acceso. En las 14, Discord muestra el coach como `recA8fK2…`. Desde el 29/09, "Fecha de inicio" llega vacía en el mail.
- **Desde cuándo:** el Élite, desde que se creó la ruta (nunca funcionó; antes las ventas Élite se daban de alta a mano). Lo de la fecha, desde el 29/09.
- **Impacto:** 5 alumnos pagos sin acceso (entre 2 y 9 días). 2 consultas a soporte.

## ¿Hay que apagarlo ya?

No. No manda nada duplicado ni escribe datos mal en la base: lo que falla es que **no** manda. Se deja encendido (el Esencial funciona) y se arregla hoy. **Mientras tanto:** dar de alta a mano a los 5 alumnos Élite (acción 1).

## Árbol recorrido

| Rama | Pregunta | Evidencia | Resultado |
|---|---|---|---|
| A | ¿Publicado y encendido? | Historial con 14 ejecuciones en septiembre | Sí, corre |
| D2 | ¿La ruta Élite se cumple? | Las 5 ejecuciones Élite terminan en "Path conditions not met". La condición dice `Programa Elite`; en la base la opción es `Programa Élite` | **Causa 1** |
| D1 | ¿Llega un código en vez de un nombre? | El paso de Discord mapea el campo `Coach`, que es un vínculo a la tabla Coaches | **Causa 2** |
| D3 | ¿Por qué "Fecha de inicio" llega vacía? | El registro de prueba del Zap es del 12/09, anterior a la pregunta nueva: el campo no existe en la prueba, así que el mapeo quedó vacío | **Causa 3** |
| C | ¿Escribe en otra base? | No aplica: el problema no es de destino | Descartado |
| E | ¿Duplicados? | Ninguna venta tiene dos mails | Descartado |

## Causa raíz

1. **El texto de la ruta no coincide exacto** con la opción de la base (falta el acento). Por eso ninguna venta Élite entró nunca a su ruta.
2. **El coach es un campo vinculado:** Zapier recibe el ID del registro, no el nombre.
3. **El registro de prueba es viejo:** Zapier solo reconoce los campos que vinieron con dato en la prueba.

## Arreglo, paso a paso

1. **Hoy, a mano:** dar acceso a la comunidad y mandar el mail de bienvenida Élite a los 5 alumnos (lista: vista "Ventas Élite · septiembre"). Responder las 2 consultas de soporte.
2. **Ruta Élite:** en la base, copiar el valor exacto de la opción (`Programa Élite`) y pegarlo en la condición del PATH. No tipearlo.
3. **Coach:** en la tabla Ventas, crear el campo lookup `Coach (nombre)` que trae el nombre desde Coaches. En el paso de Discord, mapear `Coach (nombre)` en lugar de `Coach`.
4. **Fecha de inicio:** cargar una venta de prueba con **todos** los campos completos (incluida la fecha), volver al disparador del Zap, traer ese registro como prueba y mapear `Fecha de inicio` en el mail.
5. Publicar el Zap.

## Cómo probarlo

| # | Prueba | Tiene que pasar |
|---|---|---|
| 1 | Venta de prueba Programa Élite con tu propio mail | Llega el mail Élite, la invitación a la comunidad y el aviso en Discord con el nombre del coach |
| 2 | Venta de prueba Programa Esencial | Sigue funcionando igual |
| 3 | Venta de prueba sin fecha de inicio | El mail sale igual y la frase de la fecha no queda "colgada" (revisar el texto del mail) |
| 4 | Revisar el historial | Las 3 ejecuciones de prueba con todos los pasos en verde |

Después de probar, borrar o marcar como prueba los 3 registros, y sacarte de la comunidad.

## Prevención

- **Programa como selección única cerrada**, sin editar sus opciones sin avisar a quien mantiene el Zap. Si se renombra una opción, se actualiza la ruta el mismo día.
- **Nunca mapear un campo vinculado** a un mensaje: siempre su lookup de texto.
- **Cada vez que se agrega una pregunta al formulario,** cargar un registro de prueba completo y re-mapear.
- **Chequeo semanal de 5 minutos:** comparar ventas de la semana contra accesos dados.

## Registro del incidente

```
Fecha: 06/10/2026 · Automatización: Onboarding por programa (Zapier)
Síntoma: ventas Élite sin mail ni acceso; coach como ID en Discord; fecha de inicio vacía
Impacto: 5 alumnos sin acceso entre 2 y 9 días; 2 consultas a soporte
Causa: condición del PATH sin acento; campo vinculado mapeado directo; prueba anterior al campo nuevo
Arreglo: valor copiado de la base; lookup Coach (nombre); registro de prueba completo y re-mapeo
Probado: 3 ventas de prueba, OK
Prevención: opciones cerradas; lookups para mensajes; re-mapear al cambiar el formulario; chequeo semanal
Responsable: Operaciones
```

---

**Mensaje para el equipo (opcional):**

> Equipo: el onboarding del Programa Élite no estaba saliendo por un detalle de configuración (ya está arreglado y probado). Hoy les di acceso a mano a los 5 alumnos de septiembre. Pedido para adelante: si cambian el nombre de un programa o agregan una pregunta al formulario de venta, avísenme ese día así actualizo la automatización.

---
---

## Ejemplo 2 · Inventario y simplificación

> Datos ficticios. Mentoría online para nutricionistas con tres programas (Inicial, Clínica y Premium). Zapier plan Professional (750 tareas) a nombre del mail del founder; base de Airtable en la cuenta del negocio; agenda en Calendly; equipo en Discord. La nueva operativa estratégica pidió: "Antes de tocar nada, quiero saber qué corre solo y si se puede simplificar. Nos están cobrando tareas extra".
>
> Relevamiento hecho con el prompt de solo lectura en Cowork (Zapier y Airtable) el 06/10/2026. Historial: últimos 30 días.

# Inventario de automatizaciones · Mentoría para nutricionistas · 06/10/2026

## Resumen

- **15 automatizaciones:** 11 Zaps (9 encendidos, 1 apagado, 1 borrador), 2 automatizaciones de Airtable y 2 escondidas (reparto de Calendly y mails de pago rechazado de la pasarela).
- **Consumo de Zapier:** 1.006 tareas en 30 días sobre 750 incluidas (134 %). El Zap 09 solo se lleva 520 (52 %).
- **3 hallazgos principales:** (1) el Zap 09 se dispara con cualquier edición de un alumno; (2) los mails de error de Zapier y los avisos de pago rechazado llegan al founder, que no los lee; (3) tres Zaps de onboarding casi iguales, uno por programa.

| # | Plataforma | Nombre | Qué hace | Disparador | Estado | Corridas 30 d | Tareas 30 d | Riesgo |
|---|---|---|---|---|---|---|---|---|
| 01 | Zapier | Agenda Calendly → Airtable | Crea la llamada en el CRM | Calendly · nuevo invitado | On | 64 | 128 | 🔴 duplica al reprogramar |
| 02 | Zapier | Agenda → Discord | Avisa la agenda al closer | Airtable · nuevo registro en vista | On | 64 | 64 | 🟡 |
| 03 | Zapier | Onboarding Inicial | Mail de bienvenida + aviso | Airtable · nueva venta (filtro Inicial) | On | 9 | 27 | 🟡 |
| 04 | Zapier | Onboarding Clínica | Ídem | Ídem (filtro Clínica) | On | 6 | 18 | 🟡 |
| 05 | Zapier | Onboarding Premium | Ídem + agenda la 1:1 | Ídem (filtro Premium) | On | 2 | 8 | 🟡 |
| 06 | Zapier | EOD setters → Discord | Publica el reporte | Airtable · nuevo EOD setter | On | 44 | 44 | 🟢 |
| 07 | Zapier | EOD closers → Discord | Ídem | nuevo EOD closer | On | 21 | 21 | 🟢 |
| 08 | Zapier | EOD coaches → Discord | Ídem, en 2 mensajes | nuevo EOD coach | On | 88 | 176 | 🟡 a veces pasa los 2.000 caracteres |
| 09 | Zapier | Cambio de estado del alumno → Sheets | Registra cambios de estado | Airtable · campo "última modificación" | On | 520 | 520 | 🔴 dispara de más |
| 10 | Zapier | Caso de éxito → Discord | Avisa cuando se marca un caso | Airtable · vista | On | 0 | 0 | 🟡 zombie |
| 11 | Zapier | Untitled Zap | Borrador sin publicar | — | Borrador | 0 | 0 | 🟢 ruido |
| 12 | Zapier | Recordatorio de clase | Aviso martes y miércoles | Programado | Off | 0 | 0 | 🟢 |
| 13 | Airtable | Venta → Cuotas | Crea las 3 cuotas | Registro creado en Ventas | On | 17 | — | 🟡 |
| 14 | Airtable | Cuota vencida → aviso | Mail a administración | Entra en vista "Vencidas" | On | 22 | — | 🟢 |
| 15 | Calendly / pasarela | Reparto rotativo y mails de pago rechazado | Reparte llamadas; avisa rechazos | Nativos | On | — | — | 🔴 rechazos al mail del founder |

## Mapa de cuentas y conexiones

| Cuenta o conexión | A nombre de | ¿Sigue? | Quién recibe los errores |
|---|---|---|---|
| Zapier (cuenta) | Mail personal del founder | Sí | El founder (no los lee) |
| Conexión Airtable en Zapier | Founder | Sí | — |
| Conexión Gmail (mails a alumnos) | Founder | Sí | — |
| Airtable (base) | Cuenta del negocio | — | Última persona que activó cada automatización: la ex coordinadora (13 y 14) |
| Pasarela de pago | Mail del founder | Sí | El founder |
| 7 webhooks de Discord | Escritos a mano en los Zaps 02 a 10 | — | — |

## Fichas (dos de ejemplo; en el informe real va una por automatización)

### Zapier · 09. Cambio de estado del alumno → Sheets
**Qué hace:** cada vez que cambia el estado de un alumno (activo, pausa, baja), agrega una fila a la planilla "Historial de estados".
**Cuándo se dispara:** cuando cambia el campo "Última modificación de estado" en Alumnos.
**Pasos:** 1. Airtable · registro actualizado · 2. Google Sheets · agregar fila (alumno, estado, fecha).
**Datos que lee:** Alumnos · Nombre, Estado, Última modificación de estado · **Datos que escribe:** planilla "Historial de estados", pestaña 2026.
**Cuenta dueña y conexiones:** Zapier, Airtable y Sheets a nombre del founder.
**Dueño (rol):** nadie. Hallazgo.
**Estado y uso:** encendido · 520 corridas en 30 días · 0 errores · 520 tareas.
**De qué depende:** el campo "Última modificación de estado" y la pestaña 2026.
**Qué puede fallar:** 🔴 el campo de última modificación **mira todos los campos**, no solo Estado: cualquier edición del alumno dispara el Zap. En 30 días hubo 520 corridas para 14 cambios de estado reales (cruzado con la planilla). 🟡 Si se renombra la pestaña, falla con aviso al founder.
**Riesgo si se rompe:** se pierde el historial de bajas y pausas; nadie se entera.

### Airtable · 14. Cuota vencida → aviso
**Qué hace:** cuando una cuota pasa a vencida, manda un mail a administración con el alumno y el monto.
**Cuándo se dispara:** cuando una cuota entra en la vista "Vencidas".
**Pasos:** 1. Entra en la vista · 2. Enviar mail a administración.
**Datos que lee:** Cuotas · Alumno (lookup), Monto, Vencimiento · **Escribe:** nada.
**Cuenta:** base del negocio. Los avisos de falla le llegan a la ex coordinadora (la activó ella).
**Dueño (rol):** Administración.
**Estado y uso:** encendida · 22 corridas · 0 errores.
**De qué depende:** el filtro de la vista "Vencidas" (no dice en ningún lado que la usa una automatización).
**Qué puede fallar:** 🔴 si alguien cambia el filtro de la vista para "mirar otra cosa", se corta el aviso sin error.
**Riesgo si se rompe:** cuotas vencidas sin que nadie se entere.

## Hallazgos

🔴 **Críticos**
1. **Zap 09 dispara de más** (520 corridas para 14 cambios reales; 52 % de las tareas). Arreglo de 1 minuto: en Airtable, el campo "Última modificación de estado" → campos específicos → solo Estado.
2. **Nadie ve los errores:** Zapier y la pasarela avisan al founder; las automatizaciones de Airtable, a una persona que ya no está. Arreglo: notificaciones de error de Zapier a un mail del negocio que lee Operaciones; reactivar las automatizaciones 13 y 14 desde la cuenta de Administración; avisos de la pasarela al mail del negocio.
3. **Zap 01 duplica al reprogramar:** 64 corridas para 52 agendas únicas (12 reprogramaciones). Arreglo: filtro "no seguir si es reprogramación" (rama E del árbol).

🟡 **Atención**
4. Tres Zaps de onboarding casi iguales (03, 04, 05): una corrección hay que hacerla tres veces, y ya difieren (el 05 tiene el texto del mail viejo).
5. Zap 08 falla 3 veces por mes por superar el límite de Discord.
6. Zap 10 encendido sin corridas en 60 días (zombie).
7. Siete webhooks de Discord escritos a mano en los pasos.

🟢 **Menor**
8. Borrador 11 sin publicar. 9. Zap 12 apagado (confirmar que el recordatorio ya no se usa).

## Sin acceso

- Historial de más de 30 días de Zapier (el plan no lo guarda).
- Configuración del reparto de Calendly: la cuenta es de una setter. **Supuesto a validar con la setter dueña: reparte por disponibilidad.**

---

# Simplificación · Mentoría para nutricionistas · 06/10/2026

## Antes y después

| | Antes | Después |
|---|---|---|
| Automatizaciones activas | 13 (9 Zaps + 2 Airtable + 2 nativas) | **8** (4 Zaps + 2 Airtable + 2 nativas) |
| Tareas de Zapier por mes | ~1.006 (134 % del plan) | **~430** (57 %) |
| Lugares donde corregir el mail de bienvenida | 3 | 1 |
| Webhooks escritos a mano | 7 | 3 |
| Errores que no ve nadie | todos | ninguno (un mail del negocio) |

## Grupos encontrados

| Patrón | Cuáles | Decisión | Por qué |
|---|---|---|---|
| Criterio mal configurado | 09 | **Arreglar el disparador** (no se junta con nada) | Con el campo bien configurado pasa de 520 a ~14 tareas |
| Variantes | 03, 04, 05 | **Juntar en uno** con rutas por programa y una tabla "Programas" en Airtable (mail, accesos, si agenda 1:1) | Mismo disparador, mismo dueño (Servicio). Agregar un programa pasa a ser una fila |
| Duplicadas por diseño | 01 + 02 | **Juntar:** el aviso a Discord pasa a ser el último paso del 01 | Mismo evento, mismo dueño (Ventas). Ahorra 64 tareas y un disparador por vista |
| Criterio repartido | 06, 07, 08 | **Un solo flujo de EOD** con un paso de IA que arma un resumen diario para el founder, más el reporte de cada persona en su canal | Hoy son 3 Zaps y el founder lee 150 mensajes por mes. Un resumen con alertas ("2 closers sin reporte") vale más. El paso de IA no toca plata ni clientes |
| Zombies y ruido | 10, 11, 12 | **Apagar el 10** (con aviso a Marketing) y borrar el 11. El 12 ya está apagado | Sin corridas en 60 días; nadie los reclamó |
| Nativas | 13, 14, reparto de Calendly | **Dejar** | Funcionan y no gastan tareas. Solo cambiar quién las activó y documentar la vista |

## Lo que NO se junta y por qué

- **El aviso de cuota vencida (14) con el onboarding:** dueños distintos (Administración y Servicio) y urgencias distintas. Juntarlos haría que una falla corte las dos.
- **El reporte de EOD con la agenda:** uno es diario y para el founder, el otro es al instante y para el closer.
- **No se propone un agente para el onboarding:** mueve accesos y mails a clientes; la regla es fija (programa → accesos). Alcanza con rutas.

## Plan de corte en tandas

| Tanda | Qué | Cómo se prueba | Responsable | Fecha |
|---|---|---|---|---|
| 1 | Arreglar el campo del Zap 09 · apagar 10 · borrar 11 · errores al mail del negocio · reactivar 13 y 14 desde Administración | Editar un alumno sin cambiar el estado: el Zap 09 no corre | Operaciones | 07/10 |
| 2 | 01 + 02 en un Zap con filtro de reprogramación | Agenda de prueba, reprogramarla: una sola llamada y un aviso | Operaciones | 09/10 |
| 3 | Onboarding único (03 + 04 + 05) | Una venta de prueba por programa, con tu mail | Operaciones + Servicio | 14/10 |
| 4 | EOD único con resumen de IA (diseño con Diseñador de Automatizaciones; prompt con Prompt de IA para Automatizaciones) | Una semana en paralelo en un canal de prueba antes de apagar 06, 07 y 08 | Operaciones | 21/10 |

En cada tanda: activar lo nuevo y apagar lo viejo **en el mismo momento**, mirar la primera semana y borrar lo viejo recién al mes.

## Para confirmar

| Supuesto | Con quién | ¿Cambia el plan? |
|---|---|---|
| El Zap 12 (recordatorio de clase) ya no se usa | Servicio | Si se usa, se reactiva en la tanda 1 |
| Marketing ya no usa el aviso de casos de éxito (10) | Marketing | Si lo usa, se revisa por qué no corre (rama A del árbol) |
| El reparto de Calendly es por disponibilidad | Setter dueña de la cuenta | No cambia la simplificación; sí el inventario |

¿Querés que diseñemos la primera pieza nueva (el onboarding único) con el Diseñador de Automatizaciones?

