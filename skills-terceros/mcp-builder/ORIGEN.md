# Origen · mcp-builder

| Campo | Dato |
|---|---|
| Autor | Anthropic, PBC |
| Repositorio | https://github.com/anthropics/skills |
| Ruta en el repo | `skills/mcp-builder` |
| Commit | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (09/10/2026). Último cambio en esta carpeta: `b9e19e6f` (20/04/2026) |
| Copiada el | 12/10/2026 |
| Licencia | Apache License 2.0 · "Copyright 2026 Anthropic, PBC." (archivo `LICENSE.txt` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna. Los archivos son copia exacta del original; este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** La skill oficial de Anthropic para **construir un servidor MCP propio** (en Python con FastMCP o en TypeScript con el SDK de MCP) cuando una plataforma tiene API pero no tiene conector ni servidor MCP. Trae buenas prácticas de diseño de herramientas y una guía para evaluar el servidor. Está en inglés y es para alguien con perfil técnico (o para hacerlo con Claude Code al lado).

**Cómo se usa en RealOps™.** Es el último escalón de la skill `conectar-claude-a-tus-datos`: primero se busca un conector oficial, después un servidor MCP oficial del proveedor, después uno de la comunidad evaluado con la ficha de seguridad, después un puente (Zapier, Make, n8n). Recién si nada de eso existe, se construye uno con esta skill. Para un operativo estratégico, lo normal es **encargarlo o hacerlo acompañado**, no improvisarlo con datos reales.

**Ojo: trae scripts** (Python, en `scripts/`: `evaluation.py` y `connections.py`, que usan la API de Anthropic y se conectan al servidor que estás probando). Son del autor original. Leelos antes de usarlos (regla 2 de seguridad), corrélos solo contra un servidor de prueba y nunca con una API key de un cliente.

**Versión vigente:** se actualiza en su origen. Para la última, bajala de https://github.com/anthropics/skills/tree/main/skills/mcp-builder.
