# Origen · airtable-skills

| Campo | Dato |
|---|---|
| Autor | AmirHesam Piri (he8um) |
| Repositorio | https://github.com/he8um/airtable-skills |
| Ruta en el repo | `airtable-skills/` (+ `LICENSE`, `README.md` y `examples/` de la raíz) |
| Commit | `266885e9f552e4e9b20897da0fd2cae3cb3a277a` (08/07/2026) |
| Copiada el | 12/10/2026 |
| Licencia | MIT · "Copyright (c) 2026 AmirHesam Piri" (archivo `LICENSE` de esta carpeta, sin cambios) |
| Modificaciones | Ninguna en el contenido. Solo se reubicó: el `SKILL.md` y sus carpetas, que en el repo están dentro de `airtable-skills/`, quedan en la raíz de esta carpeta para que se pueda subir como skill. No se copiaron `dist/skill.zip`, `docs/`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md` ni `.gitignore`. Este `ORIGEN.md` es el único archivo agregado. |

**Qué es.** Una skill de arquitecto de Airtable, en inglés: diseño de bases como aplicación (entidades, "grain" de cada tabla, fuente de verdad por campo, tablas puente), diccionario de campos, vistas, interfaces, automatizaciones como contrato disparador/acción con campos de guarda, permisos, auditoría y plan de migración, con un "blueprint" JSON opcional. Tiene 9 referencias que carga según la tarea.

**Cómo encaja en RealOps™.** Es el complemento en inglés, más técnico, de nuestra `arquitecto-base-airtable`: la nuestra habla el idioma del infonegocio y del alumno; esta suma rigor de arquitectura (checklists de auditoría, plantilla de tabla con "una fila = …"). Para el CRM comercial de un infonegocio, usá `crm-cliente-infonegocios`.

**Ojo: trae un script** (`scripts/validate_schema_json.py`, Python, solo lee un JSON local y valida su estructura; no se conecta a internet). Es del autor original; leelo antes de usarlo (regla 2 de seguridad). No lo corrimos.

**Versión vigente:** se actualiza en su origen: https://github.com/he8um/airtable-skills
