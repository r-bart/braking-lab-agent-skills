# Original setup files: v0.3.5

The canonical `setup-library` instructions now distinguish the read-only
`ray_openSetupFile` file opener from the separate `importSetupFile` write. The
typed write tool `ray_importSetupFile` exists, but it is not the file entrypoint.
Opening a file never saves it; the driver reviews the parsed preview before
applying the import. Import creates a new setup and its first version; it does
not append an original iRacing file to an existing setup.

The pinned domain catalog is `101-871b1a790537712e`, exported from the clean
integrated monorepo commit `fcc0797f01aba8eea26014f55b2f537a43a272d9`. It preserves
the other agent's canonical MCP changes through `88e02523e`. The later canonical
head `9febc3e52` has no additional MCP or shared-package changes. The function
names remain unchanged; catalog descriptions account for the digest update.

Validation:

- Package validator passes: ten skills, aligned provider manifests, 74 domain
  references, one production MCP endpoint. The `ray_*` opener was also checked
  manually against the actual server registration and metadata; the domain
  reference checker does not validate those tool names.
- Both v0.3.5 provider archives build and all three SHA256SUMS entries verify.
- Windows installer smoke passes for ten skills, managed update, collision,
  duplicate handling and Codex MCP. Claude CLI remains unavailable locally;
  Claude end-to-end is not certified by these checks.
- Post-review finds no unrelated identity, audience, permissions, prompts,
  integrations or asset change. Authored skills remain under `skills/` only.

The separate private staging plugin was updated to v0.3.5 and read back:
17 files, the same required staging App, USER/PRIVATE audience and preserved
assets/presentation/prompts. Only the two manifest versions and this skill's
instructions changed. The actual ChatGPT listing displays v0.3.5 and ten skills;
its icon is still generic despite valid packaged logo paths and assets. This
update does not fix the visible icon and does not deploy the MCP server.

Staging currently serves the other agent's canonical MCP v0.4.0, without the
Paddock UI tools. The integrated UI candidate is validated locally but awaits
a coordinated deployment outside live engineer testing and real-host acceptance.
Production plugin v0.3.2 was not updated. No public submission was made.
