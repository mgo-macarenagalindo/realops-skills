# Chequeo del plan de Airtable

> Referencia de la skill Arquitecto de Base en Airtable (RealOps™).
>
> **Los límites cambian y dependen del plan.** Antes de decidir nada, verificá los números de hoy en la página de precios de Airtable (airtable.com/pricing) y en la configuración del espacio de trabajo. Las cifras de abajo son **orientativas** (las que tenía el plan Free cuando se escribió esta skill) y sirven para saber **qué mirar**, no para afirmar.

## La tabla de chequeo (completala en el tiempo 1)

| Qué mirar | Referencia orientativa en Free | Lo que va a usar esta base | ¿Alcanza? | Si no alcanza |
|---|---|---|---|---|
| **Registros por base** | Del orden de mil | Registros de hoy + los que entran por mes × meses | | Pasar tablas históricas o de alto volumen (EOD, ventas de checkout, movimientos) a otra base; archivar años cerrados en CSV; o subir de plan |
| **Editores / colaboradores** | Pocos (alrededor de cinco) | Cuántas personas tienen que **editar** | | Que cargue por **formulario** quien no necesita ver la base (no ocupa lugar de editor); lectura por interface compartida |
| **Corridas de automatización por mes** | Del orden de cien | Automatizaciones × disparos por mes | | Reemplazar avisos por vistas que alguien revisa; agrupar en una corrida diaria; o mover a n8n |
| **Interfaces** | Disponibles, con funciones limitadas | Qué páginas y quién las usa | | Vistas compartidas de solo lectura |
| **Historial de cambios** | Corto (unas semanas) | ¿Hace falta auditar quién cambió qué hace meses? | | Campo "Última modificación por" + exportes periódicos |
| **Adjuntos por base** | Poco espacio | Comprobantes, grabaciones | | Guardar el archivo en Drive y en la base solo el link |
| **Sincronizaciones y extensiones** | Restringidas | ¿Se sincroniza con otra base o herramienta? | | Integración por n8n o Zapier |
| **Permisos por campo o tabla** | Planes pagos | ¿Alguien no debe ver montos? | | Interface sin esos campos, o base aparte para lo sensible |

## Cuentas rápidas

- **Registros:** sumá todas las tablas. Ej.: 300 leads + 90 llamadas + 25 ventas + 258 cuotas + 120 alumnos + 3 personas = 796. Si entran ~150 por mes, en 1 o 2 meses se pasa del orden de mil.
- **EOD:** personas × días hábiles. 5 personas × 22 días = 110 registros por mes solo de reportes.
- **Automatizaciones:** una que corre por cada registro nuevo gasta tantas corridas como registros entran.

## Qué decir siempre

- "Verificá en tu cuenta el límite de hoy: estas cifras son de referencia."
- Si la base está en la cuenta **personal** de alguien en Free, el primer paso no es técnico: pasarla a un espacio del negocio.
- Subir de plan es una **decisión del negocio** (costo contra horas y riesgo): va a "Decisiones del negocio que la base no resuelve", con el número de registros y corridas que justifica la decisión.
