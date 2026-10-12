# Ejemplo de output · Claude Conectado a tus Datos

> Datos ficticios. Caso práctico: **Mentoría Cierre Claro**, programa de 3 meses de ventas para coaches, vendido por llamada. CRM en Airtable (base "CRM Ventas" con tablas Contactos, Oportunidades, Llamadas y Cobros). La persona es asistente de operaciones, editora de la base, y trabaja en la app de escritorio de Claude.

**Lo que contó la persona:** cada lunes el founder pregunta cuántas oportunidades quedaron abiertas, cuánto se cobró y qué fuente trae más ventas. Hoy exporta un CSV y arma la respuesta a mano.

---

# Claude + Airtable · Mentoría Cierre Claro

## Conector o MCP

**Conector**, en la app de escritorio. Lo que necesitás es preguntar y pedir resúmenes en el chat; no vas a construir un agente que trabaje con la base todos los días. Si más adelante querés eso, se pasa a Claude Code con MCP.

## Checklist de conexión

- [ ] Token creado en airtable.com/create/tokens con el nombre `claude-crm-lectura`
- [ ] Permisos: `data.records:read` y `schema.bases:read` (nada de escritura)
- [ ] Acceso: solo la base **CRM Ventas** (no "todas las bases")
- [ ] Token pegado **solo** donde lo pide la conexión. No quedó en ningún documento, chat ni captura
- [ ] Claude lista bien las 4 tablas y sus campos
- [ ] Las primeras 3 preguntas verificadas contra la base
- [ ] Reglas de uso escritas en la wiki

## El primer pedido

```
Estás conectado a mi base de Airtable CRM Ventas. Antes de responder:
1. Listame las tablas y los campos que ves, para confirmar que leés bien.
2. Respondé solo con datos de la base. Si un dato no está, decímelo; no lo estimes.
3. En cada respuesta decime qué tabla y qué filtro usaste, para que lo pueda verificar.
Pregunta: ¿cuántas oportunidades quedaron abiertas esta semana (etapa distinta de
Ganada y Perdida) y de qué fuente viene cada una?
```

## Las 10 preguntas útiles para empezar

| # | Pregunta | Tabla y filtro que tiene que usar |
|---|---|---|
| 1 | ¿Cuántas oportunidades quedaron abiertas esta semana y de qué fuente viene cada una? | Oportunidades · Etapa ≠ Ganada y ≠ Perdida |
| 2 | ¿Cuáles están en Seguimiento hace más de 7 días sin actividad? | Oportunidades · Etapa = Seguimiento · última actividad < hoy − 7 |
| 3 | ¿Cuánto se cobró este mes, separado en reservas, primeros pagos y cuotas? | Cobros · Fecha en el mes · agrupado por Tipo |
| 4 | ¿Qué cuotas vencen en los próximos 7 días? | Cobros · Estado = Pendiente · Vencimiento ≤ hoy + 7 |
| 5 | ¿Qué fuente trae más ventas **ganadas** este trimestre? | Oportunidades · Etapa = Ganada · agrupado por Fuente |
| 6 | ¿Cuántas llamadas agendadas tuvo cada closer este mes y cuántas se hicieron? | Llamadas · agrupado por Closer y Estado |
| 7 | ¿Cuál es la tasa de cierre sobre agendas por fuente este mes? | Llamadas + Oportunidades · ganadas / agendadas, por Fuente |
| 8 | ¿Qué contactos entraron sin fuente cargada? | Contactos · Fuente vacía (si son muchos, el tracking está roto) |
| 9 | ¿Qué oportunidades ganadas no tienen ningún cobro asociado? | Oportunidades · Etapa = Ganada · sin registro vinculado en Cobros |
| 10 | Armame el resumen del lunes: abiertas, cobrado de la semana, cuotas por vencer y 3 alertas | Las anteriores, en 5 líneas |

Regla al preguntar: decí siempre la etapa o el estado ("ganadas", "abiertas", "pagadas") y pedí la tabla y el filtro.

## Tabla de verificación

Así quedó con las 3 primeras preguntas:

| Pregunta | Claude dijo | La base dice | ¿Coincide? |
|---|---|---|---|
| Oportunidades abiertas esta semana | 14 | 14 (vista Founder) | Sí |
| Cobrado en septiembre | USD 9.200 | USD 9.200 (vista Cobros del mes) | Sí |
| Fuente con más ventas | Webinar | Referido | **No** |

La tercera no coincidió: la pregunta decía "más ventas" y Claude contó todas las oportunidades, también las perdidas. Repreguntada como "más ventas **ganadas**", dio Referido. Va a las reglas.

## Reglas de uso · Claude conectado al CRM

> Wiki operativa · Sistemas · Claude + Airtable

- **Responsable:** operaciones.
- **Token:** `claude-crm-lectura` · solo la base CRM Ventas · solo lectura.
- **Dónde vive:** solo en la configuración de la conexión. En ningún documento.
- **Claude puede:** leer Contactos, Oportunidades, Llamadas y Cobros para responder preguntas; armar resúmenes y listas para el equipo.
- **Claude no puede (por ahora):** crear, editar ni borrar registros; cambiar tablas, campos ni vistas.
- **Cómo se pregunta:** decir siempre la etapa o el estado; pedir siempre qué tabla y qué filtro usó. Un número con el que se decide algo, se verifica.
- **Si un día se da permiso de escritura,** se actualiza esta página antes, no después.

---

¿Guardamos la pregunta 10 como plantilla para que el lunes que viene sea un solo mensaje?
