# Ejemplo de output · Stack Elegido y Justificado

> Datos ficticios, **precios incluidos**: son montos inventados para el ejemplo, no precios reales de las herramientas. Membresía de yoga online con 650 miembros a USD 29 por mes más un programa de formación de instructores de USD 1.400 vendido por llamada. Facturación aproximada: USD 24.000 por mes. Equipo de 6: founder, 1 closer, 1 setter, 2 profesoras y 1 asistente. El founder quería "pasar todo a una plataforma nueva".

---

# Stack elegido y justificado · Membresía de yoga online · Octubre

## El stack en una tabla

| Función | Herramienta | Para qué | Costo mensual | Alternativa descartada | Por qué |
|---|---|---|---|---|---|
| Comunicación interna | Discord | Canales por área y reporte de fin de día | USD 0 | Slack | El equipo ya lo usa con la comunidad; Slack sumaba una app más sin ventaja para 6 personas |
| Gestión de tareas | Notion | Tareas del equipo, calendario de contenido | USD 40 | Asana | Notion ya es la wiki y el calendario: tener las tareas ahí evita una herramienta más |
| Wiki y documentación | Notion | SOPs, accesos (nombrados), quién es quién | (incluido) | Google Drive suelto | Drive queda para archivos, no para navegar procesos |
| CRM de ventas del programa | Airtable, en una cuenta del negocio | Agendas, deals y cuotas del programa de formación | USD 45 | Seguir en la planilla; Airtable gratis | La planilla no cruza con la pasarela, ya hubo dos ventas contadas dos veces y vive en el Drive personal de la closer. El plan gratis alcanzaría unos 5 meses archivando a mano los leads cerrados; se paga desde el mes 5, cuando el límite llega en menos de 3 meses (criterio orientativo) |
| Membresía y cobro recurrente | Plataforma actual de membresías | Acceso y cobro mensual | USD 99 | La plataforma nueva que vio el founder | Resuelve lo mismo que la actual; migrar 650 miembros con cobro recurrente es el mayor riesgo del negocio |
| Cobros del programa | Pasarela actual | Cuotas del programa | Comisión por venta | — | Funciona: no se toca |
| Automatización | Zapier | Agenda → Airtable, venta → aviso a Discord | USD 30 | Make y n8n | Zapier: el más fácil y ya lo usa la asistente. Make daría más operaciones por dólar y n8n ejecuciones casi ilimitadas, pero con menos de 500 ejecuciones por mes, sin excedentes y nadie técnico, esa ventaja no se aprovecha |
| Reportes | Interface de Airtable | Ventas, cobrado y cuotas del mes | (incluido) | Herramienta de dashboards aparte | Con una sola fuente de datos alcanza para lo que el founder quiere ver |

## Costo mensual total de herramientas

| | Hoy | Propuesto |
|---|---|---|
| Herramientas | USD 323 | USD 214 |
| Ahorro | — | **USD 109 por mes** |

El ahorro sale de dar de baja dos herramientas que se pagan y no se usan (un gestor de proyectos con 2 tareas en el último mes y un programa de mails que se reemplazó por la plataforma de membresías: USD 154), menos lo que suma Airtable (USD 45). Y no se suma la plataforma nueva.

**No entran en esta cuenta** las comisiones de la pasarela por cada cobro ni el gasto en anuncios: no son herramientas, y mezclarlos esconde lo que de verdad cuesta el stack.

## Lo que no se cambia y por qué

1. **La plataforma de membresías.** Tiene los 650 cobros recurrentes. Cambiarla pone en riesgo la facturación principal para resolver un problema que no existe.
2. **La pasarela de pago.** Funciona y los clientes la conocen.
3. **Zapier.** Con este volumen, migrar a n8n no ahorra lo suficiente para justificar el aprendizaje.

## Cuándo revisar

| Herramienta | Volver a decidir cuando… |
|---|---|
| Zapier | Las ejecuciones superen el plan dos meses seguidos, o haya que mandar reportes largos partidos en varios mensajes |
| Notion para tareas | El equipo pase de 12 personas |
| Airtable | Se sume un segundo programa vendido por llamada (revisar estructura de la base) |
| Discord | Entren proveedores externos que no deberían ver los canales internos |

---

## Anexo · cómo se decidió

### Inventario de hoy

| Función | Herramienta actual | Costo | Cuenta dueña | Quién la usa | Uso real |
|---|---|---|---|---|---|
| Comunicación | WhatsApp + Discord | USD 0 | Discord del negocio | Todos | Alto, mezclado |
| Tareas | Gestor de proyectos | USD 54 | Tarjeta del founder | Founder | **Nada**: 2 tareas en un mes |
| Documentación | Notion | USD 40 | Negocio | Asistente | A medias |
| Ventas del programa | Planilla de Google | USD 0 | **Drive personal de la closer** | Closer, setter | Alto, con errores |
| Mails | Programa de mails | USD 100 | Negocio | Nadie desde marzo | **Nada** |
| Membresía | Plataforma de membresías | USD 99 | Negocio | Todos | Alto |
| Automatización | Zapier | USD 30 | **Mail personal de la asistente** | Asistente | Alto |
| **Total** | | **USD 323** | | | |

Zapier se queda, pero pasa a una cuenta del negocio: si la asistente se va, hoy se lleva las automatizaciones.

### Criterios y peso

| Criterio | Peso |
|---|---|
| Resuelve el dolor del diagnóstico (ventas contadas dos veces, cuotas cruzadas a mano) | 25 % |
| El equipo lo usa sin capacitación larga | 20 % |
| Se conecta con lo que ya hay | 15 % |
| Queda a nombre del negocio y se puede dar de baja a quien se va | 15 % |
| Costo a 12 meses | 15 % |
| Aguanta si el volumen se duplica | 10 % |

### Matriz de la función con problema: registro de ventas del programa

| Opción | Resuelve el dolor (25 %) | Sin capacitación (20 %) | Se conecta (15 %) | A nombre del negocio (15 %) | Costo (15 %) | Aguanta x2 (10 %) | Total |
|---|---|---|---|---|---|---|---|
| Seguir en la planilla | 1 | 5 | 2 | 2 | 5 | 1 | 2,7 |
| Base en Notion | 3 | 4 | 3 | 5 | 5 | 3 | 3,8 |
| Base en Airtable | 5 | 3 | 5 | 5 | 3 | 5 | **4,3** |

Fricción que justifica "resuelve el dolor": en el último mes hubo dos ventas contadas dos veces y la closer cruza cada cuota con la pasarela a mano. La planilla **es** la causa, así que no puede sacar más de 2 en ese criterio aunque sea gratis y conocida. Sin ese criterio, la planilla empataba con las otras dos opciones.

### Precios verificados

Todos los montos de este ejemplo son inventados. En un caso real, la tabla se ve así:

| Herramienta | Plan | Precio | Fuente | Fecha |
|---|---|---|---|---|
| Airtable | Team | USD [x] por editor por mes, pago anual | página oficial de precios | [fecha] |
| Zapier | [plan] | USD [x] por mes | página oficial de precios | [fecha] |
| Programa de mails | — | referencia sin verificar · [mes y año] | confirmar en [link] | — |

El total de arriba es **total estimado** mientras quede una fila sin verificar.

---

¿Querés la versión para presentarle al founder en 5 líneas, o el mensaje para el equipo con lo que cambia? Precios verificados el [fecha]; si lo presentás después de un mes, volvé a mirarlos.
