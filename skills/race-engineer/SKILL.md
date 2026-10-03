---
name: race-engineer
description: Orient a driver in Braking Lab Race Engineer, check the connected account and plan, and find which MCP actions are available. Use for broad capability or account questions before a specific coaching task is chosen.
---

# Race Engineer

Use the connected Braking Lab MCP through `execute_code`. Its `brakinglab.*` catalog, tool description, and `brakinglab.getFunctionSchema({ name })` define current arguments and behavior. For example, `await brakinglab.whoami({})` identifies the authorized account; `await brakinglab.getCapabilities({})` summarizes available work. Check the exact schema if the connected server differs.

## Orient the driver

1. Confirm the connected account with `whoami` before interpreting empty results. If it is the wrong account, explain that instead of concluding that the driver has no sessions or races.
2. Use `getCapabilities` and, for a specific action, `getFunctionSchema`. Route to the relevant task skill when a goal becomes concrete.
   When the connected server exposes `ray_paddock`, open it for a persistent Paddock workspace. Use `ray_evidence` for the thread evidence panel and `ray_openResource` for an exact session, race, setup, or note identity. The app uses the same authenticated Ray data and policies; do not invent account, readiness, telemetry, or entitlement values when its bootstrap marks a source unavailable.
3. State scope and plan limitations plainly. A Basic account may analyze in chat but cannot save AI coaching reports; do not retry a quota or entitlement refusal with another key or function.

The skills describe common workflows, not an allowlist. Other exposed MCP functions remain usable. Server authorization, quotas, validation, and direct confirmation requirements always apply. Match the driver's language in the response.

When a Paddock resource is attached to model context, use its exact identity as selection, then read current data through Ray. The attachment is neither authorization nor proof that a setup version was driven. Respect removed attachments and preserve the driver's current task. Hardware practice and Capture remain in Braking Lab; open the exact Practice exercise link returned by the server.
