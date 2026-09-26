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

## Join the private pilot

You need access to this private repository and a Braking Lab account with your driving data. Get the package from the [0.1.0 pilot release](https://github.com/r-bart/braking-lab-agent-skills/releases/tag/v0.1.0), then follow the guide for [Claude](docs/install-claude.md), [ChatGPT](docs/install-chatgpt.md), [Codex](docs/install-codex.md), or [another agent](docs/install-other-agents.md). Connect your Braking Lab account in the assistant and ask a question in your own words.

The skills guide common tasks. They do not limit what the MCP can do, change your plan, or grant extra access. Your connected client can still use other Race Engineer functions. Actions that save or change data remain subject to your Braking Lab permissions and the server's confirmation rules. [See what the Race Engineer can access](https://www.brakinglab.com/en/docs/race-engineer/security).

## Pilot status

ChatGPT completed sign-in and several read-only tasks on one account. Claude completed sign-in, but the account's usage limit prevented the first answer. Claude Code and Codex installed the plugin; their authenticated workflows still need testing. No write or confirmation flow has been verified, and neither plugin has a public directory listing.

See the [validation record](docs/validation/2026-09-26-packaging.md) for the tests and limits. The [test plan](docs/test-plan.md), [distribution plan](docs/distribution-plan.md), and [maintainer notes](docs/maintainers.md) cover the work before a public release.
