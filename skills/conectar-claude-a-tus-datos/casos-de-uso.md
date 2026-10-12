# Casos de uso · Claude Conectado a tus Datos

Cuatro situaciones de infonegocio donde dejar de exportar planillas cambia la semana. Negocios y nombres ficticios.

---

## 1. El CRM y los cobros que nadie consulta

**La situación.** En una mentoría de ventas para coaches, el CRM vive en Airtable y los cobros en Stripe. Cada vez que el founder pregunta "¿cuánto cobramos?", alguien exporta dos CSV, los cruza y arma la respuesta. Una hora por semana, y nunca igual.

**Qué le pasás.** Las dos plataformas, dónde trabajás con Claude, las tres preguntas que más te hacen y, si querés, los exports de la última semana.

**Qué te devuelve.** El camino para cada una (conector oficial de Airtable; conector oficial de Stripe con login, probado primero en el sandbox y con permisos de lectura), los campos que no conviene usar para responder, las 10 preguntas con su fuente y filtro, la tabla de verificación con "qué dicen los datos" ya calculado desde tus exports, y las reglas de uso para la wiki.

**Por qué sirve.** Es la actividad 17 del programa, llevada a todas las herramientas donde vive la plata.

---

## 2. "Encontré un MCP en GitHub, ¿lo instalo?"

**La situación.** Una agencia de lanzamientos usa GoHighLevel. Alguien del equipo encontró un servidor MCP en GitHub y quiere instalarlo en Claude Code "para que Claude vea los contactos".

**Qué le pasás.** El link del repositorio y para qué lo querés.

**Qué te devuelve.** Primero, si GoHighLevel tiene hoy conector o servidor oficial. Si no, la ficha de seguridad completa del servidor (quién lo publica, licencia, mantenimiento, qué permisos pide, si tiene modo lectura, por dónde pasan los datos) con semáforo, y la decisión: instalar en una copia de práctica, buscar otro camino (un puente con Zapier o la base que ya recibe los contactos) o no instalar.

**Por qué sirve.** Te deja decir "esto sí" o "esto no" con criterio, en vez de correr un comando que no entendés con los datos de un cliente.

---

## 3. La plataforma de cursos sin conector conocido

**La situación.** Un programa de fitness online quiere saber qué alumnos que pagaron todavía no entraron al curso. El curso está en una plataforma que nadie sabe si se conecta con Claude.

**Qué le pasás.** El nombre de la plataforma y la pregunta.

**Qué te devuelve.** La búsqueda en orden (directorio de Claude, documentación de la plataforma, registro oficial de MCP, listas de GitHub) con lo que encontró; si hay servidor oficial, cómo agregarlo con permisos aprobados uno por uno y solo lectura; si no hay, el puente (que el alta del alumno quede en la base que ya está conectada) y el plan B con un export semanal. Si la plataforma tiene API y nada más, la derivación a construir un servidor propio con la skill mcp-builder, con alguien técnico.

**Por qué sirve.** "No tiene conector" deja de ser un callejón sin salida.

---

## 4. El reporte de pauta de los lunes

**La situación.** Cada lunes alguien entra al administrador de anuncios de Meta, cambia las fechas, exporta y arma un resumen.

**Qué le pasás.** Que es Meta, de quién es la cuenta publicitaria y con qué rol entrás.

**Qué te devuelve.** Si hay conector oficial, la conexión con rol de solo lectura. Si no, el plan B (export semanal + pedido guardado) para usar desde hoy, y el tutorial de la API (`references/meta-ads-api.md`) para hacerlo más adelante con alguien técnico al lado. Es la actividad 24.

**Por qué sirve.** El reporte deja de depender de quién lo arma esa semana, sin meterte en una configuración técnica que no te toca.
