---
name: calendar-events
description: Manage a driver's Braking Lab race calendar. Use when they ask to find, add, reschedule, edit, or remove an event, including one from an iRacing or LMU schedule; race preparation belongs to race-week.
---

# Race calendar events

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code` and `getFunctionSchema` for exact inputs. At the start of a conversation, verify the connected account with `whoami`; an empty calendar may mean the wrong account is connected.

1. Locate the event with `getAllRaces` and `getRaceDetail`. Confirm the exact event before editing or deleting; similar series and repeated race weeks can have near-identical names.
2. Create with `createRaceEvent` using name, simulator, series, car, track, and race date. When using an official schedule, inspect the chosen result first, then use `createRaceFromSchedule` or `createRaceFromLMUSchedule`. If the server reports an equivalent existing race, reuse that ID instead of creating a duplicate.
3. Edit with `updateRaceEvent` and pass only changed fields. Omitted fields remain unchanged; `null` does not clear fields. Use an empty string to blank a supported free-text field.
4. For deletion, show the exact race and explain the effect before calling `deleteRaceEvent`: preparations, strategies, notepad links, and coaching reports are removed; linked telemetry sessions remain but become unlinked. Obtain the driver's explicit confirmation for this irreversible action.

Keep calendar maintenance separate from race preparation coaching. Do not infer that a session is linked to a race from a matching track and date.
