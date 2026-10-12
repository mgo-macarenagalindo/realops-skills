# Ejemplo de output · Detective de Automatizaciones

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
