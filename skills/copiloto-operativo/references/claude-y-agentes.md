# Claude y agentes de IA · guía del Copiloto Operativo

> Referencia del Copiloto Operativo de RealOps™. Leela cuando te pregunten por Claude, por skills, conectores, MCP, agentes o qué IA usar. Sale de las clases del 16/07 (chat, Cowork o Code), 27/07 (primer agente, MCP y modo Plan), 12/08 (MCP, skill y plugin) y 01/09 (agentes con skills).
>
> **Regla:** las funciones, los nombres de menú y lo que incluye cada plan cambian seguido. Explicá el concepto y decí qué buscar por nombre; **nunca afirmes qué plan incluye qué**: "revisalo en tu cuenta".

## Las superficies de Claude

| Superficie | Qué es | Para qué en operaciones |
|---|---|---|
| **Chat** (web, app de escritorio o celular) | La conversación de siempre | Pensar, redactar, analizar algo que pegás o adjuntás, decidir |
| **Proyectos** | Una carpeta dentro del chat con instrucciones fijas y archivos de referencia | Un proyecto por negocio o por cliente: la ficha de contexto vive ahí y no la repetís |
| **Cowork** | Claude trabajando en tu computadora y en el navegador (con la extensión de Chrome), por tareas | Hacer clics en Zapier, Airtable, n8n, GoHighLevel, Canva o Sheets; tareas de varios pasos con archivos |
| **Claude Code** | Claude trabajando sobre una carpeta de tu compu (en la terminal, en VS Code o en la app de escritorio) | Agentes que trabajan solos, cruzar CSV, reportes, landings, dashboards, conectar herramientas por MCP |

Tres preguntas para elegir: ¿termina en un texto que leés vos? → chat. ¿Hay que tocar una herramienta en el navegador? → Cowork. ¿Se repite, tiene archivos o tiene que recordar? → Claude Code. Para elegir tarea por tarea, derivá a **Chat, Cowork o Code**.

## Los conceptos, explicados para operaciones

| Concepto | Qué es, en una frase | Ejemplo en un infonegocio |
|---|---|---|
| **Prompt** | El pedido que le escribís | "Armame el mensaje para el founder sobre las cuotas vencidas" |
| **Proyecto** | Instrucciones y archivos que Claude tiene presentes en todas las conversaciones de ese proyecto | Proyecto "Negocio X" con la ficha, el organigrama y los precios |
| **Skill** | Una carpeta con un `SKILL.md`: un proceso escrito en lenguaje común (qué pregunta, qué pasos sigue, qué devuelve) que Claude carga solo cuando el pedido coincide con su descripción | Todas las de la biblioteca RealOps™. "Es un SOP para Claude" |
| **Conector** | Una conexión de la app de Claude con otra herramienta (Notion, Drive, Gmail, Airtable…) para leer o hacer cosas ahí | "¿Qué alumnos tienen cuota vencida?" leyendo Airtable directo |
| **MCP** | El protocolo con el que Claude se conecta a una app. En Claude Code da un control más profundo que el conector (27/07) | Cowork crea un formulario en Airtable; Code con MCP le edita el diseño |
| **Plugin** | Un paquete que junta el MCP de una app con varias skills listas (12/08) | Plugin de una herramienta que trae la conexión y los procesos para usarla |
| **Agente** | Claude con un rol, instrucciones fijas, herramientas y memoria, que hace un trabajo de varios pasos sin que le pidas cada uno | Un agente que cada lunes arma el reporte de cobros y lo deja en una carpeta |
| **CLAUDE.md** | El archivo que define al agente en Claude Code: quién es, cómo habla, con qué herramientas trabaja, sus reglas fijas | Ver **Arquitecto de Agentes en Carpeta** |
| **memory.md** | El archivo donde el agente guarda contexto y decisiones para la próxima vez | "El 05/10 decidimos que la comisión es sobre lo cobrado" |
| **Modo Plan** | En Claude Code, primero te muestra el plan y después construye | Antes de armar una base o una landing |
| **Artifact** | Una pieza que Claude arma aparte del chat (documento, tablero, página) y se puede compartir | Un tablero simple o una página para el equipo |
| **Token y límite de uso** | La "moneda" con la que Claude mide cuánto trabaja. Cada mensaje relee toda la conversación | Por eso los chats largos gastan más y pierden el hilo |

**Skill vs. proyecto vs. agente**, en una línea: el proyecto le da a Claude el *contexto*; la skill le da un *proceso*; el agente junta contexto, procesos y herramientas para trabajar *solo*.

## Cómo instalar y usar una skill

- **En Claude (web o app):** Configuración → Capacidades → Skills → Subir skill, con el zip sin descomprimir. Si te pide activar la ejecución de código, activala. Si no ves la sección, revisá qué tiene habilitado tu cuenta.
- **En Claude Code:** copiá la carpeta a `~/.claude/skills/` (para todos los proyectos) o a `.claude/skills/` dentro de un proyecto.
- **Las 4 reglas antes de instalar cualquier skill:** leé el `SKILL.md`; si tiene scripts, leelos; mirá que el repo esté mantenido; instalá de a una y probala.
- **Crear la tuya:** **De SOP a Skill** (o skill-creator de Anthropic).

## Conectores y MCP, con seguridad

- Permiso mínimo: una sola base o espacio, **solo lectura** al principio.
- Un token o API key por proyecto (20/08). Nunca se pega en un chat, en un documento ni en el CLAUDE.md.
- Nada se escribe sin que Claude muestre antes qué va a cambiar.
- Cada pedido de permiso también consume uso: definí de entrada qué puede hacer solo (16/07).
- Paso a paso: **Claude Conectado a tus Datos**.

## El pedido de 4 elementos (27/07)

1. **Contexto:** para quién es y qué pasó antes.
2. **Objetivo:** qué querés lograr, en una frase.
3. **Fuente:** de dónde sale el dato (archivo, tabla, lo que pegás).
4. **Formato:** cómo lo querés (tabla, mail listo, 5 líneas).

Si alguien te muestra un pedido que no funciona, reescribilo con los cuatro y marcá lo que falta con `[completar]`.

## Cómo no quemar el límite de uso

- Chat largo = más gasto y menos precisión. Pedí un resumen, cerralo y abrí uno nuevo dentro del proyecto.
- Pegá el texto que importa en vez de subir un PDF entero.
- En Claude Code: `/compact` resume el historial; antes, guardá lo importante en `memory.md`.
- Una tarea por conversación.

## Agentes de IA: cuál conviene

| Tipo de agente | Qué es | Cuándo | Costo y esfuerzo |
|---|---|---|---|
| **Proyecto de Claude o GPT personalizado** | Instrucciones + archivos, responde cuando le preguntás | Un asistente para el equipo o para vos (Actividad T2) | Bajo. Se arma en una tarde |
| **Skill** | Un proceso que Claude sigue siempre igual | Algo que hacés siempre igual: un reporte, un análisis, un mensaje | Bajo. Se escribe en texto (T3) |
| **Agente en carpeta (Claude Code)** | CLAUDE.md + memory.md + skills + conexiones | Trabajo recurrente con archivos y memoria: cierre de mes, reportes, análisis de llamadas | Medio. Hace falta Claude Code |
| **Agente dentro de una automatización** | Un paso de IA en n8n, Zapier, Make o GHL que corre solo con cada evento | Cada llamada que termina vuelve con un informe; cada lead se clasifica solo (Actividad 21) | Medio. Prompt + automatización. Paga por uso de IA |
| **IA dentro de la herramienta** | Campos y agentes de IA de Airtable, Notion o GHL | Resumir o clasificar registros sin sacar los datos de la base | Bajo. Según el plan de la herramienta |
| **Setter con IA** | ManyChat (u otra) + IA respondiendo y calificando en Instagram o WhatsApp | Volumen alto de mensajes repetitivos | Medio. Empezá por la herramienta que el equipo ya conoce (26/03) |

Regla de siempre: **primero el proceso escrito, después el agente.** Un agente sobre un proceso que no existe repite el caos más rápido.

## Planes de Claude (orientativo, octubre de 2026)

Gratis con límites; **Pro** unos US$20 por mes (algo menos pagando anual); **Max** unos US$100 o US$200 por mes, con mucho más uso; **Team** por usuario, con un mínimo de usuarios; la **API** se paga aparte, por uso. Qué incluye cada plan (Cowork, Claude Code, conectores, skills) cambia: **revisalo en tu cuenta o en la página oficial de precios.**

## Claude frente a otras IA

Respondé con honestidad, sin fanatismo. Claude: redacción, análisis de documentos largos, Claude Code, skills y conectores. ChatGPT: GPTs fáciles de compartir, imágenes. Gemini: si el negocio vive en Google Workspace. Microsoft Copilot: si vive en Microsoft 365. Ver `herramientas.md`, sección "Otras IA".
