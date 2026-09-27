# Install Race Engineer skills in a local agent

Use the existing [Skills CLI](https://www.skills.sh/docs/cli) to install from this public repository. It supports selecting skills, agents, and installation scope. You need Node.js and npm; Braking Lab does not publish a separate npm package.

```sh
npx skills add r-bart/braking-lab-agent-skills
```

This installs the skills only. To answer questions about your data, connect the Braking Lab MCP in the same agent and authorize your account:

| Agent                         | MCP connection                                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Codex                         | Run `codex mcp add braking-lab --url https://mcp.brakinglab.com/mcp`, then `codex mcp login braking-lab`.                                               |
| Cursor or another local agent | Add `https://mcp.brakinglab.com/mcp` as a Streamable HTTP MCP server, then complete OAuth in that agent.                                                |
| Claude Code                   | Prefer the [native plugin](install-claude.md), which includes skills and MCP. If you use the Skills CLI instead, add the MCP separately in Claude Code. |

The Skills CLI also works on Windows when Node.js and npm are available. You can inspect the nine available skills without installing them using `npx skills add r-bart/braking-lab-agent-skills --list`. The CLI sends anonymous installation telemetry by default; set `DISABLE_TELEMETRY=1` to opt out.

## Optional installer without Node.js

On macOS or Linux, the Braking Lab shell installer remains available:

```sh
curl -fsSL https://www.brakinglab.com/install.sh | sh
```

It needs `sh`, `curl`, `unzip`, and either `shasum` or `sha256sum`. It downloads a versioned portable release, verifies its SHA-256 digest against the release's `SHA256SUMS`, and copies the selected skills. When the Codex or Claude Code CLI is available, it also configures the MCP. For other agents it prints the MCP URL. Run `sh install.sh --list` on a downloaded copy to see the names, or `sh install.sh --agent codex --scope user --skills all --yes` for an unattended install. On updates, it keeps the previous managed copy in a hidden backup directory beside the skills.

Neither installation route asks for a Braking Lab password or token. A skill without an authenticated MCP connection cannot read your data. After connecting, ask “What can my Braking Lab Race Engineer do?” and then try a question about a session or race in your account.
