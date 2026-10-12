# Elegir la plataforma: Airtable, Zapier, Make o n8n

> Referencia del Diseñador de Automatizaciones (RealOps™). Cargala en el Paso 2, antes de escribir la spec. Los límites y precios de los planes cambian seguido: los de acá son orientativos (revisados en octubre de 2026). Antes de decidir, que el alumno los confirme en la página de planes de la herramienta.

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

## Límites que cambian el diseño (octubre de 2026, confirmalos)

**Airtable**
- Corridas por mes y por workspace: Free 100 · Team 25.000 · Business 100.000. Una corrida que falla también cuenta.
- Hay un tope de automatizaciones por base (depende del plan) y **las apagadas también cuentan**: borrá las que no se usan.
- En el plan gratis no está la acción "Ejecutar un script" y "Enviar un mail" solo llega a colaboradores de la base, no a alumnos ni a leads.
- Una automatización nueva no corre sobre los registros que ya existían.
- Solo un Creator u Owner crea o edita automatizaciones. Los avisos de falla le llegan a la última persona que la activó: que sea una cuenta del negocio.

**Zapier**
- Cuenta tareas por paso de acción exitoso. Un Zap de 5 acciones que corre 100 veces son 500 tareas.
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
