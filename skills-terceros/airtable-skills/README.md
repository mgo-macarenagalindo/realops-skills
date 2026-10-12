# Airtable Skills

Professional Airtable architecture guidance for AI agents.

`airtable-skills` is a repo-ready Skill package for designing, auditing, refactoring, documenting, and implementing Airtable bases with agent-friendly outputs. It helps ChatGPT, Claude, and other SKILL.md-aware agents behave like Airtable solution architects instead of generic spreadsheet assistants.

## What this Skill does

Use it for:

- Designing Airtable bases from zero
- Turning messy spreadsheets into clean Airtable applications
- Creating table schemas, field dictionaries, relationship maps, views, interfaces, forms, automations, and permission matrices
- Auditing existing bases for architecture, field, view, automation, API, and permission risks
- Producing Markdown documentation plus optional JSON blueprints for agents/developers
- Writing implementation prompts for Airtable builders, AI agents, n8n/Make/Zapier workflows, and custom API work

## What this Skill is not

This repository does not contain Airtable credentials, live Airtable API access, or a complete offline copy of Airtable documentation. It is an instruction and reference package for better Airtable reasoning, design, and implementation planning.

## Repository structure

```text
airtable-skills/
├── airtable-skills/             # installable skill folder
│   ├── SKILL.md                 # skill entrypoint
│   ├── agents/openai.yaml       # ChatGPT UI metadata
│   ├── references/              # deeper Airtable architecture references
│   └── scripts/                 # local validation helper
├── dist/skill.zip               # packaged installable skill archive
├── examples/                    # example prompts and outputs
├── docs/                        # repository documentation
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
└── CHANGELOG.md
```

## Installation

### Packaged install

Use `dist/skill.zip` as the packaged skill archive in agent environments that accept zipped skills.

### Folder install

Use the `airtable-skills/` folder directly in agent environments that accept folder-based skills with a `SKILL.md` entrypoint.

Platform requirements change over time, so check the current docs for the agent environment where you are installing it.

## Example prompts

```text
Design a professional Airtable base for vendor onboarding, contract tracking, project delivery, scorecards, and periodic reviews. Give me Markdown documentation and an optional JSON blueprint.
```

```text
Audit this Airtable schema and tell me what is structurally wrong, what will break automations, and how to refactor it safely.
```

```text
Create an Airtable automation spec for moving approved requests into a sync queue, with guard fields, failure handling, and QA views.
```

```text
Turn this spreadsheet into a normalized Airtable design with tables, linked records, views, interfaces, forms, and migration steps.
```

## Included references

The Skill includes focused references for:

- Airtable architecture
- Schema design
- Field types and formulas
- Interfaces, forms, views, and permissions
- Automations and scripting
- API, sync, and integrations
- Audit checklists
- Output templates
- Source notes and research boundaries

## JSON validation helper

The Skill includes a small local helper script:

```bash
python airtable-skills/scripts/validate_schema_json.py examples/sample-blueprint.json
```

It validates the structure of an agent-generated Airtable blueprint JSON. It does not call Airtable and does not require credentials.

## Source approach

The Skill was built from Airtable official documentation plus synthesized practitioner patterns from public Airtable community-style discussions and common implementation experience. Official Airtable documentation should remain the source of truth for exact current limits, permissions, pricing, and product behavior.

## License

MIT. See `LICENSE`.
