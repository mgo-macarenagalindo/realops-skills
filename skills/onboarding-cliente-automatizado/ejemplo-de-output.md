# Ejemplo de output · Onboarding de Cliente Automatizado

> Datos ficticios. Escuela online de oratoria para profesionales con dos programas: **Programa Voz** (3 meses) y **Programa Escenario** (6 meses, incluye sesiones 1 a 1). Se vende por llamada; se puede reservar con una seña y pagar en 1 o 3 cuotas. Unas 25 ventas por mes. CRM en Airtable, comunidad en una plataforma de membresías, equipo en Discord, Zapier ya contratado.

**Cómo es hoy (lo que contó la persona):** el closer avisa por WhatsApp a la coordinadora; ella busca el comprobante, manda el link de la comunidad, agrega a la persona al grupo, le avisa al coach y lo carga en Airtable. Tarda en promedio 2 días. En el último lanzamiento se perdieron 3 altas.

---

# Onboarding automatizado · Escuela de oratoria (caso ficticio)

**En una frase:** Cuando administración confirma que entró el pago de una venta cargada por el closer, el cliente recibe la bienvenida de su programa con todos los accesos y su coach se entera, para que nadie dé altas a mano y nadie entre sin pagar.

**Herramienta:** Zapier (ya contratado) · **Dueño:** Operaciones · **Objetivo:** de pago verificado a primer acceso en menos de 1 hora; de venta a pago verificado en el día hábil.

## Antes de construir

**De quién son las cuentas**

| Cuenta | A nombre de | ¿Del negocio? | Qué hacer |
|---|---|---|---|
| Zapier | operaciones@ (mail del negocio) | Sí | — |
| Pasarela de pago | La founder, con el mail del negocio | Sí | Sumar a administración con permisos de lectura |
| Plataforma de membresías | Cuenta personal de la founder | **No** | **Bloqueante:** pasarla al mail del negocio o, si la plataforma no lo permite, dejar a operaciones como segunda dueña antes de conectar Zapier |
| Airtable | operaciones@ | Sí | — |

**Si el plan alcanza** (límites orientativos, revisados el 12/10/2026; confirmalos en la página de precios de cada herramienta)
- Zapier: 25 ventas × 6 pasos + 25 del flujo de la pasarela ≈ 175 tareas por mes; en un lanzamiento se duplica (≈ 350). **Alcanza** con el tramo más chico de Zapier Professional (750 tareas): queda al 47 % en un lanzamiento. Con el plan Free de Zapier no se puede (solo Zaps de 2 pasos).
- Airtable: cada venta suma 1 venta + 1 alumno + hasta 3 cuotas = 5 registros → unos 125 por mes. **Alcanza**: la base está en Team (50.000 registros por base); en el plan gratis (1.000) se llenaría en unos 6 a 8 meses contando los leads.
- El aviso al equipo va por Discord porque es donde el equipo ya se habla: no se suma ninguna herramienta.

## 0. El proceso de hoy y lo que se automatiza

| Paso de hoy | Quién | ¿Se automatiza? |
|---|---|---|
| El closer avisa la venta por WhatsApp | Closer | **Se reemplaza** por el formulario de venta |
| Buscar el comprobante y confirmar que entró | Coordinación | **No:** lo hace administración en la base (botón de estado) |
| Mandar link de la comunidad | Coordinación | Sí |
| Agregar al grupo y a los eventos | Coordinación | Sí |
| Avisar al coach | Coordinación | Sí |
| Cargar en Airtable | Coordinación | **Se elimina** (el formulario ya carga) |

## 1. Disparador y campos del formulario del closer

Formulario "Registrar venta" de la tabla Ventas. Todos obligatorios salvo los marcados.

| Campo | Tipo | Para qué |
|---|---|---|
| Nombre y apellido | Texto | Mail y ficha |
| Mail (el de acceso a la comunidad) | Mail | Invitación |
| WhatsApp | Teléfono | Contacto del coach |
| Programa | Selección única: `Programa Voz` · `Programa Escenario` | Rama |
| Naturaleza | Selección única: `Reserva` · `Cierre` | Solo Cierre dispara el onboarding |
| Forma de pago | Selección única: `1 pago` · `3 cuotas` | Administración |
| Monto cobrado hoy (USD) | Moneda | Verificación |
| Comprobante | Adjunto (opcional) | Verificación |
| Coach asignado | Vínculo a Coaches (solo Programa Escenario; campo condicional) | Aviso y ficha |
| Objetivo principal del cliente | Texto largo | Llamada de onboarding |

Al enviarse, la venta queda con `Estado de pago` = **A verificar**.

## 2. Verificación de pago

- Administración tiene una vista "Ventas · A verificar". Mira el banco o la pasarela y cambia `Estado de pago` a **Pago verificado** (o **No entró**).
- **Disparador real del Zap:** registro que entra a la vista "Onboarding · Listos" (filtro: Naturaleza = Cierre **y** Estado de pago = Pago verificado **y** Onboarding enviado = vacío).
- Si a las 24 horas una venta sigue "A verificar", aviso a administración en #administración.
- Mientras tanto, el cliente recibe un mail corto: "Estamos confirmando tu pago. Hoy te llega el acceso."
- **Reserva:** recibe solo el mail de reserva confirmada (sección 6). No entra a la comunidad.

## 3. Ramas por programa

| | Programa Voz | Programa Escenario |
|---|---|---|
| Valor exacto de la condición | `Programa Voz` | `Programa Escenario` |
| Mail | Bienvenida Voz | Bienvenida Escenario |
| Comunidad | Espacio "Voz · Cohorte" | Espacios "Voz · Cohorte" + "Escenario · 1 a 1" |
| Calendario | Invitación a la clase grupal de los martes | Clase grupal + link para agendar la primera 1 a 1 |
| Coach | El coach grupal de turno | El coach asignado en el formulario |
| Llamada de onboarding | No (video de bienvenida) | Sí, con el coach, en la primera semana |

## 4. Mail de bienvenida

**Estructura:** saludo con el nombre · video de bienvenida (1 minuto, del founder) · 3 botones de próximos pasos · qué pasa esta semana · a quién escribir si algo no funciona.

**Prompt para generarlo con Claude:**

> Armá un mail de bienvenida en HTML para el Programa Escenario de una escuela de oratoria. Texto final: [pegar]. Estilo: sobrio, fondo claro, un color de acento. Logo: [URL pública del logo]. Tiene que funcionar en celular y en modo oscuro, con ancho máximo de 600 px, tablas para el diseño (no columnas modernas), botones grandes y el nombre del cliente como `{{nombre}}`. Tres botones: "Entrar a la comunidad", "Agendar mi primera sesión 1 a 1", "Ver la clase 1".

**HTML base (para pegar en el paso de mail):**

```html
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f6f6f4;">
  <tr><td align="center">
    <table width="600" cellpadding="24" cellspacing="0" style="background:#ffffff;font-family:Arial,sans-serif;color:#1f1f1f;">
      <tr><td><img src="[URL pública del logo]" alt="Escuela de oratoria" width="140"></td></tr>
      <tr><td>
        <h1 style="font-size:22px;">Hola {{nombre}}, ya estás adentro</h1>
        <p>Este es tu primer paso en el Programa Escenario. Mirá el video y seguí estos tres pasos.</p>
        <p><a href="[link del video]">▶ Ver el video de bienvenida (1 min)</a></p>
        <p><a href="[link comunidad]" style="display:inline-block;padding:14px 22px;background:#2f5d50;color:#ffffff;text-decoration:none;border-radius:6px;">Entrar a la comunidad</a></p>
        <p><a href="[link agenda 1 a 1]" style="display:inline-block;padding:14px 22px;background:#2f5d50;color:#ffffff;text-decoration:none;border-radius:6px;">Agendar mi primera sesión 1 a 1</a></p>
        <p><a href="[link clase 1]" style="display:inline-block;padding:14px 22px;background:#2f5d50;color:#ffffff;text-decoration:none;border-radius:6px;">Ver la clase 1</a></p>
        <p>¿Algo no funciona? Escribinos a [mail de soporte].</p>
      </td></tr>
    </table>
  </td></tr>
</table>
```

Probarlo enviándolo a tu mail y abriéndolo en el celular, con el modo oscuro prendido.

## 5. Aviso al equipo

**Discord · #nuevos-alumnos** (corto, sin datos de pago):

```
🎉 Nuevo alumno · {{nombre}}
Programa: {{programa}} · Coach: {{coach_nombre}}
Objetivo: {{objetivo_principal}}
Ficha: {{link_ficha}}
```

`coach_nombre` es un lookup de texto (si se mapea el vínculo, llega el código del registro). Para Programa Escenario, además: tarea al coach "Agendar llamada de onboarding" con vencimiento a 5 días.

## 6. Secuencias por segmento

| Segmento | Disparo | Qué recibe |
|---|---|---|
| Reserva | Naturaleza = Reserva y pago verificado | Mail "Tu lugar está reservado": qué falta para entrar y hasta cuándo se guarda el lugar |
| Compra adicional (de Voz a Escenario) | Venta nueva de un cliente que ya existe | Bienvenida corta del adicional, sin repetir accesos que ya tiene |
| Referidos | 21 días después del pago verificado | Mail pidiendo que recomiende a alguien, con el link de agenda con su UTM |

## 7. Controles

| Cuándo | Qué se mira | Si falla |
|---|---|---|
| 48 h | ¿Aceptó la invitación a la comunidad? (Escenario: ¿agendó la 1 a 1?) | Aviso al coach en Discord para que le escriba |
| 7 días | ¿Vio la clase 1? | Tarea al CSM: llamada corta |
| Cada lunes | Tiempo promedio de pago verificado a primer acceso | Si pasa de 1 hora, revisar el historial del Zap |

## 8. Offboarding

Disparo: `Estado del alumno` = **Cancelado** o **Suspendido** (lo cambia el CSM).

1. Mail de salida: qué pierde, desde cuándo, y un formulario de 3 preguntas de feedback.
2. Quitar de los espacios de la comunidad y del canal.
3. Quitar de los eventos del calendario.
4. Aviso al coach.

Si es por falta de pago, el protocolo de cobro va antes y es de la skill CRM de Cliente para Infonegocios; este flujo solo ejecuta la salida.

## 9. Plan de prueba

1. Venta de prueba Programa Voz con tu propio mail: no tiene que pasar nada hasta marcar "Pago verificado".
2. Marcar "Pago verificado": llega el mail Voz, la invitación al espacio correcto y el aviso a Discord con el nombre del coach (no un código).
3. Lo mismo con Programa Escenario: dos espacios, link de 1 a 1 y tarea al coach.
4. Reserva de prueba: solo mail de reserva, sin acceso.
5. Cambiar el estado a Cancelado: sale de los espacios y llega el mail de salida.
6. Volver a guardar el mismo registro: no se tiene que mandar dos veces (por el campo `Onboarding enviado`).

## 10. Cómo apagarlo y quién lo mantiene

Dueño: Operaciones. Se apaga desactivando el Zap "Onboarding por programa"; mientras esté apagado, la coordinación da las altas a mano desde la vista "Onboarding · Listos". La capacidad del plan está calculada en "Antes de construir": revisarla cada trimestre o antes de un lanzamiento.

**Siguiente paso:** pasar esta spec al Diseñador de Automatizaciones para la guía paso a paso en Zapier.
