# Notas por plataforma

> Referencia de la skill **Claude Conectado a tus Datos** (RealOps™). Relevado el **12/10/2026**. Los conectores y servidores MCP cambian rápido: antes de seguir una nota, buscá en la documentación oficial de la herramienta "MCP" o "Claude" y quedate con lo que diga hoy. Si algo de acá no coincide con lo que ves, gana lo que ves (y avisanos en la comunidad).

## Dónde buscar cuando la plataforma no está en esta lista

1. **El directorio de conectores de Claude** (Configuración → Conectores → explorar).
2. **La documentación de la herramienta:** buscá "MCP server", "Claude", "AI integrations". Si tiene servidor oficial, ahí está la dirección y el tipo de login.
3. **El registro oficial de MCP:** registry.modelcontextprotocol.io (lo mantiene el proyecto MCP; está en versión preliminar). Sirve para encontrar servidores; que un servidor esté listado **no** quiere decir que sea seguro.
4. **Listas de GitHub:** `punkpeye/awesome-mcp-servers` (licencia MIT, la más grande) y `modelcontextprotocol/servers` (servidores de referencia y enlaces a servidores oficiales de empresas).
5. **Zapier MCP:** si la herramienta está en Zapier, el conector de Zapier puede hacer de puente. Ojo: lo que Claude puede hacer depende de las acciones que habilites en Zapier, y cada acción consume tareas del plan.

Todo lo que salga de 3, 4 o 5 y no sea de la propia herramienta pasa por la **ficha de seguridad** del SKILL.md.

## Plataformas frecuentes en infonegocios

| Plataforma | Escalón habitual | Qué permiso pedir al empezar | Ojo con |
|---|---|---|---|
| **Airtable** | 1 · conector oficial | Si te pide token: token personal con `data.records:read` y `schema.bases:read`, **solo la base** que vas a usar. Todavía no `data.records:write`; nunca `schema.bases:write` | La API no muestra automatizaciones ni interfaces. Bases en cuentas personales de empleados. Los límites de llamadas dependen del plan |
| **Notion** | 1 · conector oficial (también tiene servidor remoto para Claude Code) | Al autorizar, elegí **solo las páginas o bases** que hacen falta | Páginas "públicas con link" con claves adentro: si las ves, es un hallazgo de seguridad, no un dato para usar |
| **Google Drive, Gmail, Calendar** | 1 · conectores oficiales | Conectá la **cuenta del negocio**, no la personal | El conector ve todo lo que esa cuenta ve. Con Gmail, cuidado con mails de afuera que traen instrucciones escondidas: sin permiso de enviar al principio |
| **Slack** | 1 · conector oficial | Solo los canales que hacen falta, si el conector lo permite | Mensajes privados y canales de RR. HH. |
| **Asana, Miro, Canva, Fathom, Gamma** | 1 · conectores oficiales | Lectura primero | — |
| **Supabase** | 1 · conector oficial (también servidor para Claude Code) | Un solo proyecto y **modo de solo lectura** si el servidor lo ofrece | Con permisos de escritura puede cambiar la estructura de la base: nunca de entrada |
| **Stripe** | 2 · servidor remoto oficial (verificá la dirección en docs.stripe.com) | Login de Stripe, o una **clave restringida** de solo lectura, primero en modo de prueba | Si la cuenta está a nombre personal del founder, el acceso lo da él. Algunos permisos de Stripe agrupan lectura y escritura: leé qué incluye cada uno |
| **Kajabi** | 2 · servidor oficial (Kajabi publica cómo conectarlo con Claude en su centro de ayuda) | Aprobá permiso por permiso y empezá en lectura | El admin de Kajabi suele ser solo el founder: la conexión la hace o la autoriza él |
| **GoHighLevel** | Verificá en su documentación si hay servidor oficial hoy. Hay muchos de la comunidad | Si usás token: "integración privada" con los permisos mínimos y de **una** subcuenta | Los de la comunidad pasan por la ficha. Los flujos de GHL pueden escribir en otras herramientas |
| **Calendly, Typeform, Tally, ManyChat, Hotmart** | Buscá (escalones 1 a 4). Si no hay, puente | Lectura | Muchas veces ya están conectadas a la base por Zapier: preguntarle a la base puede alcanzar |
| **Google Sheets** | 1 · por el conector de Drive (lectura de archivos) | La planilla compartida con la cuenta del negocio | Planillas "cualquiera con el link puede editar": hallazgo de seguridad |
| **Meta (anuncios)** | Buscá conector o servidor oficial. Si no hay, ver `meta-ads-api.md` | Rol de solo lectura ("ver rendimiento") en la cuenta publicitaria | Agencias que se fueron y siguen como admin; la cuenta pagada con la tarjeta personal de alguien |

## Claude Code: comandos que vas a usar

Pedile a Claude que te explique cada uno antes de correrlo.

| Para qué | Comando |
|---|---|
| Agregar un servidor remoto | `claude mcp add --transport http [nombre] [dirección]` |
| Hacer el login (OAuth) | Dentro de Claude Code: `/mcp`, elegís el servidor y seguís el navegador |
| Ver qué servidores hay (incluidos los conectores de tu cuenta de Claude) | `claude mcp list` o `/mcp` |
| Que el servidor quede solo en la carpeta de un agente y se comparta con el equipo | Agregá `--scope project` (queda en `.mcp.json`, **sin tokens escritos**) |
| Sacar un servidor | `claude mcp remove [nombre]` |
| Traer los servidores que ya tenés en la app de escritorio | `claude mcp add-from-claude-desktop` |

Un servidor local se agrega con `claude mcp add [nombre] -- [comando del servidor]` y el token como variable de entorno (`--env NOMBRE=valor`). Si el comando de instalación empieza con `npx -y` o `uvx` de un paquete que no es de la propia herramienta, primero la ficha.
