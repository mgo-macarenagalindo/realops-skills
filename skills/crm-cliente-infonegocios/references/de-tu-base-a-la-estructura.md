# De tu base a la estructura estándar

> Referencia de la skill CRM de Cliente para Infonegocios (RealOps™). Cómo leer un CRM que ya existe y llevarlo a la estructura estándar **sin rehacerlo y sin perder datos**.

## 1. Cómo leer lo que hay (en este orden)

1. **Lista de tablas** y, para cada una, "una fila = …". Si no podés completar la frase, la tabla mezcla dos cosas.
2. **Personas:** ¿setter, closer y coach son vínculos a una tabla de equipo o selecciones con nombres escritos? ¿Hay gente que ya no está?
3. **Plata:** ¿dónde está la facturación, dónde el cash, dónde las cuotas? ¿Hay **dos tablas** que registran los mismos cobros?
4. **Cuotas esperadas:** ¿columnas en el deal, tabla aparte o nada? ¿El estado de la cuota es fórmula o se mueve a mano?
5. **Canal:** ¿se carga al inicio o se reconstruye con una fórmula larga? ¿Qué pasa cuando no hay dato?
6. **Claves de KPIs:** ¿qué tablas tienen clave mes | canal o persona | mes? ¿Hay tablas de KPIs duplicadas?
7. **Restos:** campos "Copia de…", tablas sin nombre ("Table 13"), campos marcados con error, lookups que nadie mira.

Si al leer aparecen automatizaciones, interfaces o integraciones que no sabés qué hacen, pará y pasá por **Auditor de Base Heredada**.

## 2. Las dos formas que más aparecen

### Forma 1 · Centrada en la agenda
```
Leads (setting) ··· (sin vínculo, solo una casilla "Agendó")
Agendas (tabla enorme: triage + closer + formulario + UTMs + 40 lookups de vuelta) ──< Deals + Reservas ──< Cuotas cobradas
KPIs mensuales marketing ×2 (duplicadas) · Data global · KPIs del equipo · EOD de todo el equipo en una tabla
Finanzas (ingresos cargados a mano, una columna por moneda) · Ventas low ticket · Candidatos · Procesos
```
**Lo bueno:** separa setting de agendas; registra triage y closer; tiene ventas de checkout aparte.
**Lo que falla:** Leads y Agendas no están vinculados (no se puede medir al setter de punta a punta) y no hay números diarios por setter; personas como selección; cuotas proyectadas en columnas; Finanzas duplica la carga de los ingresos; KPIs duplicadas y campos "Copia de…".

### Forma 2 · Con servicio
```
Oportunidades (importadas del CRM de mensajería) ──< Deals + Reservas ──< Cuotas cobradas ──> Finanzas (por automatización)
                                                         └── Clientes (CRM de servicio) ──< Onboarding
Ingresos (sistema anterior, en paralelo) · Nómina (con capacidad por coach) · EOD por rol ──> KPIs del equipo · KPIs globales (mes | canal)
```
**Lo bueno:** el flujo Oportunidades → Deals → Cuotas → Finanzas; dos bloques de dinero (USD y moneda real); Finanzas generada por automatización; Nómina con capacidad; EOD por rol; clave mes | canal.
**Lo que falla:** el setter no queda vinculado en la oportunidad (el setting existe como números del EOD, que **cumple el mínimo estándar**, pero no se puede contrastar contra las agendas que dio cada setter); una tabla de ingresos vieja convive con la nueva (dos verdades); 12 fórmulas de proyección por mes; personas en desplegables además de la Nómina; comisiones con nombres de personas adentro de la fórmula; dos pares de vínculos entre Deals y Clientes.

## 3. Tabla de cambios (plantilla)

| Tabla hoy | Queda / cambia / se suma / se archiva | Qué se hace | Por qué |
|---|---|---|---|
| [ej. Leads] | Cambia | Se vincula con Oportunidades; Setter pasa a vínculo → Equipo | Medir al setter de punta a punta |
| [ej. Closers] | Cambia | Se renombra Equipo, suma setters, coaches, roles, estado y % | Una sola tabla de personas |
| — | Se suma | Cuotas programadas | Morosidad por cuota |
| [ej. Ingresos viejos] | Se archiva | Se oculta como `[ARCHIVO]`; no se carga más | Dos tablas de cobros = dos verdades |

**Cómo se cambia sin romper:**
1. Duplicá la base (o exportá cada tabla a CSV) antes de tocar.
2. Campo nuevo al lado del viejo; completalo; compará los dos con números concretos (ej.: cobrado de septiembre por las dos vías).
3. Recién cuando coinciden, ocultá el viejo con el prefijo `[ARCHIVO]`. Se borra un mes después, si nadie lo extrañó y ninguna automatización, interface o integración lo usa.
4. Si cambiás un campo que dispara una automatización o que lee un reporte por nombre, cambialo **primero** ahí.

## 4. Señales de alerta y su arreglo

| Señal | Arreglo |
|---|---|
| Persona como selección única o texto en varias tablas | Vínculo → Equipo, limitado a "Activos"; cargar a los que no están (como inactivos) antes de migrar |
| Gente que se fue sigue asignada (leads sin contactar, formularios a su nombre) | Marcar inactiva, reasignar abiertos, revisar dueños de formularios, automatizaciones y cuentas |
| Estado de cuota cargado a mano | Fórmula en Cuotas programadas; comparar con el estado viejo antes de ocultarlo |
| Cuotas en columnas + fórmulas de proyección por mes | Tabla Cuotas programadas y una vista agrupada por mes de vencimiento |
| Dos tablas registran cobros | Una sola fuente (Deals + Cuotas cobradas); la otra se archiva |
| Finanzas con ingresos cargados a mano | Automatización desde Deals y Cuotas; Finanzas a mano solo para egresos |
| Comisión con nombres o porcentajes escritos en la fórmula | % en Equipo, la fórmula los lee por lookup |
| Fórmula de canal con decenas de condiciones | Canal en lista cerrada al inicio; la fuente cruda se guarda aparte. Si se mantiene la fórmula, que termine en "Sin canal" |
| Clave de KPI con error cuando falta una fecha | Vista de control "Sin fecha" y regla de carga |
| Dos pares de vínculos entre las mismas tablas | Elegir uno, pasar los datos, ocultar el otro |
| Campos "Copia de…", tablas sin nombre, campos 100 % vacíos | Ocultar como `[ARCHIVO]` y borrar al mes |
| Decenas de lookups traídos "por si acaso" | Dejar solo los que usa una vista, una interface o una fórmula |
| Casilla "Agendó" o "Pasó a closer" cargada a mano | Conteo de oportunidades vinculadas |
| Setting sin ningún registro (solo se pregunta por chat) | Setting diario por formulario: los cuatro números por día y por setter |
| Base en Free cerca del límite | Ver `plan-free-airtable.md`: alternativa manual de cada pieza y cuándo pagar |
