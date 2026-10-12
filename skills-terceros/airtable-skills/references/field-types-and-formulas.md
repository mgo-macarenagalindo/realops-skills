# Field Types and Formulas Reference

## Purpose

Use this reference when selecting Airtable field types, writing formulas, using lookups/rollups, or translating spreadsheet logic into maintainable Airtable design.

## Official documentation baseline

Airtable's supported field types include primitive, computed, collaborative, linked, and interaction-oriented fields. Current field-type availability and behavior should be checked against Airtable support and developer documentation when precision matters.

## Core field type guidance

### Text fields

Use single line text for identifiers, short labels, slugs, source IDs, or values that must not be interpreted numerically.

Use long text for descriptions, notes, logs, user comments, or copied request text. Do not use long text for structured state.

### Number, currency, percent

Use numeric fields for manually entered measurable values. Use formula or rollup fields for calculated values.

Define:

- Decimal precision
- Currency symbol
- Whether blanks are allowed
- Whether zero means zero or unknown

### Single select

Use for one current state from a controlled list.

Good uses:

- Status
- Priority
- Type
- Risk Level
- Source System

Bad uses:

- Vendor, customer, employee, project, product, or any entity with metadata.
- Values that need history.
- Values that need mappings across systems.

### Multi-select

Use for lightweight tags. Avoid when each selected option needs attributes, status, quantity, owner, or history. Convert to a linked table when tags become operational.

### Linked records

Use to connect records across tables or within the same table. Linked records are the core modeling feature that turns Airtable from a spreadsheet into a relational application.

Use linked records when:

- The connected thing has its own table.
- A user needs to open the related record.
- Lookups or rollups are needed.
- Relationships need reporting.

### Lookup fields

Use lookups to display values from linked records. The source table remains the owner of the value.

Do not manually copy a field into another table when a lookup can display it.

### Rollup fields

Use rollups to aggregate values from linked records. Examples:

- Sum invoice amounts for a customer.
- Average score for a vendor.
- Earliest due date among tasks.
- Count linked items with conditions using formulas and rollups.

### Count fields

Use count fields when only the number of linked records matters. Use rollups when you need conditional counts or aggregation logic.

### Formula fields

Use formulas for deterministic derived values. Formulas should be readable, documented, and tested with edge cases.

### Created/modified time and by fields

Use Airtable-native audit fields to capture operational metadata. Do not ask users to manually enter these values.

### Collaborator fields

Use collaborator fields for assignment and ownership when the people are Airtable collaborators. Use linked `People` or `Users` tables when you need metadata for non-collaborators, external users, or users synced from another system.

### Attachment fields

Use attachment fields for files, not structured data. If file metadata matters, create fields such as `File Type`, `Received At`, `Version`, `Owner`, or a separate `Documents` table.

## Formula design rules

Airtable formulas reference field names directly; fields with spaces or special characters must be wrapped in curly braces. Prefer simple field names in formula-heavy tables.

Good formula style:

```text
IF(
  AND({Status} = "Approved", {Amount} > 0),
  "Ready",
  "Not Ready"
)
```

Formula practices:

- Break complex logic into helper formula fields.
- Name helper fields clearly, e.g. `Has Required Fields`, `Days Until Due`, `Ready For Sync`.
- Use formula fields as automation guards rather than putting all logic in automation filters.
- Make blank/null behavior explicit.
- Test formulas on example records before relying on API `filterByFormula`.

## Formula anti-patterns

Flag these:

- Nested IF formulas that encode a large hidden decision table.
- Formulas depending on unstable field names.
- Formula primary fields that integrations try to write to.
- Formulas used as the only process documentation.
- Cross-table lookup chains that are hard to reason about.
- Circular references between formulas, lookups, and rollups.

## Lookup vs rollup vs formula

| Need | Use |
|---|---|
| Display value from a linked record | Lookup |
| Aggregate values from many linked records | Rollup |
| Calculate value from fields in the same record | Formula |
| Count linked records | Count or rollup |
| Conditionally aggregate linked data | Formula helper + rollup |
| Store user-entered final value | Native field |

## Rule-table pattern

When formulas become too large, create a rules table.

Example: instead of a huge formula to determine approval route:

`Approval Rules`

| Department | Amount Min | Amount Max | Required Approver Role | SLA Days |
|---|---:|---:|---|---:|

Then link requests to rules manually, by automation, or by script. This makes business rules visible and maintainable.

## Primary field formulas

Formula primary fields are useful for transactional or junction records, but avoid making them impossible to understand.

Examples:

```text
"REQ-" & RIGHT("00000" & {Autonumber}, 5)
```

```text
{Project Name} & " - " & {Member Name}
```

Consider using helper lookups to make formulas readable.

## API and formula interaction

When using `filterByFormula` through the API:

- Build the formula in Airtable first as a formula field.
- Confirm which records return truthy values.
- URL-encode formulas in API calls.
- Avoid formulas that depend on locale-specific formatting.
- Avoid changing field names without updating integration filters.

## Field selection checklist

- Is this value manually entered, computed, looked up, rolled up, or synced?
- Does this value need validation?
- Is this value a real entity rather than a field?
- Will this value be used by automations?
- Will this value be used by API filters or upserts?
- Does this value need history?
- Does this value need to be exposed in interfaces?
- Can a non-builder understand the field's purpose?
