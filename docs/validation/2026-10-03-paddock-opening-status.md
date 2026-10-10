# Paddock opening status: 0.3.1 candidate

The real-host probe requested opening Paddock without creating or modifying data.
The opener returned successfully, but the host reported that the workspace could
not be opened. The model then incorrectly claimed that opening and integration
had succeeded. A tool result and a loaded UI resource do not establish visible
rendering.

The canonical `race-engineer` skill now requires a host acknowledgement of visible
rendering or driver confirmation before reporting a successful opening. It must
report a known host failure honestly and preserve the instruction to open only.
Without visible-render evidence, it reports that opening was requested. This
instruction change has not yet been qualified by a repeated real-host/model test.

Local package verification passed for ten skills, two aligned 0.3.1 manifests,
the production MCP endpoint, and 70 function references against the pinned
98-function catalog. Both generated archives contain ten skills and exactly one
connection mechanism; their checksums and the installer checksum passed.

The bilingual routing corpus contains 62 prompts, including the new host-failure
case and its reviewer expectation. Corpus coverage passed a structural check;
no LLM routing or reply-quality evaluation was run for this candidate. The
routing runner checks selection only and does not grade rendering claims.

The installer smoke test passed ten-skill installation, managed update, collision,
and duplicate-selection checks locally. Its final mock-MCP case failed on Windows
because the fixture builds a POSIX-separated PATH from Windows entries and cannot
find `tr`; Linux CI must qualify the complete smoke test. Shell syntax passed.
Claude CLI strict validation could not run locally because the CLI is unavailable.
These limitations do not qualify the host UI or the model response.
