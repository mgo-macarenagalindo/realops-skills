# Métricas de la landing y cómo conectarse a donde está publicada

> Referencia de **Revisor de Landing y Publicación** (RealOps™). Conectores verificados el 12/10/2026: las plataformas cambian sus integraciones seguido, así que antes de prometer un conector, fijate que esté en la lista de conectores de Claude o en la documentación de la plataforma.

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

**Pedí siempre el período y el mismo período para todo** (por ejemplo, últimos 14 días). Con pocas visitas (menos de 100 por fuente, como criterio práctico) lo que ves es una señal, no una conclusión: decilo.

Si no hay ninguna medición, la primera recomendación es instalarla antes de mandar más tráfico: UTMs en cada link (**UTMs de Punta a Punta**), Microsoft Clarity o GA4 en la página, y el campo de fuente en el CRM.

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
| **GoHighLevel** | Servidor MCP oficial de HighLevel (se conecta por subcuenta, con los permisos que apruebes) | Contactos, oportunidades y calendarios: si el envío de prueba creó el contacto, con qué etiqueta y a quién quedó asignado, y si la reserva entró | Estadísticas del funnel (vistas y opt-in por paso): captura de la pestaña de estadísticas del funnel |
| **Vercel** | Servidor MCP oficial de Vercel | Proyectos, deploys, dominio y si la última versión está publicada | Web Analytics del proyecto: captura del panel (según el plan) |
| **Hostinger** | Servidor MCP de la API de Hostinger | Dominios, DNS, sitios y certificados: si el dominio apunta bien y tiene https | Visitas: captura del panel o de Google Analytics |
| **WordPress** | Depende de la instalación (WordPress.com tiene integraciones para IA; en un WordPress propio, un plugin) | Páginas y su contenido, si está instalado | Visitas: Site Kit / Google Analytics 4, captura |
| **Kajabi · Hotmart** | Sin conector conocido a la fecha | — | Captura del panel de analíticas de la página y exporte de los contactos o ventas |
| **Netlify** | Sin conector conocido a la fecha | — | El link publicado; analíticas del plan, si las tiene, por captura |
| **Google Analytics 4** | Existe un servidor MCP de Google Analytics (se instala en Claude Code) | Visitas, fuentes, dispositivos, eventos | Si no está, exporte del informe o captura |

Si la persona trabaja en el chat de Claude sin conectores: link de la página publicada + capturas de las estadísticas + exporte del CRM. Alcanza para una buena revisión.
