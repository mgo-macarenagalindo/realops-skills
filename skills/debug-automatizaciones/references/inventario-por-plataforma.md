# Inventario de automatizaciones · cómo relevar cada plataforma

> Referencia del Detective de Automatizaciones (RealOps™), modo inventario. Sale de auditorías reales de cuentas de Zapier, n8n y Airtable en infonegocios (anonimizadas) y de la ayuda oficial de cada herramienta (revisada en octubre de 2026). Los menús cambian de nombre: si algo no aparece así, buscá la función equivalente.

## Regla de oro: solo lectura

- **No se apaga, prende, edita, duplica, borra, prueba ni reproduce nada.** Ni "Test step", ni "Replay", ni "Run once". Si una pantalla pide confirmar algo, se cancela.
- **No se copian claves, tokens ni direcciones completas de webhook.** Se anota "webhook presente" y, si hace falta distinguirlos, los últimos 4 caracteres.
- Lo que no se puede ver se anota **"sin acceso"** con el motivo (permiso, plan, carpeta de otra persona). Nunca se supone.
- Los datos de clientes que aparezcan en el historial no se copian al informe.

## Qué relevar en cada plataforma

### Zapier
| Dónde | Qué anotar |
|---|---|
| Zaps (todas las carpetas, incluidos apagados y borradores) | Total y cuántos de cada estado. Para cada uno: ID (número de la dirección `/editor/<ID>`), nombre, carpeta, estado, dueño, última edición, **si tiene un borrador sin publicar** |
| Cada Zap abierto | Disparador (app · evento · cuenta · tabla y vista), pasos numerados con filtros, rutas, Formatter, Delay, Code, búsquedas; qué campos lee y escribe |
| Zap history (últimos 30 días) | Corridas exitosas, filtradas, con error, detenidas; último error con el mensaje literal |
| Apps / Connections | Cada conexión: a qué cuenta (mail visible), si está vencida, qué Zaps la usan |
| Plan y consumo | Plan, tareas usadas / incluidas, fecha de renovación, frecuencia de consulta, días de historial, dueño de la cuenta, miembros, 2FA |
| Notificaciones de error | A quién le llegan los mails de error y con qué frecuencia |

**Señales típicas:** Zaps "encendidos" sin corridas en 60 días (zombies) · un Zap que se lleva más del 40 % de las tareas · borradores con cambios que nunca se publicaron · direcciones de webhook escritas a mano en muchos pasos · todo a nombre de una sola persona.

### Make
| Dónde | Qué anotar |
|---|---|
| Scenarios (todas las carpetas) | Nombre, estado, programación (instantáneo o cada X minutos), última ejecución |
| Cada escenario | Módulos en orden, routers con sus filtros, manejadores de error, data stores que usa |
| History | Ejecuciones, errores, advertencias, operaciones o créditos por ejecución |
| Connections, Webhooks, Data stores | A nombre de quién, qué escenarios los usan |
| Organización y plan | Operaciones o créditos usados / incluidos, miembros y roles, equipos |

**Señal típica:** escenarios programados cada pocos minutos que casi nunca encuentran datos: consumen igual.

### n8n
| Dónde | Qué anotar |
|---|---|
| Workflows | Nombre, activo o no, etiquetas, última edición, **si tiene asignado el flujo de errores** (configuración del workflow) |
| Cada workflow | Nodo disparador (webhook, programado, de app), nodos en orden, nodos de código (qué hacen, en una línea), sub-flujos que llama |
| Executions | Corridas por día, errores, duración; si hay ejecuciones "en espera" largas |
| Credentials | Cada credencial: tipo, a nombre de quién, qué flujos la usan |
| Instancia | En la nube o servidor propio; plan y ejecuciones del mes; quién es dueño de la instancia |

**Formas de relevar:** desde la pantalla, o pidiendo a quien administra que exporte los workflows (JSON) y la lista de ejecuciones. Con el JSON se lee todo sin entrar: Claude puede resumir cada flujo. **Ojo:** el JSON exportado puede traer direcciones de webhook; no lo pegues en documentos compartidos.

**Señales típicas:** flujos sin flujo de errores asignado (fallan en silencio) · dos flujos disparando por lo mismo · disparadores programados que podrían ser webhooks · nodos de espera de muchas horas.

### Airtable (automatizaciones nativas)
| Dónde | Qué anotar |
|---|---|
| Pestaña Automatizaciones de cada base | Nombre, encendida o apagada, disparador (tabla, vista, condición, horario, formulario, webhook), acciones en orden, grupos con condición |
| Historial de corridas | Corridas, fallas, último error |
| Descripción | Si dice qué hace y quién la mantiene |
| Campos que disparan | Campos de "última modificación" (¿miran todos los campos o uno?), vistas usadas como disparador (¿alguien puede cambiarles el filtro?) |
| Campos y agentes de IA | Qué generan, si siguen generando (un campo de IA que dejó de generar es una automatización rota) |
| Plan y uso | Corridas usadas del mes en el workspace, tope del plan, cuántas automatizaciones tiene la base (las apagadas cuentan para el tope) |

**Quién puede verlas:** solo alguien con permiso Creator u Owner de la base. Con acceso solo por interfaz no se ven. La API pública de Airtable no siempre las expone: si no hay acceso, deducilas desde los datos (registros que aparecen segundos después de otro, campos que se completan solos) y marcalas "a confirmar con un Creator".

**Señales típicas:** "última modificación" que mira todos los campos (dispara de más) · avisos de falla que le llegan a alguien que ya no está (le llegan a la última persona que la activó) · base en la cuenta personal de alguien.

### GoHighLevel
| Dónde | Qué anotar |
|---|---|
| Automation → Workflows | Nombre, estado (publicado o borrador), disparador, acciones, condiciones (if/else), esperas |
| Calendarios | Recordatorios y confirmaciones propios del calendario, reparto (round robin) |
| Formularios y encuestas | Acciones al enviar |
| Webhooks salientes | A qué dirección mandan (n8n, Zapier) |

**Señal típica:** dos workflows con el mismo disparador que se pisan (GoHighLevel no avisa).

### Webhooks del lado del origen (Stripe, Calendly, Typeform, Meta)
Muchas automatizaciones no se ven desde la herramienta de automatización sino desde la que **manda** el evento. Relevá en cada origen qué está suscripto, a dónde manda y quién lo creó:

| Origen | Dónde se ve | Qué anotar |
|---|---|---|
| **Stripe** | Developers (Workbench) → Webhooks | Cada endpoint: plataforma de destino (Make, Zapier, n8n), eventos que escucha (¿solo cobros exitosos o también rechazados y disputas?), fecha. Los que crea Zapier al conectar la cuenta también aparecen acá |
| **Calendly** | Las suscripciones de webhook **no se ven en pantalla**: se listan por la API (`webhook_subscriptions`), con un token de quien administra la organización. También Integraciones → Workflows para recordatorios | Destino, eventos (`invitee.created`, `invitee.canceled`), alcance (organización o usuario), quién la creó. Si nadie puede listarlas, marcalas "a confirmar" y deducilas: ¿a qué herramienta llega cada agenda además de Airtable? |
| **Typeform / Tally / Google Forms** | Connect → Webhooks e integraciones | A qué apps manda las respuestas y a nombre de qué cuenta está el formulario |
| **Meta (API de Conversiones)** | Administrador de eventos → la fuente de datos → Configuración / integraciones de socios | Qué eventos llegan por servidor (agenda, lead, compra), desde qué herramienta y a nombre de quién está el token |

**Señales típicas:** dos webhooks escuchando el mismo evento para cuentas distintas · un webhook a la cuenta de alguien que se fue o de una agencia que ya no trabaja con el negocio (y que guarda datos de clientes en su Drive) · nadie escucha los pagos rechazados · la medición de los anuncios depende de un escenario de un tercero que se puede apagar cualquier día.

### Automatizaciones escondidas (no están en ninguna herramienta de automatización)
Preguntá por estas, porque nadie las llama "automatización" y se rompen igual:
- **Agenda:** reparto de llamadas (rueda, por disponibilidad), recordatorios y mails de confirmación de Calendly o del calendario del CRM.
- **Formularios:** notificaciones al enviar, lógica de preguntas, integraciones nativas (Typeform → Airtable sin Zapier).
- **Pagos:** reintentos de cobro y mails de pago rechazado de Stripe o de la pasarela (¿a quién le llegan?).
- **Plataforma de cursos y comunidad:** mails de bienvenida, accesos automáticos al comprar.
- **Mensajería:** flujos de ManyChat, respuestas automáticas de WhatsApp Business, bots.
- **Campos de IA** que generan solos.

## Prompt para Cowork (relevamiento de solo lectura)

Pegalo en Cowork con la sesión de la herramienta abierta en el navegador. Cambiá lo que está entre corchetes.

```
Sos un auditor de automatizaciones. Tu trabajo es RELEVAR, NO MODIFICAR. Vas a recorrer la cuenta de [Zapier / Make / n8n / Airtable / GoHighLevel] de [negocio] y dejar un inventario completo.

Reglas duras:
- No apagues, prendas, edites, dupliques, borres ni pruebes nada. No toques "Publish", "Turn on/off", "Test", "Replay" ni "Run". Solo abrir y leer.
- Si una pantalla pide confirmar algo, cancelá.
- No copies claves, tokens ni direcciones completas de webhook: anotá que existen y los últimos 4 caracteres.
- No copies datos de clientes del historial.
- Lo que no puedas ver, anotalo como "sin acceso" con el motivo. No lo supongas.

Qué recorrer:
1. Todas las automatizaciones (todas las carpetas, incluidas apagadas y borradores). Total y cuántas de cada estado.
2. El historial de los últimos 30 días por automatización: corridas, errores, último error con el mensaje literal.
3. Las conexiones o credenciales: a qué cuenta (mail visible), si están vencidas, qué automatizaciones las usan.
4. El plan y el consumo: plan, uso del período, tope, renovación, dueño de la cuenta, miembros. Si es un plan gratis con tope: ¿se llegó al tope algún mes y qué días no corrió nada?
5. Si la herramienta manda eventos a otras (Stripe, Calendly, Typeform, CRM): los webhooks registrados, a qué plataforma mandan (sin la dirección completa), qué eventos escuchan y quién los creó.

Para cada automatización, escribí una ficha con estos títulos literales:
- Qué hace (una frase para alguien que no sabe la herramienta)
- Cuándo se dispara
- Pasos (numerados, con filtros y rutas)
- Datos que lee / Datos que escribe (tabla, vista, campos exactos)
- Eventos y webhooks (qué escucha, a qué plataforma manda)
- Dónde quedan los datos (base, planilla o Drive, a nombre de quién)
- Otras apps y canales
- Cuenta dueña y conexiones
- Estado y uso (corridas en 30 días, errores, consumo)
- De qué depende (nombres de campos, opciones, vistas, preguntas de formulario, canales que no se pueden renombrar)
- Qué puede fallar (🔴 en silencio · 🟡 con aviso)
- Riesgo si se rompe (qué deja de pasar y quién se entera)

Entregá: un archivo con las fichas, una tabla resumen (una fila por automatización) y una lista de hallazgos 🔴 🟡 🟢 con evidencia.
```

## Cómo se arma el informe después del relevamiento

1. **Una tabla resumen** primero (una fila por automatización: plataforma, nombre, qué hace, disparador, estado, corridas en 30 días, consumo, cuenta, riesgo). Es lo que lee el founder.
2. **Las fichas** después. Es lo que lee quien mantiene.
3. **El mapa de cuentas:** el hallazgo más repetido en los negocios del programa es "todo depende de una persona" (conexiones, mails de error y envíos a clientes desde el Gmail de alguien).
4. **Cruce con los datos:** si la ficha dice "asigna en rueda", contá en la base a quién le asignó. Si dice "avisa cada venta", contá ventas contra avisos. En un caso real, un Zap corrió 68 veces y publicó 51 avisos: 17 agendas sin anunciar, y el Zap decía "éxito".
5. **Mapa de eventos:** una tabla por evento de negocio (entra un lead, agenda, pago, venta, acceso) con todo lo que lo escucha. Es el insumo del modo simplificar: ahí se ven los "5 en 1".
6. **Campos con más de una mano:** qué campos escriben dos o más automatizaciones o una automatización y una persona.
7. **Hallazgos con evidencia** y un arreglo propuesto por hallazgo. Si algo está roto, se diagnostica con el árbol (modo 3).
