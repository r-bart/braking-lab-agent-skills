# MCP function snapshot

`tool-catalog.json` was exported from `apps/mcp-server/src/mcp/code-mode/tool-catalog.ts`
in Braking Lab monorepo commit `1d123a617c2ff901641a5637d30d3b81e1fdc841`.
`version` is the server's `CATALOG_VERSION` from that source; `names` lists the
97 functions in catalog order. `scripts/verify_contract.py` checks every
function cited by a skill against this snapshot.

Before a release, compare the snapshot with the catalog actually deployed in
staging. A local source revision alone does not prove deployment parity. When
the server catalog changes, re-export the version and names from the reviewed
source revision, then run `scripts/verify_package.py` and the staging journeys.
