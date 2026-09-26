---
name: calendar-events
description: Find, create, edit, or delete Braking Lab race calendar events, including events imported from iRacing or LMU schedules.
---

# Race calendar events

Use `execute_code` and `getFunctionSchema` for exact inputs.

1. Locate the event with `getAllRaces` and `getRaceDetail`. Confirm the exact event before editing or deleting; similar series and repeated race weeks can have near-identical names.
2. Create with `createRaceEvent` using name, simulator, series, car, track, and race date. When using an official schedule, inspect the chosen result first, then use `createRaceFromSchedule` or `createRaceFromLMUSchedule`. If the server reports an equivalent existing race, reuse that ID instead of creating a duplicate.
3. Edit with `updateRaceEvent` and pass only changed fields. Omitted fields remain unchanged; `null` does not clear fields. Use an empty string to blank a supported free-text field.
4. For deletion, show the exact race and explain the effect before calling `deleteRaceEvent`: preparations, strategies, notepad links, and coaching reports are removed; linked telemetry sessions remain but become unlinked. Obtain the driver's explicit confirmation for this irreversible action.

Keep calendar maintenance separate from race preparation coaching. Do not infer that a session is linked to a race from a matching track and date.
