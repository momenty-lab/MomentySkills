# Repository instructions

These instructions apply to the standalone MomentySkills repository.

Read and update [HANDOFF.md](HANDOFF.md) as the sole current continuation record for this repository; completing a recorded task does not authorize new work.

## Scope and public boundary

- Keep every skill portable and understandable from this repository alone.
- Write original content. Do not copy private workspace rules, private or proprietary application source, session exports, credentials, personal data, or third-party artwork into the repository. Original redistributable minimal reproductions are allowed when they are necessary.
- Describe the project and each skill through concrete, reviewable capabilities. Scope claims about quality, efficiency, cost, or runtime outcomes to the evidence that supports them. Treat personal usage reports as anecdotes, not audits, benchmarks, proof of effectiveness, or vendor endorsement.
- Keep changes focused on the requested skill, shared packaging contract, or community documentation. Avoid unrelated governance, websites, dependency upgrades, and abstractions.

Current interface scope: N/A. MomentySkills is a Markdown/Python Codex skill collection and has no user-facing runtime interface or declared iOS/Web target. If that changes, define and verify the new interface/platform scope before implementation.

<!-- momenty:local-integration -->
When this repository is embedded in a larger workspace, follow any applicable ancestor instructions available in that checkout. A standalone clone has no external workspace dependency.
<!-- /momenty:local-integration -->

## Skill contract

- Put each skill in `skills/<name>/` with a required `SKILL.md`.
- Use lowercase letters, digits, and hyphens for names; the folder and frontmatter name must match.
- Keep `SKILL.md` focused on non-obvious decisions and boundaries. Add references, examples, or scripts only when they materially help the workflow.
- Update `metadata.yaml`, README skill tables, and `CHANGELOG.md` when the public skill inventory changes.
- Treat routing profiles as configurable hypotheses. Validate availability and distinguish requested configuration from observed configuration.

## Evaluation and validation

- Accept positive, neutral, mixed, and negative outcomes. Never infer missing time, token, review, or repair values; use `unknown` with a reason.
- Redact private inputs and identify measurement provenance before sharing results.
- Add tests for meaningful executable behavior and failure cases. Do not claim that schema or keyword checks prove agent behavior.
- Use Python 3.11 or newer with `requirements-dev.txt`, then run `python scripts/validate.py` and `python -m unittest discover -s tests -v` before declaring a change validated.
- Report what was actually checked and any effectiveness or runtime behavior that remains unverified.
