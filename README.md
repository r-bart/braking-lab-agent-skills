# Race Engineer in your AI assistant

[Español](README.es.md)

Ask about the lap you just drove, the race you are preparing for, or the setup change you want to try. These nine skills help your AI assistant use the **Braking Lab Race Engineer** with your own data. If a signal is missing, the answer should say so. A setup change stays a hypothesis until you try it on track.

| You can ask                                          | Skill              |
| ---------------------------------------------------- | ------------------ |
| “What can my Race Engineer do?”                      | `race-engineer`    |
| “Where did I lose time in my last Spa session?”      | `debrief`          |
| “The car pushes wide on exit. What should I change?” | `setup-coaching`   |
| “Show me the versions of my LMU setup.”              | `setup-library`    |
| “Add next Saturday's race to my calendar.”           | `calendar-events`  |
| “Did the setup change help after I drove it?”        | `setup-evaluation` |
| “Save my braking reference for Turn 3.”              | `track-notes`      |
| “What should I practice before race day?”            | `race-week`        |
| “Compare my last two laps.”                          | `lap-comparison`   |

## Install the public beta

On macOS or Linux, run the interactive installer:

```sh
curl -fsSL https://www.brakinglab.com/install.sh | sh
```

Choose your agent, install location, and skills. The installer downloads a versioned release, checks its SHA-256 digest, and configures the Braking Lab MCP in **Codex** or **Claude Code** when their CLIs are available. You then authorize your Braking Lab account in that client. For **Cursor** or another local agent, it installs the skills and shows the MCP URL; connect the MCP in that agent before asking about your data. [Installation and verification details](docs/install-cli.md).

Alternatively, use [`npx skills add r-bart/braking-lab-agent-skills`](https://www.skills.sh/docs/cli) to install skills through the existing Skills CLI. That route does not configure the MCP. For Claude Code's native plugin, use the [Claude guide](docs/install-claude.md). ChatGPT's public directory listing is still under preparation; see the [ChatGPT status](docs/install-chatgpt.md).

You need a Braking Lab account for data-backed answers. The installer never asks for your Braking Lab password or token. OAuth happens in your AI client.

The skills guide common tasks. They do not limit what the MCP can do, change your plan, or grant extra access. Your connected client can still use other Race Engineer functions. Actions that save or change data remain subject to your Braking Lab permissions and the server's confirmation rules. [See what the Race Engineer can access](https://www.brakinglab.com/en/docs/race-engineer/security).

## Beta status

The nine skills passed format and MCP catalog checks. ChatGPT completed OAuth and reading tasks on one account; Codex staging verified calendar create, update, and delete with readback. Claude Code's first data-backed answer and other clients' end-to-end flows still need validation. The [client support matrix](docs/validation/client-support-matrix.md) records what was observed. A skill installation alone does not connect the Race Engineer.

Source, installer, and release assets are available in this repository. [Maintainer notes](docs/maintainers.md) explain packaging and checks.
