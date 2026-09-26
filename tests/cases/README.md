# Skill routing corpus

`skill-routing.json` contains 54 prompts: direct, indirect and boundary cases for
each of the nine skills, in Spanish and English. Each boundary case names the
skill expected instead of assuming that every prompt belongs to its containing
group.

Run `python3 scripts/evaluate_routing.py` after installing the candidate Codex
plugin. It starts a fresh, ephemeral Codex CLI session for every prompt and
records the first plugin skill file loaded in `dist/routing-results.json`.
The runner adds an instruction to avoid MCP calls and account access. It tests
selection only; it does not verify tool choices, data interpretation or
mutation safety. Those require the staging cases in `docs/test-plan.md`.
It also pins Codex to a read-only sandbox with approval requests denied and
does not keep model replies in its output file.
