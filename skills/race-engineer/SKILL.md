---
name: race-engineer
description: Orient a driver in Braking Lab Race Engineer, check the connected account and plan, and find which MCP actions are available. Use for opening the Paddock workspace or broad capability and account questions before a specific coaching task is chosen.
---

# Race Engineer

For Code Mode, use the connected Braking Lab MCP through `execute_code`. Its `brakinglab.*` catalog, tool description, and `brakinglab.getFunctionSchema({ name })` define current arguments and behavior. For example, `await brakinglab.whoami({})` identifies the authorized account; `await brakinglab.getCapabilities({})` summarizes available work. Check the exact schema if the connected server differs.

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

## Report opening status accurately

A successful `ray_paddock`, `ray_evidence`, or `ray_openResource` call means the opening request completed, not that the host rendered the interface. Unless the host acknowledges actual visible rendering or the driver confirms it, say that you requested opening the workspace. Do not say it opened successfully or that the integration works based only on a tool result or a loaded resource.

If the host reports an unavailable app or failed rendering, state that the interface could not be opened, even when the tool returned success. Explain the observed failure without inventing a cause. Respect a request to open only: do not create or modify data while checking the UI. One opener result, resource load, or settings check does not establish full integration, end-to-end acceptance, or 100% readiness.

## Orient the driver

1. Confirm the connected account with `whoami` before interpreting empty results. If it is the wrong account, explain that instead of concluding that the driver has no sessions or races.
2. Use `getCapabilities` and, for a specific action, `getFunctionSchema`. Route to the relevant task skill when a goal becomes concrete.
   When the connected server exposes `ray_paddock`, open it for a persistent Paddock workspace. Use `ray_evidence` for the thread evidence panel and `ray_openResource` for an exact session, race, setup, or note identity. The app uses the same authenticated Ray data and policies; do not invent account, readiness, telemetry, or entitlement values when its bootstrap marks a source unavailable.
3. State scope and plan limitations plainly. Use only existing account entitlements. Do not promote subscription upgrades, initiate purchases, collect payment details or link to checkout. Informational account help must not become a sales pitch. A Basic account may analyze in chat but cannot save AI coaching reports; do not retry a quota or entitlement refusal with another key or function.

The skills describe common workflows, not an allowlist. Other exposed MCP functions remain usable. Server authorization, quotas, validation, and direct confirmation requirements always apply. Match the driver's language in the response.

When a Paddock resource is attached to model context, use its exact identity as selection, then read current data through Ray. The attachment is neither authorization nor proof that a setup version was driven. Respect removed attachments and preserve the driver's current task. Hardware practice and Capture remain in Braking Lab; open the exact Practice exercise link returned by the server.
