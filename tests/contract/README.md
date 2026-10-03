# MCP function snapshot

`tool-catalog.json` records the reviewed canonical export from
`apps/mcp-server/src/mcp/code-mode/catalog/index.ts` in the Braking Lab monorepo.
The JSON's `sourceRevision` is the exact source commit; `version` is that source's
`CATALOG_VERSION`; `names` contains its function names in catalog order. Read
those values from the JSON instead of maintaining a second revision or count in
this document. `scripts/verify_contract.py` checks every skill reference against
that snapshot.

Re-export only after the canonical merge is committed and the source checkout
is clean. Reject an unresolved merge or dirty tracked/untracked inputs rather
than stamping a pre-merge HEAD onto newer functions. Compare the exported
version/names with the catalog actually deployed in staging before release;
a local source revision does not establish deployment parity. Run
`scripts/verify_package.py` and the staging journeys after the refresh.
