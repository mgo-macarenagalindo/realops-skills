# Handling truncated tool output on large bases

`list_tables_for_base` and `list_pages_for_base` return their full result inline for small/medium
bases. On a base with dozens of tables or hundreds of fields, the result is too large for the
tool to return directly -- instead you'll get an error message saying the output was saved to a
local file, with a path like:

```
.../tool-results/mcp-<server-id>-list_tables_for_base-<timestamp>.txt
```

**Don't try to read that whole file with the `Read` tool.** It's typically one enormous line of
JSON (tens to hundreds of thousands of characters), and `Read` will only show you the first
chunk before hitting its own token cap -- there's no clean way to page through a single giant
line by offset.

**Instead, use `Grep` directly on that file path** with a bounded regex that extracts exactly one
JSON object per match, so each match becomes its own output line via `-o` (only-matching) mode.
Two patterns have been validated against real large bases:

## Table-level metadata (id, name, description, primaryFieldId)

This pattern works because it stops matching right after `primaryFieldId`, before the nested
`"fields":[...]` array starts -- so it never has to worry about brace-matching across nested
structures:

```
pattern:  \{"id":"tbl[A-Za-z0-9]{14}","name":"[^"]*"(,"description":"(?:[^"\\]|\\.)*")?,"primaryFieldId":"fld[A-Za-z0-9]{14}"
output_mode: content
-o: true
head_limit: 0
```

## Field-level metadata (id, name, type, description)

This works because a field object from `list_tables_for_base` never contains nested braces (no
`options`/choices at this level -- those only show up via `get_table_schema`), so a
brace-excluding character class safely bounds each match:

```
pattern:  \{"id":"fld[A-Za-z0-9]{14}"[^{}]*\}
output_mode: content
-o: true
head_limit: 0
```

If the Grep result itself is still large enough to get persisted to *another* file (this
happens -- a base with ~800 fields produces roughly 80KB of matches), that file is much smaller
and safe to read with `Read` in a couple of paginated chunks (it'll tell you how many total
lines and offer an `offset` to continue).

## Adapting for interfaces/pages

`list_pages_for_base`'s JSON is more deeply nested (interfaces contain pages, pages contain
`tablesByTableId` sub-schemas), so a single clean non-nested-brace pattern won't cover
everything. When it truncates:
- First try a bounded pattern scoped to just what you need (e.g. `"id":"pag[A-Za-z0-9]{14}"`
  plus a short run of following characters for name/pageType/sourceTableId, stopping before
  `tablesByTableId` starts).
- If that's not clean enough, fall back to reading the persisted file in chunks with `Read` and
  parsing by eye -- it's slower but reliable, and interface/page counts are usually much smaller
  than field counts (tens, not hundreds), so this is rarely a bottleneck.

## Getting linked-record targets

Neither `list_tables_for_base` nor the extraction above tells you what table a
`multipleRecordLinks` field actually points to -- that requires `get_table_schema`. Batch this:
the tool accepts a `tables` array, so pass every table's link-type field IDs in as few calls as
possible (group multiple tables per call) rather than one call per table.

## Batching writes

`create_records_for_table` and `update_records_for_table` on the official remote MCP
(`https://mcp.airtable.com/mcp`) cap at 50 records per call. For a base with hundreds of fields,
plan on doing this in a loop -- e.g. ~800 fields needs roughly 16 calls of 50. This is mechanical
and doesn't need much judgment per batch; just keep going until every record's been written,
tracking source-ID -> master-record-ID mappings as you go so linked fields can reference the right
records. Prefer `update_records_for_table` with `performUpsert` (merging on the source-ID field)
so each batch creates-or-updates in one shot -- see SKILL.md Step 3. (Because that's still a lot of
write calls, the `airtable` server needs to be allowlisted so they don't each prompt -- see
SKILL.md's "Which Airtable connection this uses.")
