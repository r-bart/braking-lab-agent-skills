# Race Engineer skills 0.2.0 — public beta

The nine skills and their source are available publicly. This release adds a macOS/Linux interactive installer without a Braking Lab npm package. It can copy selected skills for Codex, Claude Code, Cursor, or another local agent. When the Codex or Claude CLI is available, it also adds the production MCP URL; the user authorizes their own Braking Lab account in that client.

Release assets are the Claude plugin ZIP, the portable Agent Plugins ZIP, the versioned shell installer, and `SHA256SUMS`. The public archive no longer contains the personal ChatGPT pilot app mapping. ChatGPT's directory listing remains a separate submission.

The beta does not claim complete OAuth and data-backed workflows in every supported agent. Consult the [observed support matrix](validation/client-support-matrix.md) and [installation guide](install-cli.md). The installer has a local smoke test for nine skills, managed updates, collisions, duplicate selections, and Codex MCP configuration with a mocked CLI.
