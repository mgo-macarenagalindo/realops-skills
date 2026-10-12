# Antipatrones · los errores que más aparecen en bases reales

> Referencia de la skill Arquitecto de Base en Airtable (RealOps™). Salen de revisar bases de infonegocios en uso (entre ellas las bases de muestra de MG Operations) y de prácticas comunes de la comunidad de Airtable. Usala en modo **mejorar**: recorré la base con esta lista y anotá cada hallazgo con su arreglo.

| # | Antipatrón | Cómo se ve | Por qué duele | Arreglo |
|---|---|---|---|---|
| 1 | **Personas como texto o selección** | "Closer", "Setter", "Coach" como desplegable en 5 tablas, cada una con su lista | Gente que se fue sigue en las listas; un espacio de más rompe un reporte; cada alta obliga a tocar 5 desplegables | Tabla Equipo + vínculo limitado a la vista "Activos" |
| 2 | **Lo que se repite, en columnas** | "Fecha 2da cuota", "Monto 3ra cuota"… o un campo por mes ("Enero: proyección") | No escala, las fórmulas se vuelven enormes, y si el año está escrito en la fórmula deja de funcionar en enero | Tabla hija (una fila por cuota, por sesión, por reporte) y vistas agrupadas por mes |
| 3 | **Dos tablas para lo mismo** | Una tabla de "Ingresos" vieja conviviendo con la nueva; dos tablas de KPIs de marketing | Dos números distintos para la misma pregunta | Una fuente; la otra se archiva |
| 4 | **Dos pares de vínculos entre las mismas tablas** | "Link to Alumnos" y "Alumnos (CRM)" en Deals | Cada uno ve la mitad de los datos | Elegir uno, pasar los datos, ocultar el otro |
| 5 | **Reglas de negocio escondidas en fórmulas** | Fórmula de comisión con nombres de personas y porcentajes escritos | Nadie la puede revisar; cambiar una regla es reescribir la fórmula en varias tablas | Porcentajes en la tabla de Equipo (o una tabla de Reglas), la fórmula los lee por lookup |
| 6 | **Estados que se mueven a mano y deberían calcularse** | "Estado de la cuota: Pagó 2° cuota" en una selección; "Vencida" cargado como texto | Queda viejo al día siguiente | Fórmula sobre fechas |
| 7 | **Casillas que cuentan cosas** | "Agendó llamada", "Pasó a closer" tildadas a mano | Se olvidan; no coinciden con los registros | Conteo de registros vinculados |
| 8 | **Fórmula de normalización gigante** | El canal se reconstruye con 15 condiciones sobre nombres de calendarios | Un calendario nuevo cae a "otro" sin aviso | Lista cerrada cargada al inicio + fuente cruda guardada aparte; si la fórmula queda, último caso = "Sin canal" |
| 9 | **Claves que dan error** | La clave "mes \| canal" sale con error cuando falta una fecha | Esos registros no entran al reporte y nadie se entera | Vista de control "Sin fecha" o "Clave con error" y regla de carga |
| 10 | **Lookups "por si acaso"** | 40 lookups de vuelta en una tabla | La tabla se vuelve ilegible y lenta | Solo los que usa una vista, interface o fórmula |
| 11 | **Restos** | "Copia de…", "Table 13", campos marcados con error, campos 100 % vacíos | Confunden y a veces alimentan algo sin que se sepa | Ocultar como `[ARCHIVO]`, borrar al mes si nada los usa |
| 12 | **Varios valores en una celda** | Todos los links de grabación del día pegados en cada sesión | No se puede auditar una por una | Un registro por cosa, un link por registro |
| 13 | **Automatización disparada por "cualquier cambio"** | "Cuando se actualiza un registro" sin filtro | Corre de más (y gasta corridas del plan) o entra en bucle | Disparar por entrar a una vista con filtro estrecho o por un campo de guarda |
| 14 | **La base en una cuenta personal** | Creada con el mail de alguien del equipo, en plan Free | Si esa persona se va, se va la base | Pasar la base (o duplicarla) a un espacio del negocio |
| 15 | **Formularios y automatizaciones a nombre de alguien que se fue** | El formulario que crea los leads es de una ex empleada | Cuando cierra su cuenta, deja de entrar todo | Inventario de dueños; recrear en una cuenta del negocio |
| 16 | **Monedas mezcladas** | Pesos y dólares sumados en el mismo campo | Totales sin sentido | Campo en moneda real + campo USD con el tipo de cambio del mes |
| 17 | **Selecciones con tipeos** | "Supendido" y "Suspendido", la misma opción dos veces | Filtros y conteos que fallan | Unificar opciones (renombrar, no borrar) |

## Cómo reportarlo

Una fila por hallazgo: tabla · campo · antipatrón (#) · evidencia (cuántos registros afecta) · riesgo · arreglo · prioridad (arreglar ya / este mes / prolijidad).
