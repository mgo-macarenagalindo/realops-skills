# Ejemplo de output · Diseñador de Automatizaciones

> Datos ficticios. Programa de 4 meses de coaching para abogados independientes, vendido por llamada, en contado o en 3 cuotas. CRM y cuotas en Airtable (plan Team, base en la cuenta del negocio). El equipo se comunica por un grupo de WhatsApp; no usan Slack. Zapier no tienen. Unas 45 cuotas vencen por mes; hoy hay 18 vencidas y nadie sabe a quién le toca cobrar.

**Lo que contó la persona:** "Quiero que nadie se olvide de las cuotas. Que se avise antes de que venzan y que, si vencen, alguien se haga cargo. ¿Tengo que pagar Zapier?"

**Filtro:** el proceso tiene criterio (quién cobra, cuándo se escala), y ya está escrito: la coordinadora tiene el SOP de cobros de la semana pasada. Se sigue.

---

# Automatización · Cuotas: aviso previo, responsable y escalado

**En una frase:** Cuando una cuota está a 3 días de vencer, o vence sin pagar, Airtable avisa al alumno y a la responsable de cobros, asigna el seguimiento y escala a los 7 y 15 días, para que ninguna cuota quede sin dueño y se cobre antes.

**Plataforma:** automatizaciones nativas de Airtable · **Por qué:** los datos nacen y terminan en la base, el plan Team permite mandar mails a personas de afuera y no hay que pagar otra herramienta. · **Alternativa:** un flujo diario en n8n (30 ejecuciones por mes) si más adelante el aviso al alumno tiene que salir por WhatsApp de forma automática.

**Comparación de ventajas (adaptada a este caso):**

| Eje | Airtable nativa ✅ | Zapier | Make | n8n |
|---|---|---|---|---|
| Costo con ~70 corridas por mes | Incluido en el plan Team | Plan pago nuevo (~210 tareas) | Plan pago nuevo o gratis justo | Nube: ~30 ejecuciones (plan pago); autoalojado: servidor |
| Control | Suficiente: todo pasa en la base | Medio | Alto | El más alto |
| Escalabilidad | Sobra margen (70 de 25.000) | Sube el costo con cada paso | Buena | La mejor |
| Autoalojado | No | No | No | Sí |
| IA | No hace falta acá | Paso de IA | Módulos de IA | Nodos y agentes |
| Curva | La más baja: la coordinadora ya usa la base | Baja | Media | Alta: nadie técnico en el equipo |

**Gana acá porque** los datos nacen y terminan en la base, ya está pagada y la mantiene quien la usa. n8n ganaría si el aviso al alumno tuviera que salir solo por WhatsApp.

**Límites usados:** orientativos, revisados en octubre de 2026 (25.000 corridas por mes en Team). Confirmalos en airtable.com/pricing.

**Dueño:** Coordinación de servicio · **Ahorro estimado:** hoy la coordinadora revisa vencidas 45 min por semana y escribe a mano: unas **3 h por mes**, más las cuotas que se cobran antes. · **Costo:** unas 45 corridas (aviso previo) + 15 (vencidas) + 10 (escalados) ≈ **70 corridas por mes** de las 25.000 del plan Team.

## 0. Cuentas

La base está en la cuenta del negocio y la coordinadora es Creator. No hay que transferir nada. Los avisos de falla le llegan a quien activa la automatización: que la active la coordinadora, no el founder.

## 1. Disparadores (tres automatizaciones, una vista cada una)

| Automatización | Vista que la dispara | Filtro de la vista |
|---|---|---|
| 🤖 Cuota · aviso 3 días | "🤖 Vence en 3 días" | Estado = Pendiente · Días para vencer = 3 · Aviso previo enviado vacío |
| 🤖 Cuota · vencida | "🤖 Vencidas sin responsable" | Estado = Vencida · Responsable vacío |
| 🤖 Cuota · escalado | "🤖 Vencidas 7 y 15 días" | Estado = Vencida · Días de atraso = 7 o 15 · Último escalado ≠ hoy |

Campos nuevos en Cuotas: `Días para vencer` y `Días de atraso` (fórmulas con la fecha de hoy), `Aviso previo enviado` (fecha), `Responsable` (vínculo a la tabla Roles), `Último escalado` (fecha), `Link de pago` (texto) y `Mensaje WhatsApp` (fórmula, ver la sección 4).

## 2. Pasos

**Aviso 3 días**
1. Disparador: la cuota entra en "🤖 Vence en 3 días".
2. Enviar un mail al alumno: nombre, número de cuota, monto, fecha y link de pago.
3. Actualizar la cuota: `Aviso previo enviado` = hoy.

**Vencida**
1. Disparador: la cuota entra en "🤖 Vencidas sin responsable".
2. Actualizar la cuota: `Responsable` = el rol "Cobros" (desde la tabla Roles, no un nombre tipeado).
3. Enviar un mail a la responsable con la lista de la cuota y el botón de WhatsApp (sección 4).

**Escalado**
1. Disparador: la cuota entra en "🤖 Vencidas 7 y 15 días".
2. Grupo con condición **si Días de atraso = 7** → mail a la responsable: "segundo contacto, mensaje 2".
3. Grupo con condición **si Días de atraso = 15** → mail a la responsable y al founder: "decidir si se pausa el acceso".
4. Actualizar `Último escalado` = hoy.

## 3. Mapeo de campos

| Origen (Cuotas) | Destino (mail o mensaje) | Transformación |
|---|---|---|
| Alumno (vínculo) | Nombre del alumno | **Lookup** `Nombre del alumno` (el vínculo mandaría `rec…`) |
| Alumno → Mail | Destinatario | Lookup de texto |
| Cuota | "Cuota 2 de 3" | tal cual |
| Monto (USD) | "US$ 1.100" | formato moneda |
| Vencimiento | "15/10" | formato D/M |
| Link de pago | Botón "Pagar" | tal cual |

## 4. Canal de aviso

El equipo vive en WhatsApp y Airtable no manda WhatsApp solo. Por eso:
- **Al alumno:** mail (plan Team, hasta 100 por día a personas de afuera: alcanza).
- **A la responsable:** mail con un link `wa.me` que abre WhatsApp con el mensaje ya escrito. El link sale del campo fórmula `Mensaje WhatsApp`: `"https://wa.me/" & {WhatsApp} & "?text=" & ENCODE_URL_COMPONENT("Hola " & {Nombre del alumno} & ", te escribo por la cuota " & {Cuota} & "…")`.
- Un toque y el mensaje sale desde el número del negocio. Si más adelante quieren que salga solo, es la alternativa en n8n con un proveedor de la API de WhatsApp.

## 5. Prompt de IA

No hace falta.

## 6. Si algo falla

| Falla | Qué hace | Quién se entera |
|---|---|---|
| La cuota no tiene link de pago | La vista "🤖 Vence en 3 días" excluye las que no tienen link; una vista aparte "⚠️ Cuotas sin link" | Coordinación, en la revisión de los lunes |
| El alumno no tiene mail | El mail no sale; Airtable marca la corrida con error | La coordinadora (activó la automatización) |
| Se pagó el mismo día del aviso | Llega el aviso igual. El texto dice "si ya pagaste, ignorá este mensaje" | — |
| Alguien cambia el filtro de una vista 🤖 | Se corta el aviso. La descripción de cada vista dice "No tocar: la usa la automatización X" | — |

## 7. Plan de prueba

1. Crear un alumno de prueba con tu propio mail y una cuota que venza en 3 días → tiene que llegar el mail y completarse `Aviso previo enviado`.
2. Cambiar la cuota a Vencida → se asigna "Cobros" y llega el mail con el botón de WhatsApp (abrilo: el texto tiene que estar completo).
3. Poner `Días de atraso` = 7 (cambiando el vencimiento) → llega el segundo contacto. Con 15 → llega también al founder (usá tu mail como founder en la prueba).
4. Casos raros: cuota sin link, alumno sin mail, cuota ya pagada.
5. Borrar los registros de prueba.

## 8. Guía de armado (Airtable)

1. En Cuotas, crear los campos de la sección 1 y la fórmula de WhatsApp.
2. Crear las tres vistas con el emoji 🤖 y la descripción "No tocar el filtro".
3. Automatizaciones → Crear → disparador "Cuando un registro entra en una vista" → tabla Cuotas → vista "🤖 Vence en 3 días".
4. Acción "Enviar un mail" → destinatario: el lookup del mail → asunto y cuerpo con los campos.
5. Acción "Actualizar registro" → el ID del registro del disparador → `Aviso previo enviado` = fecha de hoy.
6. Probar con el registro de prueba (botón de probar en cada paso) → activar.
7. Repetir para "vencida" y "escalado" (en escalado, usar "Agregar grupo con condición").
8. En la descripción de cada automatización: qué hace, dueño (Coordinación de servicio) y qué campos y vistas no se renombran.

Los nombres de los menús pueden cambiar: si alguno no aparece así, buscá la función equivalente.

## 9. Cómo apagarla

En Automatizaciones, apagar el interruptor de cada una. Mientras están apagadas, la coordinadora revisa la vista "Vencidas" los lunes y miércoles, como hoy.

## 10. La siguiente, por impacto

**Recordatorios de llamada de venta.** La asistencia a las llamadas está en 64 % (36 no-shows de 100 en el último mes). Con 4 recordatorios (al agendar, 24 h antes, a primera hora y 1 h antes) los negocios del programa suelen recuperar una parte de esas llamadas; con que vuelvan 5 por mes y se cierre 1 de cada 3, son casi 2 ventas más. Plataforma: primero los recordatorios nativos de la agenda (gratis); si no alcanzan, Zapier o n8n.

---

¿La armamos juntos paso a paso? Cuando funcione, documentala con la skill Constructor de SOP de Infonegocio (modo automatización).
