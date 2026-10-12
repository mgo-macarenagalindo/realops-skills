# Origen · skill-creator

| Campo | Dato |
|---|---|
| Autor | Anthropic, PBC |
| Repositorio | https://github.com/anthropics/skills |
| Ruta en el repo | `skills/skill-creator` |
| Commit | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (09/10/2026) |
| Copiada el | 12/10/2026 |
| Licencia | Apache License 2.0 · "Copyright 2026 Anthropic, PBC." (archivo `LICENSE.txt` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** La skill oficial de Anthropic para crear, mejorar y medir skills (evals, comparación de versiones, optimización de la descripción y empaquetado). Está en inglés.

**Ojo: trae scripts** (Python, en `scripts/` y `eval-viewer/`). Son del autor original; leelos antes de usarlos (regla 2 de seguridad). En RealOps™ la usás como paso siguiente de la skill `sop-a-skill`: la nuestra es el camino corto en castellano desde un SOP; esta es para probar la skill con evals y empaquetarla con más rigor.

**Versión vigente:** se actualiza en su origen. Para la última, bajala de https://github.com/anthropics/skills/tree/main/skills/skill-creator.

## Nota de seguridad (12/10/2026)

Una revisión automática marcó dos puntos en el visor de evaluaciones (`eval-viewer/`): `generate_review.py` inserta los datos como JSON dentro de un `<script>` sin escapar `<`, y `viewer.html` arma HTML concatenando algunos valores sin escapar comillas. El visor solo muestra, en tu compu, los resultados de tus propias pruebas, así que el riesgo es bajo. La copia queda sin modificar (es el original de Anthropic); si abrís el visor con datos que no generaste vos, revisalos antes. Para la versión al día, instalá desde el repo oficial.
