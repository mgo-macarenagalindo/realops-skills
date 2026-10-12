# Notas por plataforma

> Referencia de la skill **Claude Conectado a tus Datos** (RealOps™). Relevado el **12/10/2026**. Los conectores y servidores MCP cambian rápido: antes de seguir una nota, buscá en la documentación oficial de la herramienta "MCP" o "Claude" y quedate con lo que diga hoy. Si algo de acá no coincide con lo que ves, gana lo que ves (y avisanos en la comunidad).

## Vigencia de esta referencia

- **Cada fila dice cuándo se verificó y contra qué fuente.** Las de documentación pública no se probaron con una cuenta real del negocio: son "documentado", no "probado".
- **Revisión (criterio orientativo):** cada **3 meses** (próxima: **enero de 2027**) la hace quien mantiene la biblioteca de RealOps™ en MG Operations, y también **cada vez que un alumno avisa** en la comunidad que algo cambió. Se revisan primero las filas de cobros y plataformas de cursos (Stripe, Kajabi, Hotmart), que son las que más cambian y las que más riesgo tienen.
- **Si la fila tiene más de 3 meses**, antes de seguirla hacé la verificación de 3 pasos: 1) buscá en la documentación oficial "MCP" o "Claude"; 2) confirmá la dirección del servidor y el tipo de login; 3) probá con una pregunta de solo lectura ("listame mis sitios", "listame los últimos 5 pagos") en un entorno de prueba o una copia.
- **Plan B si no se puede probar:** sin cuenta de prueba (por ejemplo, Kajabi, que no tiene sandbox), se trabaja con un export (CSV) de la misma información hasta que el dueño de la cuenta haga la conexión, y la tabla de verificación se arma contra ese export.

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
| **Airtable** | 1 · conector oficial | Si te pide token: token personal con `data.records:read` y `schema.bases:read`, **solo la base** que vas a usar. Todavía no `data.records:write`; nunca `schema.bases:write` | La API no muestra automatizaciones ni interfaces. Bases en cuentas personales de empleados. **En el plan Free, 1.000 llamadas a la API por mes por espacio de trabajo** (ayuda de Airtable, 12/10/2026; verificá la de hoy): un agente que consulta todos los días o un puente que escribe cada registro se lo come. Preferí pocas preguntas que traigan muchos registros |
| **Notion** | 1 · conector oficial (también tiene servidor remoto para Claude Code) | Al autorizar, elegí **solo las páginas o bases** que hacen falta | Páginas "públicas con link" con claves adentro: si las ves, es un hallazgo de seguridad, no un dato para usar |
| **Google Drive, Gmail, Calendar** | 1 · conectores oficiales | Conectá la **cuenta del negocio**, no la personal | El conector ve todo lo que esa cuenta ve. Con Gmail, cuidado con mails de afuera que traen instrucciones escondidas: sin permiso de enviar al principio |
| **Slack** | 1 · conector oficial | Solo los canales que hacen falta, si el conector lo permite | Mensajes privados y canales de RR. HH. |
| **Asana, Miro, Canva, Fathom, Gamma** | 1 · conectores oficiales | Lectura primero | — |
| **Supabase** | 1 · conector oficial (también servidor para Claude Code) | Un solo proyecto y **modo de solo lectura** si el servidor lo ofrece | Con permisos de escritura puede cambiar la estructura de la base: nunca de entrada |
| **Stripe** · *documentado en docs.stripe.com/mcp el 12/10/2026* | **1 · conector oficial en el directorio de Claude**. En Claude Code: servidor remoto `https://mcp.stripe.com` (`claude mcp add --transport http stripe https://mcp.stripe.com/` y `/mcp` para el login) | **Login (OAuth)**: en la pantalla de permisos elegís la cuenta o el **sandbox** y los permisos de cada uno; empezá por el sandbox. Si no hay OAuth, una **clave de agente** ("agent API key") con solo los permisos que hacen falta, como variable de entorno | **Desde el 31/10/2026 Stripe deja de aceptar claves secretas completas y claves restringidas sin la etiqueta "Agent"**: si alguien conectó con una de esas, hay que reconectar por OAuth o crear una clave de agente. El servidor puede escribir (crear reembolsos, links de pago); Stripe pide confirmación humana para reembolsos y pagos salientes, pero igual: activá la aprobación de herramientas en tu cliente. Si la cuenta está a nombre personal del founder, el acceso lo da él. Las sesiones se revocan en Configuración → usuario → sesiones OAuth |
| **Kajabi** · *documentado en help.kajabi.com el 12/10/2026* | 2 · servidor remoto oficial `https://mcp.kajabi.com/mcp`. En la app: conector personalizado con esa dirección. En Claude Code: `claude mcp add kajabi --transport http https://mcp.kajabi.com/mcp` | Login (OAuth) de Kajabi, aprobando permiso por permiso | Según Kajabi, cubre páginas, mails, ofertas, cursos, contactos, órdenes, etiquetas y segmentos; **no** cubre analíticas, gestión de la comunidad ni procesamiento de pagos (verificalo: puede cambiar). Lo que escribe queda como **borrador** hasta que alguien lo publica desde Kajabi. El admin suele ser solo el founder: la conexión la hace o la autoriza él. Sin sandbox: probá con preguntas de lectura ("listame mis sitios") |
| **GoHighLevel** | Verificá en su documentación si hay servidor oficial hoy. Hay muchos de la comunidad | Si usás token: "integración privada" con los permisos mínimos y de **una** subcuenta | Los de la comunidad pasan por la ficha. Los flujos de GHL pueden escribir en otras herramientas |
| **Calendly, Typeform, Tally, ManyChat, Hotmart** | Buscá (escalones 1 a 4). Si no hay, puente | Lectura | Muchas veces ya están conectadas a la base por Zapier: preguntarle a la base puede alcanzar |
| **Google Sheets** | 1 · por el conector de Drive (lectura de archivos) | La planilla compartida con la cuenta del negocio | Planillas "cualquiera con el link puede editar": hallazgo de seguridad |
| **Meta (anuncios)** | Buscá conector o servidor oficial. Si no hay, ver `meta-ads-api.md` | Rol de solo lectura ("ver rendimiento") en la cuenta publicitaria | Agencias que se fueron y siguen como admin; la cuenta pagada con la tarjeta personal de alguien |

## Si el camino es un puente: cuál elegir (escalón 5)

Cualquier plataforma sirve si está bien justificada. Explicale siempre a la persona **la ventaja de cada opción para su caso**, no solo cuál elegiste. Comparación relevada el 12/10/2026: precios, cantidad de apps y funciones de IA cambian, verificalas en la página de cada una.

| Opción | Ventaja competitiva | Cuándo conviene | Lo que cuesta o complica |
|---|---|---|---|
| **Automatización nativa de la herramienta** (Airtable, GoHighLevel, Kajabi) | No suma otra herramienta ni otra cuenta; el dato no sale de la plataforma | Cuando todo pasa adentro de una sola herramienta | Topes de corridas del plan; no llega a otras apps |
| **Zapier** | La que más apps conecta y la más fácil de armar; tiene conector para Claude, así que también sirve para que Claude haga acciones en apps sin MCP propio | Equipos sin perfil técnico, pocos registros por mes, apps poco comunes | Se paga por tarea: con mucho volumen se encarece. Cada acción habilitada para Claude es un permiso más |
| **Make** | Escenarios visuales con ramas, filtros y bucles; suele salir más barato que Zapier con volumen medio | Flujos con varias condiciones o transformaciones de datos, sin programar | Curva de aprendizaje un poco mayor; se paga por operación |
| **n8n** | Código abierto: se puede alojar en un servidor propio, los datos no pasan por un tercero y el costo no crece por ejecución; trae nodos de IA y de MCP | Mucho volumen, datos sensibles, o un equipo con alguien técnico que lo mantenga | Alojarlo y mantenerlo es trabajo técnico; la versión en la nube se paga por ejecución |
| **Una base puente** (Airtable, Google Sheets, Supabase) | Claude lee una sola base ya conectada en vez de cinco herramientas | Cuando la herramienta no tiene conexión pero ya manda sus datos a una base | Los datos de la base están tan al día como el puente que los carga |

Para elegir con la persona: ¿quién lo va a mantener?, ¿cuántos registros por mes?, ¿qué tan sensibles son los datos?, ¿ya pagan alguna de estas? Si el puente es un flujo nuevo entre herramientas, el diseño completo es de la skill **Diseñador de Automatizaciones**.

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
