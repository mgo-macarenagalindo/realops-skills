# Para qué sirve cada dato · cómo aprovechar la tabla de KPIs

> Referencia de la skill **Tabla de KPIs Globales en Airtable** (RealOps™). Sale de las clases de *Decidí con datos* y de los reportes que MG Operations armó para clientes a partir de estas mismas tablas (anonimizados). Si sólo construís el tablero y no sabés leerlo, el dueño ve números; si sabés leerlo, ve decisiones.

**La secuencia que te vuelve valiosa:** construir → analizar → accionar (clase 04/06). El tablero es el primer paso. Lo que se paga es llevarle al dueño **las 3 o 4 variables que de verdad mueven el negocio** y animarte a decir qué hay que cambiar.

> **Las alarmas de este archivo son criterios orientativos de RealOps™** para saber dónde mirar primero. No son metas de la industria: después de 2 o 3 meses de datos, ajustalas a la historia del negocio.

---

## 1 · Campo por campo

### Agendas totales (por canal)
- **Pregunta que responde:** ¿cuánto volumen de conversaciones de venta genera cada canal?
- **Le sirve a:** marketing (dónde poner contenido o pauta), founder (si la agenda está llena o vacía).
- **Cuándo mirarlo:** cada semana. **Alarma (orientativa):** un canal que duplica agendas sin que suban las ventas; casi siempre es un anuncio o un setter que llena la agenda de gente que no puede comprar.
- **Error típico:** celebrar la agenda llena. Una agenda llena de gente que no compra le roba horas a los closers.

### Asistidas · No show · Canceladas → Asistencia
- **Pregunta:** ¿la gente que agenda llega a la llamada?
- **Le sirve a:** líder comercial y operaciones (recordatorios), setters.
- **Cuándo:** semanal. **Alarma (orientativa):** debajo de 50 %, o una caída en un solo canal.
- **Cómo leerlo:** si cae en todos los canales a la vez, es del sistema (recordatorios, herramienta de agenda, zoom ocupado). Si cae en uno solo, es la calidad de ese canal o de quien agenda. Separar no-show de cancelación: el no-show se ataca con recordatorios; la cancelación, con política y confirmación.

### Cierres → Cierre sobre asistidas y cierre sobre agendas
- **Pregunta:** sobre asistidas, ¿el closer cierra cuando tiene a la persona? Sobre agendas, ¿el canal y el setter traen gente que compra?
- **Le sirve a:** líder comercial (closers), marketing y setters (canal).
- **Cómo leerlo:** **miralos juntos.** Si sobre asistidas sube y sobre agendas baja, se abrió una "tijera": por ejemplo, el dueño tomó todas las llamadas, cierra mejor a quien se presenta pero no llega a sostener la asistencia. Mismo cambio, dos efectos.
- **Alarma (orientativa):** cierre sobre agendas debajo de 10 % en un canal con gasto.

### Facturación USD vs Cash total USD
- **Pregunta:** ¿lo que se vendió entra a la cuenta?
- **Le sirve a:** founder y contador.
- **Cuándo:** cuando el dueño dice "este mes facturamos X". Casi siempre está mirando lo vendido (con cuotas futuras), no lo cobrado.
- **Cómo usarlo:** en el tablero, **cash como número principal** y facturado al lado. Que no coincidan es normal: el dashboard comercial cuenta ventas del mes; el financiero, pagos reales (clase 14/05).

### Reservas · Nuevos cierres · Cuotas → Cash nuevo vs cuotas
- **Pregunta:** ¿el negocio crece por adquisición o vive de la cartera?
- **Le sirve a:** founder.
- **Cómo leerlo:** si más de la mitad del cash (umbral orientativo) viene de cuotas de ventas anteriores (y renovaciones) varios meses seguidos, el mes se ve sano pero la adquisición está frenada. La cartera se agota si no entra gente nueva y no se escala poniendo más plata.
- **Error típico:** un mes "récord" que es cobranza de cuotas viejas, y una decisión de duplicar pauta tomada sobre ese número.

### Cash nuevo por agenda
- **Pregunta:** ¿cuánta plata trae cada llamada de este canal?
- **Le sirve a:** marketing y founder para comparar canales con tickets o formas de pago distintas.
- **Cuándo:** al repartir presupuesto o esfuerzo entre canales.

### Gasto · Costo por agenda · Costo por venta · Retorno
- **Pregunta:** ¿qué anuncio trae clientes que pagan, y cuánto cuesta cada uno?
- **Le sirve a:** marketing, trafficker, founder.
- **Cómo leerlo:** el costo por agenda lo da la plataforma; **el que decide es el costo por venta**, que sólo se ve cruzando con la base. El anuncio más barato por agenda puede no vender nada.
- **Cuándo:** antes de escalar o duplicar un anuncio; en ventanas de 6 u 8 semanas, no de una.
- **Cuidado con la atribución:** la UTM guarda el último link. Hay gente que vio un anuncio y entró por otro lado. Decí qué no se puede atribuir en lugar de mostrar "este canal vendió 0" como sentencia.

### Sin canal
- **Pregunta:** ¿podemos confiar en la atribución?
- **Le sirve a:** operaciones.
- **Alarma (orientativa):** crece mes a mes, o pasa del 10 % de las agendas. Es tracking roto, no un canal.

### Vista Vencidas (fuera de la tabla, pero va al lado)
- **Pregunta:** ¿se cobran las cuotas? ¿quién debe y desde cuándo?
- **Le sirve a:** quien cobra, founder.
- **Cuándo:** cada lunes, con "vence en los próximos 7 días" al lado.

---

## 1b · Primer nivel de setters, servicio y operaciones

Estos números no van en la tabla mes | canal (se leen por persona o al corte), pero el líder de cada área los pide al lado. Acá, lo que tenés que saber leer; el diagnóstico de causas es de **Analista de KPIs**.

### Setters (desde el setting diario: una fila por setter y por día)
- **Calificados sobre conversaciones** · *Pregunta:* ¿el setter filtra? · *Le sirve a:* líder comercial. · *Cómo leerlo:* si da casi 100 %, no está filtrando: todo "califica". Contrastalo con la calificación del closer.
- **Agendados sobre calificados** · *Pregunta:* ¿convierte la conversación en llamada? · *Alarma (orientativa):* cae dos semanas seguidas.
- **Agendados declarados contra oportunidades en el CRM** · *Pregunta:* ¿lo que reporta es lo que pasó? · *Alarma:* cualquier diferencia que se repite. Si el setter cobra por agenda, este es el número que se paga.
- **Venta sobre agendadas por setter** · *Pregunta:* ¿las agendas de este setter compran? · *Cómo leerlo:* dos setters con las mismas agendas y ventas muy distintas = problema de calificación o de incentivo, no de volumen (caso E).

### Servicio y cobros (al corte)
- **% de cuotas vencidas** sobre las que ya debían estar pagas (no sobre todas) · *Le sirve a:* quien cobra, founder. · *Alarma (orientativa):* sube dos cortes seguidos. Al lado: cuántas vencidas no recibieron ningún aviso.
- **Días entre el pago y el acceso** · *Le sirve a:* coordinación de servicio. · *Cómo leerlo:* mediana y máximo, no solo promedio. Si el máximo pasa lo que promete el closer, hay una promesa rota en cada venta.
- **Clientes con cuota vencida que siguen con acceso** · *Le sirve a:* founder. · *Cómo leerlo:* si el control de accesos existe "para que no entre nadie sin pagar" y este número es alto, el control no está funcionando.

### Operaciones (calidad del dato)
- **Registros sin clave o en "Sin canal"** por tabla · *Alarma (orientativa):* más del 10 % o crece.
- **Llamadas sin closer, deals sin oportunidad, cuotas sin responsable** · *Cómo leerlo:* cada uno vuelve aproximado un KPI; decí cuál.
- **Días con reporte de fin de día cargado** por persona · *Cómo leerlo:* sin EOD, el setting diario y el "declarado contra CRM" no se pueden leer.

---

## 2 · Casos de uso: qué pieza se arma con la tabla

Elegí los que respondan a lo que el dueño pidió. Cada uno es algo que se le entregó a clientes reales.

### A. La reunión de los lunes con el tablero abierto
- **Para:** founder y líderes de área.
- **Qué se muestra:** cash de la semana y del mes (con cuotas separadas), agendas, asistencia y cierre por canal, vencidas y lo que vence esta semana.
- **Regla:** sin capturas ni planillas aparte; si un número no está en la interfaz, se agrega ahí. La reunión arranca con el tablero, no con "¿cómo venimos?".

### B. El diagnóstico comercial de varios meses
- **Para:** el dueño que siente que "algo no anda" pero no sabe qué.
- **Qué lleva:** el panorama en seis números; cómo se movieron las tasas (las tres juntas); **de dónde viene la plata** (adquisición vs cartera); canal contra canal con inversión, costo por agenda, costo por venta y retorno; la tabla completa mes a mes; salud del funnel (cancelaciones, no shows, llamadas sin resolver); y los hallazgos ordenados por impacto en la plata.
- **Plus que sorprende:** cruzar con lo que el lead declaró en el formulario (presupuesto, situación) y con la calificación que carga el closer: suelen predecir el cierre mucho mejor que el canal, y casi nadie los mira. Si el campo está vacío en la mitad de los registros, ese es un hallazgo.
- **Honestidad:** si el último mes está abierto (llamadas sin resolver al corte), se dice: "leé este mes como foto parcial".

### C. La decisión de pauta
- **Para:** founder y trafficker.
- **Qué lleva:** costo por venta por anuncio en 6 u 8 semanas, cash por agenda, y qué anuncio cortar, mantener o escalar. Con la salvedad de atribución.
- **Pasa seguido:** el dueño quiere escalar el anuncio "que mejor anda" según la plataforma, y en la base ese anuncio no tiene ventas.

### D. El panel de un lanzamiento
- **Para:** el equipo durante un lanzamiento.
- **Qué lleva:** inscriptos, inversión, agendas, ventas, cash y facturado, retorno sobre el total, el embudo y el comparativo con el lanzamiento anterior.
- **Lección:** el panel queda con lo macro; el detalle por anuncio y la atribución fina van en un documento aparte, con sus salvedades. Mostrar "ventas de Meta: 0" en el panel puede ser injusto con el trabajo del trafficker si la gente vio la campaña y compró por otro link.

### E. La conversación de comisiones e incentivos
- **Para:** founder y líder comercial.
- **Qué lleva:** ventas y cash por closer; agendas, asistencia y ventas por setter. Si el setter cobra por agenda y sus agendas no se presentan ni compran, el problema es el incentivo, no la persona (skill **Esquema de Pago y Comisiones**).

### F. La auditoría de completitud de datos
- **Para:** el dueño que paga sobre datos que no se pueden auditar.
- **Qué lleva:** registros sin canal, llamadas sin closer, no-shows que siguen "agendados", reservas sin cerrar, cuotas que la regla manda suspender y nadie suspendió, días con reporte de fin de día cargado.
- **Regla que suele salir de acá:** "sin registro no se liquida": CRM completo y comprobante subido como condición para cobrar la comisión.

---

## 3 · Cómo se lo presentás al dueño o al líder de área

1. **Una frase** que diga qué pasó con la plata ("se cobró menos de lo que se vendió y el anuncio que más escalamos no vendió").
2. **Tres números**, siempre los mismos, con el mes anterior al lado.
3. **Una decisión** con plazo y plan B.
4. **Lo que no se puede saber todavía** y qué hace falta para saberlo.

Con números, el founder acepta cambios que con opiniones rechaza. Y si el dueño no lee tablas: un mensaje de 5 líneas o un Loom de 3 minutos con el tablero abierto.
