# Ejemplo de output · Auditor de Base Heredada

> Datos ficticios. Academia online de fotografía de producto: programa de 5 meses por llamada de venta, con reserva y hasta 3 cuotas. 2 setters, 2 closers, 3 coaches. Base de Airtable "Comercial" armada por una persona que ya no está en el equipo. Quien pide la auditoría entró hace una semana como operaciones, con permiso de creador.

**Lo que pegó la persona:** capturas de las 7 tablas con sus campos, la lista de automatizaciones de la base, los 3 Zaps de la cuenta de Zapier del negocio y la frase del founder: "los números del mes los saca la coordinadora a mano y nunca coinciden con los del closer".

---

# Auditoría de base heredada · Academia (caso ficticio) · octubre 2026

## En una frase

La base funciona, pero los números del founder no salen de ella: se cuentan a mano, la facturación está inflada por reservas cargadas con el ticket completo y un Zap de cobranza sigue escribiendo en una tabla de marzo.

## Antes de tocar

- **Backup:** base duplicada como "Comercial · BACKUP 07-10" (sin automatizaciones activas en la copia).
- **Accesos:** 6 personas con permiso de creador. Solo 2 diseñan la base. → Pasar 4 a editor (acción 6 del plan).
- **Automatizaciones de Airtable:** 4. **Zaps que escriben en la base:** 3. **Interfaces:** 2 (Closers, Dirección).

| # | Automatización | Dispara | Escribe en | Estado |
|---|---|---|---|---|
| A1 | Alta de alumno | Registro creado en Ventas | Alumnos (crea registro) | Activa · se usa |
| A2 | Aviso de venta | Registro creado en Ventas | Discord (mensaje) | Activa · se usa |
| A3 | Recordatorio de cuota | Todos los días 9:00 | Mail al alumno | **Apagada desde marzo** |
| A4 | Copia a Ventas marzo | Registro creado en Ventas | Ventas marzo | **Activa · nadie sabe para qué** |
| Z1 | Calendly → Agendas | Evento agendado | Agendas | Activo · se usa |
| Z2 | ManyChat → Leads | Contacto con etiqueta | Leads | Activo · se usa |
| Z3 | Cuota vencida | Todos los días 10:00 | **Lee Ventas marzo** y avisa a cobranzas | Activo · **lee la tabla equivocada** |

## Mapa de tablas

| Tabla | Qué representa | De dónde entra el dato | Quién la usa | Registros |
|---|---|---|---|---|
| Leads | Contactos que escribieron por Instagram | Z2 (ManyChat) | Setters | 2.310 |
| Agendas | Llamadas de venta agendadas | Z1 (Calendly) + closer actualiza el estado a mano | Closers, setters | 1.140 |
| Ventas | **Mezclada:** contrato + pagos en la misma fila | Formulario del closer | Closers, administración | 212 |
| Ventas marzo | Copia de Ventas con 3 campos menos | A4 (copia automática) | Nadie (la lee Z3) | 38 |
| Pagos | Transferencias recibidas | Carga manual de administración | Administración | 604 |
| Alumnos | Alumnos con su coach y su avance | A1 + carga manual del coach | Coaches | 190 |
| KPIs | Los números del mes para el founder | **Carga manual** (la coordinadora cuenta) | Dirección | 12 |

## Informe por tabla

| Tabla | Elemento | Hallazgo | Riesgo | Acción |
|---|---|---|---|---|
| Agendas | Campo `Estado` | Mezcla estado de la llamada y del lead (Asistió · No show · Canceló · Seguimiento · Cerrado · Perdido). Un no-show en seguimiento no se puede registrar | Alto | Crear `Estado de la llamada` y `Estado del lead` nuevos; dejar `Estado` oculto como `[ARCHIVO] Estado` cuando se termine de migrar |
| Agendas | Campo `Canal` | Vacío en 468 de 1.140 registros (41 %). Se carga a mano y nadie es responsable | Alto | No es un canal: es tracking roto. Llevarlo a UTMs (skill UTMs de Punta a Punta) |
| Ventas | Campo `Monto` | Un solo campo para todo. En 17 reservas se cargó el ticket completo (USD 1.800) en vez de la seña: la facturación del período está inflada | Alto | Separar `Facturación USD` (una vez por deal, vacía en reservas) de `Cash collected USD` |
| Ventas | Columnas `Cuota 1 / Pago 1 … Cuota 3 / Pago 3` | Contrato y pagos en la misma fila; se rompe con el primer pago partido | Medio | Separar Deals y Cuotas cobradas (diseño con Arquitecto de Base en Airtable). No antes de arreglar Z3 |
| Ventas marzo | Tabla entera | Copia manual vieja; A4 la sigue alimentando y Z3 la lee | Alto | Apuntar Z3 a la vista correcta de Ventas, apagar A4 y **ocultar** la tabla. No borrarla |
| Pagos | Campo `Venta` (vínculo) | Vincula cada pago a su venta. De él cuelgan 2 rollups de Ventas (`Total pagado`, `Saldo`) | Alto | **No tocar.** Documentar en la descripción del campo |
| Pagos | Campo `Método` | Texto libre: "MP", "mercadopago", "Mercado Pago" | Medio | Convertir a selección única y unificar variantes |
| Alumnos | Campo primario | Fórmula que usa `Nombre` de un lookup; 9 registros muestran "Unnamed record" | Bajo | Revisar esos 9: les falta la venta vinculada |
| KPIs | Tabla entera | Ningún número sale de un rollup: se tipean | Alto | Rehacerla con la clave mes + canal (skill Tabla de KPIs Globales en Airtable) |

## Red flags

1. **Z3 lee Ventas marzo.** Desde abril, ninguna cuota vencida de ventas nuevas generó aviso a cobranzas. Es el hallazgo con más plata en juego.
2. **A3 apagada desde marzo.** Los alumnos no reciben recordatorio de cuota. Sumado a la red flag 1, explica por qué "la cobranza empeoró sola".
3. **El vínculo Pagos → Ventas** sostiene `Total pagado` y `Saldo`. Si alguien lo borra "para simplificar", se pierde el saldo de 212 ventas.
4. **Z1 escribe en los campos `Email` y `Fecha llamada` de Agendas.** No renombrarlos sin editar el Zap en el mismo momento.
5. **Facturación inflada por 17 reservas.** Cualquier número de "facturado" de los últimos meses está mal hasta corregirlo.

## Lo que no se toca

- Ninguna tabla se borra. Ventas marzo se **oculta** después de arreglar Z3.
- Ningún campo de vínculo se borra (Pagos → Ventas, Alumnos → Ventas, Agendas → Leads).
- `Email` y `Fecha llamada` de Agendas no se renombran (los usa Z1).
- Las 17 reservas mal cargadas no se borran: se corrige el monto y se marca la naturaleza "Reserva".

## Plan en orden de prioridad

| # | Acción | Por qué primero | Quién | Tiempo |
|---|---|---|---|---|
| 1 | Apuntar Z3 a una vista "Cuotas vencidas" de Ventas y probar con un registro de prueba | Hay cuotas vencidas sin aviso desde abril | Operaciones | 1 h |
| 2 | Revisar A3 con administración y reactivarla (o reemplazarla por Z3) | Recordatorio previo al vencimiento | Operaciones + administración | 1 h |
| 3 | Apagar A4 y ocultar Ventas marzo | Deja de generar copias | Operaciones | 15 min |
| 4 | Corregir las 17 reservas: monto de la seña y naturaleza "Reserva" | La facturación vuelve a ser real | Administración | 1 h |
| 5 | Separar estado de la llamada y estado del lead en Agendas | Sin esto no hay asistencia ni cierre por canal | Operaciones + closers | 2 h |
| 6 | Pasar 4 creadores a editor | Menos riesgo de borrados | Founder (aprueba) | 10 min |
| 7 | Rehacer KPIs con la clave mes + canal | El founder deja de recibir números contados a mano | Operaciones | 1 día |
| 8 | Separar Deals y Cuotas cobradas | Escala con pagos partidos | Operaciones | Proyecto aparte |

## Preguntas para quien armó la base o para el founder

1. ¿Para qué se creó Ventas marzo? ¿Alguien la usa para un reporte que no vimos?
2. ¿Por qué se apagó A3? (¿quejas de alumnos, mails repetidos, cambio de herramienta?)
3. ¿La reserva cuenta como venta para la comisión del closer? Hoy no está escrito en ningún lado.
4. ¿El founder quiere ver el canal "Referido"? No existe como opción.

---

## Anexo · La fórmula que pediste explicar (campo `Estado de cobro` de Ventas)

```airtable
IF({Saldo}=0, "Pagado", IF(IS_BEFORE({Próximo vencimiento}, TODAY()), "Vencida", "Al día"))
```

**Qué hace:** si el saldo es 0, dice "Pagado". Si no, mira la fecha del próximo vencimiento: si ya pasó, "Vencida"; si no, "Al día".

**Depende de:** `Saldo` (fórmula: `{Monto} - {Total pagado}`) y `Próximo vencimiento` (fecha cargada a mano).

**Prueba con 3 filas del CSV:**

| Venta | Monto | Total pagado | Saldo | Próximo vencimiento | Resultado | ¿Correcto? |
|---|---|---|---|---|---|---|
| V-101 | 1.800 | 1.800 | 0 | — | Pagado | Sí |
| V-145 | 1.800 | 600 | 1.200 | 05/09/2026 | Vencida | Sí |
| V-188 (reserva) | 1.800 | 200 | 1.600 | vacío | Al día | **No:** es una reserva cargada con el ticket completo y sin vencimiento |

**Conclusión:** la fórmula está bien; el dato de entrada no. Se arregla con la acción 4 del plan, no tocando la fórmula.
