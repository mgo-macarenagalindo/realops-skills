# Chequeo del plan de Airtable

> Referencia de la skill Arquitecto de Base en Airtable (RealOps™).
>
> **Las cifras de abajo son orientativas.** Se relevaron el **12/10/2026** en la ayuda de Airtable (support.airtable.com, artículos "Airtable plans" y "Getting started with Airtable automations") y en airtable.com/pricing. Los límites cambian: antes de decidir, mirá la página de planes y el uso real en la configuración del espacio de trabajo. Decilo siempre así: "relevado el 12/10/2026, verificá el de hoy".

## La tabla de chequeo (completala en el tiempo 1)

| Qué mirar | Free (12/10/2026) | Team (12/10/2026) | Lo que va a usar esta base | ¿Alcanza? | Si no alcanza y sigue en Free: la alternativa manual |
|---|---|---|---|---|---|
| **Registros por base** | 1.000 | 50.000 | Registros de hoy + los que entran por mes × meses | | Exportar a CSV y sacar de la base lo cerrado (meses viejos de EOD, ventas de checkout, movimientos) después de cerrar el mes; o pasar a otra base lo que **no** necesita vínculos. Medir el setting con números diarios y no con cada lead |
| **Editores** | Hasta 5 (lectura y comentarios, sin límite) | Se paga por editor | Cuántas personas tienen que **editar** | | Quien no necesita ver la base carga por **formulario** (no ocupa lugar de editor); lectura por interface o vista compartida |
| **Corridas de automatización por mes** | 100 (por espacio de trabajo) | 25.000 | Automatizaciones × disparos por mes | | Vista de control ("sin fila de KPI", "cierres sin cuotas creadas") que alguien revisa a una hora fija; pegar la columna de claves en el vínculo una vez por semana; o una herramienta externa (n8n, Zapier, Make), que no gasta corridas pero sí llamadas a la API |
| **Llamadas a la API por mes** | 1.000 (por espacio de trabajo) | 100.000 | Integraciones, n8n, Zapier, Make, Claude conectado | | Leer y escribir por lotes, una vez por día; o exportar a CSV para análisis |
| **Adjuntos por base** | 1 GB | 20 GB | Comprobantes, grabaciones | | Guardar el archivo en Drive y en la base solo el link |
| **Historial de cambios** | 2 semanas | 1 año | ¿Hace falta auditar quién cambió qué hace meses? | | Campo "Última modificación por" + export mensual de las tablas sensibles (pagos, comisiones) |
| **Interfaces** | Disponibles, con funciones limitadas | Más completas | Qué páginas y quién las usa | | Vistas compartidas de solo lectura |
| **Sincronizaciones, extensiones, permisos por campo** | Restringidos | Según el plan | ¿Se sincroniza con otra base? ¿Alguien no debe ver montos? | | Integración externa; interface sin esos campos o base aparte para lo sensible |
| **Precio** | US$0 | US$20 por editor por mes con pago anual · US$24 con pago mensual | Editores reales | | — |

Si se llega al límite de registros o de adjuntos, Airtable no borra nada, pero no deja sumar más hasta subir de plan.

## Cuentas rápidas

- **Registros:** sumá todas las tablas. Ej.: 300 leads + 90 llamadas + 25 ventas + 258 cuotas + 120 alumnos + 3 personas = 796. Si entran ~150 por mes, en uno o dos meses se pasa de 1.000.
- **EOD:** personas × días hábiles. 5 personas × 22 días = 110 registros por mes solo de reportes.
- **Automatizaciones:** una que corre por cada registro nuevo gasta tantas corridas como registros entran.
- **Tiempo manual:** sumá los minutos por semana de cada alternativa manual (con quién la hace).

## Cuándo conviene pagar (criterios orientativos)

No son reglas de Airtable: son **criterios orientativos de RealOps™**. Con que se cumpla uno, llevá la decisión al dueño o líder del área:

1. **Registros:** la proyección pasa el **80 % del límite** en los próximos dos meses.
2. **Corridas:** las automatizaciones que harían falta suman más de las corridas del plan en un mes normal.
3. **Editores:** más personas de las que permite el plan necesitan **editar** (no solo cargar por formulario).
4. **Horas:** las alternativas manuales suman más de **2 horas por semana**. Compará el costo del plan (editores × precio) contra horas por mes × costo de la hora de quien las hace.
5. **Control:** hace falta ver cambios de pagos, comisiones o permisos de más de dos semanas atrás.

Ejemplo de cómo decirlo: "Con 2 editores, el plan cuesta unos US$40 a US$48 por mes. Hoy la carga manual son 3 horas por semana. Si la hora de quien la hace cuesta más de US$4, pagar sale más barato".

## Qué decir siempre

- "Relevado el 12/10/2026: verificá en tu cuenta el límite de hoy".
- Si la base está en la cuenta **personal** de alguien en Free, el primer paso no es técnico: pasarla a un espacio del negocio. Antes de pagar, siempre.
- Subir de plan es una **decisión del negocio** (costo contra horas y riesgo): va a "Decisiones del negocio que la base no resuelve", con la cuenta que la justifica.
