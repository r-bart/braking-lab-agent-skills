---
name: setup-evaluation
description: Evaluate a Braking Lab setup after it was driven. Use when a driver asks whether a change helped, which version they used, wants to associate a run, compare confirmed usages, or record their verdict; setup changes belong to setup-coaching.
---

# Setup evaluation

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code` and inspect exact schemas with `getFunctionSchema`. At the start of a conversation, verify the connected account with `whoami`. Treat objective comparisons as observational and driver feedback as a separate judgment.

For direct confirmation operations, prefer the exposed typed tools `ray_commitSetupAssociation`, `ray_retireSetupAssociation`, and `ray_recordSetupComparison`. A modern host completes the server's `input_required` form and retries the unchanged operation with its opaque continuation. Never compose `inputResponses`, request state, or consent booleans yourself. The driver must approve through the client's form. If these typed tools are absent, use the existing `execute_code` operation only when discovery reports direct client elicitation available. If neither mechanism is available, explain the limitation and keep the evidence readable without writing.

1. Inspect `getCarSetup`, `getSetupTelemetryContext`, and `getSetupExperimentHistory`. Distinguish compatible sessions from attributed or confirmed setup usage. A `ready` telemetry status does not prove which version was driven.
2. Use `compareSetupUsages` only for suitable usages and state selection and signal limits. A two-run comparison is not verified A/B/A evidence, and it cannot establish that a setup caused a lap-time change.
3. To associate a session, call `previewSetupAssociation` first. Show its exact target, warnings, and replacement consequences, then ask for a fresh user decision. In a later turn or execution, call `commitSetupAssociation` with the unchanged preview and token. The server requests direct form confirmation through the MCP client during that call; chat text or an agent-authored boolean never substitutes for it. If the client cannot elicit, the write must fail closed. To retire an association, first identify the exact usage; `retireSetupAssociation` also triggers direct client confirmation.
4. To save a comparison, `recordSetupComparison` requires two confirmed usages of the same setup. The server requests direct form confirmation during the call. Agent-authored consent text or boolean fields are not approval.
5. To record subjective feedback, take the active evaluation ID for that specific usage from `getSetupExperimentHistory` (`null` if none) and pass it as `expectedEvaluationId` to `recordSetupEvaluation`. After a conflict, refetch and request an explicit retry so an unsaved verdict never moves to another run.

Report measured outcomes, attribution confidence, and the driver's verdict separately. If the evidence is incomplete, say what additional run or confirmation is needed.
