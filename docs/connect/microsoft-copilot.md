# Connect Microsoft Copilot

Microsoft Copilot covers the Copilot app, **Microsoft 365 Copilot**, and
**Copilot Studio**. Its equivalent of a Skill is a **declarative agent** (custom
instructions); to make live calls you add Agent Finder as a **remote MCP** tool.

## Option A — Declarative agent

**Install.** Create (or open) your agent in **Copilot Studio** and paste the
instructions from the connectors repo
([`skills/copilot/`](https://github.com/ards-project/connectors/tree/main/skills/copilot))
as the agent's instructions.

They tell Copilot to ask which Agent Finder to query, present the ranked
results, and never install anything automatically. Pair them with the MCP tool
below so the agent can actually make the call.

### How to invoke it

Ask the agent in plain language — e.g. *"Find me a tool that summarizes long
PDFs."* It asks which Agent Finder to search, queries it, and lists the matches.

## Option B — Remote MCP connector (Copilot Studio)

1. In **Copilot Studio**, open your agent → **Tools → Add a tool → Model Context
   Protocol**.
2. Add a **custom connector** using the **Streamable** MCP transport and your
   discovery service's remote MCP URL (e.g. `http://agentfinder.github.com`).
3. Configure authentication if required, then add the tool to your agent.

### How to invoke it

With the tool added, ask the agent to find a capability for your task; it calls
the Agent Finder `search` tool and lists matches. Pair with the instructions
(Option A) so it asks first and never auto-installs.

## Endpoint

Examples use GitHub's Agent Finder (`agentfinder.github.com`); Hugging Face
Discover (`https://evalstate-hf-discover.hf.space/search`) works the same way.
Point at either — or any compliant ARD discovery service — see
[Endpoints](../connect.md#endpoints).
