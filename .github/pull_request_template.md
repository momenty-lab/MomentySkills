## Problem and resulting behavior

Describe the concrete problem and what changes for a skill user or contributor.

## Evidence

List the checks or experience reports you actually ran. Distinguish requested configuration from observed configuration and identify measurement sources.

## Remaining uncertainty

State any runtime behavior, effectiveness, platform, or data that was not verified.

## Checklist

- [ ] The contribution is original or its redistributable sources are identified.
- [ ] Private rules, private or proprietary app source, sessions, credentials, personal data, private paths, and third-party artwork are excluded.
- [ ] Skill inventory changes update `metadata.yaml`, both README files, and `CHANGELOG.md`.
- [ ] Positive, neutral, mixed, negative, zero, and unknown outcomes are represented honestly where relevant.
- [ ] `python scripts/validate.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
