# Casos de uso · Arquitecto de Agentes en Carpeta

Tres situaciones de infonegocio donde esta skill te ahorra la tarde de prueba y error. Negocios y nombres ficticios.

---

## 1. El agente que escribe los informes de sesión de una mentoría

**La situación.** En una mentoría de marca personal, las mentoras escriben de memoria el informe de cada sesión 1 a 1, a la noche, o no lo escriben. Son unas 30 sesiones por semana.

**Qué le pasás.** Qué entra (la transcripción de la sesión), qué tiene que salir (qué se trabajó, decisiones, tareas con fecha, pendientes), quién lo revisa antes de mandarlo y qué no puede pasar nunca (inventar tareas, nombrar a otros alumnos).

**Qué te devuelve.** El test de las cinco preguntas (5 de 5: va), la decisión (agente **funcional de un solo negocio**: una tarea, ordenada por mes), la carpeta con `CLAUDE.md`, `memory.md`, `plantillas/informe-de-sesion.md`, el estilo de cada mentora y las 3 pruebas para darlo por listo (una de ellas comprueba que nunca le manda nada al alumno sin que la mentora lo apruebe).

**Si no sabés algo.** Si no sabés quién revisa o si las sesiones se graban todas, la skill te hace dos o tres preguntas más chicas. Si igual no sabés, deja un supuesto rotulado ("Supuesto a validar con el founder") en el `memory.md` y la carpeta sale completa igual.

**Por qué sirve.** Es la actividad 23 del programa armada en Claude Code, con memoria propia y sin repetir instrucciones en cada sesión.

---

## 2. Ordenar el trabajo de un negocio donde ya trabajás

**La situación.** Sos la persona de operaciones de una academia de pastelería online. Tenés SOPs sueltos en Drive, exportaciones con nombres como "final-final-2" y cada vez que abrís Claude le volvés a explicar el negocio.

**Qué le pasás.** Qué vende el negocio, el equipo por rol, las herramientas, lo urgente de este mes y qué no querés que Claude toque.

**Qué te devuelve.** Un agente **operativo** con la estructura 00 a 99, el `CLAUDE.md` del negocio en 5 bloques, el `memory.md` con el estado vigente y un log de decisiones vacío, y el prompt para que Claude Code ordene tu carpeta actual en dos tiempos (primero la propuesta, después el movimiento).

**Por qué sirve.** Mañana abrís la carpeta y Claude ya sabe dónde está parado. Es la base de cualquier actividad que hagas con Claude Code.

---

## 3. Separar un agente que se volvió un cajón de sastre

**La situación.** Armaste un agente para hacer landings y, de a poco, le empezaste a pedir los SOPs y los reportes de uno de tus clientes. Ahora mezcla colores de una marca con la de otra y gasta más de lo que debería.

**Qué le pasás.** El `CLAUDE.md` actual y la lista de cosas que le pedís en una semana normal.

**Qué te devuelve.** El diagnóstico (es un funcional con trabajo operativo adentro), la propuesta de **dos carpetas** (el agente de landings con `clientes/<nombre>/` y un agente operativo para ese cliente), qué línea del `CLAUDE.md` va a cada una y qué pasa al `memory.md` de cada lado.

**Por qué sirve.** Un agente con un rol claro responde mejor y gasta menos. Es la regla de la clase del 20/07, aplicada a tu carpeta.
