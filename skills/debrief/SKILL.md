---
name: debrief
description: Debrief a Braking Lab telemetry session or stint, identify evidence-backed driving priorities, and save a coaching report when the driver requests a complete debrief.
---

# Session debrief

Use `execute_code` and inspect exact function schemas with `brakinglab.getFunctionSchema({ name })` when needed.

1. Identify the right run using `getSessions` or `getLatestSession`, then `getSessionDetail`. Resolve ambiguous car, track, date, or stint with the driver.
2. Analyze only available signals: `getCornerAnalysis`, `getBrakingZones`, `getZoneConsistency`, `getDrivingSymptoms`, `getSectorAnalysis`, and relevant traces or lap comparisons. Separate observations from hypotheses. Missing signals and a single matched braking observation cannot establish measured consistency. Align braking observations by location, not zone number alone. For LMU, yaw-derived understeer or oversteer diagnoses are directional, especially when borderline.
3. Give a concise diagnosis with up to three actions for the next practice run. Do not turn a one-off factual question into a saved report.
4. When a complete debrief is requested, call `saveCoachingReport` once as the final result. Reuse one stable `operationKey` UUID if the result is uncertain. Omit `pace`; the server computes measured values. Pass the conversation language as `language` when saving. Report the returned report ID and persistence state.

If the report belongs to a race, find candidates with `getUpcomingRaces` and inspect them with `getRaceDetail`; `getSessionDetail` does not expose race linkage. Ask which race and practice phase to link when uncertain, then `linkSessionToRace` before saving. Linking a session to another race moves it; omitting the practice type clears a previous FP assignment. An omitted `raceEventId` does not auto-link the report. Explain tier, quota, scope, or evidence refusals without trying a fresh key to bypass them. Historical reports may lack the newer measured-evidence snapshot; do not present their old pace as newly certified.
