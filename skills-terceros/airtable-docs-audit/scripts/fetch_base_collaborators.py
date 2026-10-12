#!/usr/bin/env python3
"""
Fetch base/workspace/interface collaborators for one or more Airtable bases and
emit them as normalized rows ready to upsert into the master documentation base.

WHY THIS EXISTS
---------------
The Airtable MCP server exposes no collaborator/permission tool, so the "who has
access to what" layer can't come through the skill's normal MCP calls. It DOES come
from the Web API metadata endpoint:

    GET https://api.airtable.com/v0/meta/bases/{baseId}?include=collaborators&include=interfaces&include=inviteLinks

which needs only `schema.bases:read` or `workspacesAndBases:read` (all plans, base
read-only is enough). This script wraps that call so each audit run doesn't have to
re-derive the request and re-parse the (mildly nested) response by hand.

TOKEN HANDLING
--------------
This fetch only READS source bases, so it should use the read-only token. The script
never takes the token as an argument (which would leak it into shell history / process
lists). It reads it, in order of preference, from:
  1. env var AIRTABLE_PAT
  2. an MCP server's Authorization header in ~/.claude.json, trying server names in
     priority order: `airtable-read` (the dedicated read-only server), then `airtable`
     (single-server setup), then `airtable-docs-write` as a last resort.
Nothing about the token is ever printed.

USAGE
-----
    python3 fetch_base_collaborators.py appXXXXXXXXXXXXXX appYYYYYYYYYYYYYY
    python3 fetch_base_collaborators.py --summary appXXXXXXXXXXXXXX   # counts only, no PII

OUTPUT (stdout, JSON)
---------------------
{
  "users":          [{"userId","email"}],                       # de-duped across bases
  "groups":         [{"groupId","name"}],                       # de-duped across bases
  "collaborations": [{"key","collaboratorType","userId","groupId",
                      "layer","baseId","interfaceId","workspaceId",
                      "permissionLevel","grantedByUserId"}],
  "errors":         [{"baseId","error"}]
}
The `key` is a stable, unique upsert merge key: "<user|group>:<id>@<layer>:<layerId>".
"""

import json
import os
import sys
import urllib.request
import urllib.error

API = "https://api.airtable.com/v0/meta/bases/{base}?include=collaborators&include=interfaces&include=inviteLinks"
CLAUDE_JSON = os.path.expanduser("~/.claude.json")

# This fetch reads source bases, so prefer the read-only token. Try server entries in
# priority order: dedicated read server, single-server setup, then the write server.
TOKEN_SERVER_PRIORITY = ["airtable-read", "airtable", "airtable-docs-write"]


def load_token():
    tok = os.environ.get("AIRTABLE_PAT")
    if tok:
        return tok.strip()
    try:
        cfg = json.load(open(CLAUDE_JSON))
        servers = {}
        for proj in cfg.get("projects", {}).values():
            servers.update(proj.get("mcpServers", {}) or {})
        servers.update(cfg.get("mcpServers", {}) or {})
        for name in TOKEN_SERVER_PRIORITY:
            srv = servers.get(name)
            if not srv:
                continue
            auth = srv.get("headers", {}).get("Authorization", "")
            if auth.lower().startswith("bearer "):
                return auth.split(" ", 1)[1].strip()
    except Exception:
        pass
    sys.exit("No Airtable token found (set AIRTABLE_PAT, or configure an 'airtable-read'/'airtable' MCP server in ~/.claude.json).")


def fetch_base(base_id, token):
    req = urllib.request.Request(
        API.format(base=base_id),
        headers={"Authorization": "Bearer " + token},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collab_rows(base_id, data):
    """Flatten one base's response into user, group, and collaboration rows."""
    users, groups, collabs = {}, {}, {}

    def add_user(uid, email=None):
        if uid and uid not in users:
            users[uid] = {"userId": uid, "email": email or ""}
        elif uid and email and not users[uid]["email"]:
            users[uid]["email"] = email

    def add_group(gid, name=None):
        if gid and gid not in groups:
            groups[gid] = {"groupId": gid, "name": name or ""}

    def emit(collab_type, cid, layer, layer_id, perm, granted_by):
        key = f"{collab_type}:{cid}@{layer}:{layer_id}"
        # de-dupe by key: a workspace-level grant is seen once per base in that
        # workspace, but it's one grant -> keep a single row for it.
        collabs[key] = {
            "key": key,
            "collaboratorType": collab_type,   # "user" | "group"
            "userId": cid if collab_type == "user" else "",
            "groupId": cid if collab_type == "group" else "",
            "layer": layer,                    # "workspace" | "base" | "interface"
            "baseId": base_id if layer in ("base", "interface") else "",
            "interfaceId": layer_id if layer == "interface" else "",
            "workspaceId": layer_id if layer == "workspace" else "",
            "permissionLevel": perm or "",
            "grantedByUserId": granted_by or "",
        }
        if granted_by:
            add_user(granted_by)

    def walk(container, layer, layer_id):
        ic = (container or {}).get("individualCollaborators", {}) or {}
        gc = (container or {}).get("groupCollaborators", {}) or {}
        # individualCollaborators / groupCollaborators split into
        # baseCollaborators + workspaceCollaborators at the base level.
        for lst, this_layer in ((ic.get("baseCollaborators"), "base"),
                                (ic.get("workspaceCollaborators"), "workspace")):
            for c in (lst or []):
                add_user(c.get("userId"), c.get("email"))
                # workspace grants use the base's workspaceId as the layer id
                lid = layer_id if this_layer == "base" else workspace_id_holder[0]
                emit("user", c.get("userId"), this_layer, lid, c.get("permissionLevel"), c.get("grantedByUserId"))
        for lst, this_layer in ((gc.get("baseCollaborators"), "base"),
                                (gc.get("workspaceCollaborators"), "workspace")):
            for c in (lst or []):
                add_group(c.get("groupId"), c.get("name"))
                lid = layer_id if this_layer == "base" else workspace_id_holder[0]
                emit("group", c.get("groupId"), this_layer, lid, c.get("permissionLevel"), c.get("grantedByUserId"))

    workspace_id_holder = [data.get("workspaceId", "")]
    walk(data, "base", base_id)

    # Interfaces: keyed object {interfaceId: {..., individual/groupCollaborators}}
    for iface_id, iface in (data.get("interfaces") or {}).items():
        ic = (iface or {}).get("individualCollaborators") or iface.get("collaborators") or {}
        gc = (iface or {}).get("groupCollaborators") or {}
        # interface collaborators may be a flat list or the base-style split
        indiv = ic if isinstance(ic, list) else (ic.get("baseCollaborators") or [])
        grp = gc if isinstance(gc, list) else (gc.get("baseCollaborators") or [])
        for c in indiv:
            add_user(c.get("userId"), c.get("email"))
            emit("user", c.get("userId"), "interface", iface_id, c.get("permissionLevel"), c.get("grantedByUserId"))
        for c in grp:
            add_group(c.get("groupId"), c.get("name"))
            emit("group", c.get("groupId"), "interface", iface_id, c.get("permissionLevel"), c.get("grantedByUserId"))

    return users, groups, collabs


def main():
    args = [a for a in sys.argv[1:] if a != "--summary"]
    summary = "--summary" in sys.argv[1:]
    if not args:
        sys.exit("Usage: fetch_base_collaborators.py [--summary] <baseId> [baseId ...]")

    token = load_token()
    all_users, all_groups, all_collabs, errors = {}, {}, {}, []

    for base_id in args:
        try:
            data = fetch_base(base_id, token)
            if "error" in data:
                errors.append({"baseId": base_id, "error": data["error"]})
                continue
            u, g, c = collab_rows(base_id, data)
            all_users.update(u)
            all_groups.update(g)
            all_collabs.update(c)
        except urllib.error.HTTPError as e:
            errors.append({"baseId": base_id, "error": f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:200]}"})
        except Exception as e:
            errors.append({"baseId": base_id, "error": str(e)})

    if summary:
        print(json.dumps({
            "bases_ok": len(args) - len(errors),
            "users": len(all_users),
            "groups": len(all_groups),
            "collaborations": len(all_collabs),
            "errors": errors,
        }, indent=2))
    else:
        print(json.dumps({
            "users": list(all_users.values()),
            "groups": list(all_groups.values()),
            "collaborations": list(all_collabs.values()),
            "errors": errors,
        }, indent=2))


if __name__ == "__main__":
    main()
