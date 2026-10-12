# Casos de uso · Auditor de Base Heredada

Cinco situaciones de infonegocio donde esta skill te salva de romper algo el primer día. Negocios y nombres ficticios.

---

## 1. Primera semana en un negocio nuevo

**La situación.** Entrás como operaciones a una mentoría high ticket. La base de Airtable la armó una persona que se fue hace dos meses. Tiene 9 tablas, 14 automatizaciones y 11 Zaps, y nadie sabe cuál se usa. El founder te pide "ordenarla".

**Qué le pasás.** La lista de tablas y campos (capturas o lectura por el conector), las automatizaciones de la base, el relevamiento de Zapier (con el pedido de Cowork en modo lectura que trae la skill) y la página del Notion donde alguien anotó "las automatizaciones" hace un año.

**Qué te devuelve.** El cruce entre lo que dice el Notion y lo que hay, el mapa de cómo entra, viaja y sale cada dato, el inventario de automatizaciones con su cuenta dueña y sus webhooks, el informe por tabla con lo alto y medio arriba y lo bajo en un anexo, y el plan en orden. Con la lista de lo que **no** se toca, para mostrársela al founder antes de que te pida borrar algo.

**Por qué sirve.** Te deja entrar con criterio y no con miedo. Es la clase del 27/05 hecha método.

---

## 2. "Sacá a la que se fue" (sin cortar nada)

**La situación.** En un programa de 6 meses, el founder te pide que saques de todas las herramientas a una setter que se fue. Ella armó el formulario de aplicación y el Zap que pasa los leads a Airtable.

**Qué le pasás.** La lista de accesos que tenga el negocio y lo que sepas de las integraciones.

**Qué te devuelve.** El orden correcto: qué integraciones dependen de su cuenta (el formulario, el Zap, la conexión de Airtable dentro del Zap), cómo pasarlas a una cuenta del negocio y probarlas, y **recién después** sacarle el acceso. Sacar un acceso no borra datos y va primero; lo que no puede pasar es que el Zap se corte en silencio.

**Por qué sirve.** La limpieza de accesos es urgente, pero hecha sin inventario deja al negocio sin leads un fin de semana.

---

## 3. "¿Qué hace esta fórmula?"

**La situación.** En el CRM de servicio hay un campo "Riesgo" con una fórmula de 6 líneas llena de `IF` anidados. Marca a la mitad de los alumnos en rojo y nadie sabe por qué.

**Qué le pasás.** La fórmula copiada, un CSV de 10 filas (con los nombres reemplazados) y qué se supone que mide.

**Qué te devuelve.** La explicación línea por línea, la prueba contra 3 filas con la cuenta a la vista, qué automatización usa ese resultado (el aviso al CSM se dispara con "Riesgo = Alto") y el hallazgo: compara contra "Activa" cuando en la base dice "Activo". Más la fórmula corregida, para probarla en un campo nuevo antes de reemplazar la vieja.

**Por qué sirve.** No tocás una fórmula que no entendés. Y cuando la tocás, sabés qué dispara.

---

## 4. Base limpia para el año nuevo

**La situación.** Una membresía lleva dos años en la misma base: 40.000 registros, reportes diarios desde el primer día, tablas por mes. Se pone lenta y el plan de Airtable ya no alcanza.

**Qué le pasás.** La estructura actual, qué se usa hoy y las automatizaciones que tocan la base.

**Qué te devuelve.** Qué se migra (clientes activos, KPIs mensuales, finanzas, seguimientos abiertos), qué queda como archivo, la lista de "qué automatización apunta adónde" antes y después del cambio, qué semana conviene hacerlo y el aviso al equipo. El diseño de la base nueva lo deriva a Arquitecto de Base en Airtable.

**Por qué sirve.** Empezás de cero sin perder la historia que importa ni dejar un Zap escribiendo en la base vieja. Clase del 01/09.


---

## 5. "Pensé que eran tres o cuatro" (automatizaciones en muchas cuentas)

**La situación.** En un programa de 6 meses, la coordinadora relevó "todo lo que se mueve solo" y aparecieron 15 automatizaciones en 9 herramientas: Zaps de una exsetter, un Make de la agencia que ya no trabaja con el negocio, automatizaciones nativas en una base con plan gratis. Parte la vio ella; parte se la contaron por captura.

**Qué le pasás.** Su inventario tal cual, el esquema de la base y los CSV.

**Qué te devuelve.** Cada fila con su nivel de confianza (visto, visto con el dueño, reconstruido); el mapa por evento (el pago dispara cinco automatizaciones en tres cuentas: van a un solo flujo); los campos que escriben varias manos (y la trampa de pasarlos a fórmula); la falla que corre "en verde" sin escribir nada; los datos de leads que siguen saliendo a cuentas de gente que se fue; el día en que el plan gratis se cortó y qué dejó de salir desde entonces, con la alternativa manual y cuándo conviene pagar; y el orden para revocar accesos sin cortar el alta de leads.

**Por qué sirve.** Pasa de "hay un Zap" a un mapa que se puede ordenar sin romper nada.
