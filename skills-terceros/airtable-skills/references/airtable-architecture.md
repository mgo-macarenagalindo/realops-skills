# Airtable Architecture Reference

## Purpose

Use this reference when designing an Airtable base from zero or refactoring a weak spreadsheet-like base into a durable operational application.

## Architectural mindset

Treat an Airtable base as a lightweight application with:

- A data layer: tables, fields, linked records, formulas, lookups, rollups.
- An operation layer: views, statuses, queues, review surfaces, exception handling.
- A presentation layer: interfaces, forms, dashboards, shared views.
- An automation layer: triggers, actions, scripts, webhooks, integrations.
- A governance layer: permissions, naming, lifecycle ownership, documentation, audit logs.

Do not design from fields first. Design from entities, relationships, lifecycle, and user actions.

## Entity extraction

Create a table when a concept has one or more of these properties:

- It has its own lifecycle or status.
- It has fields beyond a name.
- It is reused across many records.
- It needs owners, permissions, reporting, or historical tracking.
- It is linked to more than one other entity.
- It may later become an integration target.

Keep as a field when the value is simple, low-cardinality, stable, and does not need its own metadata.

### Common entity/table patterns

| Pattern | Use | Examples |
|---|---|---|
| Master entity | Durable source of truth | Customers, Vendors, Products, Employees |
| Transaction/event | Time-bound activity | Orders, Payments, Requests, Meetings |
| Work item | Operational unit | Tasks, Tickets, Projects, Campaigns |
| Junction table | Many-to-many relationship with metadata | Project Assignments, Event Attendees, Product Bundles |
| Configuration table | Rules and options with metadata | SLA Rules, Pricing Tiers, Approval Matrix |
| Log table | Append-only audit/history | Status History, Sync Runs, Automation Errors |
| Staging table | Temporary import/review | CSV Imports, Incoming Webhooks, API Raw Events |

## Relationship modeling

Airtable linked records create relationships between records. Use them deliberately.

### One-to-many

Example: one Customer has many Orders.

- Put a linked record field on `Orders` pointing to `Customers`.
- Airtable creates a reciprocal field on `Customers`.
- Add lookup fields on `Orders` only for values that users need to see locally.
- Add rollups on `Customers` for aggregate values such as total order value.

### Many-to-many

Example: many People attend many Events.

Use a junction table when the relationship itself has fields:

- `People`
- `Events`
- `Event Attendees`
  - Person
  - Event
  - RSVP Status
  - Check-in Time
  - Ticket Type
  - Notes

Avoid a direct multi-linked field if you need per-link metadata, status, dates, scoring, quantity, or audit history.

### Self-links

Use self-linked records for hierarchy or graph relationships:

- Parent Task / Subtasks
- Manager / Direct Reports
- Parent Category / Child Categories
- Duplicate Of / Duplicates

Rename reciprocal fields immediately. Do not leave `From field:` names in production.

## Source-of-truth rules

For every field, assign exactly one source of truth:

- Native entry: user enters it in Airtable.
- Derived: formula/lookup/rollup computes it.
- Synced: external source owns it.
- Integration-owned: API or automation writes it.
- Manual override: user can override, but only in a dedicated override field.

Never allow the same business fact to be editable in multiple places.

## Naming conventions

Choose one convention and keep it stable:

- Tables: plural nouns (`Projects`, `Customers`, `Invoices`).
- Junction tables: relationship names (`Project Members`, `Order Line Items`).
- Status fields: `Status`, `Approval Status`, `Sync Status`.
- Date fields: `Created At`, `Submitted At`, `Approved At`, `Due Date`.
- Integration IDs: `External ID`, `Source System`, `Last Synced At`, `Sync Error`.
- Automation guard fields: `Ready For Automation`, `Automation Lock`, `Last Automation Run At`.

Avoid names like `New Field`, `Notes 2`, `Status Copy`, `Final Final`, `Formula Backup`.

## Base boundary rules

Keep workflows in the same base when:

- They share core entities.
- Users need joined reporting.
- Automations need low-friction linked records.
- Permissions are similar.

Split into separate bases when:

- Permissions are very different.
- Data volume or automation volume is high.
- Teams need independent schema change control.
- One domain is a master data source consumed by many bases.
- You need synced read-only distribution.

## Synced data pattern

When using synced tables:

- Treat the synced table as read-only unless the setup explicitly supports writeback.
- Add local operational fields in local tables, not inside the synced source table when ownership is unclear.
- Link local workflow tables to synced master tables.
- Keep sync provenance fields visible to builders: `Source Base`, `Source Record ID`, `Last Synced At`, `Sync Health`.

## Operational layers

Every production base should have:

- Intake views/forms: collect new work.
- Working views: queues for operators.
- QA views: incomplete, blocked, failed, duplicate, stale.
- Automation views: narrow trigger views with explicit filters.
- Reporting views: grouped/filtered stable reporting surfaces.
- Admin views: all fields, technical fields, integration fields.

## Documentation fields

For complex bases, include a `Base Docs` or `Data Dictionary` table with:

- Object type: table, field, view, automation, interface, form.
- Object name.
- Purpose.
- Owner.
- Source of truth.
- Last reviewed at.
- Change notes.

## Architecture review questions

Ask these before finalizing:

1. Which tables represent durable entities vs temporary work?
2. Which table owns each business fact?
3. Which relationships are one-to-many and which require junction tables?
4. Which fields are editable, computed, synced, or integration-owned?
5. Which users should never see raw builder fields?
6. Which automations can accidentally run too often?
7. Which data needs audit history?
8. Which parts need to survive schema changes?
