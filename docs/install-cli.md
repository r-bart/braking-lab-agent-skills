# Install Race Engineer without npm

The public beta installer runs on macOS and Linux. It needs `sh`, `curl`, `unzip`, and either `shasum` or `sha256sum`. It downloads the versioned portable release from GitHub, verifies its SHA-256 digest against that release's `SHA256SUMS`, and copies the selected skills into your agent's skills directory. It does not run code from the ZIP.

```sh
curl -fsSL https://github.com/r-bart/braking-lab-agent-skills/releases/download/v0.2.0/braking-lab-install-0.2.0.sh | sh
```

The menu asks for an agent (Codex, Claude Code, Cursor, or another local agent), a user-wide or project installation, and which of the nine skills to install. To avoid prompts, download the script and run, for example, `sh install.sh --agent codex --scope user --skills all --yes`. Run `sh install.sh --list` to see the names. The script does not replace a skill directory that it did not install; on updates, it keeps the previous managed copy in a hidden backup directory next to the skills.

## Connect Braking Lab

- **Codex:** If `codex` is on `PATH`, the installer adds `https://mcp.brakinglab.com/mcp` with `codex mcp add`. Run `codex mcp login braking-lab` and authorize your Braking Lab account.
- **Claude Code:** If `claude` is on `PATH`, the installer adds the HTTP MCP at user scope. Open a new Claude session, run `/mcp`, and authorize Braking Lab. The [native plugin](install-claude.md) is another installation route; use one route for the same skills.
- **Cursor or another agent:** The installer copies skills and prints the MCP URL. Configure a Streamable HTTP MCP connection in that client and complete OAuth there. This beta has not verified the full flow in every client.

The installer never asks for a Braking Lab password or token. A skill without an authenticated MCP connection cannot read your data. Ask “What can my Braking Lab Race Engineer do?” after connecting, then try a question about a session or race in your account.

## Alternative installation

`npx skills add r-bart/braking-lab-agent-skills` installs skills through the third-party [Skills CLI](https://www.skills.sh/docs/cli). It does not configure the MCP. The CLI sends anonymous installation telemetry by default; set `DISABLE_TELEMETRY=1` if you prefer not to send it.
