# Ejemplo de output · Revisor de Landing y Publicación

> Datos ficticios. Caso práctico: **Programa Libertad Freelance**, página de agenda construida con Constructor de Landing con 21st.dev (camino B) y pegada en un Custom Code de GoHighLevel. Está publicada hace 14 días con pauta en Meta. El negocio es cliente de la persona que revisa.

**Lo que pasó la persona:** el link publicado, el entregable del Arquitecto (oferta, avatar y copy), el texto de los 2 anuncios activos y la captura de las estadísticas del funnel de GoHighLevel. Conectó el MCP de HighLevel a la subcuenta del cliente con permisos de lectura.

---

# Revisión · Página de agenda · Programa Libertad Freelance · 14/10

## Cómo la revisé

- **Link publicado**, abierto en el navegador en 390 px y en 1440 px.
- **MCP de HighLevel** (lectura): contactos, oportunidades y calendario de los últimos 14 días. Prueba de conexión: devolvió el último contacto real de la subcuenta, con su etiqueta.
- **Captura** de las estadísticas del funnel (el conector no trae vistas por página).
- **No pude ver:** scroll ni clics (no hay Clarity ni Google Analytics instalados).

## Veredicto: SALE CON AJUSTES

Funciona de punta a punta y no hay nada inventado. Pero en 14 días convirtió 2,1 % y las métricas muestran dónde se cae: la gente que llega del anuncio de video no pasa del primer pantallazo. Ajustes de abajo antes de subir presupuesto.

## Métricas (30/09 al 13/10)

| | Anuncio A · video "Subí tus precios" | Anuncio B · carrusel "3 errores al cobrar" | Total |
|---|---|---|---|
| Visitas (estadísticas del funnel, por UTM) | 610 | 340 | 950 |
| Reservas (calendario, MCP) | 6 | 14 | 20 |
| Conversión de la página | 1,0 % | 4,1 % | 2,1 % |
| Celular | 91 % | 84 % | 88 % |

**Dónde se cae la gente:** el anuncio A trae casi el doble de visitas y convierte 4 veces menos. Su texto promete "subí tus precios esta semana con un mensaje"; la página habla de un programa de 6 meses. Es el punto 10 (anuncio = página). Sin datos de scroll no puedo confirmar en qué sección se van: instalar Clarity y Google Analytics (punto 22).

## Crítico

| # | Punto | Estado | Qué pasa | Cómo se arregla |
|---|---|---|---|---|
| 1 | Un solo CTA | ✅ | Todo lleva al calendario | — |
| 2 | Primer pantallazo en el celular | ✅ | Título, bajada y botón sin scroll | — |
| 3 | El CTA funciona | ✅ | — | — |
| 4 | Formulario probado | ✅ | Reserva de prueba del 13/10: contacto creado con nombre, mail, teléfono y `utm_content` (MCP) | — |
| 5 | Lo que pasa después (agenda directa) | ✅ | La reserva entró al calendario del closer y salió la confirmación | — |
| 6 | Automatización detrás | ✅ | Workflow de GoHighLevel en la subcuenta del negocio; asigna en rueda a los 2 closers actuales | — |
| 7 | Celular real | ✅ | — | — |
| 8 | Nada inventado | ✅ | Los 4 testimonios tienen permiso registrado | — |
| 9 | Cero `[PENDIENTE]` | ✅ | — | — |

## Mayor

| # | Punto | Estado | Qué pasa | Cómo se arregla |
|---|---|---|---|---|
| 10 | Anuncio = página | ❌ | El anuncio A promete un resultado "esta semana" que el programa no sostiene | Cambiar el anuncio, no la página: que prometa lo mismo que el hero (6 meses, tabla de precios) |
| 11 | Le habla al avatar | ✅ | El problema usa frases de las llamadas; "para quién no es" antes del calendario | — |
| 12 | Estructura que vende | ✅ | Promesa, dolor, mecanismo en 3 pasos, FAQ con objeciones reales | — |
| 13 | Prueba cerca de la decisión | ✅ | — | — |
| 14 | Urgencia real | ✅ | No usa urgencia (no hay fecha de cierre) | — |
| 15 | Marca coherente | ⚠️ | El botón usa el verde de la marca, igual que los títulos: no se distingue | El mostaza `#D9A441` del brief, solo en botones |
| 16 | Diseño con dirección | ✅ | Se reconoce la referencia: fondo crema, serif grande | — |
| 17 | Dinamismo | ⚠️ | La página es quieta de punta a punta | Dos momentos: la línea del mecanismo que se llena al hacer scroll y la luz en las tarjetas del problema (referencias de 21st en el Constructor) |
| 18 | Fotos y videos | ❌ | No hay foto de la founder y el anuncio A es un video de ella: quien llega no la reconoce | Foto real en "Quién te guía" y el mismo video arriba |
| 19 | Velocidad | ⚠️ | PageSpeed en celular: la imagen del hero pesa 2,4 MB | Comprimirla a menos de 300 KB |
| 20 | Videos | ✅ | Link directo de la biblioteca de medios | — |
| 21 | Gracias con un paso | ✅ | Botón de WhatsApp con mensaje precargado | — |
| 22 | UTMs y medición | ❌ | Los UTMs llegan; no hay Clarity ni Google Analytics: no se sabe hasta dónde baja la gente ni qué canal trae las visitas | Instalar las dos (gratis) en el código de seguimiento del funnel: Clarity para scroll, clics y grabaciones; Google Analytics para fuente y dispositivo |
| 23 | Modo oscuro | ✅ | — | — |
| 24 | Datos personales | ✅ | Aviso de privacidad debajo del calendario | — |
| 25 | Dominio y candado | ✅ | `agenda.<dominio-del-cliente>` con https; el dominio está en la cuenta del cliente | — |

## Menor

| # | Punto | Estado | Qué pasa |
|---|---|---|---|
| 26 | Ortografía y tratamiento | ⚠️ | "puedes" en la FAQ 4, en una página con voseo |
| 27 | Pestaña, imagen al compartir, favicon | ❌ | Sin imagen al compartir el link |
| 28 | Contraste y logo | ✅ | — |

## Fotos y videos que faltan

| Qué | Dónde va | Quién lo consigue |
|---|---|---|
| Foto de la founder (real, buena luz) | Quién te guía | La founder |
| El video del anuncio A, en versión de 60 segundos | Hero | Editor |
| Imagen para compartir (1200 × 630) | Configuración de la página | Diseño |

## Pruebas que faltan hacer

Ninguna de funcionamiento. Después de los cambios, repetir la reserva de prueba con UTMs en la página publicada.

## Dónde publicarla

Ya está bien publicada: GoHighLevel del cliente, dominio del cliente.

## Después de publicar

1. Cambios de arriba → reserva de prueba en la página publicada, con datos móviles y un link con UTMs.
2. Clarity y Google Analytics instalados desde hoy.
3. **Revisión fija a los 7 días (21/10)**, comparando la conversión del anuncio A antes y después del cambio. Si alguna fuente no llega a 100 visitas *(criterio orientativo)*, se lee como señal y se vuelve a mirar el 28/10.

## Para confirmar

- [SUPUESTO: el anuncio A se puede cambiar sin pausar la campaña, confirmalo con quien maneja la pauta].

---

¿Te armo el mensaje para la founder con la foto, el video y el cambio del anuncio A?
