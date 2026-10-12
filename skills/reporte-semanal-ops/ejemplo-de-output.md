# Ejemplo de output · Reporte de Ops (semanal y mensual)

> Datos ficticios. Programa de 6 meses de ventas para agentes inmobiliarios, vendido por llamada y en cuotas. Lo arma la coordinadora de operaciones para el founder.

**Paso 0, lo que contestó la persona:** el founder lee WhatsApp; la base está en Airtable con tabla de KPIs globales; quiere **semanal** (lunes 9:00 por WhatsApp) y **mensual** (Google Sheets, revisado en la reunión del primer jueves). Marketing y servicio cargan sus números en su pestaña.

---

## 1 · Semanal

**Lo que pegó la persona:**
- Semana 06/10 → 12/10 y anterior: cobrado 9.800 / 8.750 · llamadas hechas 26 / 27 · asistencia 63 % / 68 % · cierres 6 / 6 · cuotas vencidas **al domingo** 6 (12/10) / 14 (05/10).
- Vence esta semana (vista "vence en 7 días"): 9 cuotas por USD 5.400, 3 de alumnos que ya pagaron tarde la anterior.
- Notas: "aviso automático 3 días antes del vencimiento arrancó el lunes 6" · "migración del área de miembros frenada desde el 8, falta acceso admin" · "WhatsApp 2 h antes de las llamadas, yo digo que sí a prueba 2 semanas" · "¿quién me da el acceso, el founder o soporte?".

```
REPORTE DE OPS · semana 06/10 → 12/10

Logro de la semana: las cuotas vencidas bajaron de 14 a 6 con el aviso automático de 3 días antes.

Números clave (vs. semana anterior):
- Cobrado: USD 9.800 (+12 %)
- Llamadas hechas: 26 (−4 %)
- Asistencia: 63 % (−5 pts)
- Cierres: 6 (=)
- Cuotas vencidas al domingo 12/10: 6 (−57 %)

Lo trabado y lo que vence:
- Migración del área de miembros · desde el 08/10 · lo destraba: acceso de administración.
- Vence esta semana: 9 cuotas (USD 5.400); 3 son de alumnos que ya pagaron tarde. Les escribo el martes.

Decisiones que necesito:
1. ¿Sumamos un recordatorio por WhatsApp 2 h antes de cada llamada? — Opciones: sí, a prueba 2 semanas / no. Recomiendo: sí, porque la asistencia bajó 5 puntos.
2. ¿Quién me da el acceso de administración? — Opciones: vos / soporte. Recomiendo: vos, hoy, porque soporte tarda 72 h.
```

**Notas del borrador**
- Las vencidas son un stock: comparé el corte del domingo 12/10 con el del 05/10, no "las que vencieron esta semana".
- La recomendación 2 la escribí con lo que me dijiste de soporte; si no es así, cambiala.

¿Lo mandás así o ajustamos algo? Mismo día, misma hora, todas las semanas.

---

## 2 · Mensual por áreas (septiembre)

**Mensaje de envío (WhatsApp):**

```
REPORTE MENSUAL DE OPS · septiembre
En una frase: entró más plata que en agosto, pero por cuotas viejas: las ventas nuevas bajaron y la pauta trae gente que no asiste.
Los 5 números:
- Cobrado: USD 38.900 (+9 %) · de eso, cuotas anteriores 15.200 (+41 %)
- Facturado: USD 41.300 (−7 %)
- Morosidad al 30/09: 7 % (−4 pts)
- Costo por venta (pauta): USD 610 (+38 %)
- Alumnos sin clase hace más de 21 días: 11 (+5)
Decisiones del mes: 1. Bono de setters por llamada calificada que se presenta. 2. Pausar el anuncio 2. 3. Encuesta de mitad de programa a la cohorte de julio.
El detalle por área: [link a la planilla]
```

**La planilla: pestaña Resumen**

| Los 5 números | Sep | Ago | Variación | Estado |
|---|---|---|---|---|
| Cobrado total | 38.900 | 35.700 | +9 % | 🟡 |
| Facturado | 41.300 | 44.400 | −7 % | 🔴 |
| Morosidad al corte | 7 % | 11 % | −4 pts | 🟢 |
| Costo por venta (pauta) | 610 | 442 | +38 % | 🔴 |
| Alumnos sin clase > 21 días | 11 | 6 | +83 % | 🔴 |

Semáforo por área: Marketing 🔴 · Setters 🟡 · Closers 🟢 · Cobros 🟢 · Servicio 🟡 · Operaciones 🟡

**Pestañas por área (extracto)**

| Área | Métrica | Sep | Ago | Variación | Meta o alarma | Estado | Responsable | Lectura |
|---|---|---|---|---|---|---|---|---|
| Marketing | Agendas pauta | 58 | 41 | +41 % | — | ℹ️ | Marketing | El anuncio 2 duplicó agendas |
| Marketing | Costo por venta anuncio 2 | 1.450 | 520 | +179 % | < 700 | 🔴 | Marketing | Barato por agenda, caro por cliente: pausar |
| Marketing | Leads sin canal | 4 % | 3 % | +1 pt | < 10 % | 🟢 | Operaciones | Tracking sano |
| Setters | Agendas que se presentan y califican | 52 % | 64 % | −12 pts | > 60 % | 🟡 | Líder comercial | Cae en el setter con más agendas del anuncio 2 |
| Closers | Cierre sobre asistidas | 30 % | 29 % | +1 pt | > 25 % | 🟢 | Líder comercial | Los closers no son el problema |
| Cobros | Cobrado · reservas / nuevos / cuotas | 1.200 / 22.500 / 15.200 | 1.400 / 23.500 / 10.800 | | — | ℹ️ | Coordinación | El aumento es de cuotas viejas |
| Cobros | Morosidad al 30/09 | 7 % | 11 % | −4 pts | < 10 % | 🟢 | Coordinación | Efecto del aviso previo |
| Servicio | Días de pago a acceso (mediana) | 1 | 3 | −67 % | ≤ 1 | 🟢 | Operaciones | Alta automática funcionando |
| Servicio | NPS | sin dato | sin dato | | | ⚪ | CSM | No hay encuesta: se manda en octubre |
| Servicio | Bajas | sin dato | sin dato | | | ⚪ | CSM | No se registran |
| Operaciones | Horas en fricción (semana registrada) | 4 h 10 min | 7 h 20 min | −43 % | — | 🟢 | Operaciones | Bajó con la vista de cuotas compartida |
| Operaciones | Horas recuperadas por automatizaciones | 6 h / mes | 2 h / mes | +200 % | — | 🟢 | Operaciones | Alta de acceso + aviso de cuota |
| Operaciones | EOD cargados | 61 % | 74 % | −13 pts | > 80 % | 🔴 | Operaciones | Los closers dejaron de cargar en la semana del lanzamiento |

**Pestaña Sin dato:** NPS (CSM, encuesta a la cohorte de julio antes del 20/10) · Bajas (CSM, campo "motivo de baja" desde el 01/10).

**Notas del borrador**
- Las lecturas de una línea salen de la lectura de septiembre que hiciste con Analista de KPIs.
- Las tres decisiones son las tuyas; las ordené por impacto en la plata.

---

## Después de un mes de envíos: las 3 preguntas de cierre

1. ¿Qué parte leíste primero? ¿Y cuál salteaste?
2. ¿Hubo algo que me preguntaste por otro lado y debería estar acá?
3. ¿Te sirvió para decidir algo? ¿Qué?
