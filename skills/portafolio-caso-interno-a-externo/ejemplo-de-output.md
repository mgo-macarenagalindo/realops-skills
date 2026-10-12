# Ejemplo de output · Revisor de Piezas de Portafolio

> Datos ficticios. Matías es coordinador de operaciones en un programa high ticket de entrenamiento online para corredores amateurs (nombre real omitido). Trae la pieza 6, su primera automatización en n8n, y la quiere usar en entrevistas. No firmó confidencialidad ni pidió permiso.

**Lo que pegó (resumen):** "Automatización en n8n: cuando un alumno agenda la llamada de bienvenida en Calendly, busca al alumno en Airtable, lo actualiza con la fecha y le avisa por Slack a la coach que le toca. Antes lo hacía yo a mano: unas 25 llamadas por semana, 6 minutos cada una. Lo activé el 28/09. Captura del flujo: se ve el nombre del negocio en el título y la clave de Airtable en el nodo. Ahorra mucho tiempo."

---

# Revisión · Primera automatización · Matías

**Origen:** negocio real donde trabaja · **Para:** entrevistas
**Veredicto:** 🟡 **Casi**

## 1. Chequeo de origen

Es de un negocio real: no hay marcas de caso práctico. Va el chequeo de lo mostrable completo (punto 4).

## 2. La rúbrica, criterio por criterio

| Criterio | | Qué encontré y cómo arreglarlo |
|---|---|---|
| El "antes" medido | ✅ | "25 llamadas por semana, 6 minutos cada una": 2,5 horas por semana. Ponelo así, en horas. |
| Flujo en una línea | 🟡 | Está contado, no dibujado. Agregá: *Calendly (agenda nueva) → buscar alumno en Airtable → actualizar fecha → aviso en Slack a la coach.* |
| No duplica registros | ✅ | "Busca al alumno" antes de actualizar. Decí qué pasa si **no** lo encuentra (¿lo crea?, ¿avisa?). |
| Aviso con quién, cuándo y link | 🟡 | Dice que avisa a la coach, no qué dice el aviso. Pegá el texto: "Agenda nueva: [alumno] · [fecha y hora] · [link al registro]". |
| Aviso de error | ❌ | No aparece. Sumá un nodo de error que te escriba a vos si falla algún paso: una automatización que falla en silencio es peor que no tenerla. |
| Corrió una semana y hay "después" | 🟡 | Activa desde el 28/09: ya pasaron dos semanas, pero falta el después medido. Revisá el registro de ejecuciones contra el calendario y escribilo: "de 2,5 h por semana a ~10 min de control". |
| C1 · Rótulo de origen | ❌ | Falta. "Negocio real, anonimizado." |
| C2 · Números con fuente | 🟡 | "Ahorra mucho tiempo" no es un número: reemplazalo por las horas. |
| C3 · Una decisión explicada | ❌ | No hay ninguna. Por ejemplo: ¿por qué Calendly como disparador y no el formulario de inscripción? |
| C4 · Se entiende sin vos | ✅ | Sí, con el flujo dibujado queda más claro. |

## 3. Los 3 cambios que más la mejoran

1. **Agregá el aviso de error.** Un nodo que te mande un mensaje con el nombre del paso que falló. Es lo primero que pregunta quien sabe.
2. **Escribí la decisión.** "Lo dispara la agenda en Calendly y no la inscripción porque la coach solo necesita saberlo cuando hay fecha; así no recibe avisos de alumnos que todavía no agendaron."
3. **Medí el después** con el registro de ejecuciones de las dos semanas y escribilo en una línea.

## 4. Lo mostrable

- [x] Nombre del negocio → "un programa high ticket de entrenamiento online".
- [x] Nicho chico ("corredores amateurs") → "entrenamiento online", para que no se reconozca.
- [x] **Captura del flujo**: tiene el nombre del negocio en el título y **la clave de Airtable visible en el nodo**. No se usa así. Duplicá el flujo, renombralo, sacá las credenciales y capturá la copia.
- [x] Nombres de alumnos y de las coaches → "el alumno", "la coach asignada".
- [ ] No hay montos: no aplica.

**Semáforo:** 🟡 **solo en privado** (entrevistas). Para publicarlo en LinkedIn, pedí permiso:

> Hola, ¿cómo estás? Estoy armando mi portafolio y me gustaría mostrar la automatización de agendas que armé, sin nombrar el negocio ni a nadie del equipo y con capturas de una copia sin datos. ¿Te parece bien? Si querés, te lo paso antes.

## 5. La ficha de la pieza

- **Origen:** negocio real, anonimizado.
- **Contexto:** programa high ticket de entrenamiento online. Soy coordinador de operaciones.
- **El problema:** cada llamada de bienvenida agendada se pasaba a mano a la base y se avisaba a la coach por privado: ~25 por semana, 6 minutos cada una, **2,5 horas por semana**.
- **Qué construí y qué decidí:** una automatización en n8n que toma cada agenda nueva de Calendly, actualiza al alumno en Airtable y avisa en Slack a la coach asignada, con el link al registro. La dispara la agenda y no la inscripción, para que la coach solo reciba avisos con fecha.
- **El estado:** activa desde el 28/09; [falta medir el después con el registro de ejecuciones]. Resultado intermedio: la coach ya no pregunta por privado quién agendó.
- **Cómo se cuenta:** *"Automaticé el paso de cada agenda a la base y el aviso a la coach: 2,5 horas por semana que dejaron de hacerse a mano."*

## 6. Qué sigue

Trajiste una sola pieza, así que el orden no aplica todavía. La que más suma después es el **CRM** (pieza 5): esta automatización escribe en una base, y mostrar la base completa cuenta la historia entera.

**Para confirmar**
- [SUPUESTO: 6 minutos por llamada sale de tu estimación; confirmalo con el registro de ejecuciones].
- [Confirmá con tu responsable si podés mostrarlo en entrevistas sin nombrar el negocio].

---

¿Revisamos la versión corregida? En la segunda vuelta miro solo lo que estaba 🟡 o ❌.
