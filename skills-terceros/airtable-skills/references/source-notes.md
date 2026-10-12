# Source Notes and Research Boundaries

Last researched: 2026-07-08.

## Primary official sources

Use Airtable official documentation as the source of truth when exact product behavior matters.

Key public docs used while preparing this skill:

- Supported field types in Airtable overview: https://support.airtable.com/docs/supported-field-types-in-airtable-overview
- Airtable formula field functions reference: https://support.airtable.com/docs/formula-field-reference
- Linking records in Airtable: https://support.airtable.com/docs/linking-records-in-airtable
- Lookup field overview: https://support.airtable.com/docs/lookup-field-overview
- Rollup field overview: https://support.airtable.com/docs/rollup-field-overview
- Getting started with Airtable views: https://support.airtable.com/docs/getting-started-with-airtable-views
- Getting started with Airtable automations: https://support.airtable.com/docs/getting-started-with-airtable-automations
- Scripting extension overview: https://support.airtable.com/docs/scripting-extension-overview
- Airtable permissions overview: https://support.airtable.com/docs/airtable-permissions-overview
- Getting started with Airtable Interface Designer: https://support.airtable.com/docs/getting-started-with-airtable-interface-designer
- Airtable API troubleshooting: https://support.airtable.com/docs/airtable-api-common-troubleshooting
- Airtable Web API: https://airtable.com/developers/web/api/introduction

## Community and practitioner layer

Airtable Community contains large public discussion areas for Base Design, Automations, Development & APIs, Formulas, Interface Designer, MCP, and related builder topics. The practices in this skill synthesize recurring practitioner patterns such as:

- Use separate tables for real entities instead of long-lived select fields.
- Use junction tables when many-to-many relationships need metadata.
- Use narrow automation trigger views and guard fields.
- Resolve linked records explicitly in integrations instead of relying on display names.
- Keep raw data/schema surfaces separate from end-user interfaces.
- Create QA views for missing, failed, stale, duplicate, and blocked records.

Community-derived practices are guidance, not product guarantees. If an answer depends on exact current limits, permissions, pricing, or feature behavior, verify against Airtable's official documentation.

## Versioning policy for this skill

When updating this repository:

1. Re-check Airtable official docs for pages that affect behavior.
2. Update this source note with the research date.
3. Keep references concise and practical.
4. Avoid copying long passages from docs or forum posts.
5. Prefer paraphrased implementation guidance and link to source pages.

## Known limits

This skill does not contain credentials, live Airtable API access, or a full offline copy of Airtable documentation. It guides architecture, documentation, review, and agent-ready implementation. Actual base creation still requires user-approved access through Airtable, an Airtable connector, an automation platform, or manual implementation.
