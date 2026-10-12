# Elegir la plataforma: Airtable, Zapier, Make o n8n

> Referencia del Diseñador de Automatizaciones (RealOps™). Cargala en el Paso 2, antes de escribir la spec. Los límites y precios de los planes cambian seguido: **todos los números de esta referencia son ORIENTATIVOS** (revisados en octubre de 2026, no salen de las clases sino de la documentación pública). Antes de decidir, que el alumno los confirme en la página de planes de la herramienta. En cada relanzamiento se revisan con la lista del final.

## La regla corta

1. **Si todo pasa adentro de la base** (los datos nacen y terminan en Airtable, y el aviso es un mail o un mensaje): **automatización nativa de Airtable**. No sumes otra herramienta.
2. **Si hay que unir dos o más herramientas y el negocio ya paga Zapier o Make**: usá esa, siempre que la cuenta esté a nombre del negocio.
3. **Si el flujo tiene muchas ramas, código, IA, mucho volumen o va a crecer**: n8n.
4. **Lo que decide de verdad** es dónde viven los datos, quién la va a mantener y cuánto cuesta por mes con el volumen real. La herramienta que te gusta no entra en la cuenta.

## Tabla de decisión

| Criterio | Airtable nativa | Zapier | Make | n8n |
|---|---|---|---|---|
| Mejor para | Lo que pasa adentro de la base: copiar, asignar, avisar, crear tareas, recordatorios desde vistas | Unir 2 o 3 apps en línea recta, rápido, sin código | Flujos visuales con muchas ramas, iteradores y transformación de datos | Flujos largos, código, IA, webhooks propios, alto volumen, aprobaciones con botón |
| Quién la mantiene | Quien administra la base (Creator) | Cualquiera del equipo | Alguien con algo de práctica | Alguien técnico, o un agente con el manual operativo |
| Cómo cobra | **Corridas por mes, por workspace**. Cuenta cada vez que se dispara, aunque falle | **Tareas**: cada paso de acción que sale bien. Disparadores, filtros, rutas (Paths), Formatter y Delay no cuentan | **Operaciones o créditos**: cada módulo que corre. Un disparador que consulta cada X minutos gasta aunque no encuentre nada | **Ejecuciones**: cada corrida completa, tenga 3 nodos o 50. Instalado en un servidor propio no tiene tope |
| Disparador "cuando pasa algo" | Registro creado, actualizado, entra en una vista, cumple una condición, formulario enviado, botón, webhook, horario | Instantáneo (webhook) o consulta cada 1 a 15 min según el plan | Instantáneo (webhook) o programado | Webhook, disparador de la app, programado |
| Puntos débiles | Tope de corridas en el plan gratis, no espera sola, el plan gratis no tiene scripts y solo manda mail a colaboradores | El costo sube con cada paso, los Zaps se multiplican sin orden | Curva de aprendizaje, el costo de las consultas vacías | Requiere más criterio técnico, n8n en la nube cobra por ejecución |

## Ventajas competitivas de cada opción (mostralas siempre)

Para cualquier automatización, también la de la Actividad 13, se acepta la plataforma que mejor se justifique. La justificación se escribe con estos seis ejes. Es una guía cualitativa: adaptala al caso (el volumen, quién mantiene, qué ya pagan).

| Eje | Airtable nativa | Zapier | Make | n8n |
|---|---|---|---|---|
| **Costo** | Incluido en el plan de la base; el gratis alcanza para poco volumen | El más caro por volumen: cobra cada paso de acción | Más barato que Zapier por operación, pero gasta en consultas vacías | Nube: por ejecución, sin importar los pasos. Autoalojado: solo el servidor |
| **Control** | Bajo: lo que la base permite | Medio: pasos cerrados, poco detalle de errores | Alto: ves y transformás cada dato | El más alto: código, flujo de errores propio, reintentos |
| **Escalabilidad** | Hasta el tope de corridas del plan; se ordena mal con muchas automatizaciones | Escala pagando; los Zaps se multiplican sin orden | Buena con escenarios grandes | La mejor para flujos largos y mucho volumen |
| **Autoalojado** | No | No | No | **Sí** (los datos quedan en tu servidor), o nube si nadie quiere mantener servidor |
| **IA** | Campos y agentes de IA según el plan, adentro de la base | Paso de IA y conectores de modelos; simple | Módulos de IA y HTTP a cualquier modelo | Nodos de IA y agentes con herramientas; el más flexible |
| **Curva de aprendizaje** | La más baja si ya usás la base | Baja: cualquiera del equipo | Media | La más alta: alguien con criterio técnico o un manual operativo |
| **Gana cuando…** | Todo pasa adentro de la base | Hay que unir 2 o 3 apps rápido y el equipo no es técnico | Hay muchas ramas y transformación de datos, con presupuesto ajustado | Hay IA, código, aprobaciones, mucho volumen, o se quiere control de los datos |

Cómo se escribe en la spec: la tabla adaptada (podés resumir cada celda a 2 o 3 palabras), la elegida marcada y una línea "gana acá porque…". Si el alumno quiere otra (por ejemplo n8n para aprender), se acepta si la línea se sostiene; si no, se dice qué le cuesta de más (plata, mantenimiento o tiempo).

## Plan gratis de Airtable: la alternativa manual y cuándo pagar

Lo que el plan gratis no hace (orientativo, octubre de 2026): más de ~100 corridas por mes por workspace, scripts, y mails a personas que no son colaboradoras de la base (alumnos, leads).

**La alternativa manual** (sirve para todo lo que no entra):
1. Una **vista "Para hoy"** con la fórmula que dice qué toca (por ejemplo `Acción de hoy`), que la persona responsable abre a una hora fija.
2. Un campo con el **mensaje listo para copiar** o un **botón `wa.me`** con el texto armado: un toque por persona.
3. Un **resumen diario** por mail a la responsable (una corrida por día, no una por registro): unas 30 corridas por mes en vez de una por cada caso.
4. Una casilla "Avisado" con fecha para que nadie escriba dos veces.

**Cuándo conviene pagar** (criterio orientativo, para un infonegocio chico; confirmalo con los precios del momento):
- Las corridas que necesitás pasan del 80 % del tope gratis dos meses seguidos, aun con resumen diario.
- Lo manual de la alternativa lleva más de 1 hora por semana, o ya se olvidaron avisos que costaron plata (una cuota sin cobrar, un acceso tarde).
- Necesitás escribirle de forma automática a alumnos o leads (no a colaboradores).
Si se cumple uno: compará el precio del plan pago de Airtable con sumar Zapier, Make o n8n (a veces sale más barato sumar una herramienta que pagar la base para todo el equipo, porque Airtable cobra por persona).

## Límites que cambian el diseño (octubre de 2026, ORIENTATIVOS: confirmalos)

**Airtable**
- Corridas por mes y por workspace: Free 100 · Team 25.000 · Business 100.000. Una corrida que falla también cuenta. (Al 12/10/2026 la página oficial de precios no muestra las corridas; los números coinciden en guías de terceros de julio de 2026. Team: US$20 por persona por mes, anual.) El Free también tiene tope de 1.000 registros por base.
- Hay un tope de automatizaciones por base (depende del plan) y **las apagadas también cuentan**: borrá las que no se usan.
- En el plan gratis no está la acción "Ejecutar un script" y "Enviar un mail" solo llega a colaboradores de la base, no a alumnos ni a leads.
- Una automatización nueva no corre sobre los registros que ya existían.
- Solo un Creator u Owner crea o edita automatizaciones. Los avisos de falla le llegan a la última persona que la activó: que sea una cuenta del negocio.

**Zapier**
- Cuenta tareas por paso de acción exitoso. Un Zap de 5 acciones que corre 100 veces son 500 tareas.
- Planes (zapier.com/pricing, verificado el 12/10/2026): **Free** 100 tareas por mes y solo Zaps de 2 pasos · **Professional** desde 750 tareas (US$19,99 por mes, anual) · **Team** desde 2.000 tareas. Ya no existe un plan "Starter": si un alumno lo nombra, es el Professional.
- El historial se guarda por un tiempo limitado según el plan (en planes chicos, 30 días): si vas a auditar, exportalo antes.
- Los disparadores que consultan (no instantáneos) chequean cada 1 a 15 minutos según el plan.

**Make**
- Cada módulo que corre consume. Un escenario programado cada 15 minutos gasta unas 2.900 consultas por mes aunque no haya datos nuevos: si la app tiene disparador instantáneo o webhook, usalo.

**n8n**
- En la nube, cada corrida es una ejecución, sin importar los nodos. Un disparador programado cada 15 minutos son unas 2.900 ejecuciones por mes: eso solo puede comerse el plan.
- Instalado en un servidor propio no hay tope de ejecuciones, pero alguien mantiene el servidor.

## Cuentas: antes de elegir, preguntá a nombre de quién

Toda herramienta que conectes tiene que estar **a nombre de un mail del negocio**, no de una persona. Si la base, el Zapier o el formulario están en la cuenta personal de alguien:
- Si esa persona se fue: **primero recuperar o rehacer la cuenta, después automatizar**. Construir sobre esa cuenta es construir sobre algo que el negocio no controla.
- Si sigue en el equipo: se puede construir, pero la transferencia a una cuenta del negocio va como paso 0 con fecha.

## Calcular el costo antes de construir

Fórmula: **veces por mes × unidades por corrida**.
- Airtable: 1 corrida por disparo.
- Zapier: número de pasos de acción.
- Make: número de módulos (más las consultas vacías si es programado).
- n8n nube: 1 ejecución por disparo (más las corridas vacías si es programado).

Ejemplo: aviso de cuota vencida con 3 acciones, 60 cuotas por mes → Airtable 60 corridas · Zapier 180 tareas · Make 240 operaciones · n8n 60 ejecuciones. Si en vez de disparar por registro se programa "todos los días a las 9 revisá vencidas": 30 corridas por mes en cualquiera, encuentre o no.

**Regla:** si el disparo "cuando pasa algo" existe, preferilo al "cada X minutos". Gasta menos y avisa antes.

## Revisión por relanzamiento (hacerla antes de cada edición del programa)

Los planes de terceros cambian varias veces por año. En cada relanzamiento, quien mantiene la biblioteca revisa y actualiza la fecha de arriba:

| Qué revisar | Dónde |
|---|---|
| Corridas por mes y acciones del plan gratis de Airtable (mail a externos, scripts) | airtable.com/pricing y support.airtable.com (automatizaciones) |
| Tareas por mes del plan más chico de Zapier, qué cuenta como tarea, frecuencia de consulta | zapier.com/pricing y help.zapier.com |
| Operaciones o créditos de Make y su plan gratis | make.com/en/pricing |
| Ejecuciones de n8n en la nube y condiciones del autoalojado | n8n.io/pricing |

Si un número cambió, se actualiza acá y en los ejemplos que lo usan (`ejemplo-de-output.md`). Si en una conversación no se puede verificar, la skill lo dice y deja el número como orientativo.
