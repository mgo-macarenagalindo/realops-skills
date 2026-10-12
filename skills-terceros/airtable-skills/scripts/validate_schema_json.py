#!/usr/bin/env python3
"""Validate an Airtable blueprint JSON produced by the airtable-skills skill.

This script intentionally validates structure and internal references only. It does
not call Airtable and does not require credentials.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_BASE_KEYS = {
    "name",
    "purpose",
    "tables",
}

OPTIONAL_LIST_KEYS = {
    "assumptions",
    "open_questions",
    "relationships",
    "views",
    "interfaces",
    "forms",
    "automations",
    "permissions",
    "integrations",
    "risks",
    "implementation_plan",
}

ALLOWED_FIELD_SOURCES = {
    "native",
    "derived",
    "lookup",
    "rollup",
    "synced",
    "integration",
    "manual_override",
    "unknown",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"file not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid json at line {exc.lineno}, column {exc.colno}: {exc.msg}")


def as_list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{path} must be a list")
    return value


def as_dict(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{path} must be an object")
    return value


def validate_blueprint(data: Any) -> None:
    root = as_dict(data, "root")
    if "base" not in root:
        fail("root must contain a 'base' object")

    base = as_dict(root["base"], "base")
    missing = sorted(REQUIRED_BASE_KEYS - set(base.keys()))
    if missing:
        fail(f"base is missing required keys: {', '.join(missing)}")

    for key in OPTIONAL_LIST_KEYS:
        if key in base:
            as_list(base[key], f"base.{key}")

    if not isinstance(base.get("name"), str) or not base["name"].strip():
        fail("base.name must be a non-empty string")
    if not isinstance(base.get("purpose"), str) or not base["purpose"].strip():
        fail("base.purpose must be a non-empty string")

    tables = as_list(base["tables"], "base.tables")
    if not tables:
        fail("base.tables must contain at least one table")

    table_names: set[str] = set()
    field_index: dict[str, set[str]] = {}

    for i, table_value in enumerate(tables):
        table = as_dict(table_value, f"base.tables[{i}]")
        name = table.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(f"base.tables[{i}].name must be a non-empty string")
        if name in table_names:
            fail(f"duplicate table name: {name}")
        table_names.add(name)

        for required in ("purpose", "grain"):
            if required not in table or not isinstance(table[required], str) or not table[required].strip():
                warn(f"table '{name}' should define non-empty '{required}'")

        fields = as_list(table.get("fields", []), f"table '{name}'.fields")
        field_names: set[str] = set()
        for j, field_value in enumerate(fields):
            field = as_dict(field_value, f"table '{name}'.fields[{j}]")
            field_name = field.get("name")
            if not isinstance(field_name, str) or not field_name.strip():
                fail(f"table '{name}'.fields[{j}].name must be a non-empty string")
            if field_name in field_names:
                fail(f"duplicate field '{field_name}' in table '{name}'")
            field_names.add(field_name)

            if "type" not in field or not isinstance(field["type"], str) or not field["type"].strip():
                warn(f"field '{name}.{field_name}' should define a field type")

            source = field.get("source")
            if source is not None and source not in ALLOWED_FIELD_SOURCES:
                warn(
                    f"field '{name}.{field_name}' has unusual source '{source}'. "
                    f"expected one of: {', '.join(sorted(ALLOWED_FIELD_SOURCES))}"
                )
        field_index[name] = field_names

    relationships = as_list(base.get("relationships", []), "base.relationships")
    for i, rel_value in enumerate(relationships):
        rel = as_dict(rel_value, f"base.relationships[{i}]")
        from_table = rel.get("from_table")
        to_table = rel.get("to_table")
        if from_table not in table_names:
            fail(f"relationship[{i}] references missing from_table: {from_table}")
        if to_table not in table_names:
            fail(f"relationship[{i}] references missing to_table: {to_table}")
        field = rel.get("field")
        if isinstance(field, str) and field and field not in field_index.get(from_table, set()):
            warn(f"relationship[{i}] field '{field}' is not listed in table '{from_table}' fields")

    automations = as_list(base.get("automations", []), "base.automations")
    for i, automation_value in enumerate(automations):
        automation = as_dict(automation_value, f"base.automations[{i}]")
        if not automation.get("name"):
            warn(f"automation[{i}] should define a name")
        if not automation.get("trigger"):
            warn(f"automation[{i}] should define a trigger")
        if not automation.get("failure_handling"):
            warn(f"automation[{i}] should define failure_handling")

    print("OK: blueprint structure is valid")
    print(f"Tables: {len(table_names)}")
    print(f"Relationships: {len(relationships)}")
    print(f"Automations: {len(automations)}")


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        fail("usage: validate_schema_json.py <blueprint.json>")
    validate_blueprint(load_json(Path(argv[1])))


if __name__ == "__main__":
    main(sys.argv)
