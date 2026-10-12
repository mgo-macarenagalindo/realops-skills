# Ejemplo de output · Rentabilidad por Anuncio

> Datos ficticios. Mentoría de 4 meses para psicólogos que quieren armar su consultorio online: USD 1.800 en un pago o 3 cuotas de USD 650. Pauta en Meta: una campaña a landing con video y agenda (4 creativos en frío + 1 de retargeting) y una campaña para ganar seguidores. UTMs con `utm_content` igual al nombre de cada anuncio (convención de la skill UTMs de Punta a Punta).

**Lo que pegó la persona:** el export de Meta de septiembre por anuncio, la tabla de agendas y ventas de Airtable con `utm_content`, y el pedido: "el trafficker quiere duplicar el anuncio del testimonio porque es el que más agendas trae".

---

# Rentabilidad por anuncio · Mentoría para psicólogos (caso ficticio) · septiembre 2026

## En una frase

El anuncio del testimonio trae el 35 % de las agendas y una sola venta; el del mito trae el 10 % de las agendas y 4 ventas. Duplicar el testimonio sería escalar el que peor vende.

## Inversión separada por tipo de campaña

| Tipo | Gasto USD | Cómo se mide |
|---|---|---|
| Conversión · landing con video | 5.000 | Agendas, ventas y cash (tabla de abajo) |
| Seguidores | 1.000 | 820 seguidores nuevos → **USD 1,22 por seguidor**. Su retorno se lee en las agendas con `medium=bio`: 18 en septiembre contra 11 en agosto |
| **Total** | **6.000** | El retorno global no se calcula sumando las dos |

## Tabla por anuncio (campaña de conversión)

Cash = cash nuevo a la fecha (pagos únicos y primeras cuotas). Las cuotas 2 y 3 de las 4 ventas en cuotas (4 × 2 × 650 = USD 5.200 más, si se cobran) no están incluidas.

| Anuncio | Gasto | Leads | Agendas | Asistidas | Ventas | Cash | Costo por agenda | CAC | Cash por agenda | Retorno |
|---|---|---|---|---|---|---|---|---|---|---|
| ad-testimonio-01 | 1.400 | 210 | 42 | 18 | 1 | 1.800 | 33,3 | 1.400 | 42,9 | 1,29 |
| ad-errores-02 | 1.200 | 160 | 30 | 14 | 2 | 2.450 | 40,0 | 600 | 81,7 | 2,04 |
| ad-mito-03 | 600 | 50 | 12 | 10 | 4 | 6.050 | 50,0 | 150 | 504,2 | 10,08 |
| ad-carrusel-04 | 1.000 | 120 | 20 | 8 | 0 | 0 | 50,0 | — | 0 | 0 |
| ad-retarg-01 | 800 | 40 | 16 | 12 | 3 | 3.100 | 50,0 | 266,7 | 193,8 | 3,88 |
| **Total atribuido** | **5.000** | **580** | **120** | **62** | **10** | **13.400** | **41,7** | **500** | **111,7** | **2,68** |

Detalle del cash: errores = 1 en un pago + 1 en cuotas (1.800 + 650) · mito = 3 en un pago + 1 en cuotas (5.400 + 650) · retargeting = 1 en un pago + 2 en cuotas (1.800 + 1.300).

## Lo que no se puede atribuir

- **14 agendas y 2 ventas (USD 2.450) sin `utm_content`**: el 10,4 % de las 134 agendas de pauta. Probable causa: un link de la landing sin UTM en el comentario fijado de un anuncio. No se reparten entre anuncios.
- Si se atribuyeran, el retorno global no cambiaría la decisión: la diferencia entre anuncios es mucho más grande que esa fila.

## Decisiones

| Anuncio | Decisión | Por qué | Plazo | Plan B |
|---|---|---|---|---|
| ad-mito-03 | **Escalar** (de 600 a 1.200) | 4 ventas de 12 agendas; 10 de 12 asistieron. **Muestra chica:** 4 ventas son una señal, no una conclusión | 4 semanas | Si el retorno baja de 3 con el doble de gasto, volver a 600 y probar una variante del mismo ángulo |
| ad-testimonio-01 | **Revisar** (bajar a 700) | Trae el 35 % de las agendas, asiste el 43 % y vendió 1. Ocupa la agenda de los closers | 4 semanas | Si no supera 1 venta cada 20 agendas, cortar |
| ad-errores-02 | Mantener | Retorno 2,04, en línea con el total | 4 semanas | — |
| ad-retarg-01 | Mantener | Retorno 3,88; público que ya conoce la marca | — | — |
| ad-carrusel-04 | **Cortar** | 1.000 de gasto, 20 agendas, 0 ventas | Ya | Reusar el presupuesto en el mito |

Presupuesto de octubre con estas decisiones: 1.200 + 700 + 1.200 + 800 + 0 = **3.900** en conversión (antes 5.000), más 1.000 de seguidores.

## Para marketing

- El **ángulo del mito** ("lo que te dijeron de cobrar online es falso") trae menos gente pero más decidida: el closer la marcó como calificada alta en 8 de las 10 asistidas.
- El **testimonio** atrae a quien todavía no decidió cambiar: muchas preguntas sobre "si sirve para mí". Puede funcionar mejor en retargeting que en frío.
- El **carrusel** no llegó a ninguna venta: no repetir el formato en frío para esta oferta.

## Lo que falta para leer mejor

1. **Calificación del closer en todas las agendas:** hoy está cargada en 41 de 62 asistidas.
2. **Cortes por país y edad** del export de Meta, cruzados con ventas: con 10 ventas todavía no alcanza para leerlos.
3. **Cuotas 2 y 3** de las ventas en cuotas: se suman al cierre de noviembre para ver el retorno completo.
4. **El link sin UTM:** corregirlo esta semana (14 agendas sin atribuir).

---

**Mensaje para el equipo de tráfico (opcional):**

> Revisamos septiembre por anuncio, cruzando con ventas del CRM. Propuesta para octubre: subir el del mito a 1.200, bajar el testimonio a 700, cortar el carrusel y mantener errores y retargeting. Total de conversión: 3.900. Necesitamos: UTM en el comentario fijado de cada anuncio (hay un link sin UTM) y el export por país y edad a fin de mes. Revisamos de nuevo en 4 semanas.
