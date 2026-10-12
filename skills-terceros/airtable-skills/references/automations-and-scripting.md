# Automations and Scripting Reference

## Purpose

Use this reference when designing Airtable automations, scripts, webhook flows, automation-safe views, and operational runbooks.

## Automation model

An automation is a trigger plus one or more actions. Design it as an explicit contract:

- Trigger: what event starts the run.
- Scope: which table/view/condition applies.
- Preconditions: fields that must be present.
- Actions: what the automation changes or sends.
- Idempotency: what prevents duplicate side effects.
- Observability: how success/failure is visible.
- Recovery: what humans do when it fails.

## Preferred trigger strategy

Prefer narrow, deterministic triggers.

| Need | Preferred trigger |
|---|---|
| Start when record becomes complete | Record enters automation-specific view |
| Start after form submission | Form submitted or created record + guard fields |
| Start on status change | Record matches condition or enters view with status filter |
| Scheduled sync/report | Scheduled time |
| External event | Webhook received |
| Manual controlled action | Button click |

Avoid broad `when record updated` triggers unless all watched fields and loop protections are explicit.

## Automation-specific views

For view-triggered automations:

- Create one view per automation or per tightly related automation group.
- Name it `90 Automation - <Action>`.
- Filter only records that are ready.
- Include guard fields and status fields in the view.
- Lock the view when possible.
- Add a view description explaining the automation impact.

## Guard pattern

A robust automation often uses:

- `Status`
- `Ready For Automation` formula
- `Automation Lock` checkbox
- `Last Automation Run At`
- `Last Automation Result`
- `Automation Error`
- `Retry Count`

Example readiness formula concept:

```text
AND(
  {Status} = "Approved",
  {Required Field Count Missing} = 0,
  NOT({Automation Lock})
)
```

## Idempotency

Every automation with external side effects should be idempotent.

Use one or more:

- External ID as upsert key.
- Payload hash to avoid duplicate writes.
- `Sent At` or `Synced At` timestamp.
- `Automation Lock` while processing.
- `Retry Count` limit.
- Status transition after success.

## Automation spec template

```markdown
### Automation: <Name>
Purpose: <business outcome>
Trigger: <trigger type>
Trigger table/view/condition: <source>
Preconditions: <fields/statuses required>
Actions:
1. <action>
2. <action>
Writes to fields: <list>
External systems: <list>
Idempotency rule: <how duplicates are prevented>
Failure handling: <error fields/views/notification>
Test records: <required test cases>
Owner: <role>
Risks: <risks and mitigations>
```

## Testing automations

Test each step after schema changes. Retest when fields, views, trigger records, formulas, permissions, or linked records change.

Minimum test cases:

- Happy path.
- Missing required field.
- Duplicate input.
- Permission-restricted record/field.
- Synced/locked record.
- External API failure.
- Retry path.
- Record no longer matches trigger after update.

## Loop prevention

Flag automation loops when an automation updates a field that can re-trigger the same automation or another automation.

Mitigations:

- Use status transitions with terminal states.
- Set a lock before action and clear only when safe.
- Use separate input and output fields.
- Include `Last Automation Run At` in conditions.
- Use `Retry Count < N`.
- Avoid broad update triggers.

## Run history and failure handling

For production bases:

- Create a QA view for failed automation records.
- Store sanitized error summaries in fields.
- Notify an owner, not a broad channel, for failures.
- Define manual repair steps.
- Review automation revision history during incidents.
- Document dependencies on views and fields.

## Scripting extension

Use scripting when native automations are insufficient for:

- Batch updates.
- Complex validation.
- Multi-step record creation.
- Deduplication.
- Custom matching/linking logic.
- Migration cleanup.

Scripting guidance:

- Keep scripts short and named by purpose.
- Avoid hardcoding field IDs unless intentional.
- Prefer table/field constants at the top.
- Validate required fields before writes.
- Write logs to a log table for repeatable operations.
- Use dry-run mode for destructive or bulk operations.
- Document whether the script runs manually, in an automation, or in an extension.

## Script spec template

```markdown
### Script: <Name>
Run mode: manual / automation / migration
Purpose: <what it changes>
Inputs: <tables, views, config>
Writes: <tables/fields>
Dry-run available: yes/no
Safety checks: <checks>
Rollback: <rollback plan>
```

## Automation anti-patterns

Flag these:

- Triggering on every update in a high-volume table.
- No failure field or QA view.
- No idempotency for email/API/message sending.
- External integration writes to select options without governance.
- Automation depends on a personal view.
- Automation trigger view doubles as an operator view.
- Automation writes to synced or permission-restricted table without checking.
- User-facing status and technical sync status are mixed in one field.

## Release checklist

- Automation has a clear owner.
- Trigger is narrow and documented.
- Required fields are enforced before trigger.
- Test record exists and is meaningful.
- Failure state is visible.
- Notifications are targeted.
- Loop risk is reviewed.
- Permissions are reviewed.
- External side effects are idempotent.
