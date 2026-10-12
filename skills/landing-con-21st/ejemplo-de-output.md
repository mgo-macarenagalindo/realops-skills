# Ejemplo de output · Constructor de Landing con 21st.dev

> Datos ficticios. Caso práctico: **Programa Libertad Freelance** (finanzas y precios para freelancers, vendido por llamada). El copy final y el brief de marca salieron de la skill Arquitecto de Landing de Alto Ticket. El negocio usa GoHighLevel para el calendario y los mails, y quiere pegar la página ahí. La persona tiene VS Code con Claude Code y nunca usó Node.js.

---

# Construcción · Página de agenda · Programa Libertad Freelance · Camino B

## Por qué camino B

La página va **adentro del constructor que ya paga el negocio** (bloque de HTML personalizado), y la persona no maneja un proyecto React. 21st.dev se usa **como inspiración**: mirás dos componentes y Claude escribe versiones propias en HTML y CSS. No se copia código de 21st.

## Qué necesitás instalar

| Qué | ¿Lo tenés? |
|---|---|
| VS Code con la extensión Claude Code | Sí |
| Node.js, cuenta y key de 21st.dev | No hacen falta en este camino |
| El copy final y el brief de marca | Sí |
| Link del calendario de GoHighLevel, número de WhatsApp, URL del logo | Calendario y WhatsApp sí; logo `[PENDIENTE]` |

## El plan

```
libertad-freelance-landing/
├── CLAUDE.md          (reglas del proyecto: un CTA, sin menú, mobile-first, nada inventado)
├── copy.md            (el copy final, pegado tal cual)
├── index.html         (la página de agenda, autocontenida)
├── gracias.html       (la página de gracias, autocontenida)
└── CREDITOS.md        (componentes de 21st que se miraron como inspiración, con su link)
```

Secciones de `index.html`, en orden: hero (video + calendario) · problema · mecanismo · prueba (grilla de 4 videos) · para quién es / no es · FAQ (acordeón) · CTA final (calendario).

Inspiración en 21st.dev (se miran, no se instalan): un hero en dos columnas con video y un acordeón de FAQ simple. En `CREDITOS.md` va el link de cada uno: `[link del componente que elegiste]`.

## El prompt inicial para Claude Code

Activá el modo Plan y pegá:

```
Vamos a construir la landing de agenda del Programa Libertad Freelance.
Leé copy.md (el texto final, no lo cambies) y CLAUDE.md (las reglas).

Camino: HTML autocontenido para pegar en un bloque de HTML personalizado de GoHighLevel.
- Un solo archivo index.html con estilos y script adentro.
- Todos los estilos scopeados bajo la clase .lf para no chocar con el constructor.
- Tipografías: Fraunces (títulos) e Inter (texto) desde Google Fonts.
- Colores: #1F3D2B, #F6F1E7, #141414 y #D9A441 solo en botones.
- Un solo CTA (el calendario). Sin menú, sin footer con redes.
- Mobile-first: probalo pensando en 390 px de ancho.
- Todo lo editable en un objeto CONFIG al final del script, con los campos que te paso.
- Lo que no existe todavía (testimonios, logo) va como [PENDIENTE] visible.
- Hero en dos columnas inspirado en un componente de 21st.dev que te describo; escribí
  tu propia versión, no copies código.

Primero mostrame el plan: secciones, qué va en el CONFIG y cómo se ve en el celular.
No crees archivos hasta mi OK.
```

## El CONFIG

```js
const CONFIG = {
  marca: {
    nombre: "Libertad Freelance",
    colorPrincipal: "#1F3D2B",
    colorAcento: "#D9A441",
    logoUrl: ""                      // [PENDIENTE] URL pública del logo
  },
  ctaTexto: "Agendá tu llamada de diagnóstico",
  calendario: "https://[tu-calendario-de-ghl]",   // el embed del calendario
  webhookUrl: "",                    // no hay formulario propio: el calendario ya registra
  whatsapp: {
    numero: "5490000000000",         // número ficticio
    mensaje: "Hola, agendé la llamada de diagnóstico. Me dedico a ___ y lo que más me preocupa de mis precios es ___."
  },
  videoUrl: "",                      // [PENDIENTE] link directo del video del founder
  testimonios: [                     // [PENDIENTE] 4 videos con permiso
    { videoUrl: "", frase: "", rol: "" }
  ]
};
```

## Rondas de revisión

| Ronda | Qué mirás en la captura | Ejemplo de pedido |
|---|---|---|
| 1 · Celular | ¿En el primer pantallazo se entiende qué es, para quién y qué hacer? | "En el celular el título ocupa 5 líneas: bajalo a 3 con un tamaño menor" |
| 2 · Escritorio | ¿El calendario se ve entero al lado del video? ¿Hay un solo botón? | "El calendario queda cortado: dale más alto a la columna derecha" |
| 3 · Detalle | Pendientes visibles, acordeón del FAQ, botón de WhatsApp en gracias | "El botón de gracias tiene que abrir WhatsApp con el mensaje del CONFIG" |

Después de la tercera ronda, lo que siga va como pedido nuevo o al `CLAUDE.md`.

## Créditos

`CREDITOS.md`: los dos componentes de 21st.dev que se usaron como inspiración, con el link de cada uno y su autor. No se copió código.

## Lo que queda pendiente antes de publicar

- URL pública del logo.
- Video del founder y los 4 testimonios con permiso.
- Probar el embed del calendario con una reserva de prueba.

---

¿La pasamos por **Revisor de Landing y Publicación** antes de pegarla en GoHighLevel?
