# Vendored Agent Plugins schemas

These are the version 1.0.0 JSON schemas from [Agent Plugins](https://agent-plugins.org/):

- `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`
- `https://agent-plugins.org/schemas/1.0.0/mcp.schema.json`

`scripts/verify_package.py` validates the portable manifests against these pinned copies so CI does not depend on live schema hosting. Review and update both files when changing the targeted Agent Plugins version.
