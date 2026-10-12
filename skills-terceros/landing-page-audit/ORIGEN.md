# Origen · landing-page-audit

| Campo | Dato |
|---|---|
| Autor | Landingfolio |
| Fuente | https://landingfolio.com/skills/landing-page-audit.tar (listado en https://www.landingfolio.com/skills). No tiene repositorio público. |
| Versión | El `.tar` descargado el 12/10/2026 (archivos fechados 12/10/2026). SHA-256 del `.tar`: `fe920b30a63a81af79ccf8436670b0c2b0d91180c291efb7d8e7f54a2ebb7b0b` |
| Licencia | MIT · "Copyright (c) 2026 Landingfolio" (archivo `LICENSE.md` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Audita una landing (URL, captura o código) con reglas de diseño y de conversión y devuelve un informe Crítico / Mayor / Menor. Usa el MCP de Landingfolio para comparar con secciones reales; sin MCP hace la auditoría solo con reglas. En RealOps™ la usa la skill `revisor-landing-y-publicacion` para la parte visual. Está en inglés.

**Scripts.** No trae scripts.

**Versión vigente:** se actualiza en su origen. Para la última, instalala desde el original:

```
mkdir -p ~/.claude/skills && curl -fsSL https://landingfolio.com/skills/landing-page-audit.tar | tar -x -C ~/.claude/skills
```
