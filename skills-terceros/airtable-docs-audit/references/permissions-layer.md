# Permissions layer -- documenting who has access to what

This is the one part of the audit that the Airtable **MCP server can't do**: it exposes no
collaborator/permission tool (only *your own* permission level, via `list_bases` /
`list_workspaces`). The data instead comes from the Web API metadata endpoint, which the bundled
`scripts/fetch_base_collaborators.py` wraps.

Only build this layer when the user actually wants permission documentation -- it pulls real
people's emails and user IDs into the master base, so it's not something to add by default.

## The endpoint

```
GET https://api.airtable.com/v0/meta/bases/{baseId}?include=collaborators&include=interfaces&include=inviteLinks
Authorization: Bearer <PAT>
```

- **Scopes:** `schema.bases:read` *or* `workspacesAndBases:read` (the PAT set up for this skill has
  both). Minimum role: base read-only. Billing: **all plans**.
- Returns, per base: base-level `individualCollaborators` / `groupCollaborators` (each split into
  `baseCollaborators` and `workspaceCollaborators`), and an `interfaces` object keyed by interface
  ID, each with its own collaborators and invite links.
- Individual collaborator = `{userId, email, permissionLevel, grantedByUserId, createdTime}`.
  Group collaborator = `{groupId, name, permissionLevel, grantedByUserId, createdTime}`.
- Deleted collaborators are excluded; only *outstanding* invites are included.

## What "layers" means here -- a real limit worth stating

Airtable grants permission at **workspace -> base -> interface** level, with roles
`owner / create / edit / comment / read / none`. There is **no per-table or per-field
collaborator** concept in the model. So this layer links a user/group down to the base and
interface, and up to the workspace -- but it *cannot* express "who can see field X." If the user
expects field-level permissions, tell them that's not something Airtable's permission model (or
API) represents, rather than leaving them expecting it.

## Fetching

```bash
# normalized rows for one or more bases (JSON on stdout)
python3 scripts/fetch_base_collaborators.py <baseId> [<baseId> ...]

# just counts, no PII -- handy for a dry run / sanity check
python3 scripts/fetch_base_collaborators.py --summary <baseId> ...
```

The script reads the PAT from `AIRTABLE_PAT`, falling back to an MCP server's `Authorization`
header in `~/.claude.json` in priority order `airtable-read` -> `airtable` -> `airtable-docs-write`
(it reads source bases, so it prefers the read-only token). It never takes the token as an argument
and never prints it. Output shape:

```json
{
  "users":          [{"userId", "email"}],
  "groups":         [{"groupId", "name"}],
  "collaborations": [{"key", "collaboratorType", "userId", "groupId",
                      "layer", "baseId", "interfaceId", "workspaceId",
                      "permissionLevel", "grantedByUserId"}],
  "errors":         [{"baseId", "error"}]
}
```

`users`, `groups`, and `collaborations` are already de-duped across every base you pass in (one
workspace grant shared by five bases is a single row, not five).

## Reconciling into the master base

Same upsert-by-stable-ID approach as everything else (see SKILL.md Step 3), in this order so links
resolve:

1. **Users** -- upsert on `User ID`. Build a `userId -> master record ID` map from the response.
2. **Groups** -- upsert on `Group ID`. Build a `groupId -> master record ID` map.
3. **Collaborations** -- upsert on `Collaboration Key`. For each row, set the links from the maps:
   - `User` or `Group` (per `collaboratorType`)
   - `Granted By` -> the Users map (grantedByUserId)
   - `Base` -> your Bases map (for `base`/`interface` layers)
   - `Interface` -> your Interfaces map (for the `interface` layer)
   - `Workspace ID` -> plain text (for the `workspace` layer)
   - `Layer`, `Permission Level`, `Collaborator Type` -> straight copies.

**Removals** work exactly like the rest of the audit: read the existing Active Collaborations,
Users, and Groups once; anything whose stable key you didn't see this run gets Status "Removed"
(never deleted), so a revoked grant is preserved as history rather than vanishing. **Scope this to
the bases you fetched this run** -- a Collaboration whose Base/Interface belongs to a base you
didn't audit is out of scope, not revoked, so leave it Active. Because Users and Groups are shared
across bases, only mark one Removed once it's absent from *every* base still in scope, not just the
subset audited this run.

## Privacy note

These tables contain colleagues' email addresses and user IDs. That's the point of the feature, but
it means the master base is now more sensitive than a pure structure catalog -- worth mentioning to
the user so they set base sharing accordingly, especially before sharing the master base widely.
