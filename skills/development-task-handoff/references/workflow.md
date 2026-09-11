# Development handoff workflow

Use the mode that matches the task. Keep one active record and update it in place.

## Set up a continuation record

Only change project handoff setup when the current task authorizes it.

1. Inspect the project's effective agent entry, task records, status sources, and repository state.
2. Reuse an adequate maintained handoff file or clearly identified section. If none exists, create one focused `HANDOFF.md` or equivalent record in the project and identify its exact path from the project entry.
3. If a tool needs its own entry file and officially supports one, point it to the project instruction source. Do not copy the rules or create another progress record.
4. Initialize the record from confirmed user intent, accepted task sources, actual files, Git evidence, and checks already run. Mark missing facts `unknown`.

The handoff location should be discoverable without searching historical records, but this skill does not guarantee that every tool automatically reads it. Verify discovery in each actual environment.

## Save meaningful progress

Write the initial snapshot before implementation. Update it after a meaningful small result, change in scope or plan, blocker, verification run, local checkpoint, or before an operation long enough that interruption would obscure the next action.

Record outcomes rather than tool-call chronology. Link durable sources instead of copying them, replace obsolete next steps, and keep accepted decisions separate from proposals. Before a deliberate handover, reconcile the record with the actual diff and command results one last time.

## Resume work

1. Resolve the project, repository or worktree, active record, and current effective instructions from their real paths.
2. Confirm the unfinished task, accepted scope, authority, acceptance criteria, and approval gates. A handoff documents earlier authority; it does not create new authority.
3. Inspect current files, branch, `HEAD`, index, tracked and untracked changes, relevant worktrees, and recent task commits. Compare them with the recorded baseline and partial state.
4. Classify current changes and protect unrelated or unknown work. If the record and repository disagree, preserve the evidence, correct the current snapshot, and avoid guessing ownership from recency or similarity.
5. Check for another active writer or conflicting operation. Do not kill an unknown process; pause the affected mutation until the writer boundary is clear.
6. Determine which checks still apply. Bind each result to its tested inputs, rules, environment, command, and revision when available. Rerun it or mark it pending only when a relevant change or evidence gap undermines applicability; an unrelated change does not automatically invalidate it.
7. Update the reconciled record, state the confirmed progress and next action, and continue the same task within its existing authorization.

If multiple unfinished tasks compete, a required path is unresolved, access is missing, or ownership cannot be separated, continue safe read-only inspection and request only the missing decision.

## Complete or close the record

Run verification proportional to the change and inspect the final diff and repository state. Update the project's authoritative status, decision, validation, or changelog sources only when the task requires it; link them from the handoff instead of duplicating their contents.

Mark the active task complete only when its accepted scope and required verification are satisfied. Record outstanding human acceptance, unavailable checks, protected changes, or later external actions explicitly. Archive, replace, or delete a completed handoff only under the project's maintained process and current authority.

## Compact record

Adapt these fields to the existing project record instead of creating a second schema:

```text
Updated / executor: timestamp with timezone; last tool or session when known
Active task / state: one task; in progress, blocked, awaiting verification, or complete
Intent / authority: approved goal, scope, constraints, acceptance, and source references
Verified progress: completed outcomes and evidence tied to the tested state
In progress / next: partial work, exact relevant files, and next concrete action
Workspace: repository/worktree path, branch, HEAD, baseline, and last verified checkpoint
Existing changes: current-task and inherited work; protected unrelated or unknown work
Checks: command or review, working directory, result, tested state, and checks not run
Decisions / blockers: accepted decisions, proposals, failed approaches, unresolved facts
Next authority: later action that still requires user or project authorization
```

Use `not available` or `unknown` with a reason when a field cannot be established. A non-Git workspace does not gain Git history or authority by adding Git-shaped fields.

## Reconciliation example

An earlier agent records that parser tests passed at commit `abc123`, then leaves a local formatter edit for follow-up. The next tool finds the parser commit, the formatter edit, and an unrelated untracked export file.

The resumed record should keep the parser result as verified at `abc123`, mark the formatter edit as current-task but unverified, classify the export file as protected or unknown, and name the next formatter check. It should not claim the whole working tree passed, stage the export, or ask for permission to resume the already authorized formatter work. If another formatter process may still be writing, it pauses that mutation until the writer boundary is clear.
