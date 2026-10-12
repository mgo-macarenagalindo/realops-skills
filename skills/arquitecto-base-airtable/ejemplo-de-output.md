# Ejemplo de output · Arquitecto de Base en Airtable

> Datos ficticios. **Academia Pulso**: programa de 5 meses para entrenadores personales que quieren vender online. Equipo: founder, 2 setters, 2 closers, 3 coaches, 1 coordinadora. El CRM ya está en Airtable (plan Team, 2.400 registros). Los EOD se mandan por WhatsApp y nadie los junta; los candidatos para nuevos setters llegan por un formulario de Google; los procesos están en documentos sueltos. La coordinadora pide: "una base para el equipo: EOD, KPIs por persona, búsquedas y procesos".

---

## TIEMPO 1 · El mapa

# Base · Equipo Pulso · Academia Pulso · Modo: mejorar (se suma a lo que hay)

### Mapa de tablas y vínculos

```
👨🏻‍💻 Equipo ──< 🌙 EOD Setters (setting diario) ──> 📊 KPIs setters  (persona | mes) <── oportunidades por setter
     │      ──< 🌙 EOD Closers  ──────────────────> 📊 KPIs closers  (persona | mes) <── oportunidades y deals por closer
     │      ──< 🌙 EOD Servicio ──────────────────> 📊 KPIs servicio (persona | mes) <── clientes por coach
     ├──< 👥 Candidatos (búsquedas abiertas)
     └──< ⚙️ Procesos y recursos (dueño de cada proceso)
```

| Tabla | Una fila = |
|---|---|
| Equipo | una persona del equipo (ya existe en el CRM: se reutiliza) |
| EOD Setters / Closers / Servicio | un reporte de una persona en un día |
| KPIs setters / closers / servicio | una persona de ese rol en un mes (una tabla por rol: cada una con un solo vínculo desde su origen; criterio orientativo para que se lea fácil) |
| Candidatos | una persona que se postuló a una búsqueda |
| Procesos y recursos | un proceso documentado (SOP, video, plantilla) |

**Dónde va:** en la **misma base del CRM**, porque los KPIs de cada rol necesitan contar oportunidades y deals de cada closer. Si fuera una base aparte, no se podrían vincular sin sincronización.

### Qué queda, qué cambia, qué se suma

| Hoy | Qué pasa |
|---|---|
| Tabla Equipo del CRM | **Queda** y se le suman: Estado (Activo · Activo sin tomar clientes · Inactivo), Fecha de egreso, Roles como selección múltiple |
| EOD por WhatsApp | **Se reemplaza** por 3 formularios (uno por rol) que crean registros en las tablas de EOD |
| Formulario de Google de candidatos | **Se reemplaza** por un formulario de Airtable (los datos quedan donde se trabajan) |
| Documentos de procesos sueltos | **Quedan** en Drive; en la base, solo el link, el dueño y el estado |

### Chequeo del plan (cifras relevadas en la ayuda de Airtable el 12/10/2026: verificá las de hoy en tu cuenta)

| Qué mirar | Lo que va a usar | ¿Alcanza? |
|---|---|---|
| Registros por base (Team: 50.000 · Free: 1.000) | 2.400 de hoy + EOD (8 personas × 22 días = 176 por mes) + ~30 candidatos por búsqueda | Plan Team: sí, con margen de varios años. **En Free no alcanzaría ni el CRM actual** |
| Editores | Coordinadora y founder | Sí. Setters, closers y coaches cargan por formulario |
| Corridas de automatización (Team: 25.000 por mes · Free: 100) | 176 EOD por mes × 1 automatización (buscar o crear KPI) | Sí en Team |
| Interfaces | 1 (tablero del equipo) | Sí |

### Decisiones del negocio que la base no resuelve

- **¿El EOD es obligatorio todos los días hábiles?** Si sí, se suma una vista "EOD faltantes de ayer". Si no, la tasa de reporte no se mide.
- **¿Quién ve los KPIs de cada persona?** ¿Cada uno ve solo los suyos o todo el equipo ve todo? Cambia la interface y los permisos.
- **¿El "cierre" del EOD del closer cuenta la reserva?** La base puede contar las dos cosas; la definición es del negocio.

### Para confirmar

- [SUPUESTO: los coaches no tienen que cargar un EOD por cada sesión, sino un resumen del día; confirmalo con la coordinadora]
- [SUPUESTO: las búsquedas son de setters y closers; confirmalo con la founder]

¿Va este mapa? Si me das el OK, bajo a campos, vistas, automatizaciones y orden de construcción.

---

## TIEMPO 2 · El detalle (después del OK)

## 1. Campos por tabla

**🌙 EOD Setters (setting diario)**: Clave persona \| mes · Setter (vínculo, "Activos · Setters") · Fecha · **Contactados · Conversaciones · Calificados · Agendados con closer** (obligatorios: es el mínimo estándar para medir el setting aunque no se cargue cada lead) · Seguimientos · Energía · Feedback · Tasa de calificación y de agenda (fórmulas).

**🌙 EOD Closers**

| Campo | Tipo | Configuración / fórmula | Descripción |
|---|---|---|---|
| Clave persona \| mes | Fórmula (primario) | `ARRAYJOIN({Closer}) & " \| " & DATETIME_FORMAT({Fecha}, 'YYYY-MM')` | Vincula con KPIs closers |
| Closer | Vínculo → Equipo | Limitado a la vista "Activos · Closers" | |
| Fecha | Fecha | Por defecto, hoy | |
| Agendadas · Asistidas · No show · Canceladas · Reagendadas · Ofertas · Cierres · Reservas · Seguimientos | Número | Enteros | Lo que el closer declara |
| Energía | Calificación (Rating) 1 a 5 | | |
| Feedback del día | Texto largo | | |
| ¿Actualizaste el CRM? | Casilla | | |
| KPIs closers | Vínculo → KPIs closers | Lo llena la automatización | |

(EOD Servicio, mismo esquema con sus números: sesiones agendadas y asistidas, seguimientos, clientes en riesgo.)

**📊 KPIs closers** (KPIs setters y KPIs servicio siguen el mismo patrón con sus números)

| Campo | Tipo | Configuración |
|---|---|---|
| Clave persona \| mes | Texto (primario) | La escribe la automatización |
| Persona · Mes | Vínculo → Equipo · Texto | |
| Agendadas, asistidas, cierres (declarado) | Rollup | SUM desde EOD Closers |
| Cierres (en el CRM) | Conteo con condición | Deals vinculados al closer con Naturaleza = Nuevo cierre en ese mes |
| Diferencia declarado − CRM | Fórmula | `{Cierres (declarado)} - {Cierres (en el CRM)}` |
| Tasa de asistencia · Cierre sobre asistidas | Fórmula | `IF({Asistidas} > 0, {Cierres (en el CRM)} / {Asistidas}, BLANK())` |
| Días con EOD | Conteo | Registros de EOD vinculados |
| Energía promedio | Rollup | AVERAGE |

**👥 Candidatos**: Nombre · Búsqueda (Setter · Closer) · Video de presentación (URL) · Experiencia · ¿Es o fue cliente? · Estado (Nuevo · Preseleccionado · Entrevista · Prueba · Contratado · Descartado) · Motivo de descarte · Entrevistó (vínculo → Equipo) · Fecha de entrevista.

**⚙️ Procesos y recursos**: Nombre del proceso · Áreas (selección múltiple) · Dueño (vínculo → Equipo) · Documento (URL) · Video (URL) · Estado (Borrador · Vigente · Desactualizado) · Última revisión (fecha) · Días desde la revisión (fórmula).

## 2. Formularios

| Formulario | Crea registro en | Vínculos limitados a |
|---|---|---|
| EOD · Setters / Closers / Servicio | La tabla de EOD de cada rol | Persona: "Activos" del rol |
| Postulación | Candidatos | — (público, sin datos sensibles) |

## 3. Vistas

| Vista | Tabla | Filtro / orden | Para quién |
|---|---|---|---|
| EOD faltantes de ayer | Equipo | Activos sin EOD con fecha de ayer | Coordinadora |
| Declarado vs CRM | KPIs closers | Diferencia ≠ 0, mes actual | Coordinadora |
| Mis KPIs del mes | KPIs de mi rol | Persona = yo | Cada uno (por interface) |
| Candidatos por estado | Candidatos | Agrupado por Estado | Founder, coordinadora |
| Procesos para revisar | Procesos | Vigente y más de 90 días sin revisión (plazo orientativo) | Coordinadora |
| ⚠️ Control · EOD sin persona | EOD (las 3) | Persona vacía | Coordinadora |

## 4. Interface · "Equipo Pulso"

Página 1: tarjetas por persona (cierres, tasa de cierre, energía promedio, días con EOD). Página 2: candidatos en curso. Página 3: procesos vigentes, con link. Acceso: founder y coordinadora, lectura; cada persona ve "Mis KPIs del mes".

## 5. Automatizaciones

| Disparador | Acción | Guarda | Corridas/mes |
|---|---|---|---|
| Se crea un EOD (×3, una por tabla) | Buscar en la tabla de KPIs de ese rol la fila con la clave; si no existe, crearla; vincular | Clave no vacía | ~176 (en Free no entraría: la alternativa es pegar la columna de claves una vez por semana, ~10 min) |
| Candidato pasa a "Contratado" | Crear la persona en Equipo (Activo) y avisar a la coordinadora | Vista "Contratados sin alta" | 1 a 3 |

## 6. Permisos

Founder y coordinadora: creadoras. El resto, sin acceso a la base: formularios para cargar e interface para mirar. El formulario de postulación es público; no pide documentos ni datos sensibles.

## 7. Orden de construcción

- [ ] Duplicar la base del CRM como respaldo.
- [ ] Sumar Estado y Fecha de egreso a Equipo; marcar a quienes ya no están.
- [ ] Crear las 3 tablas de EOD, las 3 de KPIs por rol, Candidatos y Procesos, vacías.
- [ ] Vínculos con Equipo; vistas "Activos" por rol.
- [ ] Campos simples, después fórmulas y rollups (EOD → KPIs de cada rol).
- [ ] Cargar 10 EOD de prueba de 2 personas en 2 meses, uno sin persona.
- [ ] Formularios, con vínculos limitados.
- [ ] Vistas (incluidas las de control) e interface.
- [ ] Automatizaciones; probar con los EOD de prueba.
- [ ] Permisos; entrar con un usuario de cada rol.

## 8. Cómo probarla

- 3 EOD de un closer en el mismo mes → **una** fila en KPIs closers con la suma; un EOD del mes siguiente → **otra** fila.
- Un EOD sin persona → aparece en "⚠️ Control" y no crea fila de KPIs.
- Un closer que declara 3 cierres y tiene 2 en Deals → "Diferencia" = 1 y aparece en "Declarado vs CRM".
- Una persona marcada Inactiva → ya no aparece en el formulario de EOD.

---

¿Arrancamos a construir? Te voy guiando tabla por tabla. Hacelo primero en una copia con datos de prueba.
