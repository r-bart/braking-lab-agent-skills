---
name: training
description: Turn a measured Braking Lab braking zone into a pedal exercise and review its exact practice results. Use when a driver asks what to practice, wants a zone exercise, or asks whether practice improved their braking.
---

# Training loop

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

At conversation start verify `whoami`. Check `getCapabilities`, then the current schema of each operation with `getFunctionSchema`. Match the driver's language and keep measured driving evidence separate from pedal practice scores.

1. Inspect the exact session, lap and braking zone through `getSessionDetail`, `getLapTrace` and `getBrakingZones`. Use a measured weakness with enough captured samples; missing timing, channels or zone coverage remain unknown. Do not turn an ordinal corner index into a track turn name.
2. Before creating, explain the selected lap and zone and the intended practice target. Call `createExerciseFromZone` with one stable UUID operation key for that intended write. Preserve that key and the original inputs after timeout; retrying with another key may consume another slot. Report the persisted exercise ID and whether timing was estimated.
3. Open the returned `practiceUrl` in Braking Lab. Practice needs the SPA's pedal input, calibration and audio engine. The embedded Paddock is the exercise and result workbench; do not imply it reads the driver's pedals or controls their simulator.
4. Use `listCustomExercises` to inspect persisted identity and lap/session provenance. Read `readOwnedExerciseResource` for the exact saved `exerciseId` when the connected schema exposes it. Its bounded card rechecks current ownership and reports stored source metadata; it does not contain the full brake curve or prove that the original lap/session is still available. Read `getExerciseResults` filtered by that exact `exerciseId`. Results without stable identity cannot be attributed by name alone. Offline or unsynced Practice results are not available in Ray until cloud sync succeeds.
5. Review score dimensions with `getExerciseResults` and progression with `getBrakeMasterProgress` when relevant. Distinguish limited, unlimited and unknown exercise quota. A failed quota read never means unlimited.
6. Return to on-track evidence after practice. Compare suitable later telemetry using the same measured location and state the observational limit: a better exercise score alone does not establish faster laps or a causal improvement.

Do not evade an entitlement or quota refusal. Recover an already persisted operation with its original key when the server permits it, including after a plan downgrade. If its exercise was deleted or the inputs changed, explain the conflict before proposing a fresh operation.
