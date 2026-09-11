# Routing workflow

Read this reference for a task's first route, a profile change, high-risk or uncertain work, a failed attempt, or a fallback decision.

## 1. Establish the task boundary

Confirm the concrete deliverable, acceptance criteria, applicable instructions, authorization, relevant worktree state, and available verification. Load the minimum context that lets the executor act safely. Do not send unrelated history, secrets, or private material to another role.

Route by the combination of:

- impact and reversibility;
- coupling across components or state;
- novelty and root-cause uncertainty;
- security, privacy, financial, migration, or destructive-write exposure;
- strength of objective validation.

A one-file migration can be high risk; a mechanical multi-file rename can be low risk. Count files only as one input to coordination cost.

## 2. Resolve a runtime profile

Use the profile selected by the user or project and reuse it without asking again on every task. Profile fields are defined in [profiles.md](profiles.md). Current explicit user direction overrides conflicting project rules and saved profiles, including a later user revision that changes an earlier preset. Then apply current project rules and the selected profile; lower-priority or stale data cannot override that order.

For initial setup, inspect live availability and present concrete compliant binding choices. Ask only for preferences that materially change the route and remain unknown. Do not invent a profile or permanently block routing when the missing choice can be resolved this way.

Before each dispatch, check the current runtime for the exact model and reasoning-effort combination. A saved example, local config file, cached model list, or old successful call is not a live availability check. Do not infer order from model ID strings or claim that a binding is globally strongest, cheapest, or best.

Resolve runtime precedence before dispatch. Native role configuration may override explicit call arguments. When a full-history fork cannot accept model overrides, use a supported limited-history or no-history dispatch and provide only the context required for the bounded task. If no supported path can enforce the requested binding, do not claim the parameters took effect.

If a requested binding is unavailable, choose only an allowed fallback that fits the same risk and every active ceiling. Otherwise, report the constraint and continue only with communication, orchestration, tool-availability assessment, or read-only review of already existing attempts. Initial code diagnosis remains ceiling-bound initial execution even when it is read-only; do not let a disallowed main agent or reviewer perform it. Do not silently cross a ceiling or claim a role was dispatched.

Loading the skill does not edit runtime config or apply a profile. When the current task explicitly authorizes profile setup or calibration, create or update the project-owned profile only after reviewing the available evidence. Do not mutate unrelated runtime settings.

## 3. Choose initial execution

Profiles may distinguish these task classes:

| Class | Typical evidence | Routing intent |
| --- | --- | --- |
| `low_risk` | Local, reversible, familiar pattern, narrow impact, direct validation | Use the configured low-risk initial binding. |
| `routine` | Established project pattern, clear root cause, moderate coupling | Use the configured routine binding and preserve independent review. |
| `complex` | Cross-component state, architecture, unclear root cause, high-impact logic, or weak validation | Use the configured complex initial binding; do not climb through other attempts merely to manufacture failure. |

Diagnostics that begin a new task are initial execution. A repository bug that predates the task is the subject of the first attempt, not evidence that the attempt failed. High-risk work starts at the configured complex binding and receives full specification and quality review.

The main agent can execute when its actual configuration is allowed for the selected class. Otherwise it coordinates a compliant executor. Delegation should improve quality or efficiency for a bounded task; do not create agents solely to satisfy a diagram.

Keep one writer in a working directory. Parallel read-only checks are safe when scoped; parallel writers need isolated worktrees or clearly non-overlapping destinations.

## 4. Validate and review

The executor records what it requested, what the runtime actually exposed, the changed artifact, and objective results. Run project-native checks proportional to risk. A check not run is not a pass.

After execution and objective validation:

1. **Specification review:** independently compare the real deliverable and evidence with the request, acceptance criteria, and applicable project rules.
2. **Quality review:** independently inspect correctness, maintainability, regressions, safety, and testing appropriate to the change.

The same independent reviewer may perform both stages in sequence when project policy allows; do not create an extra reviewer agent merely to separate the labels. Keep the two conclusions distinct. Review the artifact, not only the executor's summary. If an independent review cannot be run, report it as unavailable rather than treating self-review as independent.

Record requested and observed model and effort separately. When the tool exposes only request acceptance, observed identity is `unknown`. Likewise, a read-only instruction is not proof of an enforced read-only sandbox.

## 5. Gate repair

Repair requires evidence that the current task's completed first attempt produced a locatable defect or a failed objective check against the original acceptance criteria.

The following do not open repair by themselves:

- a pre-existing repository defect being diagnosed;
- a missing dependency, unavailable service, or unverified environment;
- a reviewer preference that is outside the acceptance criteria;
- a role name, complexity label, or desire to use a stronger model.

Once the gate is met, give the repair role the original criteria, first-attempt artifact, exact failure evidence, and a bounded repair scope. Re-run the original checks and repeat specification then quality review as needed. Preserve all three facts: first attempt, repair outcome, final outcome.

Choose a retry bound before repair based on risk and reversibility. As a default guardrail, stop after two repair attempts without new evidence; for high-risk or destructive work, stop earlier and reassess. Repeating the same action against the same evidence is not escalation.

## 6. Calibrate only from evidence

Attribute failures to capability, context, requirements, environment, tooling, other, or `unknown`. Change future bindings only when representative evidence supports the cause. Change one routing variable at a time when practical, define a sample and stop condition, and keep later-discovered defects attached to the original result without rewriting history.

During calibration and for a new task class, use the strongest independent reviewer available within the explicitly approved review policy. Keep full specification and quality review for high-risk work. Reduce review for stable low-risk work only after a representative production window records first-pass outcomes, later defects, severity, and a defined sampling cadence; continue the cadence and periodic integration review.

Use only directly reported tokens, time, money, or quota, with its source and unit. Account separately for main-agent coordination, context handoff, initial execution, review, and repair. Do not count reasoning tokens again when the runtime already includes them in output totals, and do not sum parallel wall-clock stages as elapsed delivery time. Missing data is `unknown`. Do not convert between billing systems or announce savings, quality rankings, or production calibration from fixtures, rule checks, or a few hand-picked tasks.
