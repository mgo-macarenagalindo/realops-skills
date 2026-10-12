# Tu portafolio como página, en Claude

> Referencia de la skill Preparar tu Perfil para Vender Operaciones. Cómo convertir tus piezas en una página con diseño que se pueda mandar por link, poner en Destacados o mostrar en una entrevista.

## Qué tiene que tener

Una sola página, que se lea en 2 minutos y se entienda en 10 segundos:

1. **Portada.** Nombre, rol (el mismo del titular), una frase de qué hacés y para quién, foto opcional, y un botón de contacto (mail o LinkedIn).
2. **Números de arriba** (opcional): 3 datos reales, por ejemplo "8 piezas construidas · 1 operación de punta a punta · 3 herramientas que manejo en vivo". Nada inventado.
3. **Una tarjeta por pieza**, de la más fuerte a la menos fuerte:
   - Título de la pieza y rótulo de origen: **"Caso práctico"**, **"Negocio real, anonimizado"** o **"Negocio propio"**.
   - La captura (o un marco para la captura).
   - **El problema**, con número (plata, horas o cantidad).
   - **Qué construí** y **qué decidí** (una línea de criterio).
   - **El resultado** o el estado ("en prueba", "propuesto a dirección").
   - Link a la pieza (solo lectura) o al video de pantalla.
4. **Cómo trabajo**: 3 pasos (diagnóstico → implementación → seguimiento), si ofrece servicios.
5. **Cierre**: qué busca y cómo contactarla.

Si el **Revisor de Piezas de Portafolio** ya le dio la ficha de cada pieza, las tarjetas salen de ahí.

## Las capturas

- **Siempre de una copia con datos de prueba** o de un caso práctico. Nunca la base real con nombres, mails, teléfonos o montos de clientes.
- Una captura por pieza que muestre **el resultado**, no la configuración: la vista "Vencidas" con días de atraso, no la lista de campos; el tablero con sus 5 números, no el editor.
- Recortadas, sin pestañas personales ni notificaciones.
- Nombres de archivo claros: `03-crm-vista-vencidas.png`.

## Cómo pedírselo a Claude

Según dónde trabajes:

- **Claude (chat, claude.ai o la app)**: subí las capturas al chat para que Claude las vea y escriba las tarjetas, y pedile la página como **artefacto**. **Por defecto, la página sale con marcos para cada captura** (criterio orientativo): que una imagen subida al chat aparezca adentro de un artefacto publicado no está garantizado, y no conviene descubrirlo el día que mandás el link.
  - **Prueba de 2 minutos (hacela una vez):** subí una captura y pedí "mostrá esta imagen en la primera tarjeta". Si la ves en la vista previa, publicá el artefacto y **abrí el link en una ventana privada** (o desde el celular sin sesión). Si ahí también se ve, podés usar las capturas incrustadas. Si no aparece en cualquiera de los dos pasos, plan B.
  - **Plan B (siempre funciona):** dejá los marcos con el nombre del archivo, pasá la estructura a la herramienta donde vas a compartir (Notion, Gamma, Canva o Google Sites) y pegá ahí las capturas; o usá Claude Code o Cowork, que trabajan con los archivos de tu compu.
- **Claude Code o Cowork** (trabaja con archivos de tu compu): poné las capturas en una carpeta y pedile que **las incruste dentro del archivo** (no que las linkee a la carpeta), así queda un solo HTML que se abre en cualquier navegador y en cualquier compu. Antes de compartirlo, mandátelo por mail y abrilo desde otro dispositivo: si se ven las capturas, está listo.

Pedido modelo (completalo):

> Armame una página de portafolio con diseño, en una sola página HTML, para un perfil de operaciones en negocios digitales.
> - Estilo: [sobrio y profesional / cálido / moderno], colores [los de tu banner], tipografía legible, que se vea bien en el celular.
> - Portada: [nombre], [rol], [frase de qué hago y para quién], botón "Escribime" a [mail o LinkedIn].
> - Tarjetas (en este orden): [pegá la ficha de cada pieza: título, rótulo de origen, problema con número, qué construí, qué decidí, resultado o estado, link].
> - Capturas: [adjuntas / en la carpeta X]; si no se pueden incrustar, dejá un marco con el nombre del archivo.
> - Cierre: [qué busco] y contacto.
> - Reglas: no inventes números, logos ni testimonios; los casos prácticos llevan el rótulo "Caso práctico" visible en la tarjeta.

Después pedile ajustes de a uno ("la portada más corta", "las tarjetas en dos columnas", "un color de acento menos").

## Chequeo antes de publicar

- [ ] Cada pieza tiene rótulo de origen visible.
- [ ] Ninguna captura muestra datos reales de clientes, mails, teléfonos, montos de un empleador ni credenciales.
- [ ] Los números son los mismos que en el CV y en LinkedIn.
- [ ] Los verbos respetan el estado (detecté / propuse / armé / implementé / reduje).
- [ ] Se entiende en el celular.
- [ ] Alguien de afuera del programa la miró y pudo decir en una frase qué hacés.
- [ ] El link es de **solo lectura**.
- [ ] Lo abriste en una ventana privada (o en otro dispositivo) y **se ven las capturas**.
