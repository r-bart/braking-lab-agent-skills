# Maintainer notes

The skills and no-npm CLI installer are released as a public beta before either directory listing. The [test plan](test-plan.md) and [distribution plan](distribution-plan.md) still govern claims about client support and a full product launch.

## One skill source, two distribution paths

Keep `skills/` as the only authored copy. The ten `SKILL.md` files use the [Agent Skills format](https://agentskills.io/specification) and contain no Claude- or Codex-only frontmatter. The MCP server remains the source of tools, authentication, authorization, quotas, schemas, and confirmation.

This repository contains two thin platform layers, two generated archives, and one versioned installer:

```text
skills/                         Shared Agent Skills
plugin.json                     Portable Agent Plugins manifest
mcp.json                        Portable MCP configuration
.claude-plugin/plugin.json      Claude plugin manifest
.claude-plugin/marketplace.json Public Claude Code marketplace
.agents/plugins/marketplace.json Codex marketplace pointing at the same root
.mcp.json                       Claude MCP configuration
install.sh                      Interactive macOS/Linux installer
scripts/build_archive.py        Claude and portable ZIPs plus installer from one skill source
scripts/verify_package.py      Structural and schema checks
```

Run `python scripts/build_archive.py` to create the archives, installer, and `SHA256SUMS` under ignored `dist/`. The Claude archive includes `.mcp.json`; the portable archive includes `mcp.json`. Each has exactly one MCP connection mechanism. The personal ChatGPT pilot mapping is absent from public source and releases. Do not copy the skills into separate provider repositories or maintain two versions of the workflow text.

For a public OpenAI listing, create a new **With MCP** submission in the portal using the production HTTPS endpoint and include the skills in that submission. The personal pilot app ID cannot be submitted as an existing integration reference. The [submission draft](openai-submission-draft.md) contains proposed listing copy and reviewer cases; its fixtures and fields must be verified before use. The [submission requirements](https://developers.openai.com/plugins/deploy/submission) also call for domain verification and OAuth workspace domain support. The current MCP discovery advertises only `race-engineer:read` and `race-engineer:write`; `openid`, `email`, a UserInfo Endpoint, and the domain challenge need separate server work and review in the monorepo before public submission.

Codex and ChatGPT share [OpenAI's public plugin directory](https://developers.openai.com/plugins/concepts/plugins). OpenAI's [portable plugin format](https://developers.openai.com/plugins/build/plugins) uses root `plugin.json` and `mcp.json`; `.codex-plugin/plugin.json` remains a compatibility format. Claude uses [its own plugin manifest](https://code.claude.com/docs/en/plugins-reference) and [marketplace or directory distribution](https://code.claude.com/docs/en/plugin-marketplaces). A GitHub repository is source code, not a listing in either public directory. Submission and approval are separate on the two platforms.

## Current review status

| Check                                                                           | State                                             |
| ------------------------------------------------------------------------------- | ------------------------------------------------- |
| Ten named `SKILL.md` files with valid YAML frontmatter                          | Passed locally                                    |
| Function names against the private MCP `TOOL_CATALOG`                           | Passed on 2026-09-26                              |
| Manual review of report, calendar, notes, setup, and consent boundaries         | Completed on 2026-09-26                           |
| Authenticated MCP behavior on staging                                           | 80 harness cases passed; client limits documented |
| Automatic skill selection and output quality in fresh Codex and Claude sessions | Pending                                           |
| Detailed skill test plan                                                        | Written; execution pending                        |
| Claude and portable plugin manifest validation                                  | Passed locally; public beta release prepared      |
| Public directory review                                                         | Pending                                           |

The source catalog is `braking-lab-monorepo/apps/mcp-server/src/mcp/code-mode/catalog/` in the private project. Published skills must name only functions present in the deployed catalog. A successful YAML check cannot establish correct tool behavior.

## Before a release

1. Validate every skill against the Agent Skills specification. Check names match their folders, descriptions distinguish neighboring skills, and all referenced function names exist in the catalog version being released.
2. Test realistic direct and indirect requests, incomplete inputs, and requests that should use another skill. Compare fresh sessions with and without the skills. Review tool choices and the driver's answer, not just whether a skill loaded. Follow [OpenAI's skill testing guidance](https://developers.openai.com/plugins/build/skills) and [Claude's evaluation guidance](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill).
3. On an authenticated staging account, test wrong-account detection, Basic and paid entitlement refusals, missing telemetry, report quotas, unchanged retry keys, and the destructive calendar and notepad confirmations. Test setup association preview in one turn and commit in a later turn, including a client with and without MCP form elicitation. Never treat chat text as direct server consent.
4. Validate each provider's manifest and connection separately, then test OAuth and skill selection in the actual client surfaces to be claimed. A passing structural validator does not prove end-to-end behavior.
5. Review every public file for private paths, credentials, fixtures, and internal reports. Choose a license and verify required public support, privacy, and publisher details before a directory submission.

## Voice and documentation

User-facing copy follows Braking Lab's landing and docs: direct second person, concrete racing situations, product names left intact, no first-person brand voice, and no claim that a single lap or two-run setup comparison proves a cause. English and Peninsular Spanish should carry the same meaning; Spanish addresses the driver as **tú**. Keep developer contracts in this file and the skills, so the README stays useful to a driver seeing the repository for the first time.
