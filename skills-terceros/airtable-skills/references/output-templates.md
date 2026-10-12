# Output Templates

## Purpose

Use these templates when producing Airtable deliverables that users can copy into documentation, GitHub issues, agent prompts, implementation plans, or builder tasks.

## Full base blueprint template

```markdown
# Airtable Base Blueprint: <Base Name>

## 1. Executive Summary
<what this base does and who uses it>

## 2. Assumptions
- <assumption>

## 3. Open Questions
- <question>

## 4. Architecture
| Layer | Design |
|---|---|
| Data layer | <tables/entities> |
| Operation layer | <views/statuses/queues> |
| Presentation layer | <interfaces/forms> |
| Automation layer | <automations/scripts> |
| Governance layer | <permissions/docs/audit> |

## 5. Tables
### <Table Name>
Purpose: <purpose>
Grain: one record = <unit>
Primary field: <strategy>

| Field | Type | Required | Source | Example | Notes |
|---|---|---:|---|---|---|

## 6. Relationships
| From | Field | To | Cardinality | Notes |
|---|---|---|---|---|

## 7. Views
| Table | View | Purpose | Filters | Used by automation? |
|---|---|---|---|---:|

## 8. Interfaces and Forms
| Surface | Audience | Purpose | Source | Permissions |
|---|---|---|---|---|

## 9. Automations
| Automation | Trigger | Preconditions | Actions | Failure handling |
|---|---|---|---|---|

## 10. Integrations
| System | Direction | Key | Frequency | Error handling |
|---|---|---|---|---|

## 11. Permissions
| Role | Access | Can edit schema? | Can edit records? | Notes |
|---|---|---:|---:|---|

## 12. Risks
| Risk | Severity | Mitigation |
|---|---|---|

## 13. Implementation Plan
1. <step>
2. <step>

## 14. QA Checklist
- [ ] <check>
```

## JSON blueprint schema

Use this shape when the user wants agent/developer output:

```json
{
  "base": {
    "name": "Example Base",
    "purpose": "Operational system for ...",
    "language": "en",
    "assumptions": [],
    "open_questions": [],
    "tables": [
      {
        "name": "Projects",
        "purpose": "Track projects from intake to completion",
        "grain": "one record per project",
        "primary_field": {
          "name": "Project Name",
          "strategy": "human-readable unique project title"
        },
        "fields": [
          {
            "name": "Status",
            "type": "single_select",
            "required": true,
            "source": "native",
            "options": ["Draft", "Submitted", "In Review", "Approved", "Completed", "Canceled"],
            "description": "Current lifecycle state"
          }
        ]
      }
    ],
    "relationships": [
      {
        "from_table": "Projects",
        "field": "Client",
        "to_table": "Clients",
        "cardinality": "many_to_one",
        "notes": "Many projects can belong to one client"
      }
    ],
    "views": [],
    "interfaces": [],
    "forms": [],
    "automations": [],
    "permissions": [],
    "integrations": [],
    "risks": [],
    "implementation_plan": []
  }
}
```

## Agent implementation prompt template

```markdown
You are implementing an Airtable base from the blueprint below.

Rules:
- Preserve table and field names exactly unless a name is invalid in Airtable.
- Create tables before linked fields.
- Create normal fields before formulas/lookups/rollups that depend on them.
- Rename reciprocal linked fields immediately.
- Create views after fields are complete.
- Create automation trigger views before automations.
- Do not create credentials, tokens, or external webhooks unless explicitly provided by the user.
- After implementation, produce a completion report with created tables, fields, views, automations, skipped items, and manual follow-ups.

Blueprint:
<insert blueprint>
```

## Audit report template

```markdown
# Airtable Base Audit: <Base Name>

## Summary
<short diagnosis>

## Findings
### 1. <Finding>
Severity: <Critical/High/Medium/Low>
Area: <Architecture/Field/View/Automation/API/Permission>
Evidence: <evidence>
Impact: <impact>
Fix: <specific fix>
Regression test: <test>

## Prioritized Fix Plan
| Priority | Fix | Owner | Effort | Risk reduced |
|---:|---|---|---|---|

## Migration Plan
1. <step>

## QA Checklist
- [ ] <check>
```

## Automation spec template

```markdown
### Automation: <Name>
Purpose: <purpose>
Trigger: <trigger>
Trigger source: <table/view/condition>
Preconditions:
- <field/condition>
Actions:
1. <action>
Writes:
- <field/table>
Idempotency:
- <rule>
Failure handling:
- <field/view/notification>
Test cases:
- Happy path
- Missing required data
- Duplicate/retry
- Permission failure
```

## Airtable script request template

```markdown
Write an Airtable Scripting Extension script for this task:

Task: <task>
Run mode: manual / automation
Tables:
- <table>
Input fields:
- <field>
Output fields:
- <field>
Safety:
- dry-run mode required
- do not delete records unless explicitly confirmed
- log skipped records with reasons
Expected final output:
- summary count
- created/updated/skipped/failed rows
```
