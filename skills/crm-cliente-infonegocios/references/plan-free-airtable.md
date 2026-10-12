# El CRM en el plan Free de Airtable

> Referencia de la skill CRM de Cliente para Infonegocios (RealOps™). El diseño del CRM **no cambia** por estar en Free: cambia cómo se carga lo que en un plan pago haría una automatización. El chequeo completo de cualquier base está en la skill **Arquitecto de Base en Airtable**.

## 1. Los límites (verificá los de hoy)

Cifras **relevadas el 12/10/2026** en la ayuda de Airtable (support.airtable.com, "Airtable plans" y "Getting started with Airtable automations"). Los límites cambian: antes de decidir, mirá la página de planes y el uso real en la configuración del espacio de trabajo.

| Qué | Free | Team (el primer plan pago) |
|---|---|---|
| Registros por base | 1.000 | 50.000 |
| Editores | Hasta 5 (lectura y comentarios, sin límite) | Se paga por editor |
| Corridas de automatización por mes | 100 (por espacio de trabajo) | 25.000 |
| Adjuntos por base | 1 GB | 20 GB |
| Historial de cambios | 2 semanas | 1 año |
| Llamadas a la API por mes | 1.000 (por espacio de trabajo) | 100.000 |
| Precio | US$0 | US$20 por editor por mes con pago anual, US$24 con pago mensual |

Si se llega al límite de registros o de adjuntos, Airtable no borra nada, pero no deja sumar más hasta subir de plan. Las llamadas a la API importan si conectás n8n, Zapier, Make o Claude a la base: cada lectura o escritura cuenta.

## 2. Qué consume este CRM

Hacé la cuenta con la persona, tabla por tabla:

- **Registros de hoy** (todas las tablas) + **los que entran por mes** × los meses que faltan para revisar.
- El **detalle por lead** es lo que más consume. El **setting diario** consume poco: un setter son unos 22 registros por mes. Por eso, en Free, el mínimo de números por día y por setter suele alcanzar mejor que cargar cada lead.
- **Cuotas programadas:** (cuotas − 1) filas por cada cierre en cuotas.
- **Corridas:** cada automatización corre una vez por cada registro que la dispara.

## 3. La alternativa manual de cada pieza

| Pieza (en plan pago, automática) | En Free, a mano | Quién · cuánto tarda |
|---|---|---|
| Crear las Cuotas programadas al cargar un cierre en cuotas | Vista de control **"Cierres en cuotas sin cuotas programadas"** (Forma de pago = Cuotas y conteo de cuotas programadas menor a Cantidad de cuotas − 1). Se duplica la primera fila y se cambia N° y vencimiento | Quien acredita el pago · 1 minuto por cuota |
| Movimientos de Finanzas por cada cobro | Finanzas se usa **solo para egresos**. Los ingresos se concilian desde vistas de Deals y Cuotas cobradas agrupadas por mes y método (el bloque financiero ya vive ahí). Si se quiere todo en Finanzas: una importación de CSV por mes, en el cierre | Administración · 15 minutos por mes |
| Alta en Clientes al acreditar un cierre | Vista **"Acreditados sin cliente"** | Coordinación · 2 minutos por cliente |
| Vincular cada registro a su fila de KPIs | Vista **"Sin fila de KPI"** y pegar la columna de claves en el vínculo una vez por semana (receta en la skill Tabla de KPIs Globales en Airtable) | Operaciones · 10 minutos por semana |
| Avisos de cuota por vencer o vencida | Vistas "Vencen en 7 días" y "Vencidas" que el responsable de cobro abre todos los días a la misma hora | Responsable de cobro · 10 minutos por día |
| Asignar setter a cada lead | Rueda escrita en el SOP, o la asigna quien carga | Coordinación |
| Muchos editores | Setters y closers cargan **por formulario** (no ocupan lugar de editor); el founder mira por **interface o vista compartida de solo lectura** | — |
| Más de 1.000 registros | Exportar a CSV y sacar de la base lo cerrado (deals terminados de pagar hace más de un año, setting diario de meses viejos) **después** de cerrar el mes. No partir el CRM en dos bases: se rompen los vínculos | Administración · 1 vez por trimestre |

Una automatización de n8n, Zapier o Make no gasta corridas de Airtable, pero sí llamadas a la API (y tiene su propio plan). Para pocos registros por mes puede servir; derivá a **Diseñador de Automatizaciones**.

## 4. Cuándo conviene pagar (criterios orientativos)

Estos umbrales son **criterios orientativos de RealOps™**, no reglas de Airtable. Con que se cumpla uno, llevá la decisión al founder:

1. **Registros:** la proyección pasa el **80 % del límite** en los próximos dos meses.
2. **Corridas:** las automatizaciones que harían falta suman más de las corridas del plan (contá cuotas, cobros y altas de un mes normal).
3. **Editores:** más personas de las que permite el plan necesitan **editar** (no solo cargar por formulario).
4. **Horas:** las alternativas manuales de la tabla de arriba suman más de **2 horas por semana**. Compará: costo del plan (editores × precio) contra horas por mes × costo de la hora de quien las hace.
5. **Control:** hace falta ver quién cambió un pago o una comisión hace más de dos semanas (historial).

Cómo presentarlo: "Con 3 editores, el plan cuesta unos US$60 a US$72 por mes. Hoy la carga manual son 3 horas por semana de coordinación. Si la hora de coordinación cuesta más de US$5 o US$6, pagar sale más barato." Pagar es una **decisión del negocio**: va a "Decisiones del negocio que la base no resuelve".

**Antes de pagar, siempre:** pasar la base a una **cuenta del negocio**. Pagar un plan sobre la cuenta personal de alguien del equipo es pagar por un riesgo.
