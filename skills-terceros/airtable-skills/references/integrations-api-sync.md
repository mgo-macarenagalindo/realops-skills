# Integrations, API, Sync, and Webhooks Reference

## Purpose

Use this reference for Airtable API design, n8n/Make/Zapier workflows, custom sync processes, webhooks, external IDs, rate-limit-aware plans, and error handling.

## Integration design principles

- Use Airtable as an operational source of truth only when the process belongs there.
- Use stable external IDs for upsert. Do not upsert by mutable names.
- Separate user-facing statuses from technical sync statuses.
- Treat API tokens as secrets and never include them in public output.
- Design for retries, partial failure, and duplicate events.
- Log sync runs and rejected records.
- Keep schema changes coordinated with integration changes.

## Standard integration fields

Add these to integration-owned or synced tables:

| Field | Type | Purpose |
|---|---|---|
| External ID | Single line text | Stable key from source/target system |
| Source System | Single select | Name of external system |
| Source Record ID | Single line text | Source-side record ID |
| Last Synced At | Date/time | Freshness |
| Sync Status | Single select | Pending/Synced/Failed/Skipped/Manual Review |
| Sync Error | Long text | Redacted error summary |
| Payload Hash | Single line text | Detect changed payloads |
| Last Payload Snapshot | Long text or attachment | Optional debug, sanitized |

## Upsert strategy

Preferred order:

1. Match by Airtable record ID when updating known existing records.
2. Match by immutable `External ID` when syncing from another system.
3. Match by a compound natural key only if guaranteed stable.
4. Avoid matching by display name unless no better key exists.

When matching by a compound key, create a formula field such as:

```text
LOWER({Source System} & "::" & {External ID})
```

## API safety notes

Airtable API errors commonly include authentication, permissions, invalid request body, invalid select options, mismatched IDs, rate limits, and temporarily retriable errors.

Plan for:

- 401: missing/invalid token.
- 403: token/user lacks access or field/table permissions block the write.
- 404: route/resource missing or wrong endpoint path.
- 422: invalid request body, invalid select option, mismatched base/table/view/record IDs.
- 429: rate limit or plan call limit.
- 5xx/503: retry with backoff when safe.

## Rate-limit-aware workflow

For batch sync:

- Fetch source records.
- Normalize into canonical payloads.
- Validate required fields.
- Deduplicate by external key.
- Resolve linked records before creating child records.
- Batch create/update where possible.
- Throttle requests.
- Retry only safe failures.
- Write a sync report.

## Sync report shape

```json
{
  "report_type": "airtable_sync_report",
  "generated_at": "2026-07-08T00:00:00Z",
  "source_system": "",
  "target_base": "redacted",
  "dry_run": true,
  "summary": {
    "read": 0,
    "created": 0,
    "updated": 0,
    "skipped": 0,
    "failed": 0
  },
  "errors": [],
  "warnings": [],
  "next_actions": []
}
```

## n8n/Make/Zapier guidance

When designing low-code integrations:

- Define exact trigger source.
- Normalize payloads before Airtable writes.
- Resolve linked record IDs explicitly.
- Decide whether missing select options should be created or rejected.
- Use batches to reduce request volume.
- Add dead-letter/error handling.
- Keep credentials in the integration platform, not in prompts or docs.
- Emit a final report object for every run.

## Linked records through integrations

When writing linked records:

- Prefer Airtable record IDs of linked records.
- If you have source IDs, resolve them to Airtable record IDs first.
- Beware writes that try to create a linked record in a synced table or a table where the token lacks permission.
- Avoid sending display names and relying on implicit record creation unless explicitly desired.

## Attachments through API

For attachment writes, provide publicly accessible URLs when required by the API. Do not assume private or expired URLs will remain accessible.

For sensitive workflows, consider storing metadata in Airtable and files in a governed storage system.

## Webhook design

For inbound webhooks:

- Create a staging table for raw incoming events when payload quality is uncertain.
- Store event ID and payload hash.
- Deduplicate before writing operational tables.
- Validate required fields.
- Route invalid records to manual review.
- Keep raw payloads sanitized.

## Sync architecture patterns

### One-way source to Airtable

Use when Airtable is the operational surface but another system owns the facts.

- Source system owns master data.
- Airtable stores read-only synced/derived data plus local operational fields.
- Writes back to source only through explicit workflows.

### Airtable to external system

Use when Airtable is intake/workflow source.

- Airtable owns request/work item.
- External system receives approved/validated records.
- Store returned external ID.
- Use status and error fields.

### Bidirectional sync

Use only when ownership conflicts are solved.

Define:

- Field-level ownership.
- Conflict resolution.
- Last-writer policy or manual review.
- Change detection.
- Audit logs.

## Integration readiness checklist

- External ID field exists and is unique.
- Linked records can be resolved deterministically.
- Select option behavior is defined.
- API token scopes and base access are minimized.
- Field/table permissions are compatible with writes.
- Rate limits and retries are handled.
- Error logging exists.
- Dry-run mode exists for migration/backfill.
- Sync report is produced.
- Rollback or repair process is documented.
