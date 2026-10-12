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
| CRM de ventas del programa | Airtable | Agendas, deals y cuotas del programa de formación | USD 45 | Seguir en la planilla | La planilla no cruza con la pasarela y ya hubo dos ventas contadas dos veces |
| Membresía y cobro recurrente | Plataforma actual de membresías | Acceso y cobro mensual | USD 99 | La plataforma nueva que vio el founder | Resuelve lo mismo que la actual; migrar 650 miembros con cobro recurrente es el mayor riesgo del negocio |
| Cobros del programa | Pasarela actual | Cuotas del programa | Comisión por venta | — | Funciona: no se toca |
| Automatización | Zapier | Agenda → Airtable, venta → aviso a Discord | USD 30 | n8n | Son menos de 500 ejecuciones por mes y la asistente ya sabe usarlo; no hay excedentes |
| Reportes | Interface de Airtable | Ventas, cobrado y cuotas del mes | (incluido) | Herramienta de dashboards aparte | Con una sola fuente de datos alcanza para lo que el founder quiere ver |

## Costo mensual total

| | Hoy | Propuesto |
|---|---|---|
| Herramientas | USD 323 | USD 214 |
| Ahorro | — | **USD 109 por mes** |

El ahorro sale de dar de baja dos herramientas que se pagan y no se usan (un gestor de proyectos con 2 tareas en el último mes y un programa de mails que se reemplazó por la plataforma de membresías: USD 154), menos lo que suma Airtable (USD 45). Y no se suma la plataforma nueva.

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

| Función | Herramienta actual | Costo | Quién la usa | Uso real |
|---|---|---|---|---|
| Comunicación | WhatsApp + Discord | USD 0 | Todos | Alto, mezclado |
| Tareas | Gestor de proyectos | USD 54 | Founder | **Nada**: 2 tareas en un mes |
| Documentación | Notion | USD 40 | Asistente | A medias |
| Ventas del programa | Planilla de Google | USD 0 | Closer, setter | Alto, con errores |
| Mails | Programa de mails | USD 100 | Nadie desde marzo | **Nada** |
| Membresía | Plataforma de membresías | USD 99 | Todos | Alto |
| Automatización | Zapier | USD 30 | Asistente | Alto |
| **Total** | | **USD 323** | | |

### Criterios y peso

| Criterio | Peso |
|---|---|
| El equipo lo usa sin capacitación larga | 30 % |
| Se conecta con lo que ya hay | 25 % |
| Costo a 12 meses | 20 % |
| Aguanta si el volumen se duplica | 15 % |
| Qué tan fácil es salir si hay que migrar | 10 % |

### Matriz de la función con problema: registro de ventas del programa

| Opción | Sin capacitación (30 %) | Se conecta (25 %) | Costo (20 %) | Aguanta x2 (15 %) | Fácil salir (10 %) | Total |
|---|---|---|---|---|---|---|
| Seguir en la planilla | 5 | 2 | 5 | 1 | 5 | 3,7 |
| Base en Notion | 4 | 3 | 5 | 3 | 4 | 3,8 |
| Base en Airtable | 3 | 5 | 3 | 5 | 4 | **3,9** |

Gana Airtable por poco. El empate técnico con Notion se desempata por la conexión con la pasarela y el cruce de cuotas, que es justo el problema de hoy.

### Precios a verificar

Todos los montos de este ejemplo son inventados. En un caso real, cada precio se verifica en la página oficial de la herramienta el día que se arma la pieza.

---

¿Querés la versión para presentarle al founder en 5 líneas, o el mensaje para el equipo con lo que cambia? Antes de mostrarlo, verificá en la página oficial los precios marcados como a verificar.
