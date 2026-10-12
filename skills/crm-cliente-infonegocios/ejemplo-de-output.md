# Ejemplo de output · CRM de Cliente para Infonegocios

> Datos ficticios. Programa de 6 meses de finanzas personales para freelancers, USD 1.200 en un pago o 3 cuotas de USD 450. Se vende por llamada: 1 setter, 2 closers, 1 CSM, administración part-time.

---

# CRM de Cliente · Programa Brújula

**Herramienta:** Airtable · **Alcance:** ventas + servicio + cobros, en una sola base

## 1. Mapa de entidades

```
Contactos ──< Oportunidades ──< Cobros
                    │
                    └── (si Ganada) ── Alumnos ──< Sesiones
```

- Un **contacto** puede tener varias **oportunidades** (agendó en marzo, no compró, volvió en agosto).
- Cada oportunidad **Ganada** genera un registro en **Alumnos** y sus **cuotas** en Cobros.
- **Cobros** guarda todo lo que entra: reservas, pagos únicos, cuotas.

## 2. Etapas

**Ventas (en Oportunidades)**

| Etapa | Qué tiene que pasar para avanzar | Responsable |
|---|---|---|
| Lead nuevo | Respondió el primer mensaje | Setter |
| Conversación | Setter confirmó interés y presupuesto | Setter |
| Agenda | Llamada agendada con link del canal correcto | Setter |
| Asistió / No-show / Canceló | Closer marca el resultado el mismo día | Closer |
| Calificado | Closer carga calificación (alta / media / baja / no califica) | Closer |
| Ganada | Primer pago acreditado en Cobros | Closer + Administración |
| Perdida | Motivo cargado (precio, tiempo, socio, confianza, no califica, otro) | Closer |

**Servicio (en Alumnos)**

| Etapa | Qué tiene que pasar para avanzar | Responsable |
|---|---|---|
| Onboarding | Acceso dado, formulario de inicio completo, sesión de arranque agendada | CSM |
| En curso | Asistió a la sesión de arranque | CSM |
| En riesgo | Cualquier señal de riesgo activa (ver alertas) | CSM |
| Renovación | Faltan 30 días para el fin del programa | CSM |
| Finalizado / Renovó / Baja | Decisión cargada con motivo | CSM |

## 3. Campos clave

**Oportunidades**

| Campo | Tipo | Obligatorio | Quién lo carga |
|---|---|---|---|
| Contacto | Vínculo a Contactos | Sí | Setter |
| Canal de origen | Selección (Instagram orgánico, Pauta, YouTube, Referido, Lanzamiento) | Sí | Setter |
| Setter / Closer | Colaborador | Sí | Setter |
| Fecha de llamada | Fecha y hora | Sí en Agenda | Setter |
| Resultado de la llamada | Selección (Asistió, No-show, Canceló) | Sí después de la llamada | Closer |
| Calificación | Selección (Alta, Media, Baja, No califica) | Sí si asistió | Closer |
| Monto vendido | Moneda | Sí en Ganada | Closer |
| Modalidad de pago | Selección (Pago único, 3 cuotas) | Sí en Ganada | Closer |
| Nota de traspaso | Texto largo | Sí en Ganada | Closer |
| Motivo de pérdida | Selección | Sí en Perdida | Closer |

**Cobros**

| Campo | Tipo | Notas |
|---|---|---|
| Oportunidad | Vínculo | |
| Tipo | Selección (Reserva, Pago único, Cuota 1, Cuota 2, Cuota 3) | La reserva no suma facturación |
| Monto | Moneda | |
| Vencimiento | Fecha | |
| Fecha de pago | Fecha | Vacío = no pagó |
| Estado | Fórmula | Pagada / Por vencer / Vencida |
| Días de atraso | Fórmula | Sólo si está vencida |

**Alumnos**: Oportunidad ganada, CSM, fecha de inicio, fecha de fin, etapa, próxima acción, fecha de próxima acción, señal de riesgo, motivo de baja.

## 4. Vistas por rol

| Rol | Vista | Qué muestra |
|---|---|---|
| Setter | Mis agendas de la semana | Oportunidades en Agenda, ordenadas por fecha |
| Closer | Mis llamadas de hoy · Mis seguimientos | Llamadas del día; oportunidades calificadas sin cierre |
| CSM | En riesgo · Renovaciones 60/30/15 · Próxima acción vencida | Alumnos que necesitan algo hoy |
| Administración | Vencen en 7 días · Vencidas | Cuotas por cobrar, con días de atraso |
| Founder | Tablero del mes | Cierres, facturado y cobrado por canal |

## 5. Alertas

- Cuota que vence en 3 días → aviso a Administración.
- Cuota vencida → aparece en la vista "Vencidas" con días de atraso.
- Alumno sin asistencia en 14 días o con cuota vencida → señal de riesgo = Sí.
- Próxima acción vencida → aparece en la vista del CSM.
- 60, 30 y 15 días antes del fin del programa → etapa Renovación.

## 6. Protocolo de cuota vencida

| Día de atraso | Qué pasa | Quién |
|---|---|---|
| 1 | Mensaje amable con el link de pago | Administración |
| 7 | Segundo mensaje + llamada corta para entender qué pasó | CSM |
| 15 | Propuesta de plan de pago o pausa de acceso | CSM, decide el founder |
| 30 | Baja con motivo cargado; el saldo queda registrado como deuda | Founder |

## 7. Regla de uso

- El setter carga el canal **al crear** la oportunidad. Sin canal, no se puede pasar a Agenda.
- El closer carga resultado y calificación **el mismo día** de la llamada.
- Administración revisa "Vencen en 7 días" todos los lunes y jueves.
- Las planillas viejas se archivan el día que arranca el CRM. No conviven.

## 8. Lo que se automatiza después

- Oportunidad pasa a Ganada → crear las 3 cuotas en Cobros con sus vencimientos.
- Oportunidad pasa a Ganada → crear el registro en Alumnos y avisar al CSM.
- Aviso automático al alumno 3 días antes de cada vencimiento.

---

¿Querés que te lo baje a pasos de construcción en Airtable? Para compartirlo, armá una copia con datos de prueba: un CRM real tiene datos personales de clientes.
