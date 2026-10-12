# Ejemplo de output · Claude Conectado a tus Datos

> Datos ficticios. Caso práctico: **Mentoría Cierre Firme**, programa de 3 meses de ventas para coaches, vendido por llamada. CRM en Airtable (base "CRM Ventas": Contactos, Oportunidades, Llamadas, Cobros), cobros por Stripe y agenda en Calendly. Las aplicaciones entran por GoHighLevel. La persona es asistente de operaciones, editora de la base, y trabaja en la app de escritorio de Claude y en Claude Code.

**Lo que contó la persona:** cada lunes el founder pregunta cuántas oportunidades quedaron abiertas, cuánto se cobró y qué fuente trae más ventas. Hoy exporta CSV de Airtable y de Stripe y arma la respuesta a mano. Adjuntó el export de Oportunidades y Cobros del 30/09. Encontró en GitHub "un MCP de GoHighLevel" y quiere saber si lo puede instalar.

---

# Claude + Airtable, Stripe y GoHighLevel · Mentoría Cierre Firme

## Qué conectamos y por qué este camino

| Plataforma | Escalón | Por qué | Descartado |
|---|---|---|---|
| Airtable | 1 · conector oficial | Está en el directorio de Claude; lo único que necesitás es preguntar | MCP en Claude Code: no hace falta todavía |
| Stripe | 1 · conector oficial del directorio de Claude (documentado por Stripe el 12/10/2026; verificá que lo veas en tu directorio) | Login de Stripe (OAuth): en la pantalla de permisos elegís primero el **sandbox** y después la cuenta real, con permisos de lectura | Clave secreta completa o restringida sin etiqueta "Agent": Stripe deja de aceptarlas el 31/10/2026 |
| Calendly | 5 · puente que ya existe | Un Zap ya pasa cada agenda a la tabla Llamadas. Preguntarle a Airtable alcanza. Por qué Zapier y no otro: ya está pagado, lo mantiene quien arma las automatizaciones y son 60 agendas por mes (con mucho más volumen, Make o n8n saldrían más baratos) | Buscar un servidor de Calendly: no suma nada hoy |
| GoHighLevel | 4 · comunidad → **no se instala** | Ver la ficha | — |

## Ficha de seguridad · el "MCP de GoHighLevel" de GitHub

| Pregunta | Resultado |
|---|---|
| ¿Quién lo publica? | 🔴 Una cuenta personal sin otros proyectos; dice ser "para el servidor oficial", pero GoHighLevel no lo menciona en su documentación |
| ¿Código a la vista y licencia? | 🟡 Público, sin archivo de licencia |
| ¿Mantenido? | 🔴 Último cambio hace 8 meses, 3 issues sin respuesta (uno sobre el token) |
| ¿Qué pide? | 🔴 Token de integración con todos los permisos "para que funcione todo" |
| ¿Solo lectura? | 🔴 No tiene modo de lectura |

**Resultado: no se instala.** Las aplicaciones de GoHighLevel ya llegan a Oportunidades por el Zap: se le pregunta a Airtable. Para confirmar con el founder si hoy hay servidor oficial de GoHighLevel (revisar su documentación).

## Checklist de conexión

- [ ] **Airtable:** conector activado. Al autorizar, **solo la base CRM Ventas**. Si te pide token: `claude-crm-lectura`, con `data.records:read` y `schema.bases:read`
- [ ] **Stripe:** conector oficial desde el directorio de Claude (en Claude Code, `https://mcp.stripe.com`). Login con un usuario de Stripe del negocio; en los permisos, primero el **sandbox** y una pregunta de prueba ("listame los últimos 5 pagos"), después la cuenta real. Si alguna herramienta pide clave, una **clave de agente** con permisos de lectura, nunca la clave secreta
- [ ] Activada la aprobación de herramientas en Claude: el servidor de Stripe también puede escribir (reembolsos, links de pago)
- [ ] Ningún token quedó en un chat, documento, captura ni archivo de configuración compartido
- [ ] Claude lista bien las 4 tablas de Airtable y los objetos de Stripe (clientes, cobros, suscripciones)
- [ ] Las 3 primeras preguntas verificadas (tabla de abajo)
- [ ] Reglas de uso en la wiki
- [ ] Revisado en la documentación de Airtable y Stripe el límite de consultas del plan del negocio (no hace falta para preguntar en el chat; sí para un agente diario)

## Campos que no son confiables

| Campo | Problema | Regla |
|---|---|---|
| Oportunidades · `Etapa` = "Seguimiento" | Se actualiza a mano; 12 tienen "Seguimiento" desde hace más de 30 días | Para "abiertas", usá Etapa ≠ Ganada y ≠ Perdida, y avisá cuántas no tienen actividad hace 30 días |
| Cobros · `Monto` | Mezcla reservas y cuotas | Separá siempre por `Tipo` |
| Contactos · `Fuente` | Vacía en el 22 % | Decí cuántas quedan "sin fuente" antes de dar un ranking |

## El primer pedido

```
Estás conectado a mi base de Airtable "CRM Ventas" y a la cuenta de Stripe del negocio (solo lectura).
1. Listame las tablas y campos de Airtable y los objetos que ves en Stripe.
2. Respondé solo con esos datos. Si un dato no está, decímelo; no lo estimes.
3. En cada respuesta decime la fuente (Airtable o Stripe), la tabla u objeto y el filtro.
4. Reglas: "abiertas" = Etapa distinta de Ganada y Perdida. Cobrado = pagos exitosos en Stripe
   más transferencias en la tabla Cobros. En rankings por fuente, decí cuántas no tienen fuente.
```

## Las 10 preguntas útiles para empezar

| # | Pregunta | Fuente y filtro |
|---|---|---|
| 1 | ¿Cuántas oportunidades quedaron abiertas y de qué fuente? | Airtable · Oportunidades · Etapa ≠ Ganada/Perdida |
| 2 | ¿Cuáles están en Seguimiento hace más de 7 días sin actividad? | Airtable · Oportunidades · Etapa = Seguimiento · última actividad < hoy − 7 |
| 3 | ¿Cuánto se cobró este mes, separado en reservas, primeros pagos y cuotas? | Stripe (pagos exitosos) + Airtable · Cobros (transferencias) |
| 4 | ¿Qué pagos fallaron esta semana y de quién? | Stripe · pagos fallidos |
| 5 | ¿Qué cuotas vencen en los próximos 7 días? | Airtable · Cobros · sin pagar · vencimiento ≤ hoy + 7 |
| 6 | ¿Qué fuente trae más ventas **ganadas** este trimestre? | Airtable · Oportunidades · Etapa = Ganada · por Fuente |
| 7 | ¿Cuántas llamadas tuvo cada closer este mes y cuántas se hicieron? | Airtable · Llamadas (las carga el Zap de Calendly) |
| 8 | ¿Hay ventas ganadas sin ningún cobro en Stripe ni en Cobros? | Airtable · Oportunidades Ganadas cruzadas con Stripe por mail |
| 9 | ¿Qué contactos entraron sin fuente? | Airtable · Contactos · Fuente vacía |
| 10 | Resumen del lunes: abiertas, cobrado de la semana, pagos fallidos, cuotas por vencer y 3 alertas | Las anteriores, en 5 líneas |

## Tabla de verificación

"Qué dicen los datos" sale calculado desde los exports que adjuntaste (corte 30/09). Corré las preguntas con la conexión y completá la columna de Claude.

| Pregunta | Qué dicen los datos (export 30/09) | Claude conectado | ¿Coincide? | Si no, por qué |
|---|---|---|---|---|
| Abiertas al 30/09 | 14 (Etapa ≠ Ganada/Perdida) | 14 | Sí | — |
| Cobrado en septiembre | USD 9.200 (Cobros, Fecha de pago en septiembre) | USD 9.650 | **No** | Stripe incluye un pago del 30/09 a las 23 h que en Airtable se cargó el 01/10. Regla: el cobrado del mes sale de Stripe + transferencias, con fecha de Stripe |
| Fuente con más ventas ganadas | Referido (9 de 21) | Webinar | **No** | Claude contó todas las oportunidades, también las perdidas. Repreguntada como "ganadas", dio Referido |

## Reglas de uso · Claude conectado al CRM y a Stripe

> Wiki operativa · Sistemas · Claude + datos

- **Responsable:** operaciones.
- **Conexiones:** conector oficial de Airtable (solo la base CRM Ventas, lectura) y conector oficial de Stripe (usuario del negocio, permisos de lectura). Verificados el 12/10/2026: revisar en la próxima actualización de la wiki.
- **Dónde viven las credenciales:** solo en la configuración de cada conexión.
- **Cuentas:** las dos son del negocio. Si alguna pasa a la cuenta personal de alguien, se revisa esta página.
- **Claude puede:** leer y armar resúmenes y listas.
- **Claude no puede (por ahora):** crear, editar ni borrar registros; reembolsar, cobrar ni tocar nada en Stripe.
- **Cómo se pregunta:** decir siempre el estado ("ganadas", "abiertas", "cobrado"); pedir siempre la fuente y el filtro. Un número con el que se decide algo, se verifica.
- **No se instala** ningún servidor que no haya pasado la ficha de seguridad.
- **Si un día se da permiso de escritura,** se actualiza esta página antes, no después.

## Para confirmar

1. ¿Hay hoy un servidor oficial de GoHighLevel? → revisar su documentación (operaciones).
2. ¿Quién del negocio da el usuario de solo lectura de Stripe? → founder.

---

¿Guardamos la pregunta 10 como plantilla para que el lunes que viene sea un solo mensaje?
