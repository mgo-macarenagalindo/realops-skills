# Inventario de automatizaciones, webhooks y conexiones

> Referencia de la skill **Auditor de Base Heredada** (RealOps™). Se usa en el paso 4 del Modo 1. Todo se releva **en modo lectura**: no se apaga, prende, edita, duplica, prueba ni borra nada.

## 1. Planilla de relevamiento (una fila por automatización)

Sirve igual para automatizaciones nativas de Airtable o Notion, Zaps, escenarios de Make, flujos de n8n, workflows de GoHighLevel y scripts.

| Columna | Qué poner |
|---|---|
| ID | Corto y propio: A1, A2… (nativas), Z1… (Zapier), M1… (Make), N1… (n8n), G1… (GoHighLevel), CM1… (carga manual) |
| Nombre | Tal cual figura en la herramienta |
| Herramienta y cuenta dueña | "Zapier · cuenta de [rol]". Si es personal o de alguien que se fue, marcalo |
| Estado | Prendida · apagada · borrador sin publicar · prendida con cambios sin publicar |
| Disparador | Evento + app + **tabla, vista o campo observado** + horario. Ej.: "registro entra en la vista *Vencidas* de Cuotas" |
| Lee | Tablas, vistas, campos y opciones de selección exactas que usa |
| Escribe | Tablas y campos donde **crea** o **actualiza**, y salidas (Discord, mail, Sheets) |
| Conexiones | Con qué cuenta entra a cada app (el mail visible, no la clave) |
| Webhooks | "Webhook a Discord #ventas, termina en …7990". Nunca la URL completa |
| Uso real | Corridas en los últimos 30 días, cuántas con error |
| Último error | Fecha y mensaje literal |
| Qué hace | Una frase de negocio: "cuando alguien aplica en Typeform, crea el lead y le asigna setter" |
| Qué rompe si falla | Qué deja de pasar y **quién se entera** (si nadie se entera, es riesgo alto) |
| Dependencias frágiles | Nombres de campos, vistas, opciones, textos literales de preguntas de formulario, nombres exactos de personas |
| Corridas que escribieron algo | De las corridas "exitosas", cuántas crearon o actualizaron un registro. Si la diferencia es grande, hay una falla silenciosa |
| Evento de origen | El hecho de negocio que la dispara ("entra un pago", "alguien agenda"). Sirve para armar el mapa por evento |
| Datos personales que salen | Si manda nombre, mail o teléfono de leads o alumnos a otra cuenta, a cuál y de quién es |
| Confianza | Visto · visto con el dueño · reconstruido (¿?) · sin acceso |

La **carga manual** también va en la planilla, con "Disparador: cada vez que…", "Quién" y "Minutos por vez". Es parte de cómo se mueve la info y suele ser lo primero que conviene automatizar.

## 2. La cuenta, aparte

Para cada herramienta de automatización (Zapier, Make, n8n, GoHighLevel):

| Dato | Por qué importa |
|---|---|
| Dueña de la cuenta y miembros | Si la dueña se va, se pierde todo. Si hay un solo miembro, nadie más puede arreglar nada |
| Plan y consumo del período | Las tareas u operaciones que se terminan a mitad de mes cortan los flujos o generan cobros extra. **No des cifras de planes de memoria:** que lo mire en la facturación de la cuenta |
| Doble factor de acceso | Sin él, cualquiera con la clave entra a todas las conexiones |
| Conexiones (Apps / Connections) | Qué cuenta está conectada a cada app, si alguna figura vencida y cuáles no usa ningún flujo |
| Zona horaria | Un flujo programado "a las 15" puede estar corriendo a otra hora |
| Retención del historial | Cuántos días de corridas se pueden revisar |

## 3. Señales de automatismos ocultos en la base

Antes de dar por completo el inventario, recorré la base buscando campos y vistas que **existen para alimentar algo**. Para cada señal, preguntá "¿qué automatización de mi inventario la usa?". Si ninguna, va a "Para confirmar".

| Señal | Qué suele indicar |
|---|---|
| Campo de "última modificación" | Disparador de una automatización. Revisá qué campos observa: si observa **todos**, dispara con cualquier edición |
| IDs externos (`Contact ID`, `Opportunity ID`, `Stripe ID`) | Una integración que crea o actualiza desde otra herramienta |
| Campos con "(auto)", "(find record)", "para Zapier" en el nombre o la descripción | Un flujo que los lee o los escribe, a veces uno que ya no existe |
| Vistas con nombre de acción ("Para avisar", "Nuevos", "Asignación") | Disparador "registro entra en la vista". Cambiarle el filtro corta o desborda el flujo |
| Registros que aparecen segundos después de otro (mismo minuto) | Una automatización que crea registros en otra tabla |
| Claves de vinculación (`Clave KPIs`, mes + canal) | Vinculación automática a una tabla de KPIs |
| Campos de "aviso enviado", "último aviso", `Discord User ID` | Un aviso automático, o uno manual que alguien anota |
| Campos con IA | Generación automática que puede quedarse sin créditos o requerir "Generate" a mano |

## 4. Lo que no se puede ver (y cómo se informa)

- La API de Airtable da tablas, campos y registros, pero **no** automatizaciones nativas, interfaces ni filtros de todas las vistas. Para eso hace falta alguien con permiso de creador que abra la pestaña Automations.
- Una base duplicada no siempre trae sus automatizaciones.
- Un conector sin acceso a una base devuelve error de permisos: eso es "sin acceso", no "no hay".
- Una URL de webhook que funciona hoy no dice quién más la tiene.

Todo eso va a la sección "Para confirmar", con quién lo puede revisar.

## 5. Pedido listo para relevar con Claude en el navegador (Cowork)

Pegalo en Cowork con la cuenta de la herramienta abierta en el navegador (con permiso del negocio). Adaptá lo que está entre corchetes.

```
Sos un auditor de automatizaciones. Tu trabajo es relevar, no modificar.
Vas a recorrer la cuenta de [Zapier / Make / n8n / GoHighLevel] de [negocio] y dejar
un inventario completo para que otra persona pueda auditar la base [nombre] sin romper nada.

Reglas duras:
- No apagues, prendas, edites, dupliques, borres, publiques ni pruebes nada. No toques
  "Publish", "Turn on/off", "Test", "Run" ni "Replay". Solo abrir y leer.
- Si una pantalla pide confirmar algo, cancelá.
- No copies claves, tokens, contraseñas ni URLs completas de webhooks: anotá que existen
  y los últimos 4 caracteres.
- Lo que no puedas ver, anotalo como "sin acceso". No lo supongas.

Qué recorrer:
1. Todos los flujos, incluidos apagados y borradores, de todas las carpetas.
2. El historial de los últimos 30 días: corridas exitosas, con error y detenidas por flujo.
3. Las conexiones: a qué cuenta está conectada cada app y si alguna está vencida.
4. El plan, el consumo del período, la dueña de la cuenta y los miembros.

Para cada flujo, completá esta tabla:
ID | Nombre | Estado | Cuenta dueña | Disparador (app, tabla, vista o campo, horario) |
Qué lee | Qué escribe | Conexiones | Webhooks (últimos 4) | Corridas 30 días y errores |
Último error (literal) | Qué hace (frase de negocio) | Qué rompe si falla y quién se entera |
Dependencias frágiles (campos, vistas, opciones, textos de preguntas, nombres exactos)

Al final: lista de flujos que tocan la base [nombre], separados en "escriben" y "leen",
y una lista de lo que no pudiste ver.
```

Para las automatizaciones nativas de Airtable, el mismo pedido sirve abriendo la base → **Automations**: de cada una, nombre, disparador (tabla, vista o campo observado), acciones, estado, dueña y la pestaña **Run history** filtrada por fallas.


## 6. Dónde consolidar: ventajas de cada opción (criterio orientativo)

Cualquier plataforma sirve si está justificada. Esta tabla no es un ranking: es para que el plan diga **por qué esa**. Precios y topes, siempre de la página de facturación del momento, no de memoria.

| Opción | Ventajas competitivas | Cuándo conviene | Cuidado con |
|---|---|---|---|
| **Automatizaciones nativas de Airtable** | No hay otra cuenta ni otra conexión; ven los campos tal cual; las arregla quien maneja la base | Flujos que empiezan y terminan en la base (crear el alumno al entrar una venta, marcar un estado, un aviso simple) | Tope de corridas por plan, que se comparte entre todas las automatizaciones de la base; en el plan gratis se corta a mitad de mes |
| **Zapier** | La más fácil de leer para alguien no técnico; muchísimas integraciones listas; buen historial por corrida | Equipos sin perfil técnico, flujos lineales, apps poco comunes | Se cobra por tarea: cada paso cuenta, y un disparador ancho o un "nuevo o modificado" la consume rápido |
| **Make** | Ramas, filtros y manejo de errores visuales; mejor costo por operación que Zapier en flujos con muchos pasos; webhooks fáciles | Flujos con varias ramas (el "5 en 1" de un pago), quien ya usa Make | Más curva de aprendizaje; un filtro que corta "en verde" no avisa si no se le arma una ruta de error |
| **n8n** | Se puede alojar propio (sin costo por ejecución), código cuando hace falta, flujos largos | Volumen alto, un perfil técnico en el equipo o un proveedor que lo mantenga | Alguien tiene que mantener el servidor y las actualizaciones; si esa persona se va, es el mismo riesgo que una cuenta personal |
| **La integración nativa de la propia herramienta** (Calendly → CRM, Stripe → plataforma de cursos) | Cero mantenimiento; la mantiene el proveedor | Cuando hace exactamente lo que hace falta | Suele no dejar elegir campos ni reglas; mirá qué no hace |

**Reglas para elegir, siempre:**
1. **Una cuenta del negocio**, con dos personas con acceso y doble factor. Nunca la cuenta personal de alguien, aunque siga en el equipo.
2. **Menos plataformas es mejor:** si el negocio ya paga una, consolidá ahí salvo que haya una razón concreta.
3. **Cada flujo con rama de error que avise a una persona** con nombre, no a un mail que nadie abre.
4. **Buscar por ID, no por mail o nombre** (ID de cliente de la plataforma de pago, ID del alumno).
5. Decí en el plan qué ganás y qué perdés con la opción elegida.
