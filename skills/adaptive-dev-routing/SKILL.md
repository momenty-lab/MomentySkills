---
name: adaptive-dev-routing
description: Use when a concrete software development task needs model or agent role selection for implementation, debugging, testing, code review, or engineering documentation. Do not use for general chat, ordinary advice, pure research, or non-development work.
---

# Adaptive Development Routing

Route concrete development work by risk, evidence, and runtime constraints. Preserve the user's choices, keep the direct conversation strong, and optimize for a verified result rather than an unverified first response.

This skill is guidance, not a router. Loading or invoking it does not apply bindings, mutate agent or model configuration, create a scheduler, or grant permission. It may help create or update a project profile when the current task already authorizes that change and the decision has evidence. Runtime bindings come from a profile the user or project has chosen and configured.

## Start with the boundary

Apply this skill only when work will directly change or assess a software deliverable: implementation, architecture, debugging, tests, code review, or engineering documentation tied to that work.

1. Follow platform constraints and the current request. For routing preferences, the user's current explicit instruction overrides conflicting project rules and saved profiles; a later user revision can replace an earlier preference or preset. Then apply the project's current rules and profile limits.
2. Read only the current task's relevant code, specifications, validation commands, worktree state, and existing task record. Do not scan unrelated projects or load broad history by default.
3. Define acceptance criteria and evidence before execution. Classify risk from coupling, reversibility, uncertainty, impact, and available verification. File count alone does not determine task size.
4. Reuse the selected runtime profile until the user or project changes it, and verify each requested model and reasoning effort against the live tool before dispatch. If no profile is selected, inspect live availability, present concrete compliant choices, and ask only for a genuinely missing preference; do not invent bindings or a model ranking. Read [references/profiles.md](references/profiles.md) when selecting or defining a profile.

Keep the user's specified main-chat model. If none was specified, keep the runtime's strong direct-chat default. Do not downgrade the main conversation to reduce cost. The main agent owns communication, orchestration, evidence checks, and delivery; if it also executes development work, the active initial-execution ceiling applies to it.

## Execute, review, repair

Use [references/workflow.md](references/workflow.md) for initial routing, failures, fallbacks, high-risk work, or changes to a profile.

- Select the configured initial role for the task's risk and uncertainty. Initial diagnosis is initial execution, not repair.
- Delegate only bounded work that can be independently completed and checked. Keep one writer per working directory; isolate concurrent writers.
- Run objective validation proportional to impact. An unavailable environment is `unverified`, not a manufactured failure.
- After validation, perform an independent specification review and then an independent quality review against the actual deliverable and evidence. A tool dispatch request is not proof of the observed model, effort, or an independently enforced sandbox.
- Open the repair route only after a locatable failure in this task's first attempt violates an acceptance criterion. A pre-existing bug being investigated and a missing environment do not satisfy this gate.
- Preserve the first-attempt result, repaired result, and final result separately. Never relabel a repaired success as a first-pass success.

## Invariants

- Once priority is resolved, every active user and project ceiling applies and cannot be bypassed by complexity, fallback, a role name, or the main agent. An old, lower-priority profile cannot freeze a ceiling the user later changes.
- Treat requested and observed model and reasoning effort as separate facts. Use `unknown` when the runtime does not expose observation evidence; model self-report and successful dispatch are insufficient.
- Do not claim an isolated read-only reviewer sandbox unless the tool enforced one. A reviewer instructed to remain read-only is only a behavioral constraint.
- Keep retries bounded. Stop repeated repair when there is no new evidence, reassess the cause, and seek missing context or a user decision when needed.
- Do not estimate unavailable token use, money, subscription consumption, savings, or model quality. Do not call a profile production-calibrated without representative production evidence.
- Routing never expands authorization for credentials, network access, destructive actions, external messages, Git operations, deployment, or spending.

Read [references/records.md](references/records.md) only when a persistent project needs a routing record or calibration decision. A one-off task can report the same evidence in its final handoff.
