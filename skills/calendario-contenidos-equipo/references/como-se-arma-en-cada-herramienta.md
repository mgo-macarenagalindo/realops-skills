# Cómo se arma en cada herramienta

> Referencia de **Calendario de Contenidos del Equipo**. El sistema es el mismo en todas: una fila por pieza, estados, Owner que cambia con el estado, calendario, vistas por rol y formulario de métricas. Acá está **cómo** se hace en cada una. Los nombres de menús y lo que incluye cada plan cambian seguido: **antes de prometer una función, verificala en el plan que tiene el negocio.**

## Notion

- **Base:** una base de datos "Calendario de contenidos" con las propiedades de la tabla de campos (Contenido = título, Estado = propiedad *Estado*, Owner = *Persona*, Plataforma = *Selección múltiple*).
- **Plantillas de la base:** una por formato (Reel, Carrusel, Video largo, Clip), con la estructura adentro (HOOK · GUION · CAPTION · TAGS, o el checklist de YouTube). Cada plantilla ya trae Formato y Plataforma cargados.
- **Vistas:** Calendario (por Fecha de publicación) · Tablero (agrupado por Estado) · "Lo mío" (filtro Owner = yo) · "Para aprobar" (Estado = En revisión).
- **Avisos:** al asignar a alguien en la propiedad Owner le llega la notificación; también se puede @mencionar en un comentario.
- **Fecha en que entró a revisión:** con una **automatización de la base** ("cuando Estado cambia a En revisión → poner la fecha de hoy en *Entró a revisión*"), si el plan la incluye. Si no, la completa a mano quien pasa la pieza a revisión (le lleva dos segundos y es parte del criterio de "listo").
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
- **Fecha en que entró a revisión:** dos opciones. (a) Un campo *Última modificación* configurado para mirar **solo el campo Estado** (te da cuándo cambió el estado por última vez; mientras la pieza está en revisión, es la fecha en que entró). (b) Una automatización: "cuando Estado = En revisión → actualizar *Entró a revisión* con la fecha de hoy". Revisá cuántas automatizaciones y registros incluye el plan. Si la base hay que diseñarla desde cero, derivá a **Arquitecto de Base en Airtable**.
- **Formulario de métricas:** formulario de Airtable sobre una tabla "Métricas" vinculada a "Piezas".

## Otras (ClickUp, Trello, Monday)

Misma lógica: una tarjeta o tarea por pieza, una lista o columna por estado, el responsable como Owner, vista calendario, campos personalizados para formato, plataforma, objetivo, pilar y CTA. Si la herramienta no muestra un calendario o una tabla, no sirve para esto.
