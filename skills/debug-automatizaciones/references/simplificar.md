# Simplificar automatizaciones · criterio

> Referencia del Detective de Automatizaciones (RealOps™), modo simplificar. Sale de migraciones y consolidaciones reales en infonegocios (anonimizadas: una cuenta de Zapier de 23 Zaps, una instancia de n8n de 15 flujos, una migración de 14 Zaps a n8n) y de la ayuda oficial de las herramientas.

## Los seis patrones que buscás en el inventario

| Patrón | Cómo se ve | Qué se hace normalmente |
|---|---|---|
| **1 · Duplicadas** | Dos automatizaciones con el mismo disparador y el mismo destino (una en Zapier y otra en n8n; una "por consulta" y otra "por webhook") | Apagar una. Antes, comparar mapeo contra mapeo: la que se queda tiene que hacer **todo** lo que hacía la otra |
| **2 · Variantes** | Una por programa, por calendario, por closer o por canal, casi iguales | **Juntar en una** con un catálogo (tabla) o rutas. Agregar una variante pasa a ser una fila, no un flujo |
| **3 · Consultas que podrían ser avisos** | Disparadores "cada 15 minutos" o "cada hora" cuando la herramienta sabe mandar webhooks | Cambiar a webhook. Si se quiere red de seguridad, dejar la consulta una vez por día |
| **4 · Cadenas** | A crea un registro que dispara B, que actualiza un campo que dispara C | Juntar en un flujo con pasos, o al menos documentar la cadena. Las cadenas fallan en el eslabón que nadie mira |
| **5 · Zombies** | Encendidas y sin correr en 60 días (orientativo), corriendo sin datos desde hace meses, con error de conexión repetido, o borradores sin publicar | Confirmar con el área si el proceso sigue; si no, **apagar** (no borrar) con aviso. Borrar después de un mes |
| **6 · Criterio repartido en reglas** | Muchas rutas y filtros que intentan decidir algo que una persona decide leyendo (clasificar consultas, calificar un lead por lo que escribió, resumir un reporte) | Candidato a **un agente o un paso de IA** (ver abajo) |

## El "5 en 1": agrupar por evento de negocio

Las consolidaciones grandes no aparecen mirando una plataforma por vez. Aparecen cuando armás el **mapa de eventos** del inventario: por cada cosa que pasa en el negocio, todo lo que la escucha.

| Evento de negocio | Qué lo escucha (plataforma · cuenta) | Qué hace cada una | Campo o destino que comparten |
|---|---|---|---|
| Entra un pago | … | … | … |
| Se cierra una venta | … | … | … |
| Alguien agenda | … | … | … |
| Entra un lead | … | … | … |

**Señales de que hay un 5 en 1:**
- El mismo evento dispara 3 o más automatizaciones (umbral orientativo), en distintas plataformas o cuentas.
- Dos de ellas avisan lo mismo a la misma persona (el aviso propio de la herramienta + un Zap que avisa lo mismo).
- Una escribe en un lugar que ya nadie usa (la planilla vieja que "sigue sumando sola").
- Una crea un registro que dispara otra (cadena) y la segunda depende de que la primera no se corte.
- Un evento "hermano" que importa **no lo escucha nadie** (se escuchan los pagos exitosos y no los rechazados).

**Cómo se diseña la pieza única** (el detalle va con Diseñador de Automatizaciones):
1. **Un solo disparador por webhook** en el origen, que escuche también los eventos que hoy nadie escucha (pago rechazado, disputa, reprogramación).
2. **Buscar por ID, no por mail:** el ID de cliente de la pasarela o del CRM, guardado en la base la primera vez.
3. **Ramas por caso** (primer pago → alta de venta y alumno · cuota → registrar pago · rechazado → aviso a cobranzas) en vez de una automatización por caso.
4. **Lo que es cálculo, a la base:** totales, comisiones y estados como fórmulas o rollups, no como filas que escribe una automatización.
5. **Un solo aviso por evento,** al rol que actúa, con una rama de error que avise si algo no se encontró.
6. **Lo que se retira, explícito:** planillas viejas, avisos repetidos, webhooks a cuentas ajenas (se borran del origen después del corte).

## Dónde vive la pieza nueva: ventajas de cada plataforma

Se acepta cualquier plataforma **bien justificada**. Mostrá siempre las ventajas de cada opción para ese caso y marcá la elegida con una línea "gana acá porque…". Es una guía cualitativa; los números de planes cambian (los de abajo son **orientativos**, revisados en octubre de 2026: confirmalos en la página de planes).

| Eje | Airtable nativa | Zapier | Make | n8n | GoHighLevel |
|---|---|---|---|---|---|
| **Gana cuando…** | Todo pasa adentro de la base | Hay que unir 2 o 3 apps rápido y el equipo no es técnico | Hay ramas, búsquedas y transformación de datos con presupuesto ajustado | Hay mucho volumen, IA, código, o se quiere control de los datos | El CRM y la agenda ya viven ahí |
| **Cómo cobra** | Corridas por mes por workspace (Free ~100, Team ~25.000) | Tareas: cada paso de acción (Free ~100 y Zaps de 2 pasos) | Operaciones por módulo (Free ~1.000); las consultas vacías también gastan | Ejecuciones por corrida, sin importar los pasos; autoalojado sin tope | Incluido en la suscripción |
| **Control de errores** | Bajo: aviso por mail a quien la activó | Medio | Alto: rutas de error por módulo | El más alto: flujo de errores propio, reintentos | Medio; no avisa si dos workflows se pisan |
| **Quién la mantiene** | Quien administra la base | Cualquiera del equipo | Alguien con algo de práctica | Alguien técnico o un manual operativo | Quien administra el CRM |
| **Contra** | Tope de corridas, sin scripts en el Free | El más caro con volumen | Curva media | Curva alta; servidor si es propio | Cerrado a su ecosistema |

La tabla completa, con IA, escalabilidad y autoalojado, está en Diseñador de Automatizaciones (`references/elegir-plataforma.md`).

## Dos órdenes que no se negocian

1. **Migrar primero, revocar después.** Si la automatización de entrada (leads, pagos) vive en la cuenta de alguien que se fue o de una agencia, primero se rehace en una cuenta del negocio, se prueba y se activa; **recién después** se le saca el acceso a esa persona. Al revés, se corta la entrada. Lo mismo con los webhooks a cuentas ajenas: si la cuenta de un tercero se va a dar de baja en una fecha, esa fecha es el límite del plan.
2. **Un campo, una mano.** Si un campo lo escriben dos automatizaciones y una persona, el resultado depende de quién escribió último. La pieza nueva es la única que lo escribe, o el campo pasa a fórmula. Si pasa a fórmula, **las automatizaciones que lo escribían se reconfiguran en el mismo cambio**: si no, empiezan a fallar.

## Plan gratis de Airtable: alternativa manual y cuándo pagar

Números **orientativos** (octubre de 2026; confirmalos en airtable.com/pricing): Free ~100 corridas por mes por workspace, sin scripts, y el mail solo llega a colaboradores de la base · Team ~25.000 corridas, se cobra por persona.

- **Antes de pagar:** estados calculables a fórmula + vista (0 corridas) · programadas de varias veces por día a una por día o a un resumen diario · alternativa manual para lo que no entra (vista "Para hoy", mensaje listo para copiar o botón `wa.me`, casilla "Avisado" con fecha) · lo que une herramientas, a Make o n8n.
- **Cuándo conviene pagar (criterio orientativo):** más del 80 % del tope dos meses seguidos aun después de bajar el consumo · lo manual pasa de una hora por semana · el corte ya tocó clientes o plata · hay que escribirle automáticamente a alumnos o leads. Compará el plan pago contra sumar Make o n8n.
- **Mientras se decide:** que el aviso de "llegaste al tope" le llegue a una cuenta del negocio que alguien lee, y una vista o un contador del uso del mes a la vista.

## Tabla de decisión: ¿juntar, cambiar, apagar, agente o dejar?

| Si… | Entonces |
|---|---|
| Tienen el mismo disparador y el mismo dueño | **Juntar** en una con ramas |
| Tienen el mismo disparador pero dueños o urgencias distintas (una avisa a ventas al instante, otra arma un reporte semanal) | **Dejar separadas.** Juntarlas mezcla responsabilidades y una falla corta las dos |
| Son variantes de lo mismo (por programa, por calendario) | **Juntar** con un catálogo |
| Una consulta cada X minutos se lleva gran parte del consumo | **Cambiar a webhook** |
| La herramienta no manda webhooks | Bajar la frecuencia a lo que el negocio necesita de verdad (¿hace falta saberlo en 15 minutos o alcanza con 1 hora?) |
| Corre en Zapier o Make y cuesta más de lo que vale el plan siguiente, o hay más de 10 variantes (umbral orientativo) | **Migrar a n8n** (con la regla del corte) |
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
