# Origen · share-image-generator

| Campo | Dato |
|---|---|
| Autor | Landingfolio |
| Fuente | https://landingfolio.com/skills/share-image-generator.tar (listado en https://www.landingfolio.com/skills). No tiene repositorio público. |
| Versión | El `.tar` descargado el 12/10/2026 (archivos fechados 12/10/2026). SHA-256 del `.tar`: `e5e7d29709ec64e2fe45e32ae99118410abd85b014f7a8413b3b7d8c71bdf385` |
| Licencia | MIT · "Copyright (c) 2026 Landingfolio" (archivo `LICENSE.md` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Genera la imagen que aparece al compartir el link de la página en redes y mensajería (diseñada en 1200 × 630 y exportada al doble de resolución), con los colores y el logo de la marca. Útil al publicar una landing. Está en inglés.

**Scripts.** Trae un script (`scripts/render.mjs`, con playwright-core). Necesita Node.js y Chrome. Leelo antes de usarlo.

**Versión vigente:** se actualiza en su origen. Para la última, instalala desde el original:

```
mkdir -p ~/.claude/skills && curl -fsSL https://landingfolio.com/skills/share-image-generator.tar | tar -x -C ~/.claude/skills
```
