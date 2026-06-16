# Connect GitHub Copilot

GitHub Copilot is the AI coding assistant in VS Code, the other IDEs, the CLI,
and on github.com. It doesn't use "Skills" — the equivalent is **custom
instructions**, paired with Agent Finder added as a **remote MCP** tool so
Copilot gets a native `search` tool.

## Option A — Custom instructions

**Install.** Add the instructions from the connectors repo
([`skills/copilot/`](https://github.com/ards-project/connectors/tree/main/skills/copilot))
as repository custom instructions — `.github/copilot-instructions.md`.

They tell Copilot to ask which Agent Finder to query, present the ranked
results, and never install anything automatically. Pair them with the MCP tool
below so Copilot can actually make the call.

### How to invoke it

In **Copilot Chat**, ask in plain language — e.g. *"Find me an agent that can
triage GitHub issues."* It asks which Agent Finder to search, queries it, and
lists the matches.

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
Pair with the instructions (Option A) so it asks first and never auto-installs.

## Endpoint

Examples use GitHub's Agent Finder (`agentfinder.github.com`); Hugging Face
Discover (`https://evalstate-hf-discover.hf.space/search`) works the same way.
Point at either — or any compliant ARD discovery service — see
[Endpoints](../connect.md#endpoints).
