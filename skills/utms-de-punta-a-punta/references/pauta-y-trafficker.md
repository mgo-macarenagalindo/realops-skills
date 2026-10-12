# Pauta y trafficker · cómo se trackea cada anuncio

> Referencia de la skill UTMs de Punta a Punta. Cargala cuando haya tráfico pago o cuando tengas que escribir el brief para quien publica los anuncios.

## Quién hace qué

| Quién | Qué hace |
|---|---|
| **Operativo estratégico (vos)** | Define la convención, arma el brief, crea las columnas y el Zap, verifica cada semana que los leads de pauta lleguen con `utm_content` y `ad_id` |
| **Trafficker / agencia / founder que publica** | Nombra campañas, conjuntos y anuncios con la convención y carga los parámetros de URL en **cada anuncio al publicarlo**. Avisa cada anuncio nuevo o renombrado |
| **Editor de video / creativos** | Entrega cada pieza con su nombre según la regla (`formato-angulo-gancho-version`) |

Trackear es parte de publicar, no una tarea aparte: un anuncio sin parámetros es un anuncio que no se puede evaluar por ventas.

## Parámetros dinámicos de Meta

Meta reemplaza estos valores al momento del clic. Se cargan en el campo **"Parámetros de URL"** del anuncio (sección Destino / Seguimiento), no pegados en la URL del sitio web.

| Parámetro dinámico | Qué devuelve | Para qué |
|---|---|---|
| `{{campaign.name}}` | Nombre de la campaña | `utm_campaign` |
| `{{adset.name}}` | Nombre del conjunto | `utm_term` |
| `{{ad.name}}` | Nombre del anuncio | `utm_content` |
| `{{ad.id}}` | ID del anuncio (no cambia aunque lo renombres) | `ad_id`, la clave para cruzar exacto |
| `{{campaign.id}}`, `{{adset.id}}` | IDs de campaña y conjunto | Opcional |
| `{{site_source_name}}` | `fb`, `ig`, `msg` o `an` (dónde se vio) | Si querés separar Facebook de Instagram en `utm_source`. Si lo usás, la fórmula de canal tiene que tratar `fb` e `ig` con `medium=ads` como "Pauta" |
| `{{placement}}` | Ubicación (feed, historias, reels…) | Opcional, en un parámetro propio (`placement`) |

Plantilla recomendada:

```
utm_source=fb&utm_medium=ads&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&ad_id={{ad.id}}
```

Cuidado con esto:
- **Los nombres viajan tal cual.** Si el anuncio se llama `AD-07 · Video 'Facturá US$10K'`, al link llega con espacios, mayúsculas y símbolos codificados. Por eso los nombres siguen la convención (minúsculas, guiones, sin acentos ni símbolos).
- **Renombrar cambia el `utm_content` de los clics nuevos, no de los viejos.** Por eso existe el `ad_id` y la tabla de anuncios.
- **La lista exacta de parámetros dinámicos la mantiene Meta** y puede cambiar: verificá en el administrador al momento de cargarlos.
- **Se completan solo con clics reales del anuncio publicado**, no en la vista previa del editor. La prueba se hace con un clic desde el anuncio activo (o pidiéndole a alguien del equipo que entre).
- **Al duplicar un anuncio**, los parámetros se copian. Bien. Pero cambiale el nombre: dos anuncios con el mismo nombre solo se separan por `ad_id`.

## Formularios instantáneos de Meta (lead ads)

No hay link, entonces no hay UTM. Si el lead entra por Zapier con el disparador de formularios de Meta, el registro trae el **ID del anuncio, del conjunto, de la campaña y del formulario**. Mapeá el ID del anuncio a la columna `ad_id`, poné `utm_source=fb` y `utm_medium=ads` como valores fijos en el Zap, y traducí con la tabla de anuncios.

## Otras plataformas

- **Google Ads:** tiene su propio sistema (plantilla de seguimiento con `{campaignid}`, `{creative}`…). Misma lógica: el ID del anuncio a `ad_id`.
- **TikTok Ads:** también ofrece parámetros dinámicos (`__CID_NAME__`, `__AID_NAME__`, `__CID__`…). Verificá los nombres vigentes en su administrador.

## El brief de una página para el trafficker

```
Brief de tracking · [negocio] · desde [fecha]

1. Nombres
   Campaña: [objetivo]-[oferta]-[mes] (ej. aplicacion-mai-oct26)
   Conjunto: [publico]-[edad] (ej. amplio-25-45, intereses-prof)
   Anuncio: formato-angulo-gancho-version (ej. vid-promesa-10k90dias-v2)
   Minúsculas, guiones, sin acentos ni símbolos.

2. Parámetros de URL (en cada anuncio, campo "Parámetros de URL")
   utm_source=fb&utm_medium=ads&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&ad_id={{ad.id}}

3. Antes de activar
   [ ] Nombre con la convención   [ ] Parámetros cargados   [ ] Link a la landing / formulario (no al widget)

4. Después de activar
   [ ] Aviso en el canal: nombre + ID del anuncio
   [ ] El primer lead aparece en la base con utm_content y ad_id (lo verifica operaciones)

5. Cada semana
   Export de Meta por anuncio con "Identificador del anuncio", gasto y agendas. Operaciones lo cruza con ventas.
```

## Control semanal (lo hace operaciones)

- Vista "Pauta sin anuncio": leads con `utm_medium = ads` y `ad_id` vacío. Si aparecen, hay un anuncio sin parámetros: se le avisa al trafficker con el nombre.
- Vista "Anuncios nuevos": `ad_id` que no está en la tabla de anuncios. Se agrega la fila.
- Meta de tracking: más de 9 de cada 10 leads de pauta con `ad_id`.
