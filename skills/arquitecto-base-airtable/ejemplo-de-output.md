# Ejemplo de output · Arquitecto de Base en Airtable

> Datos ficticios. Membresía de yoga online (USD 29 por mes) que además vende un retiro anual en cuotas. Equipo: founder, CSM, administración, community manager. Hoy todo vive en una planilla y en la pasarela de pago.

---

# Base · Operación Prana · Estudio Prana Online

## 1. Mapa de tablas y vínculos

```
Miembros ──< Suscripciones ──< Cobros
    │
    └──< Interacciones (soporte, alertas, llamadas de la CSM)

Retiro: Inscripciones ──< Cuotas del retiro  (vinculadas a Miembros)
```

- **Miembros**: una persona, una vez.
- **Suscripciones**: cada alta (una persona que se va y vuelve tiene dos).
- **Cobros**: cada cobro mensual, exitoso o fallido.
- **Interacciones**: lo que la CSM hace con cada miembro.
- **Inscripciones** y **Cuotas del retiro**: el producto en cuotas, separado de la membresía.

## 2. Campos por tabla (los clave)

**Suscripciones**

| Campo | Tipo | Configuración |
|---|---|---|
| Miembro | Vínculo | a Miembros |
| Fecha de alta | Fecha | |
| Estado | Selección única | Activa · Cobro fallido · Pausada · Baja |
| Canal de origen | Selección única | Instagram · YouTube · Referido · Pauta · Sin dato |
| Cobros fallidos (últimos 60 días) | Rollup | COUNTA de Cobros con Resultado = Fallido y fecha en últimos 60 días |
| Último acceso a clases | Fecha | se carga desde la plataforma (semanal) |
| Días sin entrar | Fórmula | `DATETIME_DIFF(TODAY(), {Último acceso a clases}, 'days')` |
| Riesgo | Fórmula | `IF(OR({Cobros fallidos (últimos 60 días)} > 0, {Días sin entrar} > 21), "En riesgo", "OK")` |
| Motivo de baja | Selección única | Precio · Tiempo · No lo usaba · Cobro fallido no recuperado · Otro |

**Cuotas del retiro**

| Campo | Tipo | Configuración |
|---|---|---|
| Inscripción | Vínculo | |
| Monto | Moneda | USD |
| Vencimiento | Fecha | |
| Fecha de pago | Fecha | vacío = no pagó |
| Estado | Fórmula | `IF({Fecha de pago}, "Pagada", IF(IS_BEFORE({Vencimiento}, TODAY()), "Vencida", IF(DATETIME_DIFF({Vencimiento}, TODAY(), 'days') <= 7, "Por vencer", "Al día")))` |
| Días de atraso | Fórmula | `IF(AND({Fecha de pago} = BLANK(), IS_BEFORE({Vencimiento}, TODAY())), DATETIME_DIFF(TODAY(), {Vencimiento}, 'days'), 0)` |

## 3. Vistas

| Vista | Tabla | Filtro | Orden | Para quién |
|---|---|---|---|---|
| En riesgo esta semana | Suscripciones | Riesgo = En riesgo y Estado = Activa | Días sin entrar ↓ | CSM |
| Cobros fallidos a recuperar | Suscripciones | Estado = Cobro fallido | Fecha de alta ↑ | Administración |
| Vencen en 7 días | Cuotas del retiro | Estado = Por vencer | Vencimiento ↑ | Administración |
| Vencidas | Cuotas del retiro | Estado = Vencida | Días de atraso ↓ | Administración |
| Bajas del mes por motivo | Suscripciones | Estado = Baja, fecha en este mes | agrupado por Motivo | Founder |

## 4. Interface · "Tablero Prana"

- Arriba, 4 números: miembros activos, altas del mes, bajas del mes, cobros fallidos sin recuperar.
- Gráfico de barras: bajas del mes por motivo.
- Lista: "En riesgo esta semana", con botón para registrar una interacción.
- Acceso: founder (sólo lectura) y CSM (puede editar Interacciones).

## 5. Automatizaciones nativas

| Disparador | Acción |
|---|---|
| Suscripción pasa a "Cobro fallido" | Mail a Administración con el miembro y el monto |
| Cuota del retiro entra en "Por vencer" | Mail al miembro con el link de pago (plantilla) |
| Riesgo pasa a "En riesgo" | Crear registro en Interacciones con tipo = "Contactar" y responsable = CSM |

Lo que cruza herramientas (pasarela de pago → Airtable, plataforma de clases → Airtable) va en n8n: ver skill Diseñador de Automatizaciones.

## 6. Permisos

- Founder: lectura en la interface; editor de la base sólo si lo pide.
- CSM: editor en Suscripciones e Interacciones; sin acceso a Cuotas del retiro.
- Administración: editor en Cobros y Cuotas del retiro.
- Community manager: sin acceso a la base. Recibe la lista de "En riesgo" por la interface compartida, sin datos de pago.

## 7. Orden de construcción

- [ ] Duplicar la planilla actual como respaldo.
- [ ] Crear las 6 tablas vacías.
- [ ] Crear los vínculos (Miembros ↔ Suscripciones ↔ Cobros; Inscripciones ↔ Cuotas).
- [ ] Crear campos simples.
- [ ] Crear rollups y fórmulas (en este orden: Días sin entrar → Cobros fallidos → Riesgo).
- [ ] Cargar 10 miembros de prueba con casos raros (cobro fallido, baja y vuelta, retiro en cuotas).
- [ ] Crear las 5 vistas.
- [ ] Armar la interface.
- [ ] Crear las 3 automatizaciones y probarlas con un registro de prueba.
- [ ] Dar permisos y entrar con un usuario de cada rol.

## 8. Cómo probarla

- Un miembro con un cobro fallido de hace 10 días tiene que aparecer en "En riesgo" y en "Cobros fallidos a recuperar".
- Una cuota con vencimiento ayer y sin fecha de pago tiene que decir "Vencida" y "1" día de atraso.
- La CSM no tiene que poder ver montos del retiro.

---

¿Arrancamos a construir? Te voy guiando tabla por tabla. Hacelo primero en una copia con datos de prueba.
