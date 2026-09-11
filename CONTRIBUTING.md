# Contributing to MomentySkills

MomentySkills improves through original skills, reproducible observations, clear failure reports, and focused documentation fixes. Positive, neutral, mixed, and negative results are equally welcome.

## Before contributing

- Remove credentials, account details, private paths, proprietary source, prompts you cannot share, and personal data.
- Confirm that you have the right to submit the content under the [MIT License](LICENSE).
- Read the [evaluation protocol](docs/evaluation.md) before making performance or efficiency claims.
- Search existing issues before opening a duplicate. Use the skill proposal form for a new skill and the experience report for observed results.

Do not submit copied private rules, exported sessions, private or proprietary application source, third-party artwork, or vendored skill-authoring tools. Original redistributable minimal reproductions are welcome when they are relevant and safely scoped.

## Skill changes

Each skill lives at `skills/<skill-name>/SKILL.md`. A contribution should:

1. Use a lowercase name containing only letters, digits, and single hyphens; keep the directory and frontmatter name identical.
2. Give the frontmatter a concise `description` that tells Codex when the skill applies.
3. State the problem, observable workflow, boundaries, and failure conditions without promising outcomes that have not been measured.
4. Add only supporting files that the skill actually needs, and link them from `SKILL.md` where they become relevant.
5. Update `metadata.yaml`, the README skill tables, and `CHANGELOG.md` when the public inventory changes.
6. Add meaningful tests for executable behavior. A wording check alone does not demonstrate agent behavior.

Profiles and examples must distinguish requested configuration from observed configuration. Model availability differs by runtime, account, and date; do not present one profile as a universal ordering.

## Experience reports

Use the [experience report form](.github/ISSUE_TEMPLATE/experience_report.yml). When possible, run a baseline and a candidate against the same task revision and constraints. Report:

- task and environment context that can be shared safely;
- baseline and candidate setup;
- requested model and reasoning effort for each routed role;
- observed model and reasoning effort, or `unknown` with the reason;
- time and token values with their source and definition, covering main or coordination work, context handoff, initial execution, review, and repair as applicable;
- review and repair counts, including zero; use `unknown` when not measured;
- the result direction and any failures or surprises.

Never infer missing measurements. Estimates may be qualitative feedback but cannot support measured savings or calibration claims. We do not pay, rank, or recognize contributors based on whether an outcome is positive.

## Pull requests

Keep each pull request focused. Explain the problem and resulting behavior, list the evidence you collected, and identify what remains unverified. Before submitting, run:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

These commands require Python 3.11 or newer and the pinned dependency in `requirements-dev.txt`. Maintainers may ask for narrower claims, additional negative cases, or clearer provenance before merging.
