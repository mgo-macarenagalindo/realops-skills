# Métricas de la landing y cómo conectarse a donde está publicada

> Referencia de **Revisor de Landing y Publicación** (RealOps™). Conectores verificados el 12/10/2026: los servidores de HighLevel (`services.leadconnectorhq.com/mcp/`) y de Vercel (`mcp.vercel.com`) responden y piden autorización, y el de Hostinger se instala desde npm (`hostinger-api-mcp`). **No se probaron con una cuenta real**: por eso cada uno tiene su prueba de conexión de 2 minutos. Las plataformas cambian sus integraciones seguido: antes de prometer un conector, fijate que esté en la lista de conectores de Claude o en la documentación de la plataforma.
>
> Los números marcados *(criterio orientativo)* son criterios prácticos, no reglas que salen de las clases.

## Las métricas que se piden

| Métrica | Qué es | Dónde se suele ver |
|---|---|---|
| **Visitas** | Personas (o sesiones) que abrieron la página, en un período | Estadísticas del funnel o del sitio, Google Analytics 4, el panel de la plataforma |
| **Fuente** | De dónde vino cada visita: anuncio, Instagram, mail, orgánico (por UTM o referencia) | Google Analytics 4 (fuente / medio / campaña), el campo UTM del formulario o del CRM |
| **Conversión de la página** | Acciones (envíos o reservas) ÷ visitas | Estadísticas del funnel (opt-in), o se calcula: envíos del CRM ÷ visitas |
| **Clic en el CTA** | Cuántos tocaron el botón (aunque después no completen) | Evento en Google Analytics 4 o Google Tag Manager; mapas de clics de Microsoft Clarity |
| **Scroll** | Hasta dónde baja la gente (25, 50, 75, 90 %) | Microsoft Clarity (gratis, mapa de scroll); GA4 registra solo el 90 % por defecto |
| **Celular vs. compu** | Qué parte del tráfico llega desde el celular y cómo convierte cada uno | GA4 (categoría de dispositivo), Clarity |
| **Velocidad en el celular** | Cuánto tarda en verse | PageSpeed Insights (pagespeed.web.dev), Lighthouse |
| **Lo que pasa después** | Envíos → calificados → agendas → asistencias → ventas, por fuente | El CRM (Airtable, GoHighLevel). Para el costo por venta de cada anuncio, **Rentabilidad por Anuncio** |

**Pedí siempre el período y el mismo período para todo** (por ejemplo, últimos 7 días). Con pocas visitas (menos de 100 por fuente, *criterio orientativo*) lo que ves es una señal, no una conclusión: decilo.

Si no hay ninguna medición, la primera recomendación es instalarla antes de mandar más tráfico: UTMs en cada link (**UTMs de Punta a Punta**), **Microsoft Clarity y GA4** en la página, y el campo de fuente en el CRM.

## Clarity + Google Analytics: las dos, desde el día 1

| | Microsoft Clarity | Google Analytics 4 |
|---|---|---|
| Para qué | **Dónde se va la gente adentro de la página**: mapa de scroll, mapa de clics, grabaciones, "clics de rabia" | **De dónde viene y qué canal convierte**: visitas, fuente / medio / campaña (los UTM), dispositivo, eventos |
| Costo | Gratis | Gratis |
| Cómo se instala | clarity.microsoft.com → nuevo proyecto → copiar el código de seguimiento | analytics.google.com → propiedad → flujo de datos web → copiar la etiqueta (`G-…`) |
| Se cruzan | Clarity tiene integración con GA4: se ven las grabaciones de una fuente o campaña | — |

**Dónde se pega el código:** en GoHighLevel, en el código de seguimiento de la página o del funnel (cabecera); en Kajabi, en el campo de seguimiento o de Google Analytics de la configuración del sitio, si el plan lo permite; en WordPress, con Site Kit (GA4) y el plugin oficial de Clarity; en Netlify, Vercel o Hostinger con hosting, dentro del `index.html`, antes de `</head>`. Si la plataforma no deja pegar código de seguimiento, va dentro del HTML de la landing.

**Privacidad:** las grabaciones de Clarity ocultan por defecto lo que se escribe en los formularios (dejalo así). El aviso de privacidad de la página tiene que mencionar que se usan cookies de medición.

**Revisión a los 7 días (paso fijo):** a los 7 días de publicada, se mira en el mismo período: GA4 (visitas por fuente y dispositivo), Clarity (hasta dónde bajan y dónde tocan) y el CRM (aplicaciones, calificadas, reservas). Con menos de 100 visitas en una fuente *(criterio orientativo)*, esa fuente se lee como señal y se vuelve a mirar 7 días después.

## Cómo leerlas: dónde se cae la gente

| Lo que ves | Lo más probable | Qué revisar primero |
|---|---|---|
| Muchos clics en el anuncio, pocas visitas | La página tarda o hay una redirección | Velocidad en el celular, que el link del anuncio sea el correcto |
| Visitas que no pasan del primer pantallazo | El hero no le habla a quien llega, o el anuncio promete otra cosa | Hero y anuncio = página |
| Bajan hasta el final y no tocan el botón | Falta confianza o la oferta no queda clara | Prueba cerca del CTA, para quién es, FAQ, fotos y videos |
| Tocan el botón y no completan | Formulario largo, roto o que pide demasiado | Probar el formulario en el celular; sacar campos |
| Muchos envíos, pocos calificados | La página o el anuncio atraen a quien no califica | "Para quién no es", preguntas de calificación, el anuncio |
| Agendan y no se presentan | Lo que pasa después del envío | Página de gracias, recordatorios, a quién se asigna |
| El celular convierte mucho menos que la compu | Problema de diseño en el celular | Primer pantallazo, botones, formulario en el celular |
| Una fuente convierte mucho peor que otra | Esa fuente trae otra persona u otra promesa | Anuncio = página para esa fuente |

## Conectarse a donde está la landing

Primero preguntá dónde está publicada. Después, en este orden: **conector o MCP** si existe y la persona lo tiene → **navegador** (Claude en Chrome, para abrir la página publicada) → **capturas y exportes** que pega la persona. **Nunca se piden contraseñas en el chat**: el acceso lo configura la persona en su cuenta, con permisos de lectura cuando se puede.

| Dónde está | Qué conector existe | Qué se puede ver con el conector | Lo que va por captura o exporte |
|---|---|---|---|
| **GoHighLevel** | Servidor MCP oficial de HighLevel (`services.leadconnectorhq.com/mcp/`; se conecta por subcuenta, con un token de integración privada o la autorización que pida, y los permisos que apruebes) | Contactos, oportunidades y calendarios: si el envío de prueba creó el contacto, con qué etiqueta y a quién quedó asignado, y si la reserva entró | Estadísticas del funnel (vistas y opt-in por paso): captura de la pestaña de estadísticas del funnel |
| **Vercel** | Servidor MCP oficial de Vercel (`mcp.vercel.com`, se autoriza con la cuenta de Vercel) | Proyectos, deploys, dominio y si la última versión está publicada | Web Analytics del proyecto: captura del panel (según el plan) |
| **Hostinger** | Servidor MCP de la API de Hostinger (paquete `hostinger-api-mcp`, con un token de la API de Hostinger) | Dominios, DNS, sitios y certificados: si el dominio apunta bien y tiene https | Visitas: captura del panel o de Google Analytics |
| **WordPress** | Depende de la instalación (WordPress.com tiene integraciones para IA; en un WordPress propio, un plugin) | Páginas y su contenido, si está instalado | Visitas: Site Kit / Google Analytics 4, captura |
| **Kajabi · Hotmart** | Sin conector conocido a la fecha | — | Captura del panel de analíticas de la página y exporte de los contactos o ventas |
| **Netlify** | Sin conector conocido a la fecha | — | El link publicado; analíticas del plan, si las tiene, por captura |
| **Google Analytics 4** | Existe un servidor MCP de Google Analytics (se instala en Claude Code) | Visitas, fuentes, dispositivos, eventos | Si no está, exporte del informe o captura |

Si la persona trabaja en el chat de Claude sin conectores: link de la página publicada + capturas de las estadísticas + exporte del CRM. Alcanza para una buena revisión.

## Prueba de conexión de 2 minutos

| Plataforma | Qué pedirle al conector | Conectado si… | Si falla |
|---|---|---|---|
| GoHighLevel | "El último contacto creado en la subcuenta y su etiqueta" | Devuelve un contacto real, con fecha | Revisar que el token o la autorización sean de **esa** subcuenta y tengan permiso de contactos y calendarios |
| Vercel | "El último deploy del proyecto y su dominio" | Devuelve el proyecto y la URL | Volver a autorizar con la cuenta dueña del proyecto (en la del cliente, como colaborador) |
| Hostinger | "Si el dominio tiene el certificado SSL activo" | Devuelve el dominio y el estado del certificado | Revisar el token de la API en el panel de Hostinger |
| Navegador (Claude en Chrome) | Abrir el link publicado y leer el título de la página | Lee el título real | La página no está publicada o pide contraseña: pedir capturas |

Si la prueba falla, seguís con el navegador o con capturas y lo decís en "Cómo la revisé". Nunca supongas lo que el conector habría devuelto.
