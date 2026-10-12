# Ejemplo de output · Portafolio: de caso interno a pieza externa

> Datos ficticios. Matías trabaja como coordinador de operaciones en un programa high ticket de entrenamiento para corredores amateurs que preparan su primera maratón (nombre real del negocio omitido). Armó el sistema de cobros y cuota vencida. No firmó acuerdo de confidencialidad, pero no pidió permiso para mostrarlo. Lo quiere usar en entrevistas.

**Lo que pegó la persona (resumen):** "Programa de [nombre del negocio], 180 alumnos activos, ticket USD 1.600 en 4 cuotas. Antes: 31 cuotas vencidas sin seguimiento (USD 12.400). Armé tabla de cuotas en Airtable, vistas de 'vencen en 7 días' y 'vencidas', protocolo día 1/7/15 y aviso automático 3 días antes con n8n. A los 2 meses: 9 vencidas (USD 3.600). Captura de la base con los nombres de los alumnos."

---

# Pieza de portafolio · Sistema de cobros y cuota vencida

**Origen:** negocio real donde trabajo, anonimizado.

## 1. Qué cambié para poder mostrarlo

- [x] **Nombre del negocio** → "un programa high ticket de entrenamiento online".
- [x] **Nicho muy específico** ("primera maratón", corredores amateurs) + 180 alumnos → se puede reconocer en el rubro. Generalicé a "programa de entrenamiento online con más de 150 alumnos activos".
- [x] **Montos** → porcentajes y variación. USD 12.400 → USD 3.600 pasa a "−71 % del monto vencido".
- [x] **Ticket y cuotas** → "ticket alto, en cuotas" (el precio exacto identifica al negocio).
- [x] **Captura de la base** → no se usa. Hacé una copia de la base, borrá todo y cargá 10 alumnos de prueba ("Alumno 01", "Alumno 02") con fechas y montos inventados.
- [x] **Nombre del negocio dentro de la captura del flujo de n8n** (aparece en el nombre del flujo) → renombrar en la copia antes de capturar.

## 2. El caso

**Contexto.** Programa high ticket de entrenamiento online, con más de 150 alumnos activos y venta en cuotas. Soy coordinador de operaciones.

**El problema.** Las cuotas vencidas se descubrían en el cierre de mes. En el momento del relevamiento había 31 cuotas vencidas sin ningún seguimiento: alumnos que seguían entrando a las clases sin pagar y nadie que les escribiera.

**Qué construí.**
- Una tabla de cuotas vinculada a cada alumno, con estado y días de atraso calculados solos.
- Dos vistas para administración: "vencen en 7 días" y "vencidas".
- Un protocolo escrito: qué mensaje sale el día 1, el 7 y el 15, y quién decide qué pasa después.
- Un aviso automático 3 días antes de cada vencimiento (n8n).
Decidí empezar por el aviso previo y no por la cobranza de las vencidas porque prevenir costaba un mensaje; recuperar, una llamada.

**El resultado.** En 2 meses, las cuotas vencidas bajaron de 31 a 9 (−71 %) y el monto vencido bajó en la misma proporción. Administración pasó de conciliar a fin de mes a revisar dos vistas los lunes y jueves.

**Cómo se cuenta.** *"Armé el sistema de cobros de un programa en cuotas y bajé las cuotas vencidas un 71 % en dos meses."*

## 3. Qué mostrar

- Captura de la **copia con datos de prueba**: vista "Vencidas" con la columna de días de atraso.
- Captura del flujo de n8n **renombrado**, sin credenciales visibles.
- El protocolo día 1 / 7 / 15 como tabla (no tiene datos sensibles).
- **No** mostrar: la base real, el export de la pasarela, mensajes reales a alumnos.

## 4. Semáforo de riesgo

🟡 **Mostrar en privado** (entrevistas, propuestas a una persona). Aun anonimizado, alguien del rubro del running podría reconocer el negocio por el formato del programa.

Para pasarlo a 🟢 (publicarlo en LinkedIn o en tu página), pedí permiso. Mensaje sugerido:

> Hola, ¿cómo estás? Estoy armando mi portafolio y me gustaría mostrar el sistema de cobros que armamos, sin nombrar el negocio, sin montos (sólo porcentajes) y con capturas de una copia con datos de prueba. ¿Te parece bien? Si querés, te lo paso antes para que lo veas.

---

¿Querés la versión de 3 líneas para LinkedIn o para una propuesta? (Recordá: para LinkedIn, primero el permiso.)
