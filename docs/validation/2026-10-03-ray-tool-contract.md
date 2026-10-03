# Ray tool references: source validation

The package verifier now checks all seven `ray_*` names referenced by the ten
skills against 110 registered definitions, in addition to the existing 74
domain function references. The source export is pinned in both JSON snapshots
to clean monorepo revision `1402306fc6e10fe4601460eb50667d517c3b237f`, catalog
`101-871b1a790537712e`.

Eleven regression tests pass. They reject misspelled underscore names,
source/catalog mismatch, missing domain mirrors, duplicate registrations,
incorrect read-only declarations and hidden direct confirmation tools. The
file opener remains read-only; the separate import is a write. These checks
cover registration contracts, not runtime consent or authorization.

Package/skill validation, archive generation, all three SHA-256 checksums,
shell syntax and installer smoke pass locally on Windows with Git's shell.
The native `sha256sum -c` initially treated CRLF as part of filenames; verifying
the same digest/file pairs with Python's line-aware parser passes. CI checks
the generated checksums directly on Linux. The first Windows installer attempt
lacked `sh` on PATH; the existing Git shell resolved that environment issue.

Only verifier, CI, test snapshots and validation documentation change. They
are excluded from provider archives; the delivered skill texts/manifests and
private plugin remain 0.3.5. No server restart, database write, plugin upload
or production change occurs in this review. Staging still needs qualification
of the integrated candidate and the host's direct human confirmation flow.
