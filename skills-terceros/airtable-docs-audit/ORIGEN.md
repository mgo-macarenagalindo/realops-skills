# Origen · airtable-docs-audit

| Campo | Dato |
|---|---|
| Autor | Dave Williams (davepongw) |
| Repositorio | https://github.com/davepongw/airtable-docs-audit-via-mcp |
| Ruta en el repo | raíz (`SKILL.md`, `references/`, `scripts/`, `README.md`, `LICENSE`) |
| Commit | `1dedd4928d02cdae6a035902120e5c2e7e5f480e` (06/08/2026) |
| Copiada el | 12/10/2026 |
| Licencia | MIT · "Copyright (c) 2026 Dave Williams (davepongw)" (archivo `LICENSE` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Copia exacta (sin `.gitignore`). Este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Una skill en inglés que documenta una o varias bases de Airtable usando el MCP oficial de Airtable: arma una "base de documentación" con cada tabla, campo (tipo y configuración), vista, interface, formulario y automatización, vinculados entre sí, y un registro de cambios para correrla cada semana y ver qué cambió.

**Cómo encaja en RealOps™.** Complementa a `auditor-base-heredada` (la nuestra hace el informe de riesgos para decidir qué tocar; esta deja el inventario vivo de la base) y a `arquitecto-base-airtable` en modo "mejorar una base existente".

**Ojo, antes de usarla:**
- **Escribe en Airtable**: crea y actualiza registros en una base de documentación aparte. Usala con una base de prueba primero y con tokens de permiso mínimo (la propia skill recomienda uno de solo lectura para las bases que documenta y otro de escritura solo para la base de documentación).
- **Trae un script** (`scripts/fetch_base_collaborators.py`, Python) que llama a la API de Airtable con tu token para traer colaboradores e interfaces. Es del autor original; leelo antes de usarlo (regla 2 de seguridad). No lo corrimos.
- Pensada para el MCP de Airtable agregado a mano en Claude Code; con el conector de Claude.ai te va a pedir permiso en cada tanda.

**Versión vigente:** https://github.com/davepongw/airtable-docs-audit-via-mcp
