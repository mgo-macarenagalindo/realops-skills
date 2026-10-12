# Airtable Docs Audit (via MCP)

Living **documentation + change-log** for your Airtable bases — not just a one-off audit.

A [Claude](https://claude.com/claude-code) **skill** (driven through the Airtable **MCP** server)
that turns a sprawl of Airtable bases into one always-current **documentation base** — every table,
field (type, description, configuration), view, interface, page, form, and automation — cross-linked
and **change-logged over time**. Run it on demand or on a schedule; each run reconciles against
what's already documented and appends to a history so you can see how your bases drift.

Optionally, it also documents **who has access** (collaborators and their permission levels).

---

## What it produces

A master "documentation" base with cross-linked tables:

- **Bases → Tables → Fields** (fields link to their table *and* the table they point at),
  **Interfaces → Pages**, and **Automations** — the live structure, with real relationships preserved.
- **Forms** — a dedicated table covering all three Airtable form kinds (interface form pages,
  standalone forms, and embedded record-creation forms), each linked to its Source Table and
  Interface. Optional deeper per-form field detail (sections, questions, required flags) via
  `get_form_schema`.
- **Change Log** — a run-by-run record of every addition, modification, and removal. This is your
  **history**: what changed, when, and in which base.
- **Users / Groups / Collaborations** *(optional)* — who can access what, down to the
  base / interface / workspace level.

Everything is matched on **stable Airtable IDs** (`app…`, `tbl…`, `fld…`), so renames never create
duplicates, and anything that disappears from a source base is marked **Removed** (never deleted) —
which is what preserves the history and keeps any links intact.

---

## How it works: two least-privilege access tokens

The skill runs against Airtable's official remote MCP server (`https://mcp.airtable.com/mcp`), added
as **your own** MCP server with a personal access token (PAT) — not the managed Airtable connector,
which re-prompts for approval on every write batch and can't be allowlisted for unattended runs.

It uses **two PATs**, and **the tokens define the scope**:

| MCP server | PAT | Access (in Airtable) | Role |
|---|---|---|---|
| `airtable-read` | read-only | the **source** bases you want documented | the skill documents exactly these |
| `airtable-docs-write` | write | **only** the master documentation base | the skill writes the docs + Change Log here |

An Airtable PAT's scopes apply to *every* base it can reach, so you can't say "write here, read-only
there" within one token — splitting into two is the only way to get read-only sources + a writable
master. A nice side effect: **you configure scope in Airtable.** The read token's base-access list
*is* the list of bases that get documented. Add a base to the read token → it gets documented on the
next run. The write token's single base is the destination. Neither token can touch the other's
bases, so a run physically can't wander out of scope — which is what makes scheduled/unattended runs
safe.

---

## Setup

### 1. Create two Airtable personal access tokens

[Airtable → Developer hub → Personal access tokens](https://airtable.com/create/tokens)

| Token | Scopes | Access (bases) |
|---|---|---|
| **Read** (e.g. "Docs — Read") | `schema.bases:read`, `workspacesAndBases:read`, `automations:read` *(read-only — no write scopes)* | the source bases you want documented |
| **Write** (e.g. "Docs — Write") | `schema.bases:read` + `schema.bases:write`, `data.records:read` + `data.records:write` | **only** the master documentation base |

> The read token doesn't need `data.records:read` — the skill reads *structure*, not your record data.
> Add `data.recordComments:read` etc. only if you extend it.

### 2. Add two MCP servers to Claude Code / the Claude desktop app

In `~/.claude.json`, under your project's `mcpServers` (or via `claude mcp add --transport http …`):

```json
"airtable-read": {
  "type": "http",
  "url": "https://mcp.airtable.com/mcp",
  "headers": { "Authorization": "Bearer patYOUR_READ_TOKEN" }
},
"airtable-docs-write": {
  "type": "http",
  "url": "https://mcp.airtable.com/mcp",
  "headers": { "Authorization": "Bearer patYOUR_WRITE_TOKEN" }
}
```

> ⚠️ **Keep the `Bearer ` prefix.** Pasting the raw `pat…` token without `Bearer ` in front is the
> most common mistake and fails with a 401.

### 3. Allowlist the servers so batch writes don't prompt

In your project's `.claude/settings.json`:

```json
{ "permissions": { "allow": ["mcp__airtable-read", "mcp__airtable-docs-write"] } }
```

### 4. Install the skill

Drop this folder into your skills directory so it's discoverable — e.g.:

```bash
git clone https://github.com/davepongw/airtable-docs-audit-via-mcp.git ~/.claude/skills/airtable-docs-audit
```

(Exact location depends on your Claude setup; anywhere your skills are loaded from works. Note the
repo is `airtable-docs-audit-via-mcp`, but clone it into a folder named **`airtable-docs-audit`** —
that must match the skill's `name` so it loads correctly.)

### 5. Restart & run

Restart the app so the new MCP servers connect, then ask Claude something like *"document my Airtable
bases"* or invoke the skill by name.

---

## Running it

- **Interactive** — just ask. The skill reads scope from the tokens (read token → source bases, write
  token → master), sets up the master schema if needed, audits each source base, and reconciles.
- **Scheduled** — set up a recurring task (e.g. weekly). Each run appends to the **Change Log**, so
  the history builds up automatically. The self-contained scheduled prompt should name the master
  base and source bases (or rely on the token scope). Because the servers are allowlisted, unattended
  runs never stall on an approval prompt.

### The history / Change Log

The value compounds over time: because every run matches on stable IDs and writes a Change Log row
per added/modified/removed table, interface, page, or automation, you get a running record of schema
drift — new tables, renamed fields, deleted automations — without ever losing the prior state
(removed items are flagged, not deleted).

---

## Optional: permissions layer

The skill can also document collaborators. Airtable's MCP exposes no permission tool, so this uses
the Web API (`GET /v0/meta/bases/{baseId}?include=collaborators&interfaces`) via
`scripts/fetch_base_collaborators.py`, which reads the read-only token from your config. See
`references/permissions-layer.md`. Note this writes colleague emails/user IDs into the master base —
set that base's sharing accordingly. Granularity is base / interface / workspace (Airtable has no
per-field collaborators).

---

## Gotchas

- **`Bearer ` prefix** required on both tokens.
- **Desktop app env vars** aren't inherited from your shell — store tokens in the config file
  (`chmod 600 ~/.claude.json`), not `~/.zshrc`.
- **New MCP servers connect on restart** — quit and reopen after editing the config.
- **Token expiry** — an expired PAT silently breaks a scheduled run; use non-expiring tokens or a
  rotation reminder.
- **Scope-safe removals** — a run only marks records "Removed" for the bases it actually audited, so
  partial/scheduled runs don't flag out-of-scope records.

---

## Repository layout

```
airtable-docs-audit/
├── SKILL.md                          # the skill: workflow, connection routing, reconciliation
├── references/
│   ├── master-schema.md              # exact create_table payloads for every table
│   ├── extraction-techniques.md      # handling large bases + write batching
│   └── permissions-layer.md          # collaborators endpoint + reconciliation
└── scripts/
    └── fetch_base_collaborators.py   # REST collaborator fetch (optional permissions layer)
```

## License

MIT — see [LICENSE](LICENSE).
