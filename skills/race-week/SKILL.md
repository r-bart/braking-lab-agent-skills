---
name: race-week
description: Prepare for an existing Braking Lab race using practice, readiness, notes, checklist, and strategy. Use when a driver asks how ready they are or what to do before race day; use calendar-events for event maintenance.
---

# Race week

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code`; inspect current schemas with `getFunctionSchema` before mutations. At the start of a conversation, verify the connected account with `whoami` before interpreting an empty race list.

1. Resolve the exact race with `getUpcomingRaces` or `getAllRaces`, then `getRaceDetail`. Use its linked sessions and notepad IDs as the starting context. Find relevant unlinked practice with `getUnlinkedSessionsForRace`, but get driver confirmation of the race and practice phase before `linkSessionToRace`. Relinking moves a session from its prior race; omitting `practiceType` clears any existing FP assignment.
2. Review `getPreparation` and `getPreparationTemplates`. If the driver wants a plan, collect track and car familiarity plus the race goal, then `createPreparation` using the appropriate template or manual flow. Use `ray_updatePreparation` for preparation-level edits. For phases, use the separate `ray_addPreparationPhase`, `ray_editPreparationPhase` or `ray_deletePreparationPhase` tools. For checklist items, use `ray_addChecklistItem`, `ray_editChecklistItem`, `ray_deleteChecklistItem` or `ray_toggleChecklistItem`. Read the current preparation and show the resulting draft first. Toggle is not idempotent; read back after an uncertain outcome before retrying. The canonical `updatePreparationPhase` and `updateChecklistItem` action unions remain compatibility operations for native Code Mode clients; do not attempt schema discovery or generic execution to recover an operation not offered to the model.
3. Use `getRaceReadinessData` to identify evidence-backed preparation gaps. Save a readiness report with `saveRaceReadinessReport` only when a report is requested; inspect `getRaceReadinessReport` when one already exists. Do not treat an unlinked or merely compatible run as confirmed practice for this event.
4. For strategy, use `generateStrategyFromTelemetry`; surface `missingInputs` and ask for the required race and fuel data. A lap-number run is not a pit-to-pit stint. Save with `saveRaceStrategy` only when the driver wants a persistent strategy and the assumptions are clear; another save replaces that race's existing strategy when the server permits it.
5. Summarize a short race-week plan: next practice focus, open checklist items, known notes, and strategy assumptions. Do not claim unmeasured fuel or tire consumption is observed data.

Use `calendar-events` guidance if the event itself must be created or edited, and `track-notes` guidance for changes to notepad content.
