---
name: lap-comparison
description: Compare Braking Lab laps and explain measured time or braking differences. Use when a driver asks to compare their own laps or an owned lap with a public leaderboard reference; a full session debrief belongs to debrief.
---

# Lap comparison

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code` and check `getFunctionSchema` for current inputs. At the start of a conversation, verify the connected account with `whoami` before treating missing laps as no data.

1. Find owned candidate sessions with `getSessions`, then lap IDs and context with `getSessionDetail`. Choose a reference that fits the driver's question, such as their best clean lap or a specified prior lap. Make the reference explicit. For a public reference, inspect `getDesktopLeaderboard` and select only a row with `hasTelemetry`; prefilter by simulator, track layout, and car as far as the returned data allows.
2. Compare two to five owned laps with `compareLaps`, ordering `lapIds` as `[referenceLapId, ...comparedLapIds]`. Cross-session comparisons require compatible simulator, track, layout, and car; do not paper over an unknown identity. For an owned lap against a public leaderboard lap, use `compareTraces` with `isPublicB: true`; the server checks fewer identity dimensions on that path, so explain any unresolved compatibility.
3. Explain the largest supported deltas and their direction. Braking zones align by track location, not by ordinal. A null delta or an `ambiguous`, `unmatched`, or `identity_unknown` zone means unavailable evidence, not equal performance. Use `getLapTrace`, `getZoneTrace`, or `compareTraces` when traces would resolve a concrete question and signals exist.
4. If the driver asks to keep a compatible driver-versus-reference result, inspect `saveComparison` and its evidence requirements before saving. `getComparisons` can contain legacy unverified entries; label their evidence accordingly.

Imported Garage61 or legacy IDs from `getImportedLaps` cannot be used with these desktop telemetry comparison functions. One-off comparison questions stay read-only. A complete session debrief belongs to the `debrief` workflow. Explain access or tier refusals rather than silently switching to unsupported evidence.
