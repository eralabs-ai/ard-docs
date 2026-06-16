# Connect GitHub Copilot

GitHub Copilot is the AI coding assistant in VS Code, the other IDEs, the CLI,
and on github.com. Connect it to an Agent Finder either as an **Agent Skill** (a
`SKILL.md` Copilot discovers and activates on its own) or a **remote MCP
connector**. They work well together — the MCP connector gives Copilot the
`search` tool; the Skill gives it the "ask first, never auto-install" behavior.

## Option A — Agent Skill

Copilot supports Agent Skills in **agent mode** — a `SKILL.md` folder it reads
the name and description of, then activates when a request is relevant. It uses
the same `SKILL.md` format and skill folders as Claude, so the connectors repo
skill works without changes.

**Install (copy the folder)** into a directory Copilot scans —
`~/.copilot/skills/` (personal) or `.github/skills/` (project):

```
cp -r connectors/skills/find-agentic-resources ~/.copilot/skills/
```

Copilot also reads `~/.claude/skills/` and `.claude/skills/`, so a skill you
already installed for Claude is picked up automatically.

**Install (from the UI).** In Copilot Chat, open **Configure Chat** (the gear
icon) → the **Skills** tab → **New Skill (User)** or **New Skill (Workspace)**,
name it `find-agentic-resources`, and paste the body of the connectors repo's
[`SKILL.md`](https://github.com/ards-project/connectors/blob/main/skills/find-agentic-resources/SKILL.md).

### How to invoke it

Copilot won't fire this Skill automatically — invoke it explicitly with its
slash command. In **Copilot Chat (Agent mode)**, type `/agentfinder` followed by
what you need:

> `/agentfinder` find me an MCP server for querying Postgres

It asks which Agent Finder to search, queries it, and lists the matches. Pair it
with the MCP connector (Option B) so it can make the call and never auto-installs.

## Option B — Remote MCP connector (VS Code)

> **Default endpoint:** GitHub's Agent Finder at `http://agentfinder.github.com`.
> Replace it to use a different discovery service.

Add the server to your workspace `.vscode/mcp.json`:

```json
{
  "servers": {
    "agent-finder": {
      "type": "http",
      "url": "http://agentfinder.github.com"
    }
  }
}
```

### How to invoke it

Open **Copilot Chat in Agent mode**; the `agent-finder` `search` tool is
available. Ask it to find a capability and it runs the search and lists matches.
Pair with the Skill (Option A) so it asks first and never auto-installs.

## Endpoint

Examples use GitHub's Agent Finder (`agentfinder.github.com`); Hugging Face
Discover (`https://evalstate-hf-discover.hf.space/search`) works the same way.
Point at either — or any compliant ARD discovery service — see
[Endpoints](../connect.md#endpoints).
