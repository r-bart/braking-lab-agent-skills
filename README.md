# Race Engineer skills for Braking Lab

[Español](README.es.md)

Ask about the lap you just drove, the race you are preparing for, or the setup change you want to try. These skills help your AI assistant use the **Braking Lab Race Engineer** with your own data. They keep answers close to the evidence: a missing signal is never presented as a measurement, and a setup change stays a hypothesis until you drive it.

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

## Try the Race Engineer

The private pilot package includes the nine skills and the Race Engineer MCP connection. Follow the guide for [Claude](docs/install-claude.md), [ChatGPT](docs/install-chatgpt.md), [Codex](docs/install-codex.md), or [another agent](docs/install-other-agents.md). Then sign in to the Braking Lab account that holds your data and ask a question in your own words.

The skills guide common tasks. They do not limit what the MCP can do, change your plan, or grant extra access. Your connected client can still use other Race Engineer functions. Actions that save or change data remain subject to your Braking Lab permissions and the server's confirmation rules. [See what the Race Engineer can access](https://www.brakinglab.com/en/docs/race-engineer/security).

## Current status

The Claude, ChatGPT, and portable Agent Plugins packages are built from the same nine skills. Their manifests and skill structure have passed local validation. ChatGPT imported the private package, and Claude Code and Codex installed from the private repository. Live checks with an authenticated test account, including skill selection, quota limits, and confirmation flows, are still pending. Neither plugin has a public directory listing yet.

Follow the [test plan](docs/test-plan.md) for verification. The [distribution plan](docs/distribution-plan.md) covers Claude, ChatGPT, and other agents after the tests; packaging details are in [maintainer notes](docs/maintainers.md).
