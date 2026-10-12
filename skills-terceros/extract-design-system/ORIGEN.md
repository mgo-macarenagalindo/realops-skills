# Origen · extract-design-system

| Campo | Dato |
|---|---|
| Autor | Landingfolio |
| Fuente | https://landingfolio.com/skills/extract-design-system.tar (listado en https://www.landingfolio.com/skills). No tiene repositorio público. |
| Versión | El `.tar` descargado el 12/10/2026 (archivos fechados 12/10/2026). SHA-256 del `.tar`: `293e79cacc0a3059832439e8a1e512a2ae217da09a6bac4872591b5cf8e2bcc6` |
| Licencia | MIT · "Copyright (c) 2026 Landingfolio" (archivo `LICENSE.md` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Extrae el sistema de diseño (colores, tipografía, espaciado, botones) de una página en vivo o de un código y lo deja en un `DESIGN.md`. Sirve para respetar la marca del cliente en `landing-con-21st`. Está en inglés.

**Scripts.** Trae scripts (`scripts/extract-url.mjs` con playwright-core y `scripts/scan-codebase.sh`). Necesitan Node.js y Chrome. Leelos antes de usarlos.

**Versión vigente:** se actualiza en su origen. Para la última, instalala desde el original:

```
mkdir -p ~/.claude/skills && curl -fsSL https://landingfolio.com/skills/extract-design-system.tar | tar -x -C ~/.claude/skills
```
