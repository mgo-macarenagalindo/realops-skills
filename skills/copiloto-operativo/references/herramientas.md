# Herramientas y plataformas · guía del Copiloto Operativo

> Referencia del Copiloto Operativo de RealOps™. Leela cuando te pregunten por una herramienta, cuál elegir o cuánto cuesta. Los criterios salen de las clases del programa (fecha entre paréntesis).
>
> **Costos: orientativos, en dólares por mes, relevados en octubre de 2026 en fuentes públicas.** Los planes cambian seguido: siempre decí "verificalo en la página oficial antes de decidir". Para Claude, ver `claude-y-agentes.md`.
>
> **Cómo se usan los costos (criterio orientativo):**
> - Dá siempre un **rango** ("unos US$20 a 30"), nunca un precio exacto, y nombrá el plan por su nombre para que la persona lo busque.
> - Decí la fecha del relevamiento: "relevado en octubre de 2026". Si hoy pasaron **más de 3 meses** desde esa fecha, agregá: "puede estar desactualizado; para decidir, mirá la página oficial".
> - Lo que importa para decidir no es el precio de lista sino el **costo con el volumen real del negocio** (tareas, ejecuciones, usuarios). Si la persona tiene ese número, hacé la cuenta con ella.
> - Esta tabla se revisa en **cada relanzamiento del programa** (o cada 3 meses, lo que pase primero). La fecha de arriba dice cuándo fue la última revisión.
>
> **Umbrales y referencias numéricas:** las que llevan fecha entre paréntesis salen de una clase. Las que dicen **(orientativo)** son criterio de esta guía, no de las clases: presentalas así.

## Antes de recomendar cualquier herramienta

1. **¿El problema es de herramienta o de proceso?** Si nadie es dueño de una tarea, cambiar de herramienta no lo arregla (26/03: proceso antes que sistema).
2. **¿Qué ya paga el negocio?** Auditá antes de proponer migrar: optimizar lo que existe da valor rápido y sin fricción (23/07).
3. **¿Qué tan digital es el equipo?** Bicicleta antes que Ferrari (18/06): lo simple que el equipo va a usar le gana a lo potente que nadie abre.
4. **¿A nombre de quién queda?** Toda cuenta va a un mail del negocio, nunca al personal de quien la armó.
5. **Funciones, no competencia.** Las herramientas no compiten si cada una tiene su función (11/05).

---

## Decisiones rápidas

| Pregunta | Respuesta corta |
|---|---|
| ¿Dónde guardo los datos de clientes, ventas y cobros? | Base de datos: **Airtable**. Si el equipo es muy poco digital: **Google Forms + Sheets** (formularios por rol y una pestaña de tablero, 11/05) |
| ¿Dónde vive la wiki, las tareas y el contenido? | **Notion** (el "cerebro de la empresa", 13/04) |
| ¿Notion o Airtable? | Las dos, con funciones distintas. Notion para documentar y organizar; Airtable para analizar ventas y cobros. Como referencia de clase, desde unos US$30.000 por mes de facturación Airtable se vuelve necesaria (13/04 y 15/04) |
| ¿Con qué automatizo? | **Cualquier plataforma sirve si está bien justificada.** Para arrancar, la que el equipo ya conoce (26/03). Lógica simple: una fórmula o la automatización nativa de Airtable antes que una herramienta externa (03/06). Volumen alto o reportes largos: n8n suele convenir (01/09). Siempre mostrá la **ventaja competitiva** de cada opción para *este* negocio (ver "Cómo comparar plataformas de automatización") |
| ¿Zapier, Make o n8n? | Zapier: el más fácil y con más apps, el más caro por volumen. Make: visual y barato, curva media. n8n: el más potente y barato por ejecución, más técnico. Compará por **ejecuciones reales del mes**, no por precio de lista (01/09) |
| ¿Alcanza el plan gratis de Airtable? | Para arrancar, muchas veces sí. Si se queda corto, hay una forma manual de cubrir lo que falta y conviene pagar recién cuando se cumple alguna de las señales de "Plan gratis de Airtable: cuándo alcanza y cuándo pagar" |
| ¿Cómo mido una landing? | **Microsoft Clarity** (mapas de calor y grabaciones de sesiones, gratis) + **Google Analytics** (de dónde llega la gente y cuántos agendan, gratis). Las dos, desde el día uno |
| ¿Slack o Discord? | Discord es gratis y alcanza para equipos chicos (Discord + Notion + Zapier, 19/03). Slack si el negocio ya lo paga o trabaja con clientes que lo usan |
| ¿Asana, Notion o ClickUp para tareas? | Asana o Notion, por lo intuitivos. ClickUp no para equipos que no son expertos (25/03). Si el equipo es grande, tareas en Notion: Airtable cobra por usuario y compartir usuario mata las notificaciones (13/04) |
| ¿Dónde publico una landing o un tablero? | En el constructor que ya paga el negocio (GoHighLevel, WordPress). Si no hay: Netlify o Vercel. El HTML que te da Claude necesita hosting y dominio para existir en internet (06/05) |
| ¿Hace falta GoHighLevel? | Si el negocio paga cinco herramientas sueltas para agenda, formularios, mails, chat y funnels, GHL las junta y muchas veces sale más barato (01/10). Si no vende con funnels, no |

---

## Bases de datos, documentación y tareas

### Airtable
- **Qué es:** una base de datos con cara de planilla. Tablas vinculadas entre sí, vistas, formularios, interfaces por rol, automatizaciones nativas y campos de IA.
- **Para qué en un infonegocio:** el CRM de ventas (leads → llamadas → ventas → cuotas), cobros y cuota vencida, comisiones, alumnos, tablero de KPIs.
- **Cuándo sí:** cuando hay que cruzar datos (¿qué anuncio trajo ventas?, ¿quién debe?), cuando el negocio crece y la planilla ya no da.
- **Cuándo no:** para la wiki o para tareas de un equipo grande (cobra por usuario editor).
- **Costo aproximado:** plan gratis con límites de registros y automatizaciones; Team unos US$20 a 24 por usuario editor; Business unos US$45 a 54 por usuario. Los que solo ven por interfaz o formulario pueden no ocupar asiento: verificalo.
- **Plan gratis: cuándo alcanza y cuándo pagar.** Ver la sección siguiente.
- **Alternativas:** Google Sheets (simple, sin vínculos reales), Notion (bases más livianas), Supabase (base de datos de verdad, para cuando hay una app propia), el CRM de GoHighLevel.
- **Ojo:** la base tiene que estar en un workspace del negocio, no en la cuenta personal de quien la armó.
- **Skills:** Arquitecto de Base en Airtable · CRM de Cliente · Tabla de KPIs Globales · Auditor de Base Heredada.

### Plan gratis de Airtable: cuándo alcanza y cuándo pagar

Muchos alumnos arrancan sin presupuesto. Enseñá primero cómo cubrir a mano lo que el plan gratis no trae, y avisá con claridad cuándo deja de convenir.

| Lo que el plan gratis limita | Alternativa manual (sin pagar) | Señal de que conviene pagar (orientativo) |
|---|---|---|
| Tope de **corridas de automatización** por mes | Una **vista filtrada** ("cuotas que vencen hoy", "leads sin asignar") que alguien revisa a una hora fija, con el paso escrito en el SOP. O la automatización en Zapier, Make o n8n en su plan gratis | Cuando la revisión manual lleva **más de 1 hora por semana** o ya se olvidó una vez algo que costó plata (una cuota sin cobrar, un lead sin contactar) |
| Tope de **registros** por base | Archivar lo cerrado: exportar a CSV las ventas o leads de hace más de 6 a 12 meses y borrarlos de la base (el CSV queda en el Drive del negocio) | Cuando archivar se vuelve tarea de todos los meses o hace falta cruzar datos viejos con nuevos |
| **Historial** de cambios corto | Exportar la base a CSV una vez por semana a una carpeta del negocio (backup manual) | Cuando la base ya es el CRM de ventas y cobros: perder una semana de datos cuesta más que el plan |
| **Usuarios editores** | Que el equipo cargue por **formulario** y mire por **vista compartida o interfaz**; solo editan una o dos personas | Cuando más de dos personas necesitan editar a diario |
| Sin funciones de **interfaces avanzadas o permisos finos** | Formularios por rol + vistas compartidas con solo lectura | Cuando hay que esconder datos sensibles (montos, comisiones) a una parte del equipo |

Cómo decirlo: "Arrancá gratis con [la alternativa]. Cuando pase [la señal], el plan pago se paga solo: te ahorra [X horas] o el riesgo de [error]". Los límites exactos de cada plan cambian: **verificalos en la página oficial de precios de Airtable**.

### Notion
- **Qué es:** el todo en uno para documentar: páginas, bases livianas, tareas, calendario, wiki.
- **Para qué:** wiki operativa, librería de SOPs, gestor de tareas, calendario de contenidos, CRM de servicio chico.
- **Cuándo sí:** el equipo necesita encontrar información y ordenar tareas.
- **Cuándo no:** análisis de ventas con mucha data (se pone lento, 27/05); nunca como lugar para guardar claves.
- **Costo aproximado:** gratis para uso chico; Plus unos US$10 a 12 por miembro; Business unos US$20 a 24 (incluye la IA de Notion). Tip de clase: compartir páginas en vez de invitar al workspace evita pagar por usuario (19/03).
- **Alternativas:** Google Drive + Docs (sin estructura), Coda, Confluence (empresas grandes).
- **Skills:** Wiki Operativa · Calendario de Contenidos · CRM de Cliente (versión Notion).

### Google Sheets y Google Forms
- **Qué es:** planilla y formularios gratuitos de Google.
- **Para qué:** CRM simple para equipos poco digitales, reportes por formulario, tableros con fórmulas.
- **Cuándo sí:** el negocio es chico o el usuario final no es técnico. Al equipo se le enseña a cargar por formulario, nunca a tocar la hoja (11/05).
- **Cuándo no:** cuando hay que vincular ventas con cuotas y llamadas: ahí empieza el caos de copiar y pegar.
- **Costo:** gratis; Google Workspace, unos US$7 a 14 por usuario si quieren mails del negocio.

### Asana · ClickUp · Trello
- **Asana:** gestor de tareas intuitivo, bueno para proyectos con fechas. Gratis para equipos chicos; pagos desde unos US$11 por usuario.
- **ClickUp:** muy completo, interfaz compleja: no lo recomiendes a equipos no expertos (25/03).
- **Trello:** tableros simples tipo tarjetas, gratis para empezar.
- Antes de cualquier gestor: el propósito y los descriptores de cargo, si no se lee como vigilancia (25/03).

---

## Automatización

### Cómo comparar plataformas de automatización

No hay una plataforma correcta: cualquiera sirve si la elección está **bien justificada para este negocio**. Cuando compares, mostrá siempre la ventaja competitiva de cada opción y qué se resigna.

| Plataforma | Ventaja competitiva | Lo que se resigna |
|---|---|---|
| **Automatización nativa** (Airtable, GHL, Notion, Stripe) | No suma herramienta ni costo; todo pasa adentro de donde ya están los datos | Solo sirve para lo que ocurre adentro de esa herramienta; topes del plan |
| **Zapier** | La curva más corta y la mayor cantidad de apps conectadas: lo puede mantener alguien no técnico | El más caro por volumen: cobra **cada paso** como tarea |
| **Make** | Lienzo visual con ramas y filtros a menor costo que Zapier | Curva media; cobra por operación de cada módulo |
| **n8n** | El más potente y barato por ejecución completa; maneja IA, reportes largos y código; se puede instalar en un servidor propio | Más técnico: necesita a alguien que lo mantenga |
| **Workflows de GoHighLevel** | Si el negocio ya vive en GHL, automatiza agenda, mensajes y pipeline sin salir de ahí | Datos encerrados en GHL; el análisis sigue mejor en Airtable |

Para justificar, usá cuatro criterios: **quién la va a mantener**, **volumen real del mes**, **qué ya paga el negocio** y **qué tan crítica es** (si falla, ¿se pierde plata?). La recomendación sale de cruzarlos, no de la marca.

### Zapier
- **Qué es:** conecta apps sin código: "cuando pasa X en una app, hacé Y en otra". Más de 8.000 apps.
- **Para qué:** de Calendly a Airtable, de un formulario al CRM, avisos a Slack o Discord, pasos de IA (AI by Zapier).
- **Cuándo sí:** para arrancar, cuando el equipo ya lo conoce o la automatización es simple y de bajo volumen.
- **Cuándo no:** cuando pagás tareas excedentes todos los meses o los límites de caracteres te obligan a partir un reporte en tres mensajes (01/09).
- **Costo aproximado:** gratis hasta unas 100 tareas por mes; Professional desde unos US$20 (anual) o US$30 (mensual) por 750 tareas, y sube con el volumen. Cuenta **cada paso** como tarea.
- **Orden desde el día uno:** carpetas y nombres numerados (07/05). Y a nombre de una cuenta del negocio.
- **Skills:** Diseñador de Automatizaciones · Detective de Automatizaciones · Prompt de IA para Automatizaciones.

### Make (ex Integromat)
- **Qué es:** como Zapier, pero con un lienzo visual donde ves el flujo con ramas.
- **Cuándo sí:** flujos con varias ramas a menor costo que Zapier, si alguien del equipo se anima a lo visual.
- **Costo aproximado:** gratis con unas 1.000 operaciones por mes; planes pagos desde unos US$9 a 11 por mes. Cuenta operaciones por módulo.
- **Alternativas:** Zapier (más fácil), n8n (más potente).

### n8n
- **Qué es:** automatizaciones con nodos, con mucha lógica, IA y código si hace falta. Se usa en la nube o instalado en un servidor propio.
- **Para qué:** el CRM que se carga solo, reportes largos (los manda como archivo adjunto), agentes de análisis de llamadas.
- **Cuándo sí:** volumen alto, flujos complejos, IA en el medio. Es una opción fuerte, no la única: se elige si queda justificada frente a las otras.
- **Cuándo no:** para arrancar con un equipo que nunca automatizó (26/03).
- **Costo aproximado:** en la nube, desde unos €20 a 24 por mes por unas 2.500 ejecuciones (cuenta **por ejecución completa**, no por paso); instalado en un servidor propio, el software es gratis y pagás el servidor (unos US$5 a 20).
- **Migrar desde Zapier:** Claude Code puede leer tus Zaps y armar la migración (27/05). Migración = proyecto aparte, en semana de poca actividad (01/09).

### Automatizaciones nativas de Airtable
- **Qué es:** automatizaciones dentro de la base: cuando se crea o cambia un registro, mandar un mail, actualizar otro registro, correr un script.
- **Cuándo sí:** todo lo que pasa adentro de la base. Evita sumar herramienta.
- **Límite:** según el plan, un tope de corridas por mes.

---

## Marketing, ventas y comunidad

### GoHighLevel (GHL)
- **Qué es:** plataforma todo en uno de marketing y ventas: CRM de contactos y oportunidades, pipelines, calendarios, formularios, funnels y webs, mails, SMS, WhatsApp, chat de Instagram y Facebook, workflows y chatbots.
- **Para qué:** centralizar el embudo de marketing. Airtable sigue siendo donde se analiza la data (11/05, 12/08).
- **Cuándo sí:** el negocio vive de funnels, agenda y seguimiento por mensajes, y hoy paga varias herramientas sueltas.
- **Cuándo no:** el negocio vende por pocas llamadas referidas y ya tiene lo básico.
- **Costo aproximado:** Starter unos US$97 por mes, Unlimited unos US$297, más consumo de SMS, WhatsApp, llamadas e IA. Muchas agencias lo revenden con **otro nombre y otro precio** (marca blanca): a veces el founder no sabe que su CRM es un GHL (01/10).
- **Ojo:** guarda contacto, cita y oportunidad como datos separados: si una condición necesita el dueño de la oportunidad, sumá el paso Find Opportunity (25/06). No te avisa si una automatización nueva pisa otra: auditá antes de crear.
- **Alternativas:** Kommo, HubSpot, ActiveCampaign + Calendly + constructor de landings.

### ManyChat
- **Qué es:** respuestas automáticas y flujos en Instagram, WhatsApp y Facebook.
- **Para qué:** responder comentarios con un link, precalificar leads, setter con IA (ManyChat + IA para seguimientos repetitivos, 26/03).
- **Costo aproximado:** gratis para empezar; Pro desde unos US$15 por mes, sube con la cantidad de contactos.

### Métricas de una landing: Microsoft Clarity + Google Analytics
- **Microsoft Clarity:** mapas de calor, hasta dónde scrollea la gente y grabaciones de sesiones. Gratis. Responde "¿dónde se traban?".
- **Google Analytics:** de dónde llega la gente (con UTMs), cuántos ven la landing y cuántos agendan. Gratis. Responde "¿qué canal trae agendas?".
- **Se instalan las dos desde el día uno**, antes de mandar tráfico. Se marca como conversión la **agenda** (no solo el formulario), porque después de aplicar el lead agenda directo.
- **Skills:** Revisor de Landing y Publicación · UTMs de Punta a Punta.

### Calendly
- **Qué es:** agenda online con link.
- **Para qué:** llamadas de calificación y de venta, reparto entre closers.
- **Costo aproximado:** gratis con un tipo de evento; Standard unos US$10 a 12; Teams unos US$16 a 20 por usuario.
- **Ojo:** el reparto "según quién tiene lugar" sesga quién recibe qué leads. GHL tiene calendarios propios.
- **En una landing de aplicación:** después de aplicar, el lead **agenda directo** (calendario embebido o redirección al link de agenda), sin esperar a que alguien le escriba.

### Formularios: Typeform · Tally · Google Forms
- **Typeform:** lindo y conversacional, desde unos US$25 a 29 por mes. **Tally:** gratis y muy completo. **Google Forms:** gratis y simple. Para aplicación de leads, cualquiera sirve si guarda las UTMs.

### Cobros: Stripe · Hotmart · Mercado Pago
- **Stripe:** cobros con tarjeta y suscripciones o cuotas; cobra comisión por transacción. Para cobrar desde afuera de EE. UU. suele hacer falta una LLC (12/08). Los avisos de pago rechazado tienen que llegar a un mail del negocio.
- **Hotmart:** plataforma de cursos y cobro, con comisión por venta.
- **Mercado Pago:** cobros locales en Latinoamérica.

### Plataformas de cursos y comunidad: Kajabi · Circle · Skool · Hotmart
- **Kajabi:** curso, comunidad, mails y web en uno; unos US$150 a 200 por mes en planes medios.
- **Circle:** comunidad con cursos, eventos y espacios; desde unos US$90 por mes.
- **Skool:** comunidad y cursos simple, unos US$99 por mes.
- Elegí según dónde está hoy el alumno y cuánto cuesta migrar a todos.

### Comunicación interna: Slack · Discord · Comunidad de WhatsApp
- **Slack:** gratis con historial limitado; Pro unos US$7 a 9 por usuario.
- **Discord:** gratis, canales por área, bots para reportes.
- **Comunidad de WhatsApp:** si el founder no quiere sumar herramientas, canales separados dentro de WhatsApp.
- **Skill:** Centro de Comunicación y Reporte de Fin de Día.

---

## Construir y publicar (vibe coding)

### Vercel
- **Qué es:** donde se publica una web o una app hecha con código (por ejemplo, la que te arma Claude Code), conectada a un repositorio de GitHub.
- **Para qué:** tablero de KPIs propio con contraseña, landings, una app interna (Actividad 29).
- **Costo aproximado:** Hobby gratis (para uso personal y no comercial); Pro unos US$20 por usuario. Para un cliente, el proyecto va en una cuenta que pague el cliente.
- **Alternativas:** Netlify (parecido, plan gratis), Hostinger o WordPress (si el cliente ya los tiene), el constructor de GHL para landings.
- **Skills:** Dashboard con Vibe Coding · Revisor de Landing y Publicación.

### GitHub
- **Qué es:** donde se guarda el código y sus versiones. Repositorios privados gratis.
- **Para qué:** guardar el tablero o la landing; compartir skills por zip o repo.

### Supabase
- **Qué es:** una base de datos de verdad (Postgres) con login de usuarios, para apps propias.
- **Cuándo sí:** cuando se construye una app interna con usuarios y permisos, y Airtable ya queda chica o cara.
- **Costo aproximado:** gratis para empezar; Pro unos US$25 por mes.

### Lovable · Bolt · v0
- Constructores de apps con IA desde el navegador. Sirven para prototipos rápidos; para algo que tiene que durar, Claude Code + GitHub + Vercel da más control. Unos US$20 a 25 por mes.

---

## Grabar, presentar y diseñar

| Herramienta | Para qué | Costo aproximado |
|---|---|---|
| **Fathom** | Graba y transcribe llamadas de Zoom o Meet; la transcripción va a la skill Analista de Calls | Gratis con grabación ilimitada; planes pagos unos US$15 a 20 |
| **Loom** | Videos cortos de pantalla para explicar un proceso o un entregable | Gratis con límites; Business unos US$15 |
| **Canva** | Piezas gráficas, portadas, carruseles | Gratis; Pro unos US$13 a 15 |
| **Gamma** | Presentaciones y documentos con IA en minutos | Gratis con créditos; planes pagos unos US$8 a 20 |
| **Zoom** | Llamadas de venta. Una licencia por closer: si comparten una, chocan | Pro unos US$15 por licencia |

---

## Otras IA (además de Claude)

### ChatGPT (OpenAI)
- Chat general, GPTs personalizados (un asistente con instrucciones y archivos, muy fácil de armar y de compartir: la Actividad T2), generación de imágenes.
- Plus unos US$20 por mes; planes de equipo unos US$25 a 30 por usuario.

### Microsoft Copilot
- **Qué es:** la IA de Microsoft. Dos cosas distintas con el mismo nombre: el **Copilot gratuito** (chat, como ChatGPT) y **Microsoft 365 Copilot**, que trabaja adentro de Word, Excel, PowerPoint, Outlook y Teams con los archivos de la empresa.
- **Cuándo sí:** el negocio vive en Microsoft 365 (Outlook, Teams, Excel) y quiere IA adentro de esos archivos.
- **Cuándo no:** la mayoría de los infonegocios vive en Google y herramientas no-code: ahí Copilot suma poco.
- **Costo aproximado:** Microsoft 365 Copilot para empresas, unos US$30 por usuario por mes, encima de la licencia de Microsoft 365. Verificalo: Microsoft cambia sus planes seguido.
- **No confundir con GitHub Copilot**, que es para programar.

### Gemini (Google)
- La IA de Google, integrada a Gmail, Docs, Sheets y Drive. Conviene si el negocio vive en Google Workspace. Planes personales unos US$20; en Workspace, según el plan.

### Cómo elegir entre IAs
No hay una sola correcta. Claude es fuerte para redactar, analizar documentos largos, construir con Claude Code y trabajar con skills y conectores; ChatGPT para GPTs fáciles de compartir; Gemini y Copilot si el negocio vive en Google o en Microsoft. Lo que importa es el **pedido de 4 elementos** y no pegar datos sensibles en ninguna.

---

## Seguridad de cuentas (aplica a todas)

- Cada herramienta, a nombre de un mail del negocio. Cuando alguien se va: se le quitan los accesos y se transfieren las cuentas que estaban a su nombre (formularios, automatizaciones, bases).
- Claves en un **gestor de contraseñas** (Bitwarden, 1Password), nunca en un grupo de WhatsApp ni en una página pública de Notion.
- Tokens y API keys: uno por proyecto, con el mínimo permiso. Nunca se pegan en un chat.
- Herramientas que se pagan y no se usan: se dan de baja (mirá la tarjeta del negocio).
