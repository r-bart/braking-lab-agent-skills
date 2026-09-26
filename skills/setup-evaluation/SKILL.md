---
name: setup-evaluation
description: Review which setup version was actually driven, compare confirmed setup usages, associate a session with a setup, and record a driver's subjective evaluation.
---

# Setup evaluation

Use `execute_code` and inspect exact schemas with `getFunctionSchema`. Treat objective comparisons as observational and driver feedback as a separate judgment.

1. Inspect `getCarSetup`, `getSetupTelemetryContext`, and `getSetupExperimentHistory`. Distinguish compatible sessions from attributed or confirmed setup usage. A `ready` telemetry status does not prove which version was driven.
2. Use `compareSetupUsages` only for suitable usages and state selection and signal limits. A two-run comparison is not verified A/B/A evidence, and it cannot establish that a setup caused a lap-time change.
3. To associate a session, call `previewSetupAssociation` first. Present its exact target and consequences, then use `commitSetupAssociation` only after the MCP client collects direct form confirmation. Do not combine preview and commit in the same step. If the client cannot elicit, stop before the write. `retireSetupAssociation` also requires the appropriate current schema and confirmation flow.
4. To save a comparison, `recordSetupComparison` requires two confirmed usages of the same setup and direct MCP client form elicitation. Agent-authored consent text or boolean fields are not approval.
5. To record subjective feedback, take the latest evaluation ID from `getSetupExperimentHistory` and pass it as `expectedEvaluationId` to `recordSetupEvaluation`. After a conflict, refetch and request an explicit retry so an unsaved verdict never moves to another run.

Report measured outcomes, attribution confidence, and the driver's verdict separately. If the evidence is incomplete, say what additional run or confirmation is needed.
