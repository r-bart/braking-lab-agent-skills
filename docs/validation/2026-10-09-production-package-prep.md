# Production package preparation — 9 October 2026

This records package preparation, not a public upload, approved listing or
production deployment. The public plugin remains `braking-lab-race-engineer`
version **1.0.0**; private staging 1.1.7 is a separate identity.

The listing now uses **Braking Lab - Race Engineer** consistently, prioritizes
telemetry and discussion of evidence, and describes the four UI areas without
claiming physical capture or hardware control. English and Spanish descriptions,
P1 and release notes match that scope. The new pedal isotype is a real square
512 × 512 RGBA PNG, inspected visually and packaged for both logo and composer.

Verification passed:

- All ten authored skills; provider identity and single production MCP endpoint.
- Pinned tool contracts and public metadata validation.
- 32 package/contract/submission/archive tests.
- Portable and Claude archives built and inspected; no private app bindings,
  reviewer access fields or extra connection mechanisms.
- SHA256SUMS verification for both archives and installer.
- `claude plugin validate . --strict`.

The four published listing destinations were fetched and their content inspected:

- [Race Engineer](https://www.brakinglab.com/en/features/race-engineer): describes
  the product, MCP clients and OAuth connection.
- [Support](https://www.brakinglab.com/en/docs/faq#how-do-i-contact-support): lists
  the published support email and other help channels.
- [Privacy](https://www.brakinglab.com/en/privacy): covers Race Engineer,
  authorized AI-client access through OAuth, provider sharing and revocation.
- [Terms](https://www.brakinglab.com/en/terms): covers MCP access and AI outputs.

These checks establish accessible, relevant published pages; they are not legal
attestations or a replacement for the developer's portal declarations.

Worldwide targeting and commerce false are preserved. The exact verified
publisher name is determined by the intended portal identity, not overridden
by a ZIP field. No demo URL was invented: `verify_submission.py --ready` must
still refuse until a real accessible recording is supplied. The production
reviewer, native execution of all eight cases against the saved submission,
domain verification and final tool scan remain portal/deployment gates.

Public production health is now MCP 0.5.1 at commit
`8aed47ab68e1503c716b11ff355364d870984e9e`; historical documents describing 0.4.0
do not establish current deployment state. The new UI and transport follow-up
still require the separately prepared selective promotion and acceptance.
