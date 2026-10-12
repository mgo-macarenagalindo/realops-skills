# Informe de Diagnóstico Operativo · estructura para el founder

> Referencia de la skill Auditoría Operativa de Infonegocio. Sale de los dos templates de diagnóstico que usa RealOps™ (el genérico de MG Operations y el del Módulo 1), unificados, con la numeración oficial de los 6 dolores (la del Cuestionario de Diagnóstico Operativo) y 6 prioridades. Se usa **después** del Mapa de Diagnóstico Operativo: el mapa es tu documento de trabajo; este informe es lo que el founder recibe, lee y firma con su atención.

## Para qué sirve y qué no

- **Sirve para:** que el founder entienda en 5 minutos qué está roto, por qué importa en plata o en tiempo, qué se va a hacer y en qué orden, y qué le toca a él y a su equipo. Es la base del trabajo de los próximos 90 a 120 días.
- **No es:** la propuesta comercial (no lleva precio) ni el informe de cierre del servicio (eso es Informe Final y Testimonio).

## Reglas del informe

1. **Todo sale del mapa.** No aparece ningún número ni cita que no esté en el mapa. Si algo falta, va como "sin dato" o como [SUPUESTO: …, confirmalo con <rol>].
2. **Citas atribuidas al rol**, no a la persona, cuando el informe va a circular por el equipo ("— Coordinación de servicio"). Si es solo para el founder y él conoce a todos, podés usar nombre y rol.
3. **Una idea por línea.** El founder lee en el celular, entre dos llamadas.
4. **Cada problema con su costo**: plata, horas o clientes. "Desorden en las cuotas" no; "US$33.000 sin cobrar y 27 alumnos con cuota vencida adentro" sí.
5. **Cuellos en el cuerpo: los 6 de mayor impacto**, cada uno con su tabla. Los demás cuellos del mapa van en **"Otros cuellos detectados"**, una línea cada uno (título · dolor · por qué espera). El anexo del mapa no va. Así el informe se lee en el celular sin perder nada.
6. **Plan: 6 prioridades, siempre.** Son las seis del Diagnóstico Operativo de RealOps™, sin vincularlas a módulos del programa (un template trae siete con módulos: no se usa ese esqueleto). Lo que no entra en ninguna va adentro de la más cercana.
7. **Numeración oficial de los 6 dolores:** la del Cuestionario de Diagnóstico Operativo (1 Reuniones eternas · 2 Información dispersa · 3 Fuga de datos y métricas · 4 Roles difusos · 5 Cultura del sobreesfuerzo · 6 Tareas manuales). Si el template que tenés a mano trae el semáforo con 2 y 4 invertidos, no lo copies: pasá por nombre.
8. **Sin herramienta impuesta.** Los entregables se describen por lo que hacen ("tabla de cuotas con días de atraso", "canal por área") y se nombra la herramienta solo si el negocio ya la usa o el founder la eligió.
9. **Tono:** profesional, directo, sin culpas. Se habla de sistemas, no de personas que fallan.
10. **Firma:** nombre y rol de quien lo entrega (por ejemplo, "[Tu nombre] · Operaciones"). Nunca "el equipo de RealOps".

## Estructura (en este orden)

```
# Diagnóstico Operativo · [Negocio]
Síntesis, cuellos de botella y plan de acción

| Campo | Dato |
|---|---|
| Responsable del diagnóstico | [Nombre · rol] |
| Negocio | [Nombre] |
| Fecha de entrega | [DD/MM/AAAA] |
| Período del plan | [DD/MM al DD/MM · N días] |
| Fuentes | [cuestionarios o charlas con N de M roles, llamadas grabadas, herramientas auditadas, planillas y bases revisadas] |

**Objetivo del diagnóstico.** [Una o dos frases: ordenar y priorizar lo que hay que construir, distinguiendo lo urgente de lo que puede esperar, para los próximos N días.]

## 1. Resumen ejecutivo
[Un párrafo: cómo está el negocio, los 2 o 3 hallazgos que más pesan y la conclusión. Empezá por lo que funciona: el founder tiene que reconocer su negocio.]

| Dato clave | Valor |
|---|---|
| Facturado por mes (lo vendido) | |
| Cobrado por mes (lo que entró) | |
| Equipo | [N personas · roles] |
| Clientes o alumnos activos | |
| Herramientas principales | |

## 2. Semáforo de los 6 dolores del backstage
| Dolor | Estado | Orden | Lo que lo muestra |
|---|---|---|---|
| 1 · Reuniones eternas e ineficientes | CRÍTICO / MODERADO / BAJO | [solo críticos: 1 a N] | [una línea con número o cita] |
| 2 · Información dispersa | | | |
| 3 · Fuga de datos y métricas | | | |
| 4 · Roles difusos | | | |
| 5 · Cultura del sobreesfuerzo | | | |
| 6 · Tareas manuales sin automatizar | | | |
(CRÍTICO = requiere acción inmediata · MODERADO = existe a medias, hay que mejorarlo · BAJO = funciona razonablemente. Si no hay evidencia para un dolor, va "sin evidencia suficiente", no un color. Los criterios están en el SKILL.md, sección "Los 6 dolores y el semáforo".)
**Orden de los críticos:** del 1 al N por la plata por mes que traba cada dolor (la suma de sus cuellos). Debajo de la tabla, una línea: "Crítico 1 · [dolor] · US$[monto] por mes · [de qué cuellos sale]". Si un crítico no tiene número de plata, va después de los que sí, y se dice.

## 3. Cuellos de botella
### Cuello N · [Título descriptivo]
[2 o 3 oraciones: qué pasa y por qué importa.]
| | |
|---|---|
| Evidencia | "[cita]" — [rol] · o [número] |
| Impacto | [Alto / Medio / Bajo] · [por qué] |
| Esfuerzo | [Alto / Medio / Bajo] · [por qué] |
| Dolor del backstage | [1 a 6] |
| Patrón | [1 a 10 o específico] |
| Solución propuesta | [qué se construye o qué se decide, en una o dos líneas] |
(Los 6 de mayor impacto, ordenados: el 1 es el que más duele. Cerrá la sección con una línea que conecte los cuellos con el orden del plan.)

**Otros cuellos detectados** (si el mapa tenía más de 6)
- [Título] · Dolor [1 a 6] · [por qué espera: impacto medio, depende de otro cuello, etc.]

## 4. Radiografía por área
### 4.1 Ventas · 4.2 Marketing · 4.3 Servicio · 4.4 Operaciones y administración
| Lo que funciona | Lo que falla | Lo que falta |
|---|---|---|
(2 o 3 filas por área. "Lo que funciona" no se saltea: es lo que no hay que romper.)

## 5. Techo operativo
- **Hoy el negocio está limitado por:** [una frase]
- **Si mañana se duplicaran las ventas, lo primero que se rompe es:** [una frase, con el número que lo muestra]
- **Las 3 cosas que hay que resolver para romper el techo:** [tres líneas]

## 6. Plan de acción por prioridades
Las seis prioridades (siempre seis), en el orden que salió de la matriz impacto × esfuerzo y del orden de los críticos (puede no ser el orden de la lista). Si el plan no arranca por el CRÍTICO 1, una línea dice por qué (por ejemplo: "es de esfuerzo alto; arrancamos por el CRÍTICO 2, que se resuelve en una semana").

### Prioridad N · [Nombre]
Resuelve: [cuellos N, M] · Dolor: [1 a 6]
| Estado | Fechas estimadas | Bloqueante |
|---|---|---|
| PRÓXIMO / EN IMPLEMENTACIÓN / IMPLEMENTADO / PENDIENTE | [DD/MM al DD/MM] | [qué tiene que resolver el negocio, o "Sin bloqueante"] |
**Entregables:** [3 a 5, concretos]
**Resultado esperado:** [qué cambia para el founder y el equipo, en una línea]

## 7. Cronograma resumen
| Orden | Prioridad | Entregable principal | Semanas | Estado |
|---|---|---|---|---|
| 1 | | | Sem 1–2 | |
| … | | | | |
| — | Adaptación y ajustes | | Últimas 2–3 semanas | |

## 8. Tareas a cargo del equipo
Lo que depende del negocio para que el plan avance. Los bloqueantes van marcados con ⚠.
### Dirección · Responsable: [rol]
- ⚠ BLOQUEANTE · [decisión o acceso]
### Servicio · Responsable: [rol]
### Comercial y marketing · Responsable: [rol]
### Administración y finanzas · Responsable: [rol]

## 9. Nota final
- **Fecha de fin del plan:** [DD/MM/AAAA] · [N] días desde [inicio].
- **Sobre las fechas:** los entregables son una referencia; pueden superponerse o reordenarse según se resuelvan los bloqueantes. Conviene dejar las últimas 2 o 3 semanas para adaptación del equipo, tutoriales y ajustes.
- **Bloqueantes urgentes (próxima semana):** [hasta 3, con quién lo resuelve]
- **Próximos pasos:** el founder revisa y devuelve comentarios en [N] días · reunión de cierre del diagnóstico para alinear prioridades · el equipo avanza con lo marcado con ⚠.

**Cómo se conecta todo**
| Dolor del backstage | Cuellos | Prioridad que lo resuelve |
|---|---|---|

[Nombre] · [Rol]
```

## Cómo se pasa del mapa al informe

| En el mapa | En el informe |
|---|---|
| 1. Qué miré y qué no | Tabla de portada (fuentes) + lo no auditable, en una línea, en el resumen ejecutivo |
| 2. Cuellos (6 a 8) | 3. Los 6 de mayor impacto, con "Solución propuesta" y "Dolor del backstage" agregados; el resto en "Otros cuellos detectados", una línea cada uno |
| Inconsistencia más importante | Resumen ejecutivo (es la frase que el founder tiene que leer) |
| 3. Tabla por closer | 4.1 Ventas (lo que falla / lo que falta) y, si hace falta, dentro del cuello de ventas |
| 4. Matriz | Orden de la sección 6 y del cronograma |
| 5. Plan de prioridades | 6. Plan, con estado, fechas y bloqueante |
| 6. Bloqueantes | 8. Tareas del equipo (⚠) y 9. Bloqueantes urgentes |
| 7. Los 3 movimientos | 9. Próximos pasos (lo que ya está en marcha esta semana) |
| Anexo · Otros hallazgos | No va. Si alguno es un riesgo (por ejemplo, de seguridad), sube a un cuello o a un bloqueante |
| Para confirmar | Supuestos marcados en el texto + una línea en la nota final: "Pendiente de confirmar: …" |

## De patrón a dolor del backstage (guía, no regla · numeración oficial)

| Patrón del mapa | Dolor del backstage que suele mostrar |
|---|---|
| 1 Comunicación dispersa | 1 Reuniones eternas · 2 Información dispersa |
| 2 Ceguera de atribución | 3 Fuga de datos y métricas |
| 3 CRM ausente o subutilizado | 3 Fuga de datos · 2 Información dispersa |
| 4 Gestión financiera manual | 3 Fuga de datos · 6 Tareas manuales |
| 5 Roles difusos | 4 Roles difusos |
| 6 Desconexión venta → servicio | 6 Tareas manuales · 2 Información dispersa |
| 7 Sin alertas de renovación o cuota | 6 Tareas manuales · 3 Fuga de datos |
| 8 Founder sobrecargado | 5 Cultura del sobreesfuerzo · 4 Roles difusos |
| 9 Accesos y cuentas sin dueño | 2 Información dispersa · 4 Roles difusos |
| 10 Incentivos desalineados | 4 Roles difusos · 3 Fuga de datos |

## Estados del plan

- **IMPLEMENTADO:** ya funciona y el equipo lo usa.
- **EN IMPLEMENTACIÓN (foco actual):** se está construyendo esta semana. Como máximo dos a la vez (tope orientativo).
- **PRÓXIMO:** arranca cuando termine el foco actual o se destrabe su bloqueante.
- **PENDIENTE:** depende de una decisión o de un acceso que todavía no está.

En un diagnóstico de arranque casi todo está en PRÓXIMO o PENDIENTE. Está bien: el informe muestra el orden, no promete que ya está hecho.
