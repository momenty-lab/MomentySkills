# Evidence and calibration records

Use a persistent record only for an ongoing project that repeatedly routes development work or is changing a profile. Reuse the project's existing task, plan, or handoff record when possible. For a one-off task, include the same essential evidence in the final handoff instead of creating a routing log.

Keep records concise and free of credentials, private prompts, unrelated conversation, and model self-claims.

## Project profile record

Record:

```text
profile id and version:
scope and exclusions:
profile source and selected-by:
applicable user/project ceilings:
task classes and acceptance standards:
review requirements:
calibration status and evidence window:
recalibration triggers:
record owner, location, and updated date:
```

Profile presence means `configured`, not `calibrated`. Production calibration requires representative production outcomes for the stated task class and version.

## Task execution record

Record:

```text
task id, date, scope, class, and risk:
acceptance criteria and applicable rules:
profile id/version and ceiling check:
initial requested(model, effort):
initial observed(model, effort, evidence):
first attempt(pass | fail | unverified), attempts, evidence:
spec review requested/observed, conclusion, evidence:
quality review requested/observed, conclusion, evidence:
failure attribution and basis:
repair gate(open | closed), reason:
repair requested/observed, attempts, result, evidence:
final outcome(first-pass | repaired | failed | unverified):
measured usage for main/coordination, context handoff, initial execution, review, and repair; source and unit:
routing decision and follow-up trigger:
later-discovered defects:
```

Use these status meanings:

- `pass`: the original acceptance checks ran and passed.
- `fail`: a locatable current-task result violated an original acceptance criterion.
- `unverified`: evidence is unavailable or the environment could not run the check.
- `first-pass`: the initial result passed without repair.
- `repaired`: the first attempt remains failed in history and a later bounded repair passed.

For requested versus observed configuration, record the exact tool or runtime evidence. If the runtime did not expose model or effort, write `unknown`; a successful dispatch proves only that the request was accepted. For sandboxing, distinguish tool-enforced isolation from a read-only behavioral instruction.

Record costs only when a tool or trusted log reports them. Keep tokens, wall time, API money, and subscription quota as separate units. Do not count reasoning tokens again when reported output already includes them, and do not add parallel stage wall times as end-to-end elapsed time. Write `unknown` rather than estimating.

Do not create a database, daemon, scheduler, telemetry service, or duplicate project tracker for this skill.
