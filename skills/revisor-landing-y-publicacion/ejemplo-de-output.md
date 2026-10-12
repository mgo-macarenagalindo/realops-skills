# Ejemplo de output · Revisor de Landing y Publicación

> Datos ficticios. Caso práctico: **Programa Libertad Freelance**, página de agenda construida como HTML autocontenido para pegar en GoHighLevel (camino B de la skill Constructor de Landing). El negocio es cliente de la persona que revisa. La pauta arranca el lunes 19/10.

**Lo que pasó la persona:** el `index.html` y el `gracias.html`, capturas del celular (claro y oscuro), el link del calendario y que las reservas tienen que aparecer en el CRM de GoHighLevel con la fuente del lead.

---

# Revisión · Página de agenda · Programa Libertad Freelance · 14/10

## Veredicto: NO SALE (todavía)

Dos críticos sin resolver. Los dos se arreglan en menos de una hora.

## Crítico

| # | Punto | Estado | Qué pasa | Cómo se arregla |
|---|---|---|---|---|
| 1 | Un solo CTA | ✅ | Todo lleva al calendario. Sin menú | — |
| 2 | Primer pantallazo en el celular | ✅ | Título, subtítulo y botón visibles sin scroll | — |
| 3 | El CTA funciona | ✅ | El botón del hero baja al calendario | — |
| 4 | Formulario probado | — | No aplica: el calendario es el formulario | — |
| 5 | Agenda probada | ❌ no verificado | Nadie hizo una reserva de prueba | Reservar con un mail de prueba, confirmar que entra al calendario y al CRM con la fuente, que sale el mail de confirmación, y cancelar |
| 6 | Celular real | ✅ | Probado en un teléfono: sin scroll horizontal | — |
| 7 | Nada inventado | ❌ | El testimonio 3 tiene una frase pero no hay registro del permiso de esa persona | Conseguir el permiso por escrito o sacar ese testimonio (la grilla queda de 3) |
| 8 | Cero `[PENDIENTE]` | ✅ | — | — |

## Mayor

| # | Punto | Estado | Qué pasa | Cómo se arregla |
|---|---|---|---|---|
| 9 | Prueba cerca de la decisión | ✅ | Testimonios justo antes del segundo calendario | — |
| 10 | Velocidad | ⚠️ | La foto del fondo del hero pesa 3,8 MB | Comprimirla a menos de 300 KB o sacarla |
| 11 | Videos | ❌ | El video del hero abre en otra pestaña | Usar el link directo del archivo desde la biblioteca de medios del constructor |
| 12 | Gracias con un paso | ✅ | Un solo botón de WhatsApp con mensaje precargado | — |
| 13 | UTMs | ❌ no verificado | No se probó si la fuente llega al CRM | Abrir la página con `?utm_source=prueba&utm_medium=test` y reservar: el contacto tiene que quedar con esa fuente |
| 14 | Modo oscuro | ✅ | — | — |
| 15 | Datos personales | ⚠️ | El calendario pide teléfono y mail, pero no hay aviso de privacidad | Agregar debajo del calendario el texto de privacidad que usa el negocio |
| 16 | Dominio y candado | — | Se verifica al publicar | — |

## Menor

| # | Punto | Estado | Qué pasa |
|---|---|---|---|
| 17 | Ortografía y tratamiento | ⚠️ | En el FAQ aparece "puedes" (tuteo) en una página con voseo |
| 18 | Título y imagen al compartir | ❌ | La pestaña dice "Document" y no hay imagen para compartir |
| 19 | Contraste | ✅ | — |
| 20 | Favicon y logo | ⚠️ | Sin favicon |

## Pruebas que faltan hacer

1. Reserva de prueba de punta a punta (punto 5).
2. Link con UTMs + reserva, y ver la fuente en el CRM (punto 13).
3. Después de pegarla en GoHighLevel, repetir las dos pruebas en la página publicada.

## Dónde publicarla

**Recomendado: el constructor del negocio (GoHighLevel), en una página nueva con un bloque de HTML personalizado.**

- Por qué: el calendario, el CRM y los mails ya viven ahí; no se suma hosting ni costo, y queda en la cuenta del cliente.
- Paso a paso:
  1. En el constructor, crear una página nueva en el funnel de agenda, sin cabecera ni menú.
  2. Agregar un bloque de HTML personalizado y pegar `index.html` entero. Repetir con `gracias.html` en la página siguiente del funnel.
  3. En el CONFIG, completar el embed del calendario y verificar el número de WhatsApp.
  4. Conectar el dominio del negocio a esa página (o usar el subdominio que ya usa para funnels).
  5. Publicar y hacer las 3 pruebas de abajo.

No conviene Vercel con el plan gratuito: es para uso personal, no comercial.

## Después de publicar

1. Botón y reserva de prueba **en la página publicada**.
2. Abrirla en el celular con datos móviles (no wifi).
3. Link con UTMs → reserva → la fuente aparece en el CRM.

---

¿Te armo el mensaje para el founder con lo que hay que conseguir antes del lunes (el permiso del testimonio 3 y el texto de privacidad)?
