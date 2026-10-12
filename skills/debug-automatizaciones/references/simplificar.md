# Simplificar automatizaciones · criterio

> Referencia del Detective de Automatizaciones (RealOps™), modo simplificar. Sale de migraciones y consolidaciones reales en infonegocios (anonimizadas: una cuenta de Zapier de 23 Zaps, una instancia de n8n de 15 flujos, una migración de 14 Zaps a n8n) y de la ayuda oficial de las herramientas.

## Los seis patrones que buscás en el inventario

| Patrón | Cómo se ve | Qué se hace normalmente |
|---|---|---|
| **1 · Duplicadas** | Dos automatizaciones con el mismo disparador y el mismo destino (una en Zapier y otra en n8n; una "por consulta" y otra "por webhook") | Apagar una. Antes, comparar mapeo contra mapeo: la que se queda tiene que hacer **todo** lo que hacía la otra |
| **2 · Variantes** | Una por programa, por calendario, por closer o por canal, casi iguales | **Juntar en una** con un catálogo (tabla) o rutas. Agregar una variante pasa a ser una fila, no un flujo |
| **3 · Consultas que podrían ser avisos** | Disparadores "cada 15 minutos" o "cada hora" cuando la herramienta sabe mandar webhooks | Cambiar a webhook. Si se quiere red de seguridad, dejar la consulta una vez por día |
| **4 · Cadenas** | A crea un registro que dispara B, que actualiza un campo que dispara C | Juntar en un flujo con pasos, o al menos documentar la cadena. Las cadenas fallan en el eslabón que nadie mira |
| **5 · Zombies** | Encendidas y sin correr en 60 días, o borradores sin publicar | Confirmar con el área si el proceso sigue; si no, **apagar** (no borrar) con aviso. Borrar después de un mes |
| **6 · Criterio repartido en reglas** | Muchas rutas y filtros que intentan decidir algo que una persona decide leyendo (clasificar consultas, calificar un lead por lo que escribió, resumir un reporte) | Candidato a **un agente o un paso de IA** (ver abajo) |

## Tabla de decisión: ¿juntar, cambiar, apagar, agente o dejar?

| Si… | Entonces |
|---|---|
| Tienen el mismo disparador y el mismo dueño | **Juntar** en una con ramas |
| Tienen el mismo disparador pero dueños o urgencias distintas (una avisa a ventas al instante, otra arma un reporte semanal) | **Dejar separadas.** Juntarlas mezcla responsabilidades y una falla corta las dos |
| Son variantes de lo mismo (por programa, por calendario) | **Juntar** con un catálogo |
| Una consulta cada X minutos se lleva gran parte del consumo | **Cambiar a webhook** |
| La herramienta no manda webhooks | Bajar la frecuencia a lo que el negocio necesita de verdad (¿hace falta saberlo en 15 minutos o alcanza con 1 hora?) |
| Corre en Zapier o Make y cuesta más de lo que vale el plan siguiente, o hay más de 10 variantes | **Migrar a n8n** (con la regla del corte) |
| Hace algo que ya hace la herramienta de origen (recordatorios que Calendly manda solo, mails que la plataforma de cursos manda sola) | **Apagar** la automatización y usar lo nativo |
| Nadie la mira y nadie la reclama | **Apagar** (zombie) |
| Es crítica, funciona y nadie la entiende | **Dejar** y documentar antes de tocar |

## ¿Cuándo un agente de IA en vez de varias automatizaciones?

Un agente (o un paso de IA dentro de un flujo) **decide leyendo**. Una automatización **sigue reglas**. Conviene el agente cuando se cumplen las cuatro:

1. **La decisión es de criterio**, no de regla: "¿esta consulta es de cobros, de acceso o de contenido?", "¿este reporte tiene alertas?". Si la regla se puede escribir como "si el campo X = Y", no hace falta IA.
2. **Hay muchas variantes** que hoy se cubren con rutas que igual se escapan.
3. **El costo del error es bajo o hay una persona que revisa** antes de que llegue al cliente.
4. **Hay datos y ejemplos** para escribirle las reglas (preguntas frecuentes, reportes anteriores, criterios del SOP).

**No conviene** cuando: se mueve plata o accesos sin revisión humana, la regla es simple y fija, el volumen es tan bajo que lo hace una persona en 5 minutos por semana, o nadie va a mantener las instrucciones del agente.

**Ejemplos de infonegocio:**
- 5 Zaps que mandan a Discord los reportes de fin de día de setters, closers y coaches, con rutas por rol → **un flujo** que recibe todos los reportes y **un paso de IA** que arma un solo resumen diario para el founder con alertas ("2 closers sin reporte", "un alumno pidió pausa").
- 7 rutas que intentan clasificar los mensajes de alumnos por palabras clave → **un agente** que clasifica, responde lo frecuente con la wiki y deriva el resto a la persona correcta.
- Calificar un lead por "facturación mensual declarada" (una opción del formulario) → **no hace falta agente**: es un filtro. El agente tendría sentido si hubiera que leer una respuesta abierta.

Para diseñar el agente: **Arquitecto de Agentes en Carpeta** (si vive en Claude) o **Prompt de IA para Automatizaciones** (si es un paso dentro de n8n, Zapier o Airtable).

## Antes y después: cómo se mide

| Medida | Cómo |
|---|---|
| Cantidad de automatizaciones | Contar activas |
| Consumo por mes | Tareas, operaciones, ejecuciones o corridas (del historial) |
| Puntos de falla | Conexiones, webhooks escritos a mano, campos y opciones de los que depende |
| Cuentas | Cuántas piezas dependen de una sola persona |
| Avisos repetidos | Mensajes duplicados por evento |

Ejemplo real (anonimizado): 15 flujos de n8n con unas 4.500 ejecuciones por mes. Dos que "preguntaban" cada 15 minutos y cada hora se llevaban el 80 %. Cambiándolos a webhook y apagando un duplicado, el consumo bajaba a entre 900 y 2.400 por mes, y los avisos llegaban antes.

## Plan de corte en tandas

1. **Tanda 1 · Lo que no puede romper nada:** apagar zombies, borradores y duplicados que no hacen nada distinto. Bajar frecuencias.
2. **Tanda 2 · Lo interno:** avisos al equipo, reportes. Si sale mal, se entera el equipo, no el cliente.
3. **Tanda 3 · Lo que toca datos:** carga en el CRM, asignaciones. Comparar mapeo contra mapeo antes.
4. **Tanda 4 · Lo que toca clientes o plata:** mails a alumnos, accesos, cobros.

En cada tanda, la regla del corte: **construir → probar con un canal y una base de prueba → activar la nueva y apagar las viejas en el mismo momento → mirar la primera semana → borrar las viejas después de un mes.** Nunca las dos prendidas: se duplica todo.

**Ojo con los cambios que se pisan:** si dos personas (o dos sesiones de un asistente) editan el mismo flujo, la última que guarda gana y no siempre queda historial. Un responsable por tanda.
