# Ejemplo de output · Chat, Cowork o Code

> Datos ficticios. Caso práctico: **Academia Fluent Kids**, programa online de inglés para chicos de 8 a 12 años, vendido a madres y padres por llamada. La persona es asistente de operaciones.

**Lo que pegó la persona:** "Esta semana tengo que: 1) contestarle al founder por qué el onboarding de 6 familias se atrasó; 2) conectar Calendly con Airtable para que las llamadas se carguen solas; 3) resumir 12 llamadas de venta del mes para ver por qué no cierran; 4) armar el reporte del lunes como todas las semanas; 5) ordenar la carpeta de Drive del equipo." Tiene Claude en la app de escritorio, la extensión de Chrome y VS Code con Claude Code (lo revisó en su cuenta).

---

# Dónde hacer cada cosa · semana del 12/10

## Antes de empezar

Lo revisaste en tu cuenta: tenés app de escritorio, extensión de Chrome y Claude Code en VS Code. La tabla de superficies y la guía para chequear qué tenés están revisadas al 12/10/2026 (se revisan en cada relanzamiento del programa); si las leés más de 3 meses después, confirmá los nombres en el centro de ayuda oficial de Claude.

## Tabla de decisión

| Tarea | Superficie | Por qué |
|---|---|---|
| 1 · Mensaje al founder | **Chat** | Termina en un texto que vas a revisar vos. Es único |
| 2 · Calendly → Airtable | **Cowork con Chrome** | Hay que hacer clics en Zapier y en Airtable. Que te guíe mirando la pantalla |
| 3 · Resumir 12 llamadas | **Chat, dentro de un proyecto** | Es análisis de texto que pegás. El proyecto guarda el contexto del negocio y el guion de venta |
| 4 · Reporte del lunes | **Claude Code** | Se repite cada semana con el mismo formato: tiene que vivir en una carpeta con su memoria |
| 5 · Ordenar Drive | **Cowork** (o Claude Code si la carpeta está en tu compu) | Si la carpeta está en Drive web, Cowork; si la sincronizás en tu compu, Code la ordena en dos tiempos (propuesta y después movimiento) |

## Tus pedidos, reescritos con los 4 elementos

**1 · Mensaje al founder (chat)**
> **Contexto:** soy la asistente de operaciones de una academia de inglés para chicos. El founder me preguntó por qué se atrasó el onboarding de 6 familias esta semana. **Objetivo:** explicarle la causa y qué cambio propongo, sin excusas. **Fuente:** lo que pasó (abajo): el formulario de inscripción no avisó al equipo cuando cambió la plantilla, y las 6 familias quedaron sin mail de bienvenida 3 días. **Formato:** mensaje de WhatsApp de no más de 6 líneas, con la causa, lo que ya hice y una propuesta concreta.

Skill de la biblioteca: ninguna, alcanza con el pedido.

**2 · Calendly → Airtable (Cowork con Chrome)**
> **Contexto:** tenemos Calendly para las llamadas de venta y una base de Airtable "CRM" con la tabla Llamadas. **Objetivo:** que cada llamada agendada se cree sola como registro. **Fuente:** las pestañas abiertas de Zapier y Airtable. **Formato:** guiame paso a paso mirando la pantalla, un paso por vez, y frená cuando tenga que iniciar sesión o elegir permisos: eso lo hago yo.

Skill de la biblioteca: **Diseñador de Automatizaciones** (`disenador-automatizaciones`), si antes querés definir disparador, campos y qué pasa si falla; después el pedido de arriba para hacerlo.

**3 · Resumir 12 llamadas (proyecto)**
> **Contexto:** en el proyecto tenés el guion de venta y la oferta. Son 12 llamadas de septiembre que no cerraron. **Objetivo:** encontrar en qué etapa se caen y por qué. **Fuente:** las 12 transcripciones que pego abajo (solo el texto, sin nombres). **Formato:** tabla llamada · etapa donde se cayó · objeción textual, y al final las 3 causas que más se repiten.

Skill de la biblioteca: **Analista de Calls de Venta** (`analista-calls-venta`). Conviene usarla en vez de este pedido suelto: ya trae el formato por llamada y el resumen de objeciones. Antes de pegar, sacá nombre, mail y teléfono de cada familia.

**4 · Reporte del lunes (Claude Code)**
> Esto da para agente: creá la carpeta `reporte-lunes` con su `CLAUDE.md` y su `memory.md` (lo hacemos con **Arquitecto de Agentes en Carpeta**). Desde ahí el pedido de cada lunes queda en una línea: "Armá el reporte de esta semana con la exportación que dejé en 02-datos".

Skill de la biblioteca: **Reporte de Ops (semanal y mensual)** (`reporte-semanal-ops`) define el formato del reporte; el agente la usa cada lunes.

**5 · Ordenar Drive (Cowork)**
> **Contexto:** la carpeta compartida "Equipo Fluent Kids" en Drive. **Objetivo:** dejarla con la estructura 00-contexto · 01-procesos · 02-datos · 04-entregables · 99-archivo. **Fuente:** la carpeta abierta en el navegador. **Formato:** primero una tabla archivo actual · carpeta destino · nombre nuevo, **sin mover nada**; después de mi OK, movés. Lo que parezca contraseña o clave, no lo tocás y me lo marcás.

Skill de la biblioteca: **Wiki Operativa y Librería de SOPs** (`wiki-operativa`), si además de ordenar querés que la carpeta de procesos quede como wiki.

## Para no quemar tokens esta semana

1. **Las 12 llamadas: pegá el texto, no subas los PDFs.** Y en tandas de 4, en el mismo proyecto. Son llamadas reales con familias: reemplazá los nombres por "Familia 1, 2…" y borrá mails y teléfonos antes de pegar.
2. **Cerrá el chat de "todo Fluent Kids"** que usás desde agosto: pedile un resumen de 15 líneas, guardalo como contexto del proyecto y seguí en chats nuevos por tema.
3. **En Cowork, una tarea por conversación:** el Zap en una, el Drive en otra.

## Lo que conviene convertir en agente o skill

- **El reporte del lunes** → agente en Claude Code (tarea 4).
- **El análisis de llamadas**, si lo vas a hacer todos los meses → skill (con **De SOP a Skill**), o usá la skill Analista de Calls de Venta de la biblioteca.
