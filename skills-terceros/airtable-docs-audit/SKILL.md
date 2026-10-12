---
name: airtable-docs-audit
description: Audits one or more Airtable bases (or an entire connected Airtable workspace) and keeps a master "documentation" base in sync with their live structure -- every table, field (with type, description, and configuration), view, interface, page, form, and automation, all cross-linked to each other and change-logged over time. Use this whenever the user wants to document, catalog, inventory, or audit Airtable bases; wants a "single source of truth" for what's inside their Airtable bases; asks to keep Airtable documentation current on a recurring basis (e.g. weekly); or wants visibility into schema drift, orphaned fields/links, or what changed in a base over time. Trigger even if the user doesn't use the word "audit" -- phrases like "document our Airtable setup," "keep track of every base in my workspace," or "I want a base that shows what's in all our other bases" all mean this skill.
---

# Airtable Documentation Audit

This skill turns a messy sprawl of Airtable bases into one clean, always-current "documentation
base" that describes every other base's structure -- tables, fields, views, interfaces, pages,
forms, and automations -- with real relationships preserved between them (not just a flat dump).

It's meant to be run repeatedly (often on a weekly schedule). Each run reconciles what it finds
against what's already documented: new things get added, changed things get updated in place,
removed things get flagged rather than deleted, and everything is logged in a Change Log.

## Which Airtable connection(s) this uses

This skill runs against **self-added Airtable MCP server(s)** -- Airtable's official remote MCP
(`https://mcp.airtable.com/mcp`) added to your own config with a personal-access token -- rather
than the managed Airtable connector. A self-added server can be **allowlisted once**
(`mcp__<server>` in the project's `allowedTools` / `settings.json`), so the hundreds of write calls
a real audit makes (writes cap at 50 records/call) never trigger the managed connector's per-batch
"always allow" prompt. That allowlisting is what makes large and *scheduled/unattended* runs
possible; the managed connector, which re-prompts run after run, can't.

**Recommended: two servers, split by least privilege.** An Airtable PAT's scopes apply to every
base the token can reach -- you can't say "write here, read-only there" within one token -- so use
two tokens on two server entries:

- **`airtable-read`** -- a read-only token (`schema.bases:read` + `workspacesAndBases:read`; no
  data or write scopes) with access to the **source bases**. Use it for everything that reads a
  source base: `list_bases` / `search_bases`, `list_tables_for_base`, `get_table_schema`,
  `list_views_for_table`, `list_pages_for_base`, `list_automations` / `get_automation`, and the
  collaborators fetch script.
- **`airtable-docs-write`** -- a write token scoped to **only the master base**
  (`schema.bases:read`+`write`, `data.records:read`+`write`). Use it for everything that touches
  the master base: reading its existing tables/records for reconciliation, `create_table`,
  `create_records_for_table`, `update_records_for_table`.

So the routing rule is simply **by base**: source-base operations go through `airtable-read`;
master-base operations go through `airtable-docs-write`. Since the tool names are identical across
both servers, **qualify each call by server** (e.g. `mcp__airtable-read__list_tables_for_base` for a
source base vs `mcp__airtable-docs-write__update_records_for_table` for the master) so it lands on
the right token. Each token also physically can't reach the other's bases (they're not in its
access list), so a mis-route fails loudly rather than doing the wrong thing quietly.

**Single-server setup also works.** If only one self-added server is configured (named `airtable`),
use it for every operation -- the skill's logic is identical; you just give up the least-privilege
split. Either way, make sure you're not falling back to the managed connector: a bare tool name can
resolve to it and reintroduce the prompts.

## Step 0: Figure out scope -- from the tokens

With the two-server split, **the tokens themselves define the scope** -- you generally don't need to
ask. Each PAT's base-access list *is* the configuration:

1. **Which base you're documenting *to* (the master)** = the base the **write** token can reach.
   Call `list_bases` through `airtable-docs-write`. Because that token is scoped to only the master
   base, it returns exactly one base -- that's the master documentation base. (If it returns more
   than one, the write token is scoped too broadly; use the intended master and flag it to the user.)
2. **Which bases to document** = the bases the **read** token can reach. Call `list_bases` through
   `airtable-read`; every base it returns is in scope. To change what gets documented, change the
   read token's base access in Airtable -- the skill follows automatically.

Because the read token is scoped to the source bases and the write token to the master, the two lists
are disjoint by construction: the master never audits itself, and the run physically can't touch
anything outside the tokens' access. That's also what makes unattended/scheduled runs safe -- there's
no way for a run to wander outside its configured scope.

**Overrides and fallbacks:**
- If the user's request (or a scheduled prompt) explicitly names bases or a master, use those.
- If only a **single** `airtable` server is configured (no split), you can't infer scope from token
  access -- ask which master base and which sources (use `AskUserQuestion` when interactive), or fall
  back to the bases already recorded in the master's Bases table.
- If offering to create a brand-new master base, note that the write token must have access to it
  (add the new base to the write PAT's access list in Airtable).

## Step 1: Set up (or verify) the master schema

Call `list_tables_for_base` on the master base first -- don't blindly recreate tables that
already exist. Match by table name. Create whichever of these eight tables are missing. The
exact field layout (copy-pasteable `create_table` payloads) is in `references/master-schema.md`
-- read that file before creating anything, since the linked-record fields must be created in
this order (each depends on the previous table's ID):

1. **Bases** -- one row per audited source base
2. **Tables** -- one row per table, linked to its Base
3. **Fields** -- one row per field, linked to its Table, and (for linked-record fields) linked
   to the Table it points at
4. **Interfaces** -- one row per interface, linked to its Base
5. **Pages** -- one row per page *(this is easy to under-scope -- don't just stuff a text list of
   page names into the Interface record; give pages their own rows, linked to their parent
   Interface and, when applicable, to the source Table they read from)*
6. **Automations** -- one row per automation, linked to its Base
7. **Forms** -- one row per form, linked to its Base and its Source Table, and (for interface and
   embedded forms) its Interface. Covers all three form kinds: interface form pages, standalone
   forms, and embedded (record-creation) forms. See Step 2's form step for where each comes from.
8. **Change Log** -- one row per add/modify/remove detected during a run, linked to its Base

Three more tables -- **Users**, **Groups**, and **Collaborations** -- document *who has access to
what*. Only create these if the user wants permission documentation; they're populated from the Web
API rather than the MCP tools. See Step 2b and `references/permissions-layer.md`.

If the master base already has these tables from a previous run, reuse their existing table and
field IDs (fetch via `list_tables_for_base`) rather than recreating anything.

**A note on Bases-level metadata:** a base itself doesn't have a "description" field in Airtable
-- what it has is a **Base Guide** (the welcome/help content shown when you open a base, editable
from the base's "..." menu). None of the current Airtable connector tools expose a way to read
or write a base's guide content, so leave that field blank / noted as "not retrievable via
current connector tools" rather than treating it as a bug or leaving it mislabeled as a
"description." If a future version of the connector exposes base guide content, wire it in here.

## Step 2: Audit each source base

For every base in scope:

1. `list_tables_for_base` -- gets every table with its fields (id, name, type, description).
   **This will very likely exceed the tool's output size limit for any base of real size** and
   get saved to a local file instead of returned inline. When that happens, don't try to read the
   whole file at once -- see `references/extraction-techniques.md` for the exact search patterns
   that pull out clean table/field records without hitting the limit again.
2. For every field whose type is a linked-record type, you still need to know *which* table it
   links to -- `list_tables_for_base` doesn't include that. Call `get_table_schema`, batching as
   many tables/fields into as few calls as possible, to get each link field's target table.
3. `list_views_for_table` per table, for the Field Count / views context on the Tables row.
4. `list_pages_for_base` -- gets every interface and every page inside it, plus the
   `standaloneForms` and `embeddedForms` arrays. Same truncation risk as step 1 for
   interface-heavy bases; same technique applies.
5. `list_automations` then `get_automation` on each, for full trigger/action detail.
6. **Forms** all come from the `list_pages_for_base` result (no separate call), in three places:
   (a) interface pages with `pageType: "form"`; (b) the top-level `standaloneForms` array (forms
   not attached to an interface -- `interfaceId: null`); and (c) the top-level `embeddedForms`
   array (record-creation modals opened from page buttons -- they carry an `interfaceIds` array but
   are **not** navigable pages, so they are deliberately *not* recorded as Pages, only as Forms).
   Each form exposes an id (`pag…`), name, `sourceTableId` (+ `sourceTableName`), and -- for
   interface and standalone forms -- a `description` (embedded forms return no description). Record
   one **Forms** row per form. If you need a form's field-by-field structure (sections, questions,
   required flags), call `get_form_schema`; that detail is optional and best-effort.

Not every Airtable MCP build exposes the same tool set. If the connected `airtable` server doesn't
offer view tools (`list_views_for_table`) or automation tools (`list_automations` /
`get_automation`), don't treat that as a failure -- skip that step, leave the corresponding master
records/fields blank, and note the gap in the Step 4 report (e.g. "automations not audited -- the
connected server exposes no automation tools"). This mirrors how the Base Guide gap is handled: a
missing capability is recorded honestly, not worked around or silently dropped.

Pull every description you can find (table, field, interface, page, automation) -- even if a
description is empty, that's worth recording as "no description set" so gaps are visible, rather
than silently skipping the field. For the base itself, see the Base Guide note above -- there's
currently no tool-accessible equivalent to a table/field description at the base level.

If a base is large (dozens of tables, hundreds of fields), and you have access to the `Agent`
tool, consider auditing multiple bases in parallel via subagents -- one per base -- rather than
working through them serially. Give each subagent the master schema's exact table/field IDs (from
step 1) so they're all writing into the same structure consistently, and have each one report
back its counts when done.

## Step 2b: Collaborators & permissions (optional -- REST-backed)

Only do this when the user wants to document *who has access to what*. Unlike everything else in
this skill, the collaborator data doesn't come from the MCP tools -- the server exposes no
permission tool. It comes from the Web API, wrapped by a bundled script:

```bash
python3 scripts/fetch_base_collaborators.py <baseId> [<baseId> ...]
```

This returns normalized, de-duped `users`, `groups`, and `collaborations` rows (a collaboration is
one user-or-group's permission on one workspace / base / interface). Read
`references/permissions-layer.md` before running it -- it covers the endpoint and scopes, how the
response maps onto the Users/Groups/Collaborations tables, the upsert/removal reconciliation, and
two things worth telling the user plainly:

- **Granularity stops at base/interface/workspace.** Airtable has no per-table or per-field
  collaborators, so you can't document "who can see field X" -- don't imply otherwise.
- **This adds real PII** (colleague emails and user IDs) to the master base, making it more
  sensitive than a pure structure catalog. Flag that so sharing is set accordingly.

## Step 3: Reconcile into the master base

Everything is matched by the source Airtable ID (base ID, table ID, field ID, page ID, form ID,
automation ID) -- never by name, since names get renamed but IDs don't. Each master table stores that source
ID in its own text field ("Base ID", "Table ID", "Field ID", etc.), and those fields are the match
keys below. Matching on the stable ID is what keeps links intact across runs even when things get
renamed.

**Use native upsert -- don't hand-roll the create-vs-update decision.** `update_records_for_table`
takes a `performUpsert` option: pass `{"fieldIdsToMergeOn": ["<the ID field>"]}` and, for each
record, supply its fields *without* a record `id`. The server then matches on the ID field per
record -- no match creates a new record, one match updates that record in place, and (because
source IDs are unique) you'll never get the multiple-match error or a duplicate. This does the
"new" and "changed" cases from a single batch call, so you don't need to pre-read the whole master
table and diff it yourself. Write one table at a time in dependency order (Bases, then Tables, then
Fields, ...) so parent records exist before children link to them; the upsert response returns each
resulting record's ID, which is how you build the source-ID -> master-record-ID map that the next
table's link fields reference. **Forms** upsert on **Form ID** and must come *after* Tables and
Interfaces exist, since each Form links to its Source Table and (for interface/embedded forms) its
Interface; resolve those links from the Tables and Interfaces source-ID -> record-ID maps.

Two things upsert can't do, which you still handle explicitly:

- **Removals.** Upsert only ever creates or updates -- it can't notice something that vanished from
  the source. So still read the existing Active records for each entity type once (their ID field +
  Status), and for any whose source ID you did *not* encounter this run, set Status to "Removed".
  Don't delete the master record -- leaving it (with its links intact) preserves history and
  anything referencing it. This read is also the cheapest way to know, for the Change Log, which
  upserted records were genuinely new vs. already present. **Scope removals to the bases you
  actually audited this run.** A run often covers only a subset of the tracked bases (scheduled
  runs especially); a record whose parent Base is *not* in this run's scope is out of scope, not
  removed -- leave it Active and untouched. Only compare-and-mark within the bases you fetched, or
  a partial run will wrongly flag everything else as Removed.
- **Relationship rewrites** (e.g. a linked-record field's target table changed) -> these ride along
  in the same upsert; just include the corrected "Links To Table" reference in that field's record.

Writes cap at **50 records per call**, so loop in chunks of 50 -- a base with ~800 fields is
roughly 16 calls. This many write calls is exactly why the `airtable` server must be allowlisted
(see "Which Airtable connection this uses"); an un-allowlisted connector would prompt on every one.

For the Change Log, log one row per Table / Interface / Page / Form / Automation you added, modified,
or marked removed -- not one row per individual Field. The Fields table itself already is the
record of what fields exist; a per-field change-log row on every run adds a lot of noise for
little benefit. If the user wants field-level change history too, that's a reasonable ask --
just confirm with them first, since it multiplies the Change Log's size substantially on bases
with hundreds of fields.

## Step 4: Report back

Summarize what happened: counts added/updated/removed per entity type, per base, plus anything
you couldn't resolve (a link you couldn't match, a description you couldn't retrieve, a base you
had to skip and why). Keep it short -- the master base itself is the detailed record.

## Running on a recurring schedule

Running this skill doesn't make it recur on its own -- an agent only acts when triggered. When the
user wants ongoing documentation, **ask them how often they'd like it to run** rather than assuming
a cadence -- offer sensible options (e.g. weekly, every two weeks, monthly) and, once they pick,
confirm the day and time it should fire. Then create a scheduled task at that cadence (see the
`schedule` skill / the `mcp__scheduled-tasks__create_scheduled_task` tool).

The task's prompt must be self-contained, so the unattended run doesn't need a human to answer
Step 0's questions. Have it name:
- the specific **master base ID**,
- the specific **source bases** (or "entire workspace") to audit,
- whether to include the **permissions layer** (Step 2b) -- confirm this explicitly, since it pulls
  collaborators' emails/user IDs into the master base on every run, and the user may not want PII
  refreshed unattended.

For an unattended run the `airtable` server **must** be allowlisted (see "Which Airtable connection
this uses") -- there's no human present to click "always allow," so any un-approved write batch
would silently stall the whole audit. This is the core reason the skill targets a self-added,
allowlistable server instead of the managed connector.
