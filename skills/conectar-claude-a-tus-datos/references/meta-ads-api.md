# Meta Ads por API (cuando no hay conector)

> Referencia de la skill **Claude Conectado a tus Datos** (RealOps™). Es un camino **técnico**: hacelo con alguien que haya trabajado con la API de Meta o con Claude Code al lado, contándole qué ves en cada pantalla y frenando en cada paso de permisos. Si nada de esto te resulta familiar, quedate con el plan B del final.

## Antes de empezar

- **¿Hay conector o servidor oficial?** Buscalo primero (escalones 1 y 2 de la skill). Si existe, no hace falta nada de esto.
- **¿Quién es dueño de la cuenta publicitaria?** El acceso lo da el dueño desde su portfolio comercial (Business Manager). Nunca se usa el usuario y la contraseña de nadie.
- **¿Para qué lo querés?** Si es un reporte semanal, el plan B alcanza. La API se justifica para un agente o un tablero que se actualiza solo.

## Los pasos, en grande

1. **Usuario del sistema.** En la configuración del portfolio comercial, quien es admin crea un "usuario del sistema" (una cuenta que no es de una persona, pensada para integraciones). Así, si alguien del equipo se va, la conexión no se corta.
2. **Asignarle la cuenta publicitaria con el permiso mínimo.** Solo la cuenta que vas a leer y con permiso de ver rendimiento, no de administrar.
3. **Generar el token** de ese usuario con el permiso de **solo lectura de anuncios** (en la API se llama `ads_read`). Nada de permisos de administración ni de páginas si no hacen falta.
4. **Guardar el token en la herramienta puente**, nunca en un chat ni en un documento. Puede ser un flujo de n8n o Make que una vez por día o por semana trae los datos por anuncio y los deja en una tabla (Airtable, Google Sheets o Supabase) que Claude ya puede leer.
5. **Verificar:** que la tabla puente tenga los mismos números que el administrador de anuncios para una semana elegida. Recién ahí se usa para decidir.
6. **Revisar vencimientos y límites:** los tokens pueden vencer y la API limita cuántas consultas acepta. Anotá en la wiki quién lo renueva y dónde se ve el error si falla.

## Plan B (sin API)

Cada lunes, exportá desde el administrador de anuncios el reporte por anuncio (fechas, gasto, resultados) y pasáselo a Claude con un pedido guardado. Es manual, pero seguro, y para un reporte semanal casi siempre alcanza. El análisis de costo por venta por anuncio está en la skill **Rentabilidad por Anuncio**.

## Nunca

- Mostrar el token ni datos de facturación de la cuenta.
- Dar permisos de administración "porque es más fácil".
- Dejar como admin a una agencia o una persona que ya no trabaja con el negocio: si la ves, es un hallazgo para el founder.
