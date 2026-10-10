---
name: setup-library
description: Find and inspect a driver's Braking Lab car setups and version history. Use when they ask which setup they own, compare exact stored versions, import original LMU or iRacing garage files, or append a complete LMU version; explain why native iRacing .sto rewriting is unsupported; parameter changes belong to setup-coaching.
---

# Setup library

## Native iRacing .sto requests

A request to decrypt, rewrite or generate a native iRacing `.sto` is unsupported.
Explain this before verifying the account, checking capabilities or calling any
Braking Lab tool. Do not ask for a `.sto` to try decryption, promise an edited
file or fabricate its bytes. A readable garage `.htm`/`.html` export is a
separate supported workflow; propose it without starting an import.

## Conversation and saved changes

The Ray interface is for reading evidence. A “with Ray” action starts a conversation; it is not permission to persist its seed. Before a domain create, edit, delete or association, read the current owned target, ask for missing facts and show the exact draft or deletion scope. Obtain the driver's approval of that draft before the write; use direct native MCP elicitation wherever the server requires it. Agent-authored text, booleans and context attachments are never substitutes for that consent. After saving, read the affected resource again and report its actual persisted state. Preserve the original operation key on uncertain writes; do not blindly retry.

Navigation and attachment are separate. Only “Use in chat” attaches evidence; an attachment identifies a resource, not its approval or proof that a setup was driven. Respect removed attachments. Preferences are the sole immediate-write UI exception. The host controls the chat, composer and confirmation presentation. File previews are read-only; import original setup bytes through the SPA.

Prefer individually exposed `ray_*` tools when the connected host offers them to the model. The unprefixed function names below describe the same canonical operations. Use the input schema supplied with each typed tool. If a tool is not offered to the model, do not recover it through hidden schema discovery or generic execution. `execute_code` is the compatibility path for Code Mode clients; it must not enable operations absent from the individually reviewed server catalog. Server permissions and direct client confirmation still apply.

For Code Mode, use `execute_code`; check exact inputs with `getFunctionSchema` before writes. Check `getCapabilities` for the three bounded owned-resource functions before using them; deployments may differ. If unavailable, inspect existing setup/version history and explain that the bounded reader or comparison is not enabled on this connection. At the start of a conversation, verify the connected account with `whoami` before interpreting an empty setup library.

1. Find the owned setup with `listCarSetups`, then inspect its simulator, car, source, versions, and lineage using `getCarSetup`. Resolve near-duplicate names by canonical setup identity and effective values, not filename or display name alone. When exposed by the connected schema, pin an explicit setup and version before calling `readOwnedSetupVersionResource`; never replace a missing selected version with the latest. This bounded card reports identity and exact eligibility, not private file access or proof that the version was driven.
2. When exposed by the connected schema, call `compareOwnedSetupVersionResources` with the exact `from` and `to` setup/version pairs. Follow `nextOffset` until null if the driver needs the complete diff. Keep both source digests and `changesDigest` stable across pages; discard accumulated pages and restart deliberately if any changes. Report unavailable identity/vocabulary honestly. Observed parameter differences are not causal driving evidence or proof of cross-channel exact matching.
3. For original LMU `.svm` or iRacing garage `.htm`/`.html` files, inspect the exposed `ray_openSetupFile` file entrypoint first. Opening it is read-only; the driver reviews the parsed preview and explicitly applies the separate `importSetupFile` action. When using that schema-defined import directly, preserve unchanged original bytes and bounded metadata. It creates a new setup with its first version; it does not append the file to an existing setup. Never decode and re-encode HTML to construct an upload, fabricate file bytes, or bypass a server-requested direct confirmation. A native `.sto` is unsupported. Existing `createCarSetup` requires a driver-supplied complete `.svm`; `addSetupVersion` requires a complete `.svm` and the exact existing setup/channel. Do not mix source channels or infer a full setup from fragments.
4. Use one stable `operationKey` and the same payload for each intended write, including after an uncertain response. Inspect the setup/version history before starting a separate attempt; do not mint a new key to bypass an uncertain result. If an append reports `SETUP_BASE_MOVED`, refetch the latest version before a new, deliberate append with a new key.

The MCP does not expose general setup rename or delete actions. For parameter changes derived from an existing version, use the `setup-coaching` workflow and `remixSetup`.
