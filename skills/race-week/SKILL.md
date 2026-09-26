---
name: race-week
description: Prepare for an existing Braking Lab race using linked practice sessions, readiness, preparation checklist, track notes, and telemetry-based strategy.
---

# Race week

Use `execute_code`; inspect current schemas with `getFunctionSchema` before mutations.

1. Resolve the exact race with `getUpcomingRaces` or `getAllRaces`, then `getRaceDetail`. Use its linked sessions and notepad IDs as the starting context. Find relevant unlinked practice with `getUnlinkedSessionsForRace`, but get driver confirmation of the race and practice phase before `linkSessionToRace`. Relinking moves a session from its prior race; omitting `practiceType` clears any existing FP assignment.
2. Review `getPreparation` and `getPreparationTemplates`. If the driver wants a plan, collect track and car familiarity plus the race goal, then `createPreparation` using the appropriate template or manual flow. Use `updatePreparation`, `updatePreparationPhase`, and `updateChecklistItem` for later progress.
3. Use `getRaceReadinessData` to identify evidence-backed preparation gaps. Save a readiness report with `saveRaceReadinessReport` only when a report is requested; inspect `getRaceReadinessReport` when one already exists. Do not treat an unlinked or merely compatible run as confirmed practice for this event.
4. For strategy, use `generateStrategyFromTelemetry`; surface `missingInputs` and ask for the required race and fuel data. A lap-number run is not a pit-to-pit stint. Save with `saveRaceStrategy` only when the driver wants a persistent strategy and the assumptions are clear; another save replaces that race's existing strategy when the server permits it.
5. Summarize a short race-week plan: next practice focus, open checklist items, known notes, and strategy assumptions. Do not claim unmeasured fuel or tire consumption is observed data.

Use `calendar-events` guidance if the event itself must be created or edited, and `track-notes` guidance for changes to notepad content.
