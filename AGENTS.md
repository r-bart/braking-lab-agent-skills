# Agent guidance

This repository distributes the Braking Lab Race Engineer skills. Keep `skills/` as the only authored copy. The Claude, ChatGPT, and portable packages are generated from that directory by `scripts/build_archive.py`; never maintain separate skill text for a provider.

## Package contracts

- Keep the plugin name and version aligned in `plugin.json`, `.claude-plugin/plugin.json`, and both marketplace entries.
- Keep the Claude marketplace plugin source as `"./"`: the plugin lives at the marketplace root. A `github` source makes Claude Code clone it again over SSH and can fail for public users without a GitHub SSH key. Test a clean install from the hosted marketplace before publishing installation instructions.
- Keep `mcp.json` and `.mcp.json` pointed at the same reviewed production endpoint. Their transport types differ by format.
- Each public archive has exactly one connection mechanism: Claude uses `.mcp.json`, and portable Agent Plugins uses `mcp.json`.
- The private ChatGPT pilot app mapping is deliberately absent from the public source and release. For a public OpenAI submission, send the production MCP endpoint and skills through a new **With MCP** portal draft.
- Do not commit credentials, private telemetry, setup corpus files, or staging endpoints into a distributable package.
- Installation guides must link to release assets or explain how to build locally. `dist/` is ignored and is not a path available after cloning the repository.

## Before a release

1. Run `python -m pip install -r requirements-dev.txt` in a virtual environment, then `python scripts/verify_package.py` with `agentskills` on `PATH`.
2. Run `python scripts/build_archive.py` and verify `dist/SHA256SUMS` from inside `dist/`.
3. Run `claude plugin validate . --strict` and check the GitHub Actions run.
4. Test installation and OAuth in each client being claimed. Record outcomes without account identifiers or private session data in `docs/validation/`.
5. Public beta of the skills and CLI installer can precede directory approval. State tested client behavior accurately; do not present this repo or the installer as a ChatGPT directory listing.

Authenticated mutations must follow the MCP server's own consent and confirmation rules. A skill or a chat response does not grant extra permission.
