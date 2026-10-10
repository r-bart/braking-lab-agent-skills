---
name: track-notes
description: Manage Braking Lab Track Notes. Use when a driver asks to find, add, or change corner references, map pins, or general circuit notes, link notes to a race, or remove a notepad.
---

# Track notes

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code`; inspect `getFunctionSchema` for exact mutation arguments. At the start of a conversation, verify the connected account with `whoami` before interpreting missing notes.

1. Find the right layout, car, and simulator with `getTrackNotepads`; load full content with `getTrackNotepad` before editing. Create a new notepad with `createTrackNotepad` only after checking whether the driver already has one for that context.
2. `updateTrackNotepad` replaces any supplied `cornerNotes`, `pins`, or `videos` array in full. Start from the fetched arrays, change the intended entries, and submit complete revised arrays. Preserve unrelated entries. Put gear, braking landmark, pressure, turn-in, apex, speed, throttle, and exit data in their structured fields; use free-text `notes` for the remainder.
3. Use `linkNotepadToRace` or `unlinkNotepadFromRace` after resolving both exact IDs. A race association is not implied by matching track names.
4. Before `deleteTrackNotepad`, show the exact target and obtain explicit confirmation. Deletion is irreversible and removes its race links, while race events remain.

Telemetry may inform notes, but unknown or ambiguous corner alignment must not be promoted to a precise landmark or measured instruction.
