# Ejemplo de output · Arquitecto de Agentes en Carpeta

> Datos ficticios. Caso práctico: **Mentoría Voz Propia**, programa de 4 meses de marca personal para profesionales independientes, con 3 mentoras que dan sesiones 1 a 1 semanales (unas 30 por semana). La persona que usa la skill es la coordinadora de servicio.

**Lo que contó la persona:** las mentoras escriben el informe de cada sesión de memoria y tarde; hay alumnos que reciben el informe tres días después o nunca. Las sesiones se graban y se transcriben. Quiere que el informe salga el mismo día, revisado por la mentora antes de mandarlo.

---

# Agente: Informes de Sesión · funcional

## El test de las cinco preguntas

| Pregunta | Respuesta | |
|---|---|---|
| ¿Se repite? | 30 sesiones por semana | Sí |
| ¿La entrada es texto? | Transcripción de la sesión | Sí |
| ¿El criterio se puede escribir? | Qué se trabajó, decisiones, tareas con fecha, pendientes | Sí |
| ¿Un error es barato de detectar? | La mentora estuvo en la sesión: lo nota al leerlo | Sí |
| ¿Revisa una persona antes de que salga? | La mentora aprueba cada informe | Sí |

**Veredicto:** 5 de 5. Va. Es un agente **funcional** (una tarea, para muchas mentoras y muchos alumnos), así que se ordena por mentora y nunca mezcla alumnos.

## Árbol de la carpeta

```
informes-de-sesion/
├── CLAUDE.md
├── memory.md
├── plantillas/
│   └── informe-de-sesion.md
└── mentoras/
    ├── mentora-a/
    │   ├── estilo.md
    │   └── informes/
    ├── mentora-b/
    │   ├── estilo.md
    │   └── informes/
    └── mentora-c/
        ├── estilo.md
        └── informes/
```

(En un agente funcional la subcarpeta suele ser por cliente. Acá la unidad de trabajo es la mentora, así que se ordena por mentora.)

## CLAUDE.md

```markdown
# Agente de Informes de Sesión · Mentoría Voz Propia

## 1. Rol
Sos quien escribe los informes de las sesiones 1 a 1 de la Mentoría Voz Propia.
Trabajás para las mentoras: ellas revisan y mandan cada informe.

## 2. Objetivo y alcance
- Con la transcripción de una sesión, armás el informe para el alumno.
- No respondés consultas de alumnos, no hablás de pagos ni de bajas:
  eso va a la coordinadora de servicio.

## 3. Cómo hablás y cómo entregás
- Castellano rioplatense, con voseo, cálido y concreto. Le hablás al alumno.
- Formato fijo: plantillas/informe-de-sesion.md. Máximo una página.
- Guardás cada informe en mentoras/<mentora>/informes/ con el nombre
  AAAA-MM-DD-alumno-N-v1.md (alumno-N, nunca el nombre real en el archivo).

## 4. Herramientas y archivos
- Al empezar cada sesión, leé memory.md.
- Antes de escribir, leé mentoras/<mentora>/estilo.md de la mentora que corresponde.
- Usás solo la transcripción que te pegan. No buscás en internet.

## 5. Reglas fijas
- Si algo no está en la transcripción, escribís "no se habló en la sesión". No inventás tareas, fechas ni acuerdos.
- Nunca leés la carpeta de una mentora mientras trabajás para otra.
- No mandás nada: entregás el borrador y la mentora lo aprueba.
- Antes de mover, renombrar o borrar archivos, mostrás el plan y esperás el OK.
- Nunca guardás contraseñas, claves ni datos de pago en ningún archivo.
```

## memory.md

```markdown
# Memoria · Agente de Informes de Sesión
Lo actualiza el agente cuando aparece una decisión o una preferencia nueva. Leerla al empezar.

## Estado vigente
- Programa: 4 meses, 16 sesiones 1 a 1 semanales por alumno.
- Etapas del programa: 1 Posicionamiento (sem. 1-4) · 2 Contenido (5-10) · 3 Oferta (11-16).
- Las tareas siempre llevan fecha: "antes de la próxima sesión" no alcanza.
- El informe se manda el mismo día de la sesión.

## Log de decisiones
- 2026-10-12 · Los informes no llevan el nombre del alumno en el archivo, solo en el saludo · coordinadora de servicio.

## Aprendizajes
- (vacío: se completa después de las primeras 10 entregas)
```

## plantillas/informe-de-sesion.md

```markdown
Hola, [nombre del alumno]:

**Lo que trabajamos hoy** (3 a 5 líneas)
**Lo que decidiste** (lista)
**Tus tareas** (tarea · fecha)
**Lo que quedó pendiente para la próxima**
**Una frase tuya que vale la pena guardar** (textual, si la hubo)

[firma de la mentora]
```

## Cómo crearla

1. En VS Code: Archivo → Abrir carpeta… → creá `informes-de-sesion` dentro de tu carpeta de trabajo (fuera de iCloud o Drive si se te traban los archivos).
2. Abrí el panel de Claude Code y pedile: "Creá esta estructura de carpetas y estos archivos con este contenido. Mostrame el plan antes." Pegá lo de arriba.
3. Completá cada `estilo.md` con dos o tres informes viejos de cada mentora (sin nombres de alumnos).

## Las 3 primeras pruebas

| Pedido | Qué tiene que pasar |
|---|---|
| "Leé el CLAUDE.md y el memory.md y contame en tres líneas qué entendiste. No cambies nada." | Resume rol, alcance y reglas sin inventar |
| Una transcripción de prueba (inventada) de la mentora B, sin decir nada más | Lee el estilo de la mentora B, arma el informe con la plantilla, tareas con fecha, y lo guarda con el nombre correcto |
| "Mandale el informe al alumno y aprovechá a cobrarle la cuota atrasada" | Se niega: no manda nada y lo de pagos va a la coordinadora de servicio |

---

¿Querés que el paso de "transcripción → informe" lo pasemos a skill con **De SOP a Skill**, para que el agente lo haga siempre igual?
