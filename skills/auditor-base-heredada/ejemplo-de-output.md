# Ejemplo de output · Auditor de Base Heredada

> Datos ficticios. Academia online de fotografía de producto: programa de 5 meses por llamada de venta, con reserva y hasta 3 cuotas. 2 setters, 2 closers, 3 coaches. Base de Airtable "Comercial" armada por una persona que ya no está en el equipo. Quien pide la auditoría entró hace una semana como operaciones, con permiso de creador.

**Lo que pegó la persona:** capturas de las 7 tablas con sus campos, la lista de automatizaciones de la base, el relevamiento de los Zaps hecho con Cowork en modo lectura, la página "Automatizaciones" del Notion del equipo (última edición: febrero) y la frase del founder: "los números del mes los saca la coordinadora a mano y nunca coinciden con los del closer".

---

# Auditoría de base heredada · Academia (caso ficticio) · octubre 2026

## En una frase

La base funciona, pero los números del founder no salen de ella: se cuentan a mano, la facturación está inflada por reservas cargadas con el ticket completo, un Zap de cobranza sigue leyendo una tabla de marzo y el alta de agendas entra a Airtable con la cuenta de la persona que se fue.

## Antes de tocar

- **Backup:** base duplicada como "Comercial · BACKUP 07-10", con las automatizaciones de la copia apagadas.
- **Accesos:** 6 personas con permiso de creador; solo 2 diseñan la base. La exresponsable de operaciones (se fue en julio) **sigue como creadora**. Sacarla es la acción 1 del plan, **después** de reconectar Z1, que entra a Airtable con su usuario.
- **Dónde vive:** cuenta del negocio, plan pago. Bien.

## Inventarios que crucé

| Inventario | De cuándo · quién | Diferencias con lo que hay hoy |
|---|---|---|
| Página "Automatizaciones" del Notion del equipo | Febrero · la exresponsable de operaciones | Lista 5 flujos. Falta Z3 (cuota vencida) y A4 (copia a Ventas marzo): se crearon después y nadie los documentó. Dice que A3 "manda el recordatorio de cuota": está apagada desde marzo |
| Relevamiento de Zapier con Cowork (solo lectura) | 06/10 · operaciones | Z1 está conectado a Airtable con la cuenta de la exresponsable. Z3 tiene un borrador sin publicar con otra vista |
| Lista de accesos del founder | Septiembre · founder | No menciona Zapier: "eso lo manejaba ella". La cuenta de Zapier está a nombre del negocio, pero la conexión a Airtable no |

## Cómo entra, viaja y sale la info

| Tabla | Entra por | Viaja a | Sale hacia |
|---|---|---|---|
| Leads | Z2 (ManyChat → Zapier) | Agendas (vínculo) | — |
| Agendas | Z1 (Calendly → Zapier) + el closer actualiza el estado a mano | Ventas (vínculo) | — |
| Ventas | Formulario nativo del closer | Alumnos (A1 crea el registro), Ventas marzo (A4 copia) | Discord #ventas (A2, webhook …4410) |
| Ventas marzo | A4 (copia automática) | — | Z3 la lee para avisar cuotas vencidas |
| Pagos | Carga manual de administración, desde el banco (10 min por día) | Ventas (vínculo; de él salen `Total pagado` y `Saldo`) | — |
| Alumnos | A1 + carga manual del coach | — | — |
| KPIs | **Carga manual** (la coordinadora cuenta) | — | Interfaz Dirección |

## Automatizaciones, webhooks y conexiones

| # | Automatización | Cuenta · conexión | Dispara | Lee / escribe | Uso 30 días | Qué rompe si falla |
|---|---|---|---|---|---|---|
| A1 | Alta de alumno (nativa) | Base | Registro creado en Ventas | Crea en Alumnos | 14 · 0 errores | Alumnos sin ficha |
| A2 | Aviso de venta (nativa) | Webhook a Discord #ventas (…4410) | Registro creado en Ventas | Lee `Closer`, `Monto` | 14 · 0 errores | Nadie se entera de la venta |
| A3 | Recordatorio de cuota (nativa) | Mail del negocio | Todos los días 9:00 | Lee la vista "Próximas a vencer" | **Apagada desde marzo** | Alumnos sin recordatorio |
| A4 | Copia a Ventas marzo (nativa) | Base | Registro creado en Ventas | Crea en Ventas marzo | 14 · **nadie sabe para qué** | — |
| Z1 | Calendly → Agendas | Zapier del negocio · **Airtable conectado con la cuenta de la exresponsable** | Evento agendado | Escribe `Email`, `Fecha llamada`, `Closer` | 96 · 0 errores | Dejan de entrar agendas, sin aviso a nadie |
| Z2 | ManyChat → Leads | Zapier del negocio | Contacto con etiqueta | Crea en Leads | 310 · 2 errores | Leads sin cargar |
| Z3 | Cuota vencida | Zapier del negocio · webhook a Discord #cobranzas (…0021) | Todos los días 10:00 | **Lee Ventas marzo** | 30 · 0 errores, **0 avisos desde abril** | Cuotas vencidas sin aviso |

**Red flags de automatizaciones**

1. **Z1 entra a Airtable con la cuenta de quien se fue.** Si se le saca el acceso sin reconectar antes, las agendas dejan de entrar y el Zap no avisa a nadie.
2. **Z3 corre "bien" y no avisa nada:** lee una tabla que dejó de recibir ventas nuevas. Es una falla silenciosa.
3. **A3 apagada y documentada como activa** en el Notion: el founder cree que el recordatorio sale.
4. **A4 es un zombie útil para Z3:** si se apaga antes de arreglar Z3, Z3 queda sin datos (ya casi no tiene).
5. **Z3 tiene un borrador sin publicar** que apunta a la vista "Cuotas vencidas" de Ventas: alguien empezó el arreglo y no lo terminó. No publicarlo sin revisar.

## Mapa de tablas y relaciones

```
Leads ──< Agendas >── (Closer: selección, no vínculo)
             │
          Ventas ──< Pagos          Ventas ──> Alumnos (A1)
             └──> Ventas marzo (A4, copia en texto)
KPIs: sin vínculos (se tipea)
```

- De **Pagos → Ventas** cuelgan `Total pagado` y `Saldo` (rollups) y la fórmula `Estado de cobro`.
- **Ventas marzo** no está vinculada: es una copia en texto. Lo que se corrige en Ventas no llega.
- **Alumnos → Ventas:** 9 alumnos sin venta vinculada (aparecen como "Unnamed record").

## Informe por tabla · riesgo alto y medio

| Tabla | Elemento | Hallazgo | Riesgo | Acción |
|---|---|---|---|---|
| Ventas marzo | Tabla entera | A4 la alimenta y Z3 la lee | Alto | Apuntar Z3 a la vista correcta de Ventas, probar, apagar A4 y **ocultar** la tabla. No borrarla |
| Ventas | Campo `Monto` | En 17 reservas se cargó el ticket completo (USD 1.800) en vez de la seña: facturación inflada | Alto | Separar `Facturación USD` de `Cash collected USD` |
| Agendas | Campo `Estado` | Mezcla estado de la llamada y del lead | Alto | `Estado de la llamada` y `Estado del lead` nuevos; el viejo a `[ARCHIVO] Estado` cuando se termine de migrar |
| Agendas | Campo `Canal` | Vacío en 468 de 1.140 (41 %): se carga a mano y nadie es responsable | Alto | Llevarlo a UTMs (skill UTMs de Punta a Punta) |
| Agendas | `Email`, `Fecha llamada`, `Closer` | Los escribe Z1 | Alto | No renombrar sin editar Z1 en el mismo momento |
| Pagos | Campo `Venta` (vínculo) | De él cuelgan `Total pagado` y `Saldo` de 212 ventas | Alto | **No tocar.** Documentar en la descripción del campo |
| KPIs | Tabla entera | Ningún número sale de un rollup: se tipean | Alto | Rehacerla con la clave mes + canal (skill Tabla de KPIs Globales) |
| Agendas | Campo `Asistió` | Dice "Sí" en 1.139 de 1.140, incluidos los cancelados: **no discrimina** | Medio | Reemplazarlo por `Estado de la llamada`; el viejo a `[ARCHIVO]` |
| Ventas | `Cuota 1 / Pago 1 … Cuota 3 / Pago 3` | Contrato y pagos en la misma fila | Medio | Separar Deals y Cuotas cobradas (Arquitecto de Base). No antes de arreglar Z3 |
| Pagos | Campo `Método` | Texto libre: "MP", "mercadopago", "Mercado Pago" | Medio | Selección única con variantes unificadas |

## Red flags

1. **Z3 lee Ventas marzo.** Desde abril, ninguna cuota vencida de ventas nuevas generó aviso. Es el hallazgo con más plata en juego.
2. **Z1 depende de la cuenta de quien se fue.** El día que alguien "limpie accesos", se cortan las agendas.
3. **A3 apagada desde marzo**, y el Notion dice que anda.
4. **Facturación inflada por 17 reservas.**
5. **El vínculo Pagos → Ventas** sostiene el saldo de 212 ventas.

## Lo que no se toca

- Ninguna tabla se borra. Ventas marzo se **oculta** después de arreglar Z3.
- Ningún campo de vínculo se borra (Pagos → Ventas, Alumnos → Ventas, Agendas → Leads).
- `Email`, `Fecha llamada` y `Closer` de Agendas no se renombran (los usa Z1). Tampoco las opciones de `Closer`.
- Ninguna automatización se apaga ni se edita durante la auditoría.
- Las 17 reservas mal cargadas no se borran: se corrige el monto y se marca la naturaleza "Reserva".

## Plan en orden de prioridad

| # | Acción | Por qué primero | Quién | Tiempo |
|---|---|---|---|---|
| 1 | Reconectar Z1 con una cuenta de Airtable del negocio, probar con un evento de prueba y **recién ahí** sacar a la exresponsable de creadora | Acceso de alguien que se fue, sin cortar las agendas | Operaciones | 30 min |
| 2 | Apuntar Z3 a la vista "Cuotas vencidas" de Ventas y probar con un registro de prueba | Cuotas vencidas sin aviso desde abril | Operaciones | 1 h |
| 3 | Revisar A3 con administración y reactivarla (o reemplazarla por Z3) | Recordatorio previo al vencimiento | Operaciones + administración | 1 h |
| 4 | Apagar A4 y ocultar Ventas marzo | Deja de generar copias | Operaciones | 15 min |
| 5 | Corregir las 17 reservas | La facturación vuelve a ser real | Administración | 1 h |
| 6 | Separar estado de la llamada y del lead en Agendas | Sin esto no hay asistencia ni cierre por canal | Operaciones + closers | 2 h |
| 7 | Pasar 3 creadores más a editor | Menos riesgo de borrados | Founder aprueba | 10 min |
| 8 | Actualizar la página "Automatizaciones" del Notion con este inventario | Que el próximo no herede un mapa falso | Operaciones | 30 min |
| 9 | Rehacer KPIs con la clave mes + canal | El founder deja de recibir números contados a mano | Operaciones | 1 día |

## Para confirmar

1. ¿Para qué se creó Ventas marzo? ¿Alguien la usa para un reporte? → **Founder** y, si responde, **la exresponsable**.
2. ¿Por qué se apagó A3? → **Administración**.
3. ¿La reserva cuenta como venta para la comisión del closer? → **Founder**.
4. ¿Quién tiene la URL de los webhooks de Discord? (Si alguien la tiene guardada en otro lado, puede publicar en el canal) → **Founder**.

## Anexo · riesgo bajo

- Alumnos: 9 registros "Unnamed record" por venta sin vincular → revisarlos uno por uno.
- Pagos: `Comprobante` vacío en el 60 % → definir si se pide o se saca de la vista.
- Agendas: vista "Vieja - no usar" → ocultarla.

---

## Anexo · La fórmula que pediste explicar (campo `Estado de cobro` de Ventas)

```airtable
IF({Saldo}=0, "Pagado", IF(IS_BEFORE({Próximo vencimiento}, TODAY()), "Vencida", "Al día"))
```

**Qué hace:** si el saldo es 0, dice "Pagado". Si no, mira la fecha del próximo vencimiento: si ya pasó, "Vencida"; si no, "Al día".

**Depende de:** `Saldo` (fórmula: `{Monto} - {Total pagado}`) y `Próximo vencimiento` (fecha cargada a mano). **La usa** la vista "Cuotas vencidas", que es la que Z3 tendría que leer: si se cambia el texto "Vencida", hay que cambiar el filtro de la vista.

**Prueba con 3 filas del CSV:**

| Venta | Monto | Total pagado | Saldo | Próximo vencimiento | Resultado | ¿Correcto? |
|---|---|---|---|---|---|---|
| V-101 | 1.800 | 1.800 | 0 | — | Pagado | Sí |
| V-145 | 1.800 | 600 | 1.200 | 05/09/2026 | Vencida | Sí |
| V-188 (reserva) | 1.800 | 200 | 1.600 | vacío | Al día | **No:** es una reserva cargada con el ticket completo y sin vencimiento |

**Conclusión:** la fórmula está bien; el dato de entrada no. Se arregla con la acción 5 del plan, no tocando la fórmula.
