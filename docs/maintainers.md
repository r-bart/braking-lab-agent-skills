# Maintainer notes

The repository is private during skill validation. Complete the [test plan](test-plan.md) before deciding on plugin packaging or distribution. Changing the repository's visibility to private on 2026-09-26 cannot retract access to content from the period when it was public.

## One skill source, two distribution paths

Keep `skills/` as the only authored copy. The nine `SKILL.md` files use the [Agent Skills format](https://agentskills.io/specification) and contain no Claude- or Codex-only frontmatter. The MCP server remains the source of tools, authentication, authorization, quotas, schemas, and confirmation.

The next packaging step can add two thin platform layers to this same repository:

```text
skills/                         Shared Agent Skills
plugin.json                     OpenAI Agent Plugins manifest, proposed
mcp.json                        OpenAI portable MCP configuration, proposed
.claude-plugin/plugin.json      Claude plugin manifest, proposed
.mcp.json                       Claude MCP configuration, proposed
```

These files are **not present yet**. Their exact schemas and authentication behavior must be checked in each client before release. Do not copy the skills into separate provider repositories or maintain two versions of the workflow text.

Codex and ChatGPT share [OpenAI's public plugin directory](https://developers.openai.com/plugins/concepts/plugins). OpenAI's [portable plugin format](https://developers.openai.com/plugins/build/plugins) uses root `plugin.json` and `mcp.json`; `.codex-plugin/plugin.json` remains a compatibility format. Claude uses [its own plugin manifest](https://code.claude.com/docs/en/plugins-reference) and [marketplace or directory distribution](https://code.claude.com/docs/en/plugin-marketplaces). A GitHub repository is source code, not a listing in either public directory. Submission and approval are separate on the two platforms.

## Current review status

| Check                                                                           | State                                               |
| ------------------------------------------------------------------------------- | --------------------------------------------------- |
| Nine named `SKILL.md` files with valid YAML frontmatter                         | Passed locally                                      |
| Function names against the private MCP `TOOL_CATALOG`                           | Passed on 2026-09-26                                |
| Manual review of report, calendar, notes, setup, and consent boundaries         | Completed on 2026-09-26                             |
| Authenticated MCP behavior on staging                                           | Pending: local connection requires reauthentication |
| Automatic skill selection and output quality in fresh Codex and Claude sessions | Pending                                             |
| Detailed skill test plan                                                        | Written; execution pending                          |
| Claude and OpenAI plugin manifest validation                                    | Pending packaging                                   |
| Public directory review                                                         | Pending                                             |

The source catalog is `braking-lab-monorepo/apps/mcp-server/src/mcp/code-mode/catalog/` in the private project. Published skills must name only functions present in the deployed catalog. A successful YAML check cannot establish correct tool behavior.

## Before a release

1. Validate every skill against the Agent Skills specification. Check names match their folders, descriptions distinguish neighboring skills, and all referenced function names exist in the catalog version being released.
2. Test realistic direct and indirect requests, incomplete inputs, and requests that should use another skill. Compare fresh sessions with and without the skills. Review tool choices and the driver's answer, not just whether a skill loaded. Follow [OpenAI's skill testing guidance](https://developers.openai.com/plugins/build/skills) and [Claude's evaluation guidance](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill).
3. On an authenticated staging account, test wrong-account detection, Basic and paid entitlement refusals, missing telemetry, report quotas, unchanged retry keys, and the destructive calendar and notepad confirmations. Test setup association preview in one turn and commit in a later turn, including a client with and without MCP form elicitation. Never treat chat text as direct server consent.
4. Validate each provider's manifest and connection separately, then test OAuth and skill selection in the actual client surfaces to be claimed. A passing structural validator does not prove end-to-end behavior.
5. Review every public file for private paths, credentials, fixtures, and internal reports. Choose a license and verify required public support, privacy, and publisher details before a directory submission.

## Voice and documentation

User-facing copy follows Braking Lab's landing and docs: direct second person, concrete racing situations, product names left intact, no first-person brand voice, and no claim that a single lap or two-run setup comparison proves a cause. English and Peninsular Spanish should carry the same meaning; Spanish addresses the driver as **tú**. Keep developer contracts in this file and the skills, so the README stays useful to a driver seeing the repository for the first time.
