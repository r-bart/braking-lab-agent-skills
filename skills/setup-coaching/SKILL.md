---
name: setup-coaching
description: Diagnose handling and propose a testable Braking Lab setup change. Use when a driver reports understeer, oversteer, instability, or another car behavior and wants an explanation or a setup remix; use setup-evaluation to assess a driven change.
---

# Setup coaching

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code`. Check `getFunctionSchema` before mutations; the connected MCP catalog is authoritative. At the start of a conversation, verify the connected account with `whoami` before interpreting missing setups or telemetry.

1. Establish simulator, car, track, conditions, the actual setup/version, and the driver's handling complaint. Use `getCarSetup`, `getCarParamSpace`, `explainSetupParam`, and `getSetupTendencies` for available controls and interpretation. Use telemetry only where the session is compatible; `getSetupTelemetryContext` separates compatibility, attribution, selection quality, and signal availability. Compatible telemetry alone does not prove that the named version was driven.
2. Inspect `getSetupExperimentHistory` before suggesting another change. Explain what is measured, what is subjective, and what remains unknown. Avoid causal claims from two runs.
3. State one handling hypothesis and change one or two adjustable parameters where possible. Explain expected effect and tradeoff. Use `listReferenceSetups` or `buildSetupFromInterview` only when their particular flow fits the request and current schema.
4. If the driver wants a version created, use `remixSetup` with a current base and valid parameter values. For LMU, `valueRaw` is an integer option index; for iRacing, provide the exact garage `valueDisplay` in the base parameter's units. Use one stable `operationKey` for that intended mutation, including uncertain retries. On `SETUP_BASE_MOVED`, refetch and make a deliberate new attempt rather than silently changing the base or key.

An LMU remix can produce a downloadable `.svm`; an iRacing remix may be a recipe. Describe the returned artifact accurately. Do not present a setup suggestion as proven faster until it has been driven and evaluated.
