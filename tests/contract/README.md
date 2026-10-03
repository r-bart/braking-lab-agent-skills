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

`ray-tools.json` additionally exports `rayUiToolDefinitions`,
`rayOpenerDefinitions` and `rayAdditionalToolDefinitions` from
`apps/mcp-server/src/mcp/ui/tools.ts` at the same clean source revision. It
records names, annotations, visibility and input field/required names, without
data or credentials. This covers the underscore tool names omitted by the
domain-function token matcher, including direct confirmation routes and the
read-only file opener. The verifier rejects unknown names, source mismatch,
missing domain mirrors and policy drift. Run `python -m unittest discover -s
tests -p '*_test.py'` to exercise the rejection paths.

These are source registration contracts. They do not prove that a host renders
a consent form, that a runtime authorizes a mutation, or that the matching
candidate is deployed; those remain separate acceptance gates.
