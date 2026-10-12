# Origen · screenshot-capture

| Campo | Dato |
|---|---|
| Autor | Landingfolio |
| Fuente | https://landingfolio.com/skills/screenshot-capture.tar (listado en https://www.landingfolio.com/skills). No tiene repositorio público. |
| Versión | El `.tar` descargado el 12/10/2026 (archivos fechados 12/10/2026). SHA-256 del `.tar`: `5b36cb5af763d4f306ebb63c9681918204be9c7ec67ed00e04a14d929e2511c7` |
| Licencia | MIT · "Copyright (c) 2026 Landingfolio" (archivo `LICENSE.md` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Saca capturas de una página, una sección o un elemento con Chrome sin ventana. Sirve para pasarle capturas a las otras skills de landing. Está en inglés.

**Scripts.** Trae un script (`scripts/screenshot.mjs`, con playwright-core). Necesita Node.js y Chrome. Leelo antes de usarlo.

**Versión vigente:** se actualiza en su origen. Para la última, instalala desde el original:

```
mkdir -p ~/.claude/skills && curl -fsSL https://landingfolio.com/skills/screenshot-capture.tar | tar -x -C ~/.claude/skills
```
