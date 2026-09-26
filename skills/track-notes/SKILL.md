---
name: track-notes
description: Find, create, update, or delete Braking Lab track notepads, edit structured corner notes, and link or unlink a notepad from a race.
---

# Track notes

Use `execute_code`; inspect `getFunctionSchema` for exact mutation arguments.

1. Find the right layout, car, and simulator with `getTrackNotepads`; load full content with `getTrackNotepad` before editing. Create a new notepad with `createTrackNotepad` only after checking whether the driver already has one for that context.
2. `updateTrackNotepad` replaces any supplied `cornerNotes`, `pins`, or `videos` array in full. Start from the fetched arrays, change the intended entries, and submit complete revised arrays. Preserve unrelated entries. Put gear, braking landmark, pressure, turn-in, apex, speed, throttle, and exit data in their structured fields; use free-text `notes` for the remainder.
3. Use `linkNotepadToRace` or `unlinkNotepadFromRace` after resolving both exact IDs. A race association is not implied by matching track names.
4. Before `deleteTrackNotepad`, show the exact target and obtain explicit confirmation. Deletion is irreversible and removes its race links, while race events remain.

Telemetry may inform notes, but unknown or ambiguous corner alignment must not be promoted to a precise landmark or measured instruction.
