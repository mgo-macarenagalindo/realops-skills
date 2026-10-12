# Ejemplo de output · Dashboard con Vibe Coding

> Datos ficticios. Caso práctico del programa: academia online de marketing para emprendedores, programa de 6 meses de USD 1.500 en un pago o 3 cuotas de USD 500, vendido por llamada. Quien pide la skill no trabaja en el negocio: lo quiere para su portafolio, con datos inventados, y después conectarlo a una base de prueba de Airtable.

**Lo que contó la persona:** "Quiero un tablero con link para mostrar en entrevistas. Tengo Claude Code en la app de escritorio, cuenta de GitHub y nunca usé Vercel."

---

# Dashboard · Academia de marketing (caso práctico) · plan de construcción

## Para quién y qué decisión toma

El founder lo abre en el celular a las 8 de la mañana.
- **Cada día:** ¿hay algo que resolver hoy? (cuotas que vencen, un número en rojo)
- **Cada semana:** ¿el mes viene bien o mal contra el anterior?
- **Cada mes:** ¿de qué canal vino la plata?

## Los 5 KPIs

| KPI | Fórmula y fuente | Se compara con | Rojo cuando | Decisión si está en rojo |
|---|---|---|---|---|
| Cash cobrado | Suma de `monto_usd` con `fecha_pago` dentro del mes (ventas.csv). Se calcula desde la fecha de pago, no desde un campo de estado | Mes anterior | Cae más de 15 % | Revisar si cayeron ventas nuevas o cuotas, antes de tocar la pauta |
| Ventas nuevas | Ventas con fecha en el mes | Mes anterior | Menos de 15 | Mirar agendas y cierre por canal |
| Cierre sobre agendas | Llamadas con resultado Cerrada ÷ todas las llamadas agendadas del mes (llamadas.csv) | Rango 15-20 % | Debajo de 10 % | El funnel deja pasar leads no calificados: revisar el formulario de agenda |
| Cuotas vencidas | Cuotas con `fecha_vencimiento` anterior a hoy y `fecha_pago` vacía: cantidad y monto | Semana anterior | Más de 5 | Activar el protocolo de cuota vencida esa semana |
| Bajas del mes | Alumnos que pasaron a baja ÷ activos al inicio del mes | Mes anterior | Más de 5 % | Revisar con servicio en qué semana se caen |

Elegidos con la ficha de la skill Analista de KPIs (modo 2). Las referencias de cierre son las que se usan en el programa, como orientación.

## Paso 2 · Datos de ejemplo

```prompt
Generá dos archivos CSV con datos inventados de una academia online que vende un
programa de USD 1.500 (o 3 cuotas de USD 500), entre julio y octubre de 2026:

ventas.csv (120 filas): fecha, cliente (nombres inventados), canal (Orgánico /
Pauta / Referido), monto_usd, cuotas (1 o 3), fecha_vencimiento, fecha_pago
(vacía si no pagó), closer (Closer 1 / Closer 2). Sin columna de "estado": el
estado se calcula de las fechas.

llamadas.csv (500 filas): fecha, canal, closer, resultado (Cerrada / No cerrada /
No asistió).

Que sea realista: cierre sobre agendas entre 15 y 22 %, algo más de ventas en
octubre, 5 a 10 % de cuotas vencidas, y 3 o 4 bajas por mes en una tabla aparte
alumnos.csv (alumno, fecha_alta, estado: Activo / Baja, fecha_baja). Ningún dato real.
```

## Paso 3 · CLAUDE.md del proyecto

Carpeta local: `proyectos/dashboard-academia`, con los CSV en `data/`.

```markdown
# Dashboard de KPIs · Academia (caso práctico)

## Qué es
Un dashboard web de 5 KPIs para el founder de una academia online. Lo mira en
el celular a la mañana. Tiene que entenderse en 30 segundos.

## Los 5 KPIs
[pegar la tabla de 5 filas de arriba]

## Reglas técnicas
- Una sola página HTML con CSS y JavaScript, sin frameworks ni instalación.
- Gráficos con una librería desde un CDN.
- Lee los datos de los CSV de data/ (modo demo).

## Reglas de diseño
- Fondo claro, una tipografía legible, números grandes.
- Verde y rojo solo para estado.
- Se lee bien a 400 px de ancho.
- Números en formato argentino: 1.234,5.

## Seguridad
- Nunca claves, tokens ni datos reales de clientes en el código.
- Antes de cambios grandes, mostrar un plan y esperar OK.
```

**Prompt del plan (en modo Plan):**

```prompt
Leé el CLAUDE.md y los CSV de data/. Proponeme un plan para el dashboard:
1. Las 5 tarjetas de arriba y qué comparación muestra cada una.
2. Dos gráficos abajo (cash por semana y ventas por canal) y por qué esos.
3. Un bloque "Qué mirar hoy" con 2 o 3 alertas calculadas.
4. Un selector de mes.
5. Cómo vas a calcular cada KPI desde los CSV, en palabras, para que lo verifique.
No escribas código todavía. Si algún KPI no se puede calcular con estos datos, decímelo.
```

**Qué revisar en el plan:** que "Cierre sobre agendas" divida por **todas** las agendadas (incluidas las que no asistieron). Si lo calcula sobre las asistidas, es otra tasa: corregilo antes de construir.

## Paso 4 · Construir y verificar

```prompt
Dale, construilo según el plan aprobado. Cuando termines:
1. Decime cómo lo abro en el navegador.
2. Calculá aparte los 5 KPIs de octubre desde los CSV y mostrame la tabla:
   KPI · valor en el dashboard · valor calculado aparte.
   Si no coinciden, arreglalo antes de mostrármelo.
```

Lo que devolvió con los datos de ejemplo de este caso:

| KPI (octubre) | Dashboard | Calculado aparte |
|---|---|---|
| Cash cobrado | USD 41.250 | USD 41.250 |
| Ventas nuevas | 18 | 18 |
| Cierre sobre agendas | 18,8 % (18 de 96) | 18,8 % |
| Cuotas vencidas | 7 · USD 3.500 | 7 · USD 3.500 |
| Bajas del mes | 2,1 % (3 de 140) | 2,1 % |

Verificación a mano: contar con una tabla dinámica de Sheets las filas de octubre con resultado "Cerrada" en llamadas.csv: 18. Coincide.

**Ronda de ajustes (con captura):**

```prompt
Te pego cómo se ve en el celular. Ajustes:
- Las tarjetas quedan de a cuatro y no se leen: que queden de a dos.
- El gráfico de canales, barras horizontales ordenadas de mayor a menor.
- La tarjeta de cuotas vencidas tiene que mostrar cantidad y monto.
Hacé solo estos cambios, no toques el resto.
```

## Paso 5 · GitHub y Vercel

- [ ] GitHub Desktop → agregar la carpeta como repositorio → **revisar la lista de archivos** (solo `index.html`, `CLAUDE.md` y `data/` con CSV inventados) → commit → publicar como **privado**.
- [ ] Vercel → nuevo proyecto → importar el repositorio → framework "Other" → publicar.
- [ ] Abrir el link en el celular.
- [ ] Es portafolio con datos inventados: el plan gratuito sirve. Si algún día es para un negocio, revisar las condiciones vigentes de Vercel (a octubre de 2026, el plan gratuito no permite uso comercial) y que lo pague el cliente en su cuenta.

## Paso 6 · Conexión en vivo (base de prueba de Airtable)

1. Crear en Airtable un token con permisos de **solo lectura** y acceso **solo** a la base de prueba.
2. En Vercel → Settings → Environment Variables, cargar tres variables: el token, el ID de la base y una contraseña para el tablero. **No se pegan en el chat ni en el código.**
3. Prompt:

```prompt
Quiero que el dashboard lea los datos de Airtable en vez de los CSV. Reglas:
- El token NUNCA va en el navegador ni en el repo. Creá una función del lado del
  servidor en Vercel que lea las variables de entorno (token e ID de la base), pida
  los registros de las tablas [Ventas, Llamadas, Alumnos] con paginación, calcule
  los 5 KPIs del mes pedido y devuelva SOLO los números agregados, sin nombres.
- Protegé todo el sitio (incluida la función) con un middleware de autenticación
  básica que compare contra la variable de entorno SITE_PASSWORD. La contraseña
  nunca escrita en el código.
- Que la respuesta quede en caché 30 minutos.
- Si falla, la página muestra "No se pudieron cargar los datos".
- Si la URL tiene ?demo=1, que use los CSV y no pida contraseña (para el portafolio).
Los campos de cada tabla son: [pegar la lista].
Mostrame el plan primero y después explicame cómo lo pruebo en Vercel.
```

4. Commit y push. Vercel lo publica solo.

## Pruebas

| # | Prueba | Resultado |
|---|---|---|
| 1 | 5 KPIs contra cálculo a mano | ✅ Coinciden |
| 2 | Celular sin zoom | ✅ Tarjetas de a dos |
| 3 | Incógnito pide contraseña | ✅ |
| 4 | Buscar el token en el código fuente y en GitHub | ✅ No aparece |
| 5 | Cambiar un registro en Airtable y esperar 30 min | ✅ Cambia el número |
| 6 | Elegir un mes sin datos | ✅ "Sin datos" |

## Cómo contarlo

**En una entrevista (30 segundos):**

> "Armé un tablero de cinco KPIs para el founder de una academia, cada uno con su fórmula y la decisión que dispara. Lo construí con Claude Code, lee la base en vivo con un token de solo lectura y está publicado con contraseña. Con el demo te muestro cómo en 30 segundos se ve si el mes viene bien o mal."

**Guion del Loom (2 minutos):** qué pregunta responde (15 s) · las 5 tarjetas y qué decisión dispara cada una (60 s) · el bloque "Qué mirar hoy" (20 s) · cómo se protege el dato (15 s) · cierre con lo que harías después (10 s).
