---
name: lap-comparison
description: Compare Braking Lab laps and explain measured time or braking differences. Use when a driver asks to compare their own laps or an owned lap with a public leaderboard reference; a full session debrief belongs to debrief.
---

# Lap comparison

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code` and check `getFunctionSchema` for current inputs. At the start of a conversation, verify the connected account with `whoami` before treating missing laps as no data.

1. Find owned candidate sessions with `getSessions`, then lap IDs and context with `getSessionDetail`. Choose a reference that fits the driver's question, such as their best clean lap or a specified prior lap. Make the reference explicit. For a public reference, inspect `getDesktopLeaderboard` and select only a row with `hasTelemetry`; prefilter by simulator, track layout, and car as far as the returned data allows.
2. Compare two to five owned laps with `compareLaps`, ordering `lapIds` as `[referenceLapId, ...comparedLapIds]`. Cross-session comparisons require compatible simulator, track, layout, and car; do not paper over an unknown identity. For an owned lap against a public leaderboard lap, use `compareTraces` with `isPublicB: true`; the server checks fewer identity dimensions on that path, so explain any unresolved compatibility.
3. Explain the largest supported deltas and their direction. Braking zones align by track location, not by ordinal. A null delta or an `ambiguous`, `unmatched`, or `identity_unknown` zone means unavailable evidence, not equal performance. Use `getLapTrace`, `getZoneTrace`, or `compareTraces` when traces would resolve a concrete question and signals exist.
4. If the driver asks to keep a compatible driver-versus-reference result, inspect `saveComparison` and its evidence requirements before saving. `getComparisons` can contain legacy unverified entries; label their evidence accordingly.

Imported Garage61 or legacy IDs from `getImportedLaps` cannot be used with these desktop telemetry comparison functions. One-off comparison questions stay read-only. A complete session debrief belongs to the `debrief` workflow. Explain access or tier refusals rather than silently switching to unsupported evidence.
