---
name: development-task-handoff
description: Use when software development work must move between agents, tools, sessions, or workspaces, or when an interrupted task needs to resume from repository evidence without losing scope, authority, ownership, or verification state.
---

# Development Task Handoff

Continue one authorized development task from files and evidence. A handoff is a compact current-state record: it does not replace project truth, grant authority, prove that another writer stopped, or synchronize tools automatically.

## Start from evidence

Before preparing or resuming a handoff:

1. Resolve the actual project and workspace. Read the effective instructions through entry mechanisms the current tool really supports; do not assume it discovers parent files or invent a tool-specific config name.
2. Identify the authorized task, accepted decisions, scope, acceptance criteria, approval gates, and exactly one active continuation record. A switch of agent, tool, session, or workspace changes none of them.
3. Inspect the relevant project sources and current repository evidence. Treat handoff claims as evidence to corroborate, not as a substitute for the files and diff.

Read [references/workflow.md](references/workflow.md) for the applicable setup, progress-save, deliberate-handover, resume, or completion procedure and compact record fields.

## Preserve sources of truth

Keep each fact with its authority and link to it from the handoff:

| Fact | Typical authority |
| --- | --- |
| User intent and permission | Current user instruction and accepted task record |
| Project rules and decisions | Effective project instructions and decision records |
| Product or project state | The project's maintained status sources |
| Implementation state and history | Files, repository status, diff, and commits |
| Verification result | Actual command or review output tied to a specific state |
| Continuation snapshot | Exactly one active handoff file or clearly identified section |

Do not create a progress file per tool, mirror a project tracker, copy complete history, or reconstruct unknown state from timestamps and file similarity. Use `unknown` when a fact cannot be established.

## Invariants

- Keep one active handoff and one active writer for an affected working directory. A last-executor field is context, not a lock; pause conflicting mutation if another writer may still be active.
- Classify existing changes as current-task work, understood inherited related work, protected unrelated work, or unknown work. Continue only where the task can be isolated without absorbing protected work.
- A passing check applies to its tested state and scope. Reuse it only after checking relevant inputs, rules, environment, and later changes; unrelated changes do not automatically make it stale.
- A handoff transfers understanding, not permission. Preserve existing approval gates for destructive changes, external writes, Git publication, deployment, spending, credentials, or other restricted actions.
- Do not reset, clean, stash, switch away from, stage, commit, delete, or overwrite unrelated or unknown work merely to make the workspace look clean.
- Record partial edits and failed or unrun checks honestly. Never relabel an attempt as complete or a stale result as current.
- Keep credentials, private logs, personal data, and unrelated conversation out of the record. Include only the minimum context another executor needs.
- Use `unknown` when evidence cannot establish a fact. If the task, workspace, ownership, path, or permission remains unresolved, continue safe read-only diagnosis and ask only for the missing fact or decision.
