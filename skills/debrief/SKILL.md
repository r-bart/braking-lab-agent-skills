---
name: debrief
description: Analyze a Braking Lab telemetry session or stint and identify driving priorities. Use when a driver asks what happened in a run or requests a complete debrief and coaching report; a direct lap-to-lap question belongs to lap-comparison.
---

# Session debrief

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code` and inspect exact function schemas with `brakinglab.getFunctionSchema({ name })` when needed. At the start of a conversation, verify the connected account with `whoami` before interpreting missing sessions.

1. Identify the right run using `getSessions` or `getLatestSession`, then `getSessionDetail`. Resolve ambiguous car, track, date, or stint with the driver.
2. Analyze only available signals: `getCornerAnalysis`, `getBrakingZones`, `getZoneConsistency`, `getDrivingSymptoms`, `getSectorAnalysis`, and relevant traces or lap comparisons. Separate observations from hypotheses. Missing signals and a single matched braking observation cannot establish measured consistency. Align braking observations by location, not zone number alone. For LMU, yaw-derived understeer or oversteer diagnoses are directional, especially when borderline.
3. Give a concise diagnosis with up to three actions for the next practice run. Do not turn a one-off factual question into a saved report.
4. When a complete debrief is requested, call `saveCoachingReport` once as the final result. Reuse one stable `operationKey` UUID if the result is uncertain. Omit `pace`; the server computes measured values. Pass the conversation language as `language` when saving. Report the returned report ID and persistence state.

If the report belongs to a race, find candidates with `getUpcomingRaces` and inspect them with `getRaceDetail`; `getSessionDetail` does not expose race linkage. Ask which race and practice phase to link when uncertain, then `linkSessionToRace` before saving. Linking a session to another race moves it; omitting the practice type clears a previous FP assignment. An omitted `raceEventId` does not auto-link the report. Explain tier, quota, scope, or evidence refusals without trying a fresh key to bypass them. Historical reports may lack the newer measured-evidence snapshot; do not present their old pace as newly certified.
