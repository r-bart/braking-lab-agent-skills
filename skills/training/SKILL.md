---
name: training
description: Turn a measured Braking Lab braking zone into a pedal exercise and review its exact practice results. Use when a driver asks what to practice, wants a zone exercise, or asks whether practice improved their braking.
---

# Training loop

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

At conversation start verify `whoami`. Check `getCapabilities`, then the supplied input schema of each offered typed operation. Native Code Mode clients may inspect `getFunctionSchema` when that compatibility operation is available. Match the driver's language and keep measured driving evidence separate from pedal practice scores.

1. Inspect the exact session, lap and braking zone through `getSessionDetail`, `getLapTrace` and `getBrakingZones`. Use a measured weakness with enough captured samples; missing timing, channels or zone coverage remain unknown. Do not turn an ordinal corner index into a track turn name.
2. Before creating, explain the selected lap and zone and the intended practice target. Call `createExerciseFromZone` with one stable UUID operation key for that intended write. Preserve that key and the original inputs after timeout; retrying with another key may consume another slot. Report the persisted exercise ID and whether timing was estimated.
3. Open the returned `practiceUrl` in Braking Lab. Practice needs the SPA's pedal input, calibration and audio engine. The embedded Paddock is the exercise and result workbench; do not imply it reads the driver's pedals or controls their simulator.
4. Use `listCustomExercises` to inspect persisted identity and lap/session provenance. Read `readOwnedExerciseResource` for the exact saved `exerciseId` when the connected schema exposes it. Its bounded card rechecks current ownership and reports stored source metadata; it does not contain the full brake curve or prove that the original lap/session is still available. Read `getExerciseResults` filtered by that exact `exerciseId`. Results without stable identity cannot be attributed by name alone. Offline or unsynced Practice results are not available in Ray until cloud sync succeeds.
5. Review score dimensions with `getExerciseResults` and progression with `getBrakeMasterProgress` when relevant. Distinguish limited, unlimited and unknown exercise quota. A failed quota read never means unlimited.
6. Return to on-track evidence after practice. Compare suitable later telemetry using the same measured location and state the observational limit: a better exercise score alone does not establish faster laps or a causal improvement.

Do not evade an entitlement or quota refusal. Recover an already persisted operation with its original key when the server permits it, including after a plan downgrade. If its exercise was deleted or the inputs changed, explain the conflict before proposing a fresh operation.
