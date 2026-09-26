---
name: setup-coaching
description: Diagnose handling from Braking Lab telemetry and driver feedback, explain setup parameters, and propose or create a small, testable setup remix.
---

# Setup coaching

Use `execute_code`. Check `getFunctionSchema` before mutations; the connected MCP catalog is authoritative.

1. Establish simulator, car, track, conditions, the actual setup/version, and the driver's handling complaint. Use `getCarSetup`, `getCarParamSpace`, `explainSetupParam`, and `getSetupTendencies` for available controls and interpretation. Use telemetry only where the session is compatible; `getSetupTelemetryContext` separates compatibility, attribution, selection quality, and signal availability. Compatible telemetry alone does not prove that the named version was driven.
2. Inspect `getSetupExperimentHistory` before suggesting another change. Explain what is measured, what is subjective, and what remains unknown. Avoid causal claims from two runs.
3. State one handling hypothesis and change one or two adjustable parameters where possible. Explain expected effect and tradeoff. Use `listReferenceSetups` or `buildSetupFromInterview` only when their particular flow fits the request and current schema.
4. If the driver wants a version created, use `remixSetup` with a current base and valid parameter values. For LMU, `valueRaw` is an integer option index; for iRacing, provide the exact garage `valueDisplay` in the base parameter's units. Use one stable `operationKey` for that intended mutation, including uncertain retries. On `SETUP_BASE_MOVED`, refetch and make a deliberate new attempt rather than silently changing the base or key.

An LMU remix can produce a downloadable `.svm`; an iRacing remix may be a recipe. Describe the returned artifact accurately. Do not present a setup suggestion as proven faster until it has been driven and evaluated.
