# Ejemplo de output · Copiloto Operativo

> Datos ficticios. Programa grupal de 6 meses para psicólogas y psicólogos que quieren vender online, vendido por llamada en 3 cuotas. La persona que usa la skill es la coordinadora de operaciones. Se muestra la conversación completa: una pregunta general, un problema del día a día y una pregunta de herramientas.

---

**Persona:** Antes que nada: ¿qué es un MCP? Lo escucho todo el tiempo.

**Copiloto:** Es la forma en que Claude se conecta con otra app para leer y hacer cosas ahí, sin que le pegues los datos a mano.

- **En la app de Claude** eso se llama **conector**: lo activás en la configuración, elegís qué puede ver y le preguntás, por ejemplo, "¿qué alumnos tienen cuota vencida?" leyendo tu base directamente.
- **En Claude Code** se configura como **MCP** y da un control más profundo: además de leer, puede, por ejemplo, editar el diseño de un formulario de Airtable.
- Arrancá siempre con **solo lectura** y una sola base. El token de acceso no se pega nunca en un chat.

Para conectarlo paso a paso está la skill **Claude Conectado a tus Datos**. ¿Querés que lo aterricemos a tu negocio?

**Persona:** Sí, pero primero tengo un problema con las cuotas.

**Copiloto:** Antes de arrancar necesito conocer tu terreno. Contame:
1. ¿Sobre qué negocio trabajamos: el tuyo, el negocio donde trabajás o un caso práctico del programa? ¿Qué vende?
2. ¿Cuál es tu rol y de qué sos responsable?
3. ¿Cuántas personas son y quién hace qué?
4. ¿Qué herramientas usan? (comunicación, CRM, cobros, tareas, documentos, automatizaciones)
5. ¿Cuál es hoy tu mayor dolor de cabeza?

**Persona:** Donde trabajo. Programa de 6 meses para psicólogos, USD 1.800 en 3 cuotas. Soy coordinadora de operaciones: onboarding, cobros y soporte. Somos 6: el founder, 2 closers, 1 setter, 1 coach y yo. Usamos Slack, una planilla de Google para ventas y cuotas, Stripe y transferencias, y Notion. No automatizamos nada. El dolor: las cuotas vencidas. Nadie las persigue.

**Copiloto:** Entendido. Dos preguntas:
1. ¿Cuántas cuotas vencidas hay hoy y por cuánta plata?
2. ¿Cuántas horas por semana se te van en revisar la planilla contra Stripe?

**Persona:** 14 vencidas, unos USD 8.400. Reviso los lunes, 3 horas más o menos.

**Copiloto:**

**Lo que tenés hoy, en números**

| Dato | Valor |
|---|---|
| Cuotas vencidas | 14 |
| Monto vencido | USD 8.400 (equivale a 4,7 programas vendidos) |
| Horas de conciliación manual | 3 h por semana · ~12 h por mes |
| Quién persigue la deuda | Nadie (depende de que alguien se acuerde) |

Esto no es un problema de herramienta: es plata ya vendida que no entra porque nadie es dueño de cobrarla.

**Lo primero, esta semana:** una regla escrita de quién persigue y cuándo. Te propongo esta:

| Día desde el vencimiento | Qué pasa | Quién |
|---|---|---|
| Día 1 | Mensaje amable con el link de pago | Coordinación de operaciones |
| Día 7 | Segundo mensaje + aviso al closer que vendió | Coordinación de operaciones |
| Día 15 | Llamada del closer | Closer |
| Día 30 | Pausa de acceso, previa decisión del founder | Founder |

**El mensaje para el founder** (nombra roles, no personas):

> Hola [nombre]. Hoy tenemos 14 cuotas vencidas por USD 8.400 y nadie es responsable de perseguirlas. Te propongo una regla de 4 pasos (día 1, 7, 15 y 30) con un dueño por paso; te la dejo abajo. Necesito que me confirmes dos cosas antes del viernes: si los closers se suman en el día 15 y si a los 30 días pausamos el acceso. Con eso arrancamos el lunes con las 14.

**Lo siguiente sería** escribir el SOP de cuota vencida con la regla aprobada, con la skill **Constructor de SOP de Infonegocio**. Pedido para arrancar:

```
Quiero documentar el proceso de cuota vencida de un programa de 6 meses en 3 cuotas.
La regla aprobada es: [pegá la tabla]. Dueño del proceso: coordinación de operaciones.
```

**Persona:** Y cuando funcione, ¿con qué automatizo el aviso del día 1? El founder no quiere pagar nada más.

**Copiloto:** Con lo que ya tienen alcanza para arrancar.

| Opción | Qué hace y su ventaja | Costo extra | Contra |
|---|---|---|---|
| **Stripe** (lo que ya pagan) | Los recordatorios y reintentos de pago de suscripciones y facturas, configurados desde Stripe. Ventaja: ya está pago y no suma herramienta | US$0 | Solo cubre lo que se cobra por Stripe, no las transferencias |
| **Zapier gratis** | Planilla → aviso por mail o Slack cuando una cuota pasa a vencida. Ventaja: el más fácil de mantener para un equipo que nunca automatizó | US$0 hasta unas 100 tareas por mes | Se queda corto si crece el volumen |
| **n8n o Make** | Lo mismo, con más volumen y lógica. Ventaja: más barato por volumen y con ramas | Desde unos US$10 a 25 por mes | Es una herramienta nueva para un equipo que nunca automatizó |

Costos orientativos, relevados en octubre de 2026: verificalos en la página oficial antes de decidir.

**Mi recomendación:** primero Stripe para las cuotas con tarjeta (cero costo y cero herramientas nuevas) y, para las transferencias, el mensaje del día 1 a mano durante un mes con la regla nueva. Si al mes son más de 20 avisos por semana *(umbral orientativo: es el punto en que hacerlo a mano pasa de una hora por semana)*, ahí se justifica automatizarlo; diseñalo con **Diseñador de Automatizaciones**.

**Para confirmar**
- Qué cuotas se cobran por Stripe y cuáles por transferencia (con el founder o quien concilia).
- Si en su cuenta de Stripe ya están activos los recordatorios (en la configuración de facturación de Stripe).

¿Querés que te devuelva todo esto como ficha de contexto para usar en las próximas conversaciones?
