# Ejemplo de output · Retención, Upsells y LTV

> Datos ficticios. "Consulta Llena" es una mentoría grupal de 4 meses para nutricionistas: USD 1.800 contado o 3 cuotas de USD 650, 90 alumnos activos, una coordinadora y una CSM. Usan Airtable, Zapier (plan básico), Circle y WhatsApp. No hay nada para después del programa. Lo pide Lucía, la operativa estratégica del negocio. Camino A.

---

# Plan de LTV · Consulta Llena · 12 de octubre

## El LTV hoy

| Parte del LTV | Cálculo | Por alumno |
|---|---|---|
| Programa inicial (cobrado) | 55 % contado × USD 1.800 + 45 % en cuotas × USD 1.950 × 92 % cobrado | USD 1.797 |
| Renovación | No existe oferta: 0 % × 0 | USD 0 |
| Upsell o cross-sell | No existe | USD 0 |
| Referidos | 9 ventas por referido en el trimestre ÷ 90 alumnos × USD 1.800 | USD 180 |
| **LTV hoy** | | **≈ USD 1.977** |

El 92 % cobrado de las cuotas sale de la tabla de cuotas al 10/10. Lo que viene de servicio (referidos) es el 30 % de las ventas del trimestre, sin que nadie lo empuje.

## Dónde se pierde valor

1. **40 alumnos terminan en los próximos 90 días y no tienen a dónde seguir.** 15 en octubre, 12 en noviembre y 13 en diciembre. Hoy la tasa de renovación es 0 % por diseño, no por falta de interés: 6 de ellos ya preguntaron en la comunidad si pueden "seguir en los en vivo".
2. **Los referidos cierran 6 veces más que los anuncios y nadie sabe quién refirió.** De 20 leads referidos cerraron 9 (45 %); de 130 leads de anuncios, 9 (7 %). No hay campo "referido por", así que no se puede agradecer ni repetir.
3. **6 de los 40 que terminan están en rojo** (más de 21 días sin asistir o una cuota vencida). Si se les ofrece renovar sin rescatarlos antes, la oferta les llega como un reclamo.

## Las 3 palancas elegidas y por qué

1. **Ventana de renovación** · la plata más cercana: 15 alumnos terminan este mes.
2. **Referidos con sistema** · ya funciona sin empuje; registrarlo y pedirlo en el momento justo lo multiplica.
3. **Semáforo de riesgo con rescate** · protege lo vendido y prepara a los rojos para la renovación.

Quedan para el trimestre que viene: encuesta de mitad de camino con NPS y casos de éxito en la tabla.

## El sistema, ficha por ficha

### 1 · Ventana de renovación (semiautomático)

- **Qué número mueve:** tasa de renovación por cohorte.
- **Disparador:** "días a fin de contrato" = 45 (fórmula sobre la fecha de fin).
- **Datos:** fecha de fin, semáforo, asistencias, micro-objetivos cumplidos, cuotas al día (tabla Alumnos).
- **Pasos:** cada lunes, Zapier arma en Airtable la vista "Renovaciones de la semana" y manda a la CSM por WhatsApp el resumen con el link. La CSM agenda una llamada de 20 minutos con cada verde y amarillo. En la llamada: qué logró (con sus números), qué le falta y la oferta para seguir. Los rojos pasan antes por el rescate (ficha 3).
- **Quién actúa:** la CSM; Lucía revisa la vista los lunes.
- **Mensaje base:** "Hola, Ana. Te quedan 6 semanas de programa y quiero que las aprovechemos. ¿Hacemos 20 minutos esta semana para ver qué lograste y qué te falta?"
- **Oferta:** "Consulta Llena · Continuidad", encuentro grupal semanal + comunidad, mensual. **[SUPUESTO: USD 120 por mes con mínimo de 3 meses, lo decide la founder]**.
- **Registro:** la renovación entra como **venta nueva** con naturaleza "Renovación", no como cuota 4.
- **Costo:** unas 4 tareas de Zapier por semana, 17 por mes.
- **Cómo se prueba:** con 3 alumnos de prueba con fechas de fin a 44, 45 y 46 días.

### 2 · Referidos con sistema (automático + una regla)

- **Qué número mueve:** ventas por referido por mes.
- **Disparadores:** día 21 desde el acceso; micro-objetivo del mes 2 cumplido.
- **Datos:** campo nuevo "Referido por" en Leads (el formulario de aplicación pregunta "¿quién te recomendó?"), fecha de acceso, micro-objetivos.
- **Pasos:** mail y WhatsApp automáticos con el pedido y el link de aplicación con UTM "referido". Cuando un referido compra, se avisa a la coordinadora para dar el beneficio.
- **Regla del beneficio:** **[SUPUESTO: un mes de Continuidad gratis o USD 100 por cada referido que compra, lo decide la founder]**.
- **Costo:** unas 30 tareas por mes.
- **Cómo se prueba:** una aplicación de prueba con "¿quién te recomendó?" completo.

### 3 · Semáforo de riesgo con rescate (semiautomático)

- **Qué número mueve:** rojos rescatados en 14 días.
- **Regla (SOP):** rojo = más de 21 días sin asistir o una cuota vencida; amarillo = 14 a 21 días sin asistir; verde = el resto.
- **Pasos:** fórmula del semáforo en Alumnos; vista "En rojo" con la nota del último contacto; aviso diario a la CSM con los rojos nuevos. La CSM llama en 48 horas. Si es por cuota, pasa a la regla de cobranza de la coordinadora.
- **Costo:** unas 22 tareas por mes.

## Lo que le falta a la tabla de clientes

Fecha de fin de contrato (hoy se calcula a mano) · semáforo con nota · micro-objetivo del mes y si se cumplió · referido por (en Leads) · motivo de baja · naturaleza del ingreso (en Ventas).

## Plan 30-60-90 y cuánto puede sumar

| Palanca | Cuándo | Cálculo | Conservador | Probable |
|---|---|---|---|---|
| Ventana de renovación | Arranca el 19/10 con la cohorte de octubre | 40 alumnos × tasa × USD 120 × 3 meses | 10 % → 4 × USD 360 = **USD 1.440** | 20 % → 8 × USD 360 = **USD 2.880** |
| Referidos con sistema | Arranca el 26/10 | Ventas extra por mes × 3 meses × USD 1.800 − beneficio | +1 por mes → **USD 5.100** | +2 por mes → **USD 10.200** |
| Rescate de rojos | Arranca el 19/10 | Rojos con cuota vencida que se regularizan × USD 650 | 2 → **USD 1.300** | 4 → **USD 2.600** |
| **Total en 90 días** | | | **≈ USD 7.840** | **≈ USD 15.680** |

Todo con lo cobrado. La renovación sigue sumando después de los 90 días si el mínimo es de 3 meses y el alumno sigue.

## Cómo se mide cada mes

1. Tasa de renovación de la cohorte que terminó.
2. Ventas por referido y su tasa de cierre.
3. Alumnos en rojo y rojos rescatados.
4. Parte de las ventas nuevas que vino de servicio (renovación + upsell + referido).
5. LTV por alumno, con lo cobrado.

## Para confirmar

- **Precio y formato de la Continuidad** (USD 120 por mes, mínimo 3 meses; es el 6,7 % del ticket, dentro del rango **ORIENTATIVO** de 5 % a 10 %): lo decide la founder antes del 16/10.
- **Beneficio por referido**: la founder.
- **Las tasas de 10 % y 20 %** son escenarios **ORIENTATIVOS** (referencia de la biblioteca, no de una clase): se reemplazan por la real después de la cohorte de octubre.
- **Que Zapier entre en el plan básico** con las 70 tareas nuevas por mes: quien administra la cuenta.
- **Comisión de la CSM por renovación**: pasar por la skill Esquema de Pago y Comisiones.

---

¿Pasamos las tres fichas a Diseñador de Automatizaciones para construirlas? ¿Te armo el guion de la llamada de renovación y los mensajes de referidos y de rescate?
