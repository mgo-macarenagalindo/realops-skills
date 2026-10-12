# Cómo se arma en cada herramienta

> Referencia de **Calendario de Contenidos del Equipo**. El sistema es el mismo en todas: una fila por pieza, estados, Owner que cambia con el estado, calendario, vistas por rol y formulario de métricas. Acá está **cómo** se hace en cada una. Los nombres de menús y lo que incluye cada plan cambian seguido: **antes de prometer una función, verificala en el plan que tiene el negocio.**

## Notion

- **Base:** una base de datos "Calendario de contenidos" con las propiedades de la tabla de campos (Contenido = título, Estado = propiedad *Estado*, Owner = *Persona*, Plataforma = *Selección múltiple*).
- **Plantillas de la base:** una por formato (Reel, Carrusel, Video largo, Clip), con la estructura adentro (HOOK · GUION · CAPTION · TAGS, o el checklist de YouTube). Cada plantilla ya trae Formato y Plataforma cargados.
- **Vistas:** Calendario (por Fecha de publicación) · Tablero (agrupado por Estado) · "Lo mío" (filtro Owner = yo) · "Para aprobar" (Estado = En revisión).
- **Avisos:** al asignar a alguien en la propiedad Owner le llega la notificación; también se puede @mencionar en un comentario.
- **Fecha en que entró a revisión:** en el plan gratis, con un **botón** "Mandar a revisión" que cambia el Estado y pone la fecha de hoy, o a mano (quien pasa la pieza la completa; le lleva dos segundos y es parte del criterio de "listo"). Con plan Plus o superior, con una **automatización de la base** ("cuando Estado cambia a En revisión → poner la fecha de hoy en *Entró a revisión*"). Ver "Lo que depende del plan".
- **Costo:** se puede compartir una página con alguien sin sumarlo como miembro pago del espacio de trabajo (revisá cómo cobra hoy Notion antes de invitar gente).

## Google Sheets

- **Pestaña "Piezas":** una fila por pieza, una columna por campo. Estado, Formato, Objetivo y Pilar con **lista desplegable** (validación de datos). Fecha con formato de fecha. Owner con un desplegable de nombres.
- **Pestaña "Grilla":** la semana en columnas (lun a dom) y los canales en filas, con fórmulas que traen las piezas de cada día (o se completa a mano en la reunión semanal).
- **Pestaña "Plantillas":** el texto de cada formato para copiar en una celda de texto largo, o un link a un Google Doc por pieza.
- **Vistas por persona:** vistas de filtro guardadas ("Lo mío · editor", "Para aprobar").
- **Avisos:** Sheets no avisa al cambiar una celda. Al pasar la pieza, quien la pasa deja un **comentario con @mención** al nuevo Owner: le llega el mail.
- **Fecha en que entró a revisión:** a mano (quien pasa la pieza escribe la fecha) o con un script que la complete al cambiar el estado; si nadie sabe armar el script, a mano.
- **Freelancers:** una planilla o pestaña de entregas aparte, nunca la planilla madre si tiene datos de leads o alumnos.
- **Formulario de métricas:** Google Forms conectado a una pestaña "Métricas".

## Asana

- **Proyecto "Contenido":** una tarea por pieza. Los estados son **secciones** del tablero (Idea, En redacción, En grabación, En edición, En revisión, Para publicar, Publicado) o un campo personalizado "Estado".
- **Campos personalizados:** Formato, Plataforma, Objetivo, Pilar, CTA, Aprueba, Link publicado, Métrica a 7 días.
- **Owner:** el responsable de la tarea; al reasignar, le llega el aviso.
- **Vistas:** Calendario · Tablero · "Mis tareas" para cada persona.
- **Plantillas de tarea:** una por formato, con el checklist como subtareas.
- **Reglas:** según el plan, "cuando la tarea pasa a la sección En revisión → asignar a quien aprueba". El tiempo que estuvo en revisión se ve en el historial de la tarea; si querés una fecha visible, un campo de fecha que completa quien la mueve.

## Airtable

- **Tabla "Piezas"** con los campos de la tabla (Estado = selección única, Owner y Aprueba = colaborador). Si ya hay una base de ventas, en la misma base, para cruzar el código de anuncio con leads y ventas.
- **Vistas:** Calendario · Kanban por Estado · vistas filtradas por persona · formulario de entrega para freelancers (ven el formulario, no la base).
- **Fecha en que entró a revisión:** dos opciones. (a) Un campo *Última modificación* configurado para mirar **solo el campo Estado** (te da cuándo cambió el estado por última vez; mientras la pieza está en revisión, es la fecha en que entró). (b) Una automatización: "cuando Estado = En revisión → actualizar *Entró a revisión* con la fecha de hoy". La opción (a) no gasta ejecuciones: en el plan gratis, usá esa. Ver "Lo que depende del plan". Si la base hay que diseñarla desde cero, derivá a **Arquitecto de Base en Airtable**.
- **Formulario de métricas:** formulario de Airtable sobre una tabla "Métricas" vinculada a "Piezas".

## Lo que depende del plan (revisar una vez por cohorte)

Las herramientas cambian sus planes seguido. Esta tabla se revisa **al empezar cada cohorte** (última revisión: **12/10/2026**, en las páginas de precios de Notion y Airtable y en fuentes de terceros para los números de Airtable que la página oficial no muestra). Los números son **orientativos**: antes de prometerle algo al negocio, abrí la página de precios y fijate el plan que tiene.

| Función que usa el sistema | En el plan gratis | La alternativa manual (plan gratis) | Cuándo conviene pagar |
|---|---|---|---|
| **Notion · automatización de la base** ("cuando Estado cambia → poner fecha") | No: el plan gratis trae solo automatizaciones con botones. Las de la base son del plan Plus (US$10 por persona por mes) | Un **botón** "Mandar a revisión" que cambia el Estado y pone la fecha, o la fecha a mano al pasar la pieza (es parte del criterio de "listo") | Cuando más de 2 personas mueven piezas y la fecha a mano se olvida más de una vez por semana |
| **Notion · invitados y archivos** | Hasta 10 invitados externos; archivos de hasta 5 MB | Los crudos y editados van al **Drive del negocio** (link en la pieza), nunca adjuntos en Notion | Si el equipo con acceso pasa de 10 personas externas |
| **Airtable · registros** | Orientativo: 1.000 registros por base | Archivar las piezas "Medido" de más de 3 meses en una tabla aparte o exportarlas a CSV y borrarlas | Cuando la base (piezas + leads + ventas) pasa los 800 registros: a ese ritmo se llena en semanas |
| **Airtable · automatizaciones** | Orientativo: 100 ejecuciones por mes | Campo **Última modificación** configurado solo sobre Estado (no usa automatizaciones); avisos con @mención en un comentario de la fila | Cuando necesitan más de 3 automatizaciones que corren todos los días (100 ejecuciones se van en un mes con 4 o 5 piezas por semana y dos automatizaciones por pieza) |
| **Airtable · editores** | Orientativo: hasta 5 editores por espacio de trabajo | Freelancers por **formulario** y **vista compartida de solo lectura** (no cuentan como editores ni se cobran) | Cuando más de 5 personas tienen que editar la base. En los planes pagos se cobra por editor (Team, orientativo US$20 por persona por mes anual); quien solo lee o completa formularios no paga |
| **Asana · reglas** | Según el plan | Reasignar a mano al mover la tarea de sección | Cuando el equipo ya paga Asana por otra cosa: ahí las reglas salen sin costo extra |
| **Google Sheets** | Gratis completo | El aviso siempre va por comentario con @mención | Nunca hace falta pagar para este sistema |

**Regla para el alumno:** el sistema se arma **primero en el plan gratis con la alternativa manual**. Pagar es una decisión del founder con un motivo concreto de la última columna, no un requisito para empezar. *Criterio orientativo de RealOps: los umbrales de "cuándo conviene pagar" no salen de una clase; ajustalos al negocio.*

## Otras (ClickUp, Trello, Monday)

Misma lógica: una tarjeta o tarea por pieza, una lista o columna por estado, el responsable como Owner, vista calendario, campos personalizados para formato, plataforma, objetivo, pilar y CTA. Si la herramienta no muestra un calendario o una tabla, no sirve para esto.
