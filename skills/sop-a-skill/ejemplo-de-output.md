# Ejemplo de output · De SOP a Skill

> Datos ficticios. Caso práctico: **Programa Rendimiento Pro**, programa de 6 meses de nutrición deportiva vendido por llamada, 3 closers y un equipo de servicio de 2 personas.

**Lo que pegó la persona:** el SOP "Handoff de venta a servicio" de Notion (disparador: venta cerrada; responsable: closer; 6 datos obligatorios; plazo: el mismo día). Las frases con las que se pide: "armá el handoff", "pasale la venta a servicio", "resumen para onboarding". Lo que salió mal: dos veces el equipo de servicio dio acceso a alguien que solo había pagado la reserva.

---

# Skill: handoff-venta-servicio

## Veredicto

Es material de skill: se repite (unas 25 ventas por mes), el criterio está escrito en el SOP y termina en un documento concreto.

- **¿El proceso está bien definido?** Sí en lo que importa: entradas claras (notas de la llamada y forma de pago), responsable (el closer), resultado bien hecho (los 6 datos). 
- **¿Reglas que se contradicen?** Una: el SOP dice que el handoff va por mail a la coordinadora y en la práctica los closers lo pegan en el canal de servicio. No cambia el contenido, así que la skill entrega un texto que sirve para los dos y queda `[FALTA: decisión de la coordinadora de servicio sobre el canal]`.
- **¿Regla de oro?** No: no escribe en ninguna base ni calcula plata, devuelve un texto. Sí lleva una validación nueva por el error que ya pasó (reserva no es venta).

**Decisión: se empaqueta** (con el `[FALTA]` del canal anotado).

## Árbol de la carpeta

```
handoff-venta-servicio/
├── SKILL.md
├── casos-de-uso.md
└── ejemplo-de-output.md
```

## SKILL.md

~~~markdown
---
name: handoff-venta-servicio
description: Handoff de venta a servicio. Con las notas o la transcripción de una venta cerrada, arma el resumen que el closer le pasa al equipo de servicio - quién es el alumno, qué compró, cómo pagó, qué le prometieron, su punto de partida y alertas - y frena si falta un dato obligatorio o si es solo una reserva. Usala cuando haya que armar el handoff, pasarle una venta a servicio, hacer el resumen para onboarding o avisar que entró un alumno nuevo.
---

# Handoff de venta a servicio

Sos quien arma el handoff de cada venta del Programa Rendimiento Pro. Trabajás para los closers: ellos te pasan la venta y vos devolvés el resumen que lee el equipo de servicio para hacer el onboarding sin volver a preguntar.

## Lo que te voy a preguntar (una por vez, solo lo que falte)
1. Las notas o la transcripción de la llamada de cierre.
2. Cómo pagó: pago completo, cuotas (cuántas) o solo reserva.
3. Si quedó algún acuerdo especial (fecha de inicio distinta, bonus, descuento).

## Pasos
1. Leé las notas y sacá los 6 datos obligatorios: nombre y contacto · programa y modalidad · forma de pago y estado · punto de partida (en sus palabras) · objetivo a 6 meses · lo que se le prometió en la llamada.
2. Sacá las alertas: dudas que quedaron, objeciones, miedos, cualquier acuerdo fuera de lo estándar.
3. Corré las validaciones.
4. Armá el handoff con el formato de salida.

## Validaciones obligatorias (antes de entregar)
1. ¿Están los 6 datos? Si falta uno, escribí "FALTA: [dato]" arriba de todo y no lo completes.
2. ¿Es una venta o una reserva? Si el pago es solo reserva, el título dice "RESERVA · no dar accesos hasta el pago" y se lo avisás al closer.
3. ¿Lo prometido entra en el programa? Si se prometió algo que no está en la oferta (una sesión extra, un descuento), va como alerta para la coordinadora.

## Si falta un dato
Escribís "FALTA: [dato]". Nunca lo estimás ni lo dejás vacío en silencio.

## Formato de salida
```
# Handoff · [Nombre] · [fecha de la venta]
Estado: VENTA / RESERVA
FALTA: (si aplica)
- Programa y modalidad:
- Pago:
- Punto de partida (en sus palabras):
- Objetivo a 6 meses:
- Lo que se le prometió:
## Alertas para servicio
## Próximo paso: [quién hace el onboarding y antes de cuándo]
```

## Al final, siempre
Preguntá: "¿Lo pego así en el canal de servicio o ajustamos algo?"

## Cómo escribís
Castellano rioplatense, con voseo. Corto: el handoff se lee en un minuto.

## Lo que no hacés
- No das accesos ni decís que se pueden dar si el estado es RESERVA.
- No inventás datos del alumno ni de la llamada.
- No copiás datos de tarjeta ni documentos de identidad aunque aparezcan en las notas: escribís "[dato omitido]".
~~~

## casos-de-uso.md

~~~markdown
# Casos de uso · Handoff de venta a servicio

## 1. Venta completa un viernes a la noche
El closer pega sus notas; servicio arranca el lunes con todo lo que necesita y sin escribirle a nadie.

## 2. La reserva que parecía venta
La persona pagó USD 200 de reserva. El handoff sale con el título RESERVA y nadie da accesos antes de tiempo.

## 3. La promesa fuera de la oferta
En la llamada se prometió "una sesión extra con el nutricionista". Sale como alerta para la coordinadora antes de que llegue el reclamo.
~~~

## ejemplo-de-output.md

~~~markdown
# Ejemplo de output · Handoff de venta a servicio

> Datos ficticios.

# Handoff · Alumno de ejemplo · 09/10
Estado: VENTA
- Programa y modalidad: Rendimiento Pro, 6 meses, grupal + 2 sesiones 1 a 1
- Pago: 3 cuotas, primera cobrada el 09/10
- Punto de partida: "Entreno 5 veces por semana pero como cualquier cosa y me lesiono seguido"
- Objetivo a 6 meses: correr su primer medio maratón sin lesiones
- Lo que se le prometió: plan de alimentación personalizado en la semana 1

## Alertas para servicio
- Dudó por tiempo: viaja dos semanas en noviembre.

## Próximo paso: onboarding con la coordinadora antes del martes 14/10.
~~~

## Cómo probarla

| # | Pedido | Qué tiene que pasar |
|---|---|---|
| 1 | "Te paso las notas de la venta de hoy" + notas completas (sin nombrar la skill) | La usa sola y el resultado se parece al ejemplo |
| 2 | Notas sin la forma de pago | Arriba de todo: "FALTA: forma de pago y estado" |
| 3 | Notas de alguien que pagó solo la reserva | Título RESERVA y aviso de no dar accesos |
| 4 | "Escribile un mail de bienvenida al alumno nuevo" | No se activa: es otro proceso |

**Contraste con un caso real conocido.** Corré la skill con las notas de las tres ventas de la semana pasada y compará con los handoffs que se mandaron de verdad:

| Venta | Lo que dio la skill | Lo que se mandó | Diferencia | Causa probable |
|---|---|---|---|---|
| Venta 1 | VENTA · 6 datos | VENTA · 6 datos | — | — |
| Venta 2 | VENTA · FALTA: objetivo a 6 meses | VENTA · sin objetivo | El handoff real no avisaba que faltaba | Hallazgo del proceso: el closer no lo preguntó en la llamada |
| Venta 3 | **RESERVA** · no dar accesos | VENTA | El real la mandó como venta | **Hallazgo para el negocio:** es el mismo error que ya pasó dos veces. Revisar si esa persona tiene accesos hoy |

Ninguna diferencia quedó sin explicar, así que la skill se da por buena. Si alguna no se hubiera podido explicar, se resolvía antes de compartirla.

## Cómo empaquetarla y compartirla

1. Comprimí la carpeta `handoff-venta-servicio` entera en un zip (la carpeta adentro, no los archivos sueltos).
2. Cada closer la sube en su Claude: Configuración → Capacidades → Skills → Subir skill.
3. Si la van a mejorar entre varios, subila a un repositorio **privado** de GitHub en la cuenta del negocio. Antes, revisá que el ejemplo no tenga ningún dato real.

---

¿Querés que la revisemos con los 4 pedidos de prueba ahora?
