# Braking Lab Agent Skills

Portable task guidance for using the Braking Lab Race Engineer MCP. Each directory under `skills/` is a standalone Agent Skill with a `SKILL.md` entrypoint. The skills are independent of Claude or Codex plugin packaging.

| Skill | Use it for |
| --- | --- |
| `race-engineer` | Identify the connected account and discover available MCP capabilities |
| `debrief` | Analyze a session and, when requested, save a coaching report |
| `setup-coaching` | Diagnose handling and propose or create a setup remix |
| `setup-library` | Find, inspect, create, and version owned car setups |
| `calendar-events` | Manage race calendar events |
| `setup-evaluation` | Associate setup use, compare confirmed runs, record feedback |
| `track-notes` | Manage corner notes and their race links |
| `race-week` | Prepare for a race using practice, readiness, and strategy |
| `lap-comparison` | Compare compatible laps and explain measured differences |

## Runtime contract

The connected MCP server exposes one tool, `execute_code`, which calls `brakinglab.*` functions. Read its current tool description and use `brakinglab.getFunctionSchema({ name })` for exact arguments before a call; the server catalog is authoritative. The skills guide common workflows, **not the list of allowed actions**. Every function exposed by the MCP remains available without a dedicated skill. Installing a skill does not grant account access, raise quotas, or bypass server validation and confirmation.

The skill text contains no credentials or MCP endpoint. The host must connect the user's Braking Lab account separately. Answer in the user's language.

## Source and validation

Authored against the MCP catalog in `braking-lab-monorepo/apps/mcp-server/src/mcp/code-mode/catalog/` on 2026-09-26. Check function names and behavior against the connected server when using a different deployment or version.

Validate each skill with the Agent Skills `quick_validate.py` validator, then test actual tool use, tier refusals, and mutation boundaries against a test account before distributing a plugin bundle.
