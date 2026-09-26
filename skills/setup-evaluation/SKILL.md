---
name: setup-evaluation
description: Evaluate a Braking Lab setup after it was driven. Use when a driver asks whether a change helped, which version they used, wants to associate a run, compare confirmed usages, or record their verdict; setup changes belong to setup-coaching.
---

# Setup evaluation

Use `execute_code` and inspect exact schemas with `getFunctionSchema`. At the start of a conversation, verify the connected account with `whoami`. Treat objective comparisons as observational and driver feedback as a separate judgment.

1. Inspect `getCarSetup`, `getSetupTelemetryContext`, and `getSetupExperimentHistory`. Distinguish compatible sessions from attributed or confirmed setup usage. A `ready` telemetry status does not prove which version was driven.
2. Use `compareSetupUsages` only for suitable usages and state selection and signal limits. A two-run comparison is not verified A/B/A evidence, and it cannot establish that a setup caused a lap-time change.
3. To associate a session, call `previewSetupAssociation` first. Show its exact target, warnings, and replacement consequences, then ask for a fresh user decision. In a later turn or execution, call `commitSetupAssociation` with the unchanged preview and token. The server requests direct form confirmation through the MCP client during that call; chat text or an agent-authored boolean never substitutes for it. If the client cannot elicit, the write must fail closed. To retire an association, first identify the exact usage; `retireSetupAssociation` also triggers direct client confirmation.
4. To save a comparison, `recordSetupComparison` requires two confirmed usages of the same setup. The server requests direct form confirmation during the call. Agent-authored consent text or boolean fields are not approval.
5. To record subjective feedback, take the active evaluation ID for that specific usage from `getSetupExperimentHistory` (`null` if none) and pass it as `expectedEvaluationId` to `recordSetupEvaluation`. After a conflict, refetch and request an explicit retry so an unsaved verdict never moves to another run.

Report measured outcomes, attribution confidence, and the driver's verdict separately. If the evidence is incomplete, say what additional run or confirmation is needed.
