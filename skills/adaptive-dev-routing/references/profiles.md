# Runtime profiles

A profile is user- or project-owned data that maps routing roles to model and reasoning-effort requests. Loading the skill alone does not select, install, or edit one. When the current task authorizes setup or calibration, the skill may help create or update a project profile after evidence review. The current user request, project policy, runtime permissions, and live availability always take precedence.

Use a profile after the user or project selects it, then reuse that policy until a current instruction changes it; do not request repeated confirmation for each task. The example in `../examples/founder-profile.json` is an optional founder preference for efficiency and verified quality, not a universal default, a model ranking, or production calibration.

## Profile fields

This file is the schema authority for bundled JSON examples. A minimal profile contains:

| Field | Meaning |
| --- | --- |
| `schema_version` | Format version string. |
| `profile_id` | Stable profile identifier. |
| `display_name` | Human-readable label. |
| `calibration_status` | Evidence state such as `illustrative` or a project-defined calibrated status with a record. |
| `bindings.main_chat.selection` | Direct-chat policy. Preserve `user-specified-or-strongest-available` unless the user chooses otherwise. |
| `bindings.initial_execution.low_risk` | Model binding for bounded, reversible, directly verifiable work. |
| `bindings.initial_execution.routine` | Model binding for established patterns and clear diagnoses. |
| `bindings.initial_execution.complex` | Model binding for cross-component, uncertain, or high-risk initial work and diagnostics. |
| `bindings.spec_review` | Independent specification-review binding. |
| `bindings.quality_review` | Independent quality-review binding. |
| `bindings.repair` | Binding eligible only after the repair gate opens. |
| `ceilings.initial_execution.maximum_config` | Human-readable ceiling anchor. Never use it for lexical model comparison. |
| `ceilings.initial_execution.allowed_configs` | Exact allowed initial `{model, reasoning_effort}` pairs. Membership in this list enforces the profile ceiling. |
| `gates.repair.requires` | Evidence required before using the repair binding. |
| `gates.repair.excludes` | Conditions that do not satisfy the gate. |
| `availability_check` | Whether live support must be checked before dispatch. Use `required-before-dispatch`. |

Every model binding is an object with exactly the request fields the runtime needs:

```json
{"model": "runtime-model-id", "reasoning_effort": "runtime-effort-id"}
```

For custom or future model IDs, enumerate the allowed initial combinations explicitly. Do not derive superiority, cost, or eligibility from names, release dates, effort labels, or a provider family. A requested combination still requires a live availability check.

## Precedence and customization

Resolve precedence before comparing limits: current explicit user direction overrides conflicting project rules and saved profiles, and a later user revision can replace an earlier preference. Then apply current project rules and the selected profile. At the same priority, satisfy every active ceiling. A project may remove allowed configurations, choose a different binding, or prohibit a review model; profile customization cannot bypass a higher-priority ceiling.

Review and repair bindings are separate from initial execution. A model allowed for review or gated repair is not thereby allowed for initial implementation or initial diagnosis. Fallback must remain in `allowed_configs` and fit the selected task class and risk.

If a runtime cannot enforce a requested model, effort, or sandbox property, record the request separately from observation and use `unknown` for what cannot be established.
