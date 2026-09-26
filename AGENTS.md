# Agent guidance

This repository distributes the Braking Lab Race Engineer skills. Keep `skills/` as the only authored copy. The Claude, ChatGPT, and portable packages are generated from that directory by `scripts/build_archive.py`; never maintain separate skill text for a provider.

## Package contracts

- Keep the plugin name and version aligned in `plugin.json`, `.claude-plugin/plugin.json`, and both marketplace entries.
- Keep `mcp.json` and `.mcp.json` pointed at the same reviewed production endpoint. Their transport types differ by format.
- Each archive must contain exactly one connection mechanism: Claude uses `.mcp.json`, ChatGPT uses `.app.json`, and portable Agent Plugins uses `mcp.json`.
- `openai/app.json` contains a personal pilot app mapping. Replace it with a reviewed public mapping during submission; an imported private package is not a public directory listing.
- Do not commit credentials, private telemetry, setup corpus files, or staging endpoints into a distributable package.

## Before a release

1. Run `python -m pip install -r requirements-dev.txt` in a virtual environment, then `python scripts/verify_package.py` with `agentskills` on `PATH`.
2. Run `python scripts/build_archive.py` and verify `dist/SHA256SUMS` from inside `dist/`.
3. Run `claude plugin validate . --strict` and check the GitHub Actions run.
4. Test installation and OAuth in each client being claimed. Record outcomes without account identifiers or private session data in `docs/validation/`.
5. Keep the repository and releases private until the gates in `docs/distribution-plan.md` and `docs/test-plan.md` are met. Directory submission and approval are separate from building archives.

Authenticated mutations must follow the MCP server's own consent and confirmation rules. A skill or a chat response does not grant extra permission.
