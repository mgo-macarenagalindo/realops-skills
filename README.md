# Skills de RealOps™

Las 15 skills de Claude del programa **RealOps™** de Macarena Galindo (MG Operations): diagnóstico, SOPs, CRM, automatizaciones, métricas, propuestas y portafolio, pensadas para operar infonegocios (programas online, membresías, mentorías, high ticket con setters y closers).

Son solo texto: cada skill es una carpeta con un `SKILL.md` (las instrucciones que sigue Claude), `casos-de-uso.md` y `ejemplo-de-output.md` (un resultado completo con datos ficticios). No hay scripts ni programas adentro.

---

## Las 15 skills

| Hito | Skill | Carpeta | Zip para claude.ai |
|---|---|---|---|
| Empezá acá | Copiloto Operativo | [skills/copiloto-operativo](skills/copiloto-operativo) | [zips/copiloto-operativo.zip](zips/copiloto-operativo.zip) |
| Diagnosticá | Auditoría Operativa de Infonegocio | [skills/auditoria-operativa-infonegocio](skills/auditoria-operativa-infonegocio) | [zips/auditoria-operativa-infonegocio.zip](zips/auditoria-operativa-infonegocio.zip) |
| Diagnosticá | Mapa de Fricción Invisible | [skills/mapa-friccion-invisible](skills/mapa-friccion-invisible) | [zips/mapa-friccion-invisible.zip](zips/mapa-friccion-invisible.zip) |
| Centralizá | Constructor de SOP de Infonegocio | [skills/constructor-sop-infonegocio](skills/constructor-sop-infonegocio) | [zips/constructor-sop-infonegocio.zip](zips/constructor-sop-infonegocio.zip) |
| Centralizá | CRM de Cliente para Infonegocios | [skills/crm-cliente-infonegocios](skills/crm-cliente-infonegocios) | [zips/crm-cliente-infonegocios.zip](zips/crm-cliente-infonegocios.zip) |
| Automatizá | Arquitecto de Base en Airtable | [skills/arquitecto-base-airtable](skills/arquitecto-base-airtable) | [zips/arquitecto-base-airtable.zip](zips/arquitecto-base-airtable.zip) |
| Automatizá | Diseñador de Automatizaciones | [skills/disenador-automatizaciones](skills/disenador-automatizaciones) | [zips/disenador-automatizaciones.zip](zips/disenador-automatizaciones.zip) |
| Decidí con datos | Analista de Calls de Venta | [skills/analista-calls-venta](skills/analista-calls-venta) | [zips/analista-calls-venta.zip](zips/analista-calls-venta.zip) |
| Decidí con datos | Analista de KPIs | [skills/analista-kpis](skills/analista-kpis) | [zips/analista-kpis.zip](zips/analista-kpis.zip) |
| Decidí con datos | Reporte Semanal de Ops | [skills/reporte-semanal-ops](skills/reporte-semanal-ops) | [zips/reporte-semanal-ops.zip](zips/reporte-semanal-ops.zip) |
| Escalá sin caos | Mapa de Customer Journey de Infonegocio | [skills/mapa-customer-journey-infonegocio](skills/mapa-customer-journey-infonegocio) | [zips/mapa-customer-journey-infonegocio.zip](zips/mapa-customer-journey-infonegocio.zip) |
| Next Level | Offer Doc con IA | [skills/offer-doc-con-ia](skills/offer-doc-con-ia) | [zips/offer-doc-con-ia.zip](zips/offer-doc-con-ia.zip) |
| Next Level | Escritor de Propuestas de Consultoría | [skills/escritor-propuestas](skills/escritor-propuestas) | [zips/escritor-propuestas.zip](zips/escritor-propuestas.zip) |
| Next Level | Coach de Presentación de Sistemas | [skills/coach-presentacion](skills/coach-presentacion) | [zips/coach-presentacion.zip](zips/coach-presentacion.zip) |
| Next Level | Portafolio: de caso interno a pieza externa | [skills/portafolio-caso-interno-a-externo](skills/portafolio-caso-interno-a-externo) | [zips/portafolio-caso-interno-a-externo.zip](zips/portafolio-caso-interno-a-externo.zip) |

¿No querés instalar nada? En [prompts/](prompts) tenés 5 de estas funciones como un prompt para copiar y pegar en cualquier chat.

---

## Cómo instalar una skill

### Opción A · En Claude (web o app de escritorio), la más simple

1. Entrá al zip de la skill en la tabla de arriba y tocá **Download raw file** (el ícono de descarga, arriba a la derecha). No lo descomprimas.
2. En Claude, andá a **Configuración → Capacidades** y buscá la sección **Skills**. Si te pide activar la ejecución de código, activala.
3. Tocá **Subir skill** y elegí el zip.
4. Activala y probala con un pedido real. Cada carpeta trae en `casos-de-uso.md` ejemplos de pedidos para arrancar.

Si no ves la sección Skills, revisá qué tiene habilitado tu cuenta o consultalo en la comunidad.

### Opción B · En Claude Code (todas de una)

1. Bajá este repo: botón verde **Code → Download ZIP**, o clonalo con GitHub Desktop.
2. Copiá las carpetas de `skills/` que quieras a `~/.claude/skills/` (para usarlas en cualquier proyecto) o a `.claude/skills/` dentro de la carpeta de un proyecto (solo para ese proyecto).
3. Abrí Claude Code de nuevo: las skills se cargan solas.

### Cómo actualizarla

Cuando haya una versión nueva, bajá el zip otra vez y subilo en el mismo lugar (reemplaza a la anterior). En Claude Code, volvé a copiar la carpeta.

---

## Las 4 reglas antes de instalar cualquier skill (esta o de otro lado)

1. **Abrí el `SKILL.md` y leelo.** Si no entendés lo que dice, no la instales.
2. **Fijate si tiene scripts.** Si los tiene, leelos. Las de este repo no tienen.
3. **Mirá si el repo está mantenido.** Uno abandonado hace años es una skill vieja.
4. **Instalá de a una y probala** antes de sumar la siguiente.

---

## Creá tu propia skill

Una skill es una carpeta con un archivo `SKILL.md`. Arriba lleva un encabezado con `name` (el nombre de la carpeta, en minúsculas y con guiones) y `description` (qué hace y cuándo usarla: Claude la lee para decidir cuándo activarla). Abajo van las instrucciones, en lenguaje común. Usá cualquiera de las de este repo como modelo.

---

Material del programa RealOps™ · MG Operations. Para uso de los alumnos del programa.
