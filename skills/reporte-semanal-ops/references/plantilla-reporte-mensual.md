# Plantilla del reporte mensual por áreas

> Referencia de la skill **Reporte de Ops (semanal y mensual)** (RealOps™). La estructura sirve igual para Google Sheets, Excel o una interfaz de Airtable; las fórmulas están en sintaxis de Google Sheets (en Excel son iguales, salvo que el separador de argumentos sea `;` según el idioma).

---

## Pestañas

| Pestaña | Qué tiene | Quién la carga |
|---|---|---|
| **Resumen** | Una frase · los 5 números del founder · semáforos por área · 3 decisiones | Operaciones (integra) |
| **Marketing** | Leads, agendas, gasto, costo por venta por canal y por anuncio | Marketing (o sale de la base) |
| **Setters** | Agendas, presentadas y calificadas, ventas de sus agendas, leads sin contactar | Líder comercial (o base + EOD) |
| **Closers** | Llamadas, asistencia, cierre sobre asistidas, ventas y facturado por closer | Líder comercial (o base) |
| **Cobros y finanzas** | Cobrado en 3 cubetas, facturado, morosidad al corte, vencido, comisiones | Quien cobra / finanzas |
| **Servicio** | Activos, días a acceso, participación, en riesgo, NPS, bajas, renovaciones, referidos | CSM o coordinación de servicio |
| **Operaciones** | Horas en fricción, interrupciones, automatizaciones y horas recuperadas, completitud de datos, proyectos | Operaciones |
| **Sin dato** | Cada número que falta, quién lo resuelve y para cuándo | Operaciones |
| **Diccionario** | Definición de cada número, una sola vez | Operaciones |
| **Datos** *(opcional)* | Export de la base o de la tabla de KPIs, para que las fórmulas lean de acá | Automático o pegado |

## Columnas de cada pestaña de área

| Métrica | Mes actual | Mes anterior | Variación | Tipo | Meta o alarma | Sentido | Semáforo | Fuente | Responsable | Lectura (1 línea) |
|---|---|---|---|---|---|---|---|---|---|---|

- **Tipo**: `volumen`, `tasa` o `stock`.
- **Sentido**: `sube es bueno` o `baja es bueno` (la morosidad y el costo por venta bajan es bueno).

### Fórmulas (fila 2, columnas B a H)

Variación (en % para volumen y stock, en puntos para tasas):

```
=SI(B2="";"sin dato";SI(E2="tasa";(B2-C2)*100;SI(C2=0;"—";(B2-C2)/C2)))
```

En Sheets en inglés: `=IF(B2="","sin dato",IF(E2="tasa",(B2-C2)*100,IF(C2=0,"—",(B2-C2)/C2)))`.

Semáforo contra la meta o alarma (F) según el sentido (G):

```
=IF(B2="","⚪ sin dato",IF(G2="sube es bueno",IF(B2>=F2,"🟢",IF(B2>=F2*0.9,"🟡","🔴")),IF(B2<=F2,"🟢",IF(B2<=F2*1.1,"🟡","🔴"))))
```

(En Sheets en español: `SI` en lugar de `IF` y `;` en lugar de `,`.) El 10 % de tolerancia es un default: ajustalo por métrica con el founder.

## La pestaña Resumen

```
REPORTE MENSUAL DE OPS · [mes] · corte [último día]
En una frase: [qué pasó con la plata]

Los 5 números del founder           Mes      Anterior   Variación   Estado
Cobrado total (3 cubetas)           …        …          …           🟢/🟡/🔴
Facturado                           …        …          …
Morosidad al corte                  …        …          … pts
Costo por venta (pauta)             …        …          …
[número de servicio u operaciones]  …        …          …

Semáforo por área:  Marketing 🔴 · Setters 🟡 · Closers 🟢 · Cobros 🔴 · Servicio ⚪ · Operaciones 🟡

Decisiones del mes (con responsable y fecha):
1. …
2. …
3. …
```

Los 5 números del founder se eligen una vez (con **Analista de KPIs**, modo 2) y no cambian todos los meses.

## Si es un dashboard en vez de planilla

Misma lógica, en una página por área: arriba los números grandes con el mes anterior y el semáforo; abajo el detalle (por canal, por setter, por closer); al costado, la lectura de una línea. Filtros públicos por mes y por canal. En Airtable, la página tipo "dashboard" de Interfaces; para un tablero web, skill **Dashboard con Vibe Coding**.

## Reglas de la planilla

- **Nadie escribe en Resumen**: todo sale por fórmula de las pestañas.
- Lo que se puede leer de la base, se lee (pestaña Datos); lo manual lo carga el responsable del área, no operaciones.
- Una pestaña vacía dice "sin dato · no entregado". No se completa.
- El mes anterior se copia **como valores** al cerrar el mes, para que no cambie si alguien corrige la base después.
