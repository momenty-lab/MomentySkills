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

The scaffold and final six-file public skill snapshot are integrated. The reviewed skill hashes are preserved. An isolated `.agents/skills` collision and symlink check, official `quick_validate`, native skill discovery, and repository enablement all passed. Native discovery made no model calls.

Eight synthetic routing cases produced the expected decisions. Case F exposed one fallback ambiguity; its wording was narrowed and the case was rechecked. Full repository validation passed independently with Python 3.11 and pinned `PyYAML==6.0.2`, and all four validator unit tests passed. The staged 42-file destination diff check and secret scan also passed with no findings.

The destination checkout is initialized on `main` with all 42 files staged. The public GitHub repository exists with Issues and Discussions enabled, wiki disabled, private vulnerability reporting enabled, and the experience and skill-proposal labels created. No initial commit or content push has occurred yet. Next: create the initial commit, push `main`, and confirm the GitHub Actions validation result. The repository remains unreleased and its production effectiveness and population-level impact remain unverified.
