# Schema Design Reference

## Purpose

Use this reference to produce table schemas, field dictionaries, primary field strategies, lifecycle states, and naming conventions.

## Schema deliverable format

For each table, provide:

- Table name
- Purpose
- Primary field strategy
- Ownership
- Record lifecycle
- Fields
- Linked tables
- Views
- Automations that depend on it
- Risks and notes

## Table definition template

```markdown
### Table: <Table Name>

Purpose: <why this table exists>
Grain: one record = <exact unit>
Owner: <role/team>
Primary field: <field and generation rule>
Source of truth: <native/synced/integration/derived>
Lifecycle: <statuses or states>

| Field | Type | Required | Source | Example | Notes |
|---|---|---:|---|---|---|
```

## Primary field strategy

Airtable requires every table to have a primary field. Choose the primary field deliberately.

Good primary fields:

- Human-readable and unique enough.
- Stable after creation.
- Useful in linked record pickers.
- Often formula-based for transactional records.

Patterns:

| Table type | Primary field pattern |
|---|---|
| People/Companies | Name |
| Products | SKU + Product Name formula |
| Projects | Project Code + Project Name formula |
| Requests | Request ID formula using autonumber |
| Line items | Parent record + item/service formula |
| Logs | Timestamp + event type formula |
| Junction records | Linked A + linked B formula |

Avoid primary fields that are long text notes, formulas with fragile lookups, volatile statuses, or non-unique free-text fields.

## Field dictionary columns

When producing a field dictionary, include:

- Field name
- Field type
- Required/optional
- Editable by users?
- Source of truth
- Validation rule
- Example value
- Used by automations?
- Used in interfaces?
- Used by API/integrations?
- Risk notes

## Field type selection heuristics

| Need | Prefer | Avoid |
|---|---|---|
| Controlled workflow state | Single select | Free text |
| Multiple tags with no metadata | Multi-select | Linked records if no metadata needed |
| Entity with metadata/history | Linked record table | Single/multi-select |
| Derived calculation | Formula | Manual number copied from elsewhere |
| Aggregate over links | Rollup | Manual totals |
| Display linked value | Lookup | Duplicate editable field |
| Unique generated number | Autonumber | Manual ID |
| User assignment | Collaborator | Text email unless integration requires it |
| External integration identity | Single line text `External ID` | Airtable record URL |
| Boolean gate | Checkbox | Status option when only true/false is needed |

## Status modeling

Use explicit statuses. Define allowed transitions when the process matters.

Example status model:

```text
Draft -> Submitted -> In Review -> Approved -> Completed
                         |             |
                         v             v
                      Rejected       Canceled
```

For each status option, define:

- Meaning
- Who can set it
- Required fields before transition
- Automation triggered
- Exit criteria
- Reporting category

## Guard fields

For automation-heavy bases, add guard fields:

| Field | Type | Purpose |
|---|---|---|
| Ready For Automation | Formula or checkbox | Narrow trigger conditions |
| Automation Lock | Checkbox | Prevent duplicate/loop execution |
| Last Automation Run At | Date/time | Observability |
| Last Automation Result | Single select | Success/failure/manual review |
| Automation Error | Long text | Store sanitized error summary |
| Retry Count | Number | Prevent infinite retries |

## Integration fields

For API or sync workflows, add:

| Field | Type | Purpose |
|---|---|---|
| External ID | Single line text | Stable upsert key |
| Source System | Single select | Origin of record |
| Source Record ID | Single line text | Source-side identifier |
| Last Synced At | Date/time | Sync freshness |
| Sync Status | Single select | Pending/Synced/Failed/Skipped |
| Sync Error | Long text | Redacted error message |
| Payload Hash | Single line text | Detect changed payloads |

## Select option governance

For single/multi-select fields:

- Define option names exactly.
- Define meaning and allowed transitions.
- Avoid duplicate meanings such as `Done`, `Completed`, `Finished`.
- Avoid color as the only semantic indicator.
- Avoid allowing integrations to silently create options unless that is an explicit governance decision.

When options need owners, metadata, SLA, pricing, mappings, or lifecycle rules, convert them to a linked table.

## Formula governance

For every formula field, document:

- Inputs
- Output type
- Null/blank behavior
- Error behavior
- Downstream dependencies
- Whether it is used in automation triggers or API filters

Avoid deeply nested formulas when a rules/configuration table would be clearer.

## Required field strategy

Airtable field-level required constraints are limited compared with traditional databases. Enforce completeness with:

- Form required fields for intake.
- Formula fields such as `Missing Required Fields`.
- QA views filtering incomplete records.
- Status transitions that require prerequisites.
- Automation guard fields that only become true when prerequisites pass.

## Schema review checklist

- Does each table have a clear grain?
- Is every repeated entity modeled once?
- Are derived values non-editable?
- Are integration fields stable and explicit?
- Are linked record fields named from the user's perspective?
- Are reciprocal fields renamed and useful?
- Are statuses controlled and documented?
- Are views defined for incomplete and failed records?
- Are fields used by automations clearly marked?
