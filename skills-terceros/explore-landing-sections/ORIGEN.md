# Origen · explore-landing-sections

| Campo | Dato |
|---|---|
| Autor | Landingfolio |
| Fuente | https://landingfolio.com/skills/explore-landing-sections.tar (listado en https://www.landingfolio.com/skills). No tiene repositorio público. |
| Versión | El `.tar` descargado el 12/10/2026 (archivos fechados 12/10/2026). SHA-256 del `.tar`: `5cd23697a2f47c6c1f70108a1d38c2ddca1adec5148e6217165afc5d1a29382d` |
| Licencia | MIT · "Copyright (c) 2026 Landingfolio" (archivo `LICENSE.md` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Explora 3 a 6 direcciones para una sección de la landing (hero, precios, testimonios, FAQ, CTA…) en una página HTML de comparación, con ejemplos reales de Landingfolio. En RealOps™ la usa la skill `referencias-landing-landingfolio`. Está en inglés.

**Scripts.** Trae un script de shell (`scripts/scan-brand.sh`) que solo lee la carpeta del proyecto para detectar colores y tipografías. Leelo antes de usarlo.

**Versión vigente:** se actualiza en su origen. Para la última, instalala desde el original:

```
mkdir -p ~/.claude/skills && curl -fsSL https://landingfolio.com/skills/explore-landing-sections.tar | tar -x -C ~/.claude/skills
```
