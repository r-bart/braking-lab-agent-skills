---
name: setup-library
description: Browse and inspect a driver's Braking Lab car setups and version history, or create and append LMU setup versions from driver-supplied full .svm files.
---

# Setup library

Use `execute_code`; check exact inputs with `getFunctionSchema` before writes.

1. Find the owned setup with `listCarSetups`, then inspect its simulator, car, source, versions, and lineage using `getCarSetup`. Resolve near-duplicate names by canonical setup identity and effective values, not filename or display name alone.
2. For a new LMU setup, use `createCarSetup` only with a driver-supplied complete `.svm`. For a new version, use `addSetupVersion` with a complete `.svm` and the correct existing setup/channel. Do not mix source channels or infer a full setup from fragments.
3. Use one stable `operationKey` and the same payload for each intended write, including after an uncertain response. Inspect the setup/version history before starting a separate attempt; do not mint a new key to bypass an uncertain result. If an append reports `SETUP_BASE_MOVED`, refetch the latest version before a new, deliberate append with a new key.

iRacing garage `.htm`/`.html` imports currently happen in the app; encrypted `.sto` is not readable here. The MCP does not expose general setup rename or delete actions. For parameter changes derived from an existing version, use the `setup-coaching` workflow and `remixSetup`.
