# Master schema -- exact table definitions

Create these in order (each links to the previous one's table ID, so it must exist first).
Use `create_table` with these payloads, substituting `<MASTER_BASE_ID>`. Record the returned
table ID and each field's ID -- you'll need them for every subsequent step.

If the master base already has tables with these names, don't recreate them -- read their
existing schema via `list_tables_for_base` instead and reuse those IDs.

## 1. Bases

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Bases",
  "description": "One record per audited source Airtable base.",
  "fields": [
    {"name": "Base Name", "type": "singleLineText"},
    {"name": "Base ID", "type": "singleLineText", "description": "Airtable base ID (appXXXXXXXXXXXXXX) -- stable identifier used to match records across runs."},
    {"name": "Base Guide", "type": "multilineText", "description": "The base's Base Guide content (Airtable's base-level welcome/help text) -- not a 'description' field, bases don't have one. See the note below."},
    {"name": "Workspace", "type": "singleLineText"},
    {"name": "Permission Level", "type": "singleLineText"},
    {"name": "Last Audited", "type": "date", "options": {"dateFormat": {"name": "iso", "format": "YYYY-MM-DD"}}}
  ]
}
```

Note: bases don't have a "description" field the way tables and fields do. What they have is a
**Base Guide** -- the welcome/help content editable from a base's "..." menu in the Airtable UI.
None of the current Airtable connector tools (`list_bases`, `search_bases`, `list_tables_for_base`,
`list_workspaces`, etc.) expose a way to read or write that guide content. Leave "Base Guide"
blank / noted as "not retrievable via current connector tools" until a tool exposes it -- don't
call it a "description" and don't treat the gap as a bug.

## 2. Tables (links to Bases)

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Tables",
  "description": "One record per table found in an audited source base.",
  "fields": [
    {"name": "Table Name", "type": "singleLineText"},
    {"name": "Table ID", "type": "singleLineText", "description": "Airtable table ID (tblXXXXXXXXXXXXXX)."},
    {"name": "Description", "type": "multilineText"},
    {"name": "Primary Field Name", "type": "singleLineText"},
    {"name": "Field Count", "type": "number", "options": {"precision": 0}},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

Tables (and fields, below) genuinely do have a "description" field via the Airtable API -- this
is different from the Bases-level Base Guide gap noted above.

## 3. Fields (links to Tables, twice)

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Fields",
  "description": "One record per field found in an audited source table.",
  "fields": [
    {"name": "Field Name", "type": "singleLineText"},
    {"name": "Field ID", "type": "singleLineText", "description": "Airtable field ID (fldXXXXXXXXXXXXXX)."},
    {"name": "Type", "type": "singleLineText"},
    {"name": "Description", "type": "multilineText"},
    {"name": "Configuration", "type": "multilineText", "description": "Choices, formula text, rollup/lookup source, or other field-specific options."},
    {"name": "Table", "type": "multipleRecordLinks", "options": {"linkedTableId": "<TABLES_TABLE_ID>"}},
    {"name": "Links To Table", "type": "multipleRecordLinks", "description": "Only set when Type is a linked-record type; points at the target Table record.", "options": {"linkedTableId": "<TABLES_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

## 4. Interfaces (links to Bases)

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Interfaces",
  "description": "One record per interface found in an audited source base.",
  "fields": [
    {"name": "Interface Name", "type": "singleLineText"},
    {"name": "Interface ID", "type": "singleLineText", "description": "Airtable interface ID (pbdXXXXXXXXXXXXXX)."},
    {"name": "Description", "type": "multilineText"},
    {"name": "Published Status", "type": "singleLineText"},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

## 5. Pages (links to Interfaces, Tables, and Bases)

Give pages their own rows -- don't fold them into a text blob on the Interface record. A page
has real structure worth capturing on its own: what kind of page it is, what table backs it, and
(for overview/form pages) real authored content.

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Pages",
  "description": "One record per page inside an interface (or a standalone form).",
  "fields": [
    {"name": "Page Name", "type": "singleLineText"},
    {"name": "Page ID", "type": "singleLineText", "description": "Airtable page ID (pagXXXXXXXXXXXXXX)."},
    {"name": "Page Type", "type": "singleSelect", "options": {"choices": [{"name": "list"}, {"name": "dashboard"}, {"name": "overview"}, {"name": "form"}]}},
    {"name": "Description / Content", "type": "multilineText", "description": "Authored text for overview pages, form description for form pages, or a summary of dashboard elements for dashboard pages."},
    {"name": "Interface", "type": "multipleRecordLinks", "description": "Blank for standalone forms.", "options": {"linkedTableId": "<INTERFACES_TABLE_ID>"}},
    {"name": "Source Table", "type": "multipleRecordLinks", "description": "The table this page reads from/writes to, if any.", "options": {"linkedTableId": "<TABLES_TABLE_ID>"}},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Standalone", "type": "checkbox", "options": {"icon": "check", "color": "greenBright"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

## 6. Automations (links to Bases)

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Automations",
  "description": "One record per automation found in an audited source base.",
  "fields": [
    {"name": "Automation Name", "type": "singleLineText"},
    {"name": "Automation ID", "type": "singleLineText", "description": "Airtable automation ID (wflXXXXXXXXXXXXXX)."},
    {"name": "Description", "type": "multilineText"},
    {"name": "Trigger Type", "type": "singleLineText"},
    {"name": "Trigger Config", "type": "multilineText"},
    {"name": "Actions", "type": "multilineText", "description": "One line per action node: type + description."},
    {"name": "Deployment Status", "type": "singleLineText"},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

## 7. Forms (links to Bases, Tables, and Interfaces)

One record per form found in an audited source base. Forms come from `list_pages_for_base` in
three shapes -- interface pages with `pageType: "form"`, the `standaloneForms` array, and the
`embeddedForms` array (record-creation modals; not navigable pages, so recorded only here, not in
Pages). Create this table **after** Bases, Tables, and Interfaces exist -- it links to all three.
Match/upsert on **Form ID**.

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Forms",
  "description": "One record per form (interface form page, standalone form, or embedded record-creation form) found in an audited source base.",
  "fields": [
    {"name": "Form Name", "type": "singleLineText"},
    {"name": "Form ID", "type": "singleLineText", "description": "Airtable form page ID (pagXXXXXXXXXXXXXX) -- stable match key across runs."},
    {"name": "Form Type", "type": "singleSelect", "options": {"choices": [{"name": "Interface Form"}, {"name": "Standalone"}, {"name": "Embedded"}]}},
    {"name": "Description", "type": "multilineText", "description": "The form's authored description / help text. Embedded forms return no description."},
    {"name": "Source Table", "type": "multipleRecordLinks", "description": "The table this form creates or updates records in.", "options": {"linkedTableId": "<TABLES_TABLE_ID>"}},
    {"name": "Interface", "type": "multipleRecordLinks", "description": "The interface this form belongs to. Blank for standalone forms; for embedded forms, use the first of its interfaceIds.", "options": {"linkedTableId": "<INTERFACES_TABLE_ID>"}},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

Note: interface form pages also appear in the Pages table (as `pageType` "form"); documenting them
here too is intentional -- the Forms table is the single place that unifies all three form kinds
(including embedded forms, which are deliberately excluded from Pages). If the master base already
has a Forms table, reuse it -- and if its primary field is a generic "Name" and its lifecycle field
is named something other than "Status" (e.g. "Audit Status"), map onto whatever exists rather than
renaming the user's columns.

## 8. Change Log (links to Bases)

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Change Log",
  "description": "Run-by-run log of additions, modifications, and removals detected across source bases.",
  "fields": [
    {"name": "Entity Name", "type": "singleLineText"},
    {"name": "Date", "type": "date", "options": {"dateFormat": {"name": "iso", "format": "YYYY-MM-DD"}}},
    {"name": "Base", "type": "multipleRecordLinks", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Entity Type", "type": "singleSelect", "options": {"choices": [{"name": "Base"}, {"name": "Table"}, {"name": "Field"}, {"name": "Interface"}, {"name": "Page"}, {"name": "Automation"}]}},
    {"name": "Change Type", "type": "singleSelect", "options": {"choices": [{"name": "Added"}, {"name": "Modified"}, {"name": "Removed"}]}},
    {"name": "Details", "type": "multilineText"}
  ]
}
```

## 9-11. Permissions layer (optional -- only when documenting collaborators)

These three tables document *who has access to what*. They're populated from the Web API
(`GET /v0/meta/bases/{baseId}?include=collaborators&include=interfaces`), **not** from the MCP
tools -- see `references/permissions-layer.md` for the full rationale, the fetch script, and the
plan/scope/granularity caveats. Create them only if the user asked for permission documentation.
Create **Users** and **Groups** before **Collaborations** (it links to both). Bases and Interfaces
(tables 1 and 4) must already exist.

### 9. Users

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Users",
  "description": "One record per individual collaborator found on any audited base/workspace/interface.",
  "fields": [
    {"name": "Email", "type": "singleLineText"},
    {"name": "User ID", "type": "singleLineText", "description": "Airtable user ID (usrXXXXXXXXXXXXXX) -- stable match key across runs."},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

Note: the collaborators endpoint returns `userId` + `email` but no display name, so there's no
Name field. Email is the human-readable primary; User ID is the upsert merge key.

### 10. Groups

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Groups",
  "description": "One record per user group that collaborates on any audited base/workspace/interface.",
  "fields": [
    {"name": "Group Name", "type": "singleLineText"},
    {"name": "Group ID", "type": "singleLineText", "description": "Airtable group ID -- stable match key across runs."},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

### 11. Collaborations (links to Users, Groups, Bases, Interfaces)

The join table: one record per (collaborator, layer) grant. This is what carries the permission
level and links a user/group to the specific layer they can access.

```json
{
  "baseId": "<MASTER_BASE_ID>",
  "name": "Collaborations",
  "description": "One record per access grant: a user or group's permission on a specific workspace, base, or interface.",
  "fields": [
    {"name": "Collaboration Key", "type": "singleLineText", "description": "Stable unique key '<user|group>:<id>@<layer>:<layerId>' -- the upsert merge field."},
    {"name": "Collaborator Type", "type": "singleSelect", "options": {"choices": [{"name": "User"}, {"name": "Group"}]}},
    {"name": "User", "type": "multipleRecordLinks", "options": {"linkedTableId": "<USERS_TABLE_ID>"}},
    {"name": "Group", "type": "multipleRecordLinks", "options": {"linkedTableId": "<GROUPS_TABLE_ID>"}},
    {"name": "Layer", "type": "singleSelect", "description": "Which access layer this grant is on.", "options": {"choices": [{"name": "Workspace"}, {"name": "Base"}, {"name": "Interface"}]}},
    {"name": "Base", "type": "multipleRecordLinks", "description": "Set for Base and Interface layers.", "options": {"linkedTableId": "<BASES_TABLE_ID>"}},
    {"name": "Interface", "type": "multipleRecordLinks", "description": "Set only for the Interface layer.", "options": {"linkedTableId": "<INTERFACES_TABLE_ID>"}},
    {"name": "Workspace ID", "type": "singleLineText", "description": "Set only for the Workspace layer (wspXXXXXXXXXXXXXX)."},
    {"name": "Permission Level", "type": "singleSelect", "options": {"choices": [{"name": "none"}, {"name": "read"}, {"name": "comment"}, {"name": "edit"}, {"name": "create"}, {"name": "owner"}]}},
    {"name": "Granted By", "type": "multipleRecordLinks", "description": "The user who granted this access (grantedByUserId).", "options": {"linkedTableId": "<USERS_TABLE_ID>"}},
    {"name": "Status", "type": "singleSelect", "options": {"choices": [{"name": "Active"}, {"name": "Removed"}]}}
  ]
}
```

Because "Granted By" and "User" both link to Users, `create_table` will create two reciprocal
fields on the Users table -- that's expected; rename or ignore them as you like.
