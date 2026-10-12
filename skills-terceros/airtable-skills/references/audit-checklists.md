# Airtable Audit Checklists

## Purpose

Use this reference for auditing existing Airtable bases, reviewing generated designs, or preparing a base for production launch.

## Audit scoring

Use this severity scale:

| Severity | Meaning |
|---|---|
| Critical | Can corrupt data, leak sensitive data, create duplicate external side effects, or block operations |
| High | Likely to cause operational failures, reporting errors, or expensive rework |
| Medium | Reduces maintainability or creates avoidable manual work |
| Low | Cosmetic, naming, documentation, or minor UX issue |

## Base architecture audit

Check:

- Does the base have a clear purpose?
- Are table boundaries aligned to real entities?
- Are there mega-tables mixing unrelated concepts?
- Are synced/source tables clearly separated from local workflow tables?
- Is each table's record grain clear?
- Is there a documented source of truth for key fields?
- Are there staging/log tables for imports, webhooks, or sync runs?
- Are there obvious duplicate tables or duplicate business facts?

## Relationship audit

Check:

- Are repeated entities modeled as linked records instead of text/select fields?
- Are many-to-many relationships with metadata modeled through junction tables?
- Are reciprocal linked fields renamed and useful?
- Are lookup fields used instead of duplicated editable fields?
- Are rollups used for aggregates instead of manual totals?
- Are linked record fields limited or filtered where user selection risk is high?
- Are there lookup chains that are too deep to maintain?

## Field audit

Check:

- Is the primary field stable and useful?
- Are required values enforceable through forms, views, formulas, or status gates?
- Are statuses controlled with clear definitions?
- Are select options deduplicated and meaningful?
- Are formulas readable and documented?
- Are computed fields not manually duplicated elsewhere?
- Are technical fields hidden from user-facing views/interfaces?
- Are attachment fields used appropriately?
- Are external IDs present for integrations?

## View audit

Check:

- Does every operational table have working, review, QA, admin, and archive views?
- Are automation views narrow and separate from human working views?
- Are critical automation views locked or protected?
- Are stale, incomplete, duplicate, failed, and blocked records visible?
- Are personal views separated from production views?
- Are view names understandable and ordered?

## Interface/form audit

Check:

- Do non-builders use interfaces/forms instead of raw base tables?
- Are interfaces designed by role?
- Are only relevant fields visible?
- Are forms collecting required data at intake?
- Are form submissions routed to a review state?
- Are shared views exposing sensitive lookup fields or linked records?
- Is there a data leakage review before external sharing?

## Automation audit

Check:

- Does each automation have a purpose and owner?
- Is the trigger narrow and documented?
- Does the automation have guard fields?
- Can the automation loop?
- Are external side effects idempotent?
- Are failure states stored in fields or logs?
- Is there a QA view for failed runs?
- Are test records meaningful?
- Do schema changes require retesting?
- Are automation descriptions updated?

## API/integration audit

Check:

- Are tokens kept out of public docs and prompts?
- Are token scopes minimized?
- Does the integration use stable IDs?
- Are linked records resolved to Airtable record IDs?
- Are select option creation rules explicit?
- Is rate limiting handled?
- Are errors mapped to action steps?
- Is there a dry-run mode for migrations?
- Are sync reports emitted?
- Are partial failures visible and repairable?

## Permission audit

Check:

- Are too many users Creator/Owner?
- Are external collaborators restricted?
- Are interfaces and base permissions aligned?
- Are shared links reviewed?
- Do automations depend on a user whose access may be removed?
- Are table/field edit restrictions compatible with automations and API writes?
- Is sensitive data hidden from non-authorized users?

## Performance and scale audit

Check:

- Are high-volume automations too broad?
- Are lookup/rollup chains excessive?
- Are formulas recalculating across large linked sets unnecessarily?
- Are views overloaded with too many visible fields?
- Are integrations making avoidable API calls?
- Are record limits, attachment usage, and automation limits considered?

## Production readiness checklist

Before launch:

- Field dictionary is documented.
- Status lifecycle is documented.
- Permission matrix is approved.
- Automation specs are documented.
- QA views exist.
- Test data covers happy and failure paths.
- Integration dry-run has passed.
- Backup/export strategy is known.
- Owners are assigned.
- Change control process is agreed.

## Refactor recommendation format

```markdown
### Finding: <Issue>
Severity: Critical/High/Medium/Low
Area: Architecture/Fields/Views/Automation/API/Permissions
Evidence: <what indicates the issue>
Impact: <business/technical risk>
Recommended fix: <specific action>
Migration notes: <how to change safely>
Regression test: <how to confirm fixed>
```
