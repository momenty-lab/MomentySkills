# MomentySkills task handoff

This file is the sole current task record for the initial public-repository bootstrap.

## Objective

Bootstrap an original, bilingual, community-ready repository for `momenty-lab/MomentySkills`, led by the experimental `adaptive-dev-routing` skill. Staging, destination integration, GitHub publication, security setup, and any later release are distinct reviewable phases.

## Plan

1. Establish the public boundary and repository metadata.
2. Write English and Chinese onboarding, safe opt-in installation, customization, evaluation, contribution, security, conduct, provenance, and roadmap documentation.
3. Add GitHub contribution forms and a read-only validation workflow.
4. Test-drive a small Python validator for YAML and JSON, skill frontmatter and names, metadata consistency, and local Markdown links.
5. Run the validator and unit tests with Python 3.11 and the pinned development dependency, then review the staged file inventory and disclosure boundary.

## Acceptance criteria

- The repository is usable without any private parent repository, private or proprietary app source, private rules, session data, or artwork.
- Claims identify the founder's experience as a personal report and do not imply an audit, benchmark, measured savings, or OpenAI affiliation.
- Installation refuses an existing clone destination or same-name skill path instead of overwriting it.
- Experience reports accept positive, neutral, mixed, and negative results and distinguish requested configuration from observed configuration; unknown measurements are allowed and labeled.
- Validation has passing and adverse fixtures and makes no claim to simulate agent routing behavior.

## Status

Bootstrap complete. The initial public snapshot was committed as [`ff1ffff7d82a917569de2480570bcb54f6516093`](https://github.com/momenty-lab/MomentySkills/commit/ff1ffff7d82a917569de2480570bcb54f6516093) and pushed to `origin/main`. The repository is public, GitHub recognizes the MIT license, Issues and Discussions are enabled, wiki is disabled, and private vulnerability reporting is enabled.

GitHub Actions [run 34567660377](https://github.com/momenty-lab/MomentySkills/actions/runs/34567660377) succeeded on that commit. A fresh independent clone pinned to the same commit passed `python scripts/validate.py` and had a clean `git status`; the maintained local public checkout was also clean. Before publication, repository validation, all four validator unit tests, the staged diff check, secret scan, official `quick_validate`, isolated collision and symlink behavior, native skill discovery, and eight synthetic routing decisions were checked. Native discovery made no model calls, and the reviewed public skill hashes were preserved.

These results verify the initial commit named above. A later documentation-only commit, including this closure update, requires its own CI check and is not pre-verified by this record. No active bootstrap implementation remains. The next direction is community feedback; completing this task does not authorize new work. Production calibration and population-level effectiveness remain unknown, and no stable release has been tagged.
