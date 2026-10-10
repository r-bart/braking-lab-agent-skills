# Production preparation after owner QA

The owner reports QA completed and authorizes selective main promotion and
production qualification, after finishing the other preparation. No production
deployment or reviewer write has been performed in this preparation pass.

## Verified independently

- PR 149 is mergeable; all required checks passed on candidate `1605a2607`.
- Railway production follows main, builds MCP plus its embedded Ray UI as one
  deployment, and retains one replica. No separate SPA, Capture or Landing
  deployment or database migration is required by this handoff.
- The current production deployment is
  `693ad84b-f4e5-44d0-ac1d-3d8606950814`, main `1f3cb5110`, readiness ready,
  health provenance certified. It is eligible for rollback. Discovery uses
  the production origin and existing four scopes. This is preflight evidence,
  not acceptance of the new candidate.
- Rechecked package and contract validators, all four listing URLs and 32
  package tests. The public icon is the current contained 512px pedal PNG.
- Organization settings currently show individual verification Approved and
  business verification not started. The selected directory identity/name
  must still be verified on the actual draft; package developerName does not
  prove business approval. No verification enrollment was started.
- The portal has no observed Braking Lab draft. The existing Verxion review
  was left untouched. No package was uploaded before completing the demo.

## Review expectation correction

P5 now explicitly requires an exact draft and the pilot's approval before the
write, even though its initial prompt asks for a saved result. Afterwards the
agent must reread, preserve corner notes/pins/videos and avoid duplicate lines.
This aligns the review case with the ten skills' conversational save policy;
it does not remove separately required native MCP elicitation.

## Prepared next operations

The monorepo contains a bounded reviewer read-only SQL preflight and a launch
runbook with proposed dedicated production identity, sample-data scope,
transactional profile/membership changes, resumable normal ingest/import flows,
qualification and rollback. Production inspection approval is pending; exact
write approval follows its schema/collision preview. Do not repoint the existing
staging-only reviewer CLI or copy staging tokens to production.

Production review cases, final screenshots, a real recording and its anonymous
HTTPS URL depend on the qualified production deployment and dedicated reviewer
connection. The current browser tool has no recording capability; arrange a
real screen recorder, then check playback before adding a demo URL. Existing
pilot screenshots are private QA and are excluded from public archives.

The private staging listing still displays a generic host icon despite valid
contained assets. It is tracked in `ray-private-icon-host-discrepancy.md` and
must be observed on the actual production draft; do not declare it fixed from
manifest validation alone. No support message was sent.

The owner QA report is accepted. A separate read of the exact synthetic staging
association session returned zero rows at 17:50:40 UTC. That read does not
certify positive native-consent persistence; no agent acceptance was sent.

## Review outcome

Preparation changes only review expectations and documentation. No tool,
permission, public schema, private audience, fixture or runtime code changed.
Public archive construction remains deterministic, excludes credentials and
private App bindings, and keeps the single production MCP endpoint. Remaining
gates are explicit, not encoded as invented success or a placeholder demo URL.

Official reference checked this pass:
<https://developers.openai.com/plugins/deploy/submission>.
