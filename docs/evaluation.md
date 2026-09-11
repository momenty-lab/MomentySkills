# Evaluation protocol

MomentySkills needs evidence that another person can inspect. A polished success story without a comparable baseline, measurement source, or failure detail is feedback, but it is not a benchmark.

## Current evidence boundary

`adaptive-dev-routing` is an experimental hypothesis. Its production effectiveness is unverified and this project has no population-level measurements. Repository validation checks packaging and syntax; it does not run agents or establish routing quality.

Current validation evidence as of 2026-09-11:

| Layer | Evidence | Result | What it does not establish |
| --- | --- | --- | --- |
| Packaging and metadata | Repository validator plus four unit fixtures: valid minimal skill, broken local resource, malformed JSON, and missing frontmatter name. | Validator and all four tests passed. | Agent routing behavior or effectiveness. |
| Synthetic decisions | Eight controlled routing cases covering task class, ceilings, review, repair, and fallback decisions. | All eight produced the expected decisions; Case F wording was narrowed after review and then rechecked. | Production outcomes or representative population performance. |
| Native discovery | Isolated `.agents/skills` collision and symlink checks, official `quick_validate`, native skill listing, and repository enablement. | All checks passed; the discovery check made no model calls. | Whether a model will follow the skill well on a real task. |
| Production effectiveness | No representative production measurement has been collected. | Unknown. | Quality improvement, time or token savings, calibration, or population-level impact. |

### Synthetic decision cases

The following compact cases let a reviewer replay the routing decisions against the current skill and founder profile. They are manual decision simulations only: no actual dispatch, observed model identity, product patch, or production measurement occurred.

| Case | Synthetic input | Expected routing outcome |
| --- | --- | --- |
| A | The user asks for general advice about why some coding tasks benefit from slower reasoning; there is no concrete software deliverable. | The skill does not apply. Answer in the selected main chat; execution, reviews, and repair are not applicable. |
| B | A new payment-authorization bug has an unknown cause and financial/security impact. Main chat is `gpt-6-astra` / `ultra`; founder-profile bindings are available. | Classify as complex. Preserve main chat, request `gpt-5.6-sol` / `xhigh` for initial execution, then `gpt-6-astra` / `high` for specification and quality review. Repair stays closed until this task's first attempt has a locatable failure. |
| C | A customer-impacting bug predates the task. The user says “use repair now” but gives no exact initial-binding exception. | Treat diagnosis as complex initial execution at `gpt-5.6-sol` / `xhigh`. Do not open the repair gate merely because the existing bug or the word “repair” is present. |
| D | A patch exists, but required CI cannot run because its SDK is unavailable; no source defect has been located. | Record the first attempt as `unverified`. Specification and quality review may report separate source conclusions, but missing CI is not a pass or failure and does not open repair. |
| E | The completed first patch fails a reproducible original permission test with a recorded path and assertion. | Preserve the first attempt as `fail`, open repair, request `gpt-6-astra` / `high`, apply a bounded repair, rerun the original checks, and retain separate first-attempt, repair, and final outcomes. |
| F | The selected initial binding cannot be enforced: the only spawn path rejects model overrides, no compliant fallback exists, and the main agent's exact pair is unavailable or outside the active ceiling. | Do not dispatch or make initial edits. Continue only communication, orchestration, tool-availability assessment, or read-only review of existing attempts. Initial code diagnosis remains ceiling-bound. Report the work blocked until a compliant executor exists or policy is explicitly changed. |
| G | The latest user instruction names `gpt-6-astra` / `high` for initial execution on this task only, conflicting with an older project cap. | Apply the current exact user override for this task, preserve the main-chat selection, and do not persistently edit the profile. Existing review policy and the repair gate still apply. |
| H | A candidate passes one synthetic fixture; only executor output tokens are reported, while coordination, handoff, review, repair, and elapsed totals are missing. | Record `fixture pass only`; mark missing costs `unknown`. Do not claim savings, production calibration, or reduced review requirements. |

## Choose a comparison

When practical, compare:

- **Baseline:** how the same task would normally be attempted without this candidate profile or change.
- **Candidate:** the profile or skill revision being evaluated.

Keep the task, starting revision, requirements, available tools, and environment as similar as practical. If they differ, describe the difference instead of adjusting the story after seeing the result. A useful report may also describe a single run when no baseline is available; label it clearly.

## Record requested and observed configuration

For every routed role that applies, record the requested model and reasoning effort. Then separately record what the runtime actually used, or `unknown` and why it could not be observed. Relevant roles may include initial execution by task risk, main chat, specification review, quality review, and repair.

Do not treat a requested configuration as proof that the runtime honored it. Model names, reasoning efforts, and availability can differ by account, host, product, and date.

## Measurement provenance and total scope

For every number, state its source and definition:

| Field | What to report |
| --- | --- |
| Time | Start/end or elapsed value, timezone where relevant, and whether it came from a system clock, tool log, or platform UI. |
| Tokens | Value, unit or included token categories when known, and whether it came from an official UI, API response, or tool log. |
| Reviews | Count and what qualified as a specification or quality review. Use `0` only when measured; otherwise use `unknown`. |
| Repairs | Count and what qualified as a repair cycle. Use `0` only when measured; otherwise use `unknown`. |
| Outcome | Positive, neutral, mixed, or negative, plus the concrete acceptance evidence and unresolved failures. |

Account for main or coordination work, context handoff, initial execution, specification review, quality review, and repair. State which stages a total includes and which it excludes. A partial total may be useful, but it must not be presented as end-to-end cost.

If a time, token, review, repair, or stage total was not actually measured, record `unknown`; never reconstruct it from memory and present it as observed. Estimates and impressions may be shared as qualitative feedback, but they do not support measured savings, efficiency, or routing-calibration claims.

## Review the result

Evaluate the artifact against the task's acceptance criteria before interpreting time or token use. Record regressions, reviewer disagreements, retries, manual interventions, and tasks that were abandoned. Efficiency without an acceptable result is not a positive result.

Avoid selecting only successful runs. If you tested several attempts, report the number attempted and why any run was excluded. Disclose relevant conflicts of interest and whether any reward was tied to the result. MomentySkills does not incentivize positive findings.

## Protect private data

Share the smallest context needed to understand the observation. Remove repository secrets, credentials, customer or personal data, private paths, proprietary source, raw session logs, and hidden prompts you do not have permission to publish. A redacted report should say what category was removed when that affects interpretation.

## Minimum useful report

A report is still useful when measurements are incomplete. The minimum is a shareable task description, requested and observed configurations (with `unknown` where necessary), outcome, acceptance evidence, and confirmation that private data was redacted. Baseline comparison, environment detail, measured totals, limitations, and stage costs improve interpretation but remain optional; missing measurements must not be inferred.
