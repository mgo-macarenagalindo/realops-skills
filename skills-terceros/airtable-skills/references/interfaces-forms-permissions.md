# Interfaces, Forms, Views, and Permissions Reference

## Purpose

Use this reference when designing operational views, forms, interfaces, dashboards, shared views, and permission models.

## Views

Views are operational lenses over the same underlying table data. Design views as workflow surfaces, not as random saved filters.

### Standard view set

For each important table, consider:

| View type | Purpose |
|---|---|
| `00 Admin - All Fields` | Builder/debug view with every field visible |
| `10 Intake - New` | Newly submitted records |
| `20 Working - Active` | Operator queue |
| `30 Review - Pending` | Approval/review queue |
| `40 Done - Completed` | Completed records |
| `80 QA - Missing Required Fields` | Incomplete records |
| `81 QA - Stale Records` | Records inactive too long |
| `82 QA - Failed Automation` | Automation failures |
| `90 Automation - Trigger Name` | Narrow automation trigger view |
| `99 Archive` | Closed/old records |

### View rules

- Use numeric prefixes when ordering matters.
- Keep automation trigger views narrow and documented.
- Lock critical views when possible.
- Do not use one shared view for multiple unrelated automations.
- Keep personal views separate from production workflow views.
- Use view descriptions to document the view's purpose and impact.

## Forms

Forms are intake surfaces. Use them to collect complete records and reduce later cleanup.

Good form design:

- Require fields that are truly mandatory at intake.
- Use help text for ambiguous questions.
- Use conditional visibility when possible.
- Use single/multi-select options instead of free text for controlled values.
- Avoid exposing internal admin fields.
- Route form submissions into an intake/review state, not directly into final approved status.

Form output pattern:

```markdown
### Form: <Name>
Purpose: <who submits and why>
Creates records in: <Table>
Default status: <Status>
Required fields: <list>
Hidden/defaulted fields: <list>
Post-submit automation: <list>
QA view: <view>
```

## Interfaces

Interfaces are user-facing apps over Airtable data. Use interfaces to simplify operational work and hide builder complexity.

Interface design principles:

- Build by role: operator, reviewer, requester, executive, external collaborator.
- Show only fields needed for the user's job.
- Separate create/edit/review/reporting experiences.
- Use detail pages for record-level work.
- Use dashboards for aggregate reporting.
- Avoid exposing technical integration fields to non-builders.
- Use clear labels and field descriptions.

Interface spec template:

```markdown
### Interface: <Name>
Audience: <role/persona>
Purpose: <job to be done>
Pages:
- <Page>: <purpose, source table/view, visible fields, actions>
Permissions: <who can view/edit>
Risks: <what could go wrong>
```

## Permissions

Design permissions before launch. Airtable permissions determine what collaborators can view or edit across workspaces, bases, interfaces, admin panel, forms, and related surfaces.

### Permission matrix template

| Role | Workspace/Base permission | Interfaces | Tables/views | Can edit schema? | Can edit records? | Notes |
|---|---|---|---|---:|---:|---|
| Builder/Admin | Creator/Owner | All | Admin views | Yes | Yes | Schema owner |
| Operator | Editor or interface-only | Operational interfaces | Working views | No | Limited | Day-to-day work |
| Reviewer | Commenter/editor/interface-only | Review interface | Review views | No | Status/notes only | Approval gate |
| Requester | Form/interface-only | Request form/status interface | Own records only if supported | No | Limited | Intake user |
| External collaborator | Minimal | External interface/shared view | Restricted | No | Usually no | Data exposure risk |

### Permission risks

Flag these:

- Everyone is Creator/Owner.
- External users can access raw tables.
- Interfaces hide fields visually but base permissions still allow table access.
- Shared views expose sensitive fields.
- Form links are public without adequate data classification.
- API tokens belong to a human user with excessive access.
- Automations run under an owner whose permissions may change.

## Shared views

Use shared views for read-only publication, not for collaborative editing. If external users need to update data, prefer forms, interfaces with controlled permissions, or an external app/integration.

Before sharing:

- Hide sensitive fields.
- Check linked record fields and lookup fields for indirect data leakage.
- Confirm filters do not expose unexpected records.
- Document who owns the link.
- Define expiration/review cadence.

## Launch readiness checklist

- Critical views are locked or protected.
- Non-builders have interface-first access.
- Raw admin fields are hidden from operational users.
- Forms have required fields and clear help text.
- Shared links are reviewed for sensitive data.
- Permission matrix is documented.
- Each interface page has an owner.
- QA views exist for incomplete, blocked, failed, stale, and duplicate records.
