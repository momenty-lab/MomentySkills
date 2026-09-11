# MomentySkills

[简体中文](README.zh-CN.md)

MomentySkills is an original, open-source collection of experimental skills for Codex. It starts with `adaptive-dev-routing`, a practical framework for choosing model and reasoning configurations for development work, then adding independent specification review, quality review, and repair gates where they are useful.

> “After the official Codex usage statistics reported that I had used 20 billion tokens, I wanted to put more serious effort into improving development efficiency—and share the experiments so the community can validate them, challenge them, and benefit together.” — MomentySkills founder

The token figure is the founder's personal report of what official Codex surfaces displayed. It is not an independently audited measurement or evidence that this skill improves quality, time, or token use. MomentySkills is an independent community project and is not affiliated with or endorsed by OpenAI.

## Status

Everything in this repository is experimental. The first skill packages a testable routing hypothesis, not a benchmark result. Production effectiveness has not been verified, and there are no population-level measurements yet. See [Evaluation](docs/evaluation.md) for the evidence we want contributors to collect.

## Skills

| Skill | Purpose | Maturity |
| --- | --- | --- |
| [`adaptive-dev-routing`](skills/adaptive-dev-routing/SKILL.md) | Select an available model and reasoning effort for a development task, then apply explicit review and repair gates. | Experimental |

Each skill is a portable directory with its own `SKILL.md` and only the references, examples, or scripts it needs. The collection does not depend on a Momenty app or a private workspace.

## Install safely

The [Codex skills documentation](https://developers.openai.com/codex/skills) lists `$HOME/.agents/skills` for user skills and `.agents/skills` for repository skills. Symlinked skill directories are supported. Codex normally detects changes automatically; restart it if an installed skill does not appear.

Clone into a dedicated source directory, then explicitly opt in with a symlink. This example stops before changing anything if either the clone destination or the same-name skill path already exists:

```bash
repo_dir="${HOME}/src/MomentySkills"
skill_dir="${HOME}/.agents/skills/adaptive-dev-routing"

if [ -e "$repo_dir" ] || [ -L "$repo_dir" ]; then
  echo "Refusing to replace existing path: $repo_dir" >&2
  exit 1
fi
if [ -e "$skill_dir" ] || [ -L "$skill_dir" ]; then
  echo "Refusing to replace existing skill: $skill_dir" >&2
  exit 1
fi

mkdir -p "$(dirname "$repo_dir")" "$(dirname "$skill_dir")"
git clone https://github.com/momenty-lab/MomentySkills.git "$repo_dir" &&
  ln -s "$repo_dir/skills/adaptive-dev-routing" "$skill_dir"
```

Do not remove or overwrite an existing personal skill to install this one. For repository-only discovery, use the same collision check before linking the skill under that repository's `.agents/skills/` directory.

## Use it

Ask Codex for a concrete development task and let normal skill discovery use the description in `SKILL.md`, or invoke it explicitly:

```text
$adaptive-dev-routing choose a configuration for this implementation and explain the review gates.
```

Treat the returned route as a proposal constrained by the models and reasoning efforts available in your runtime. Record the requested configuration separately from the configuration you actually observe.

## Customize it

Read the [profile guide](skills/adaptive-dev-routing/references/profiles.md), copy the [founder profile example](skills/adaptive-dev-routing/examples/founder-profile.json) to a file you control, and change only values supported by your Codex runtime. Keep personal paths, account data, and private project rules outside this public clone.

Select the copied profile explicitly when you use the skill:

```text
$adaptive-dev-routing Use my profile at ./my-routing-profile.json for this task and report the requested route.
```

The example profile is a starting hypothesis. It is not a universal ranking of models or reasoning levels. When you share a result, include the profile revision or relevant settings so someone else can understand what was requested.

## Contribute evidence and skills

All outcomes are useful: positive, neutral, mixed, and negative. Use an experience report to compare a baseline and candidate when possible, state requested and observed configurations, identify the source of any time or token totals, and mark unmeasured review, repair, or other stage costs as `unknown`. Redact private data before submission. Reports are never rewarded based on being positive.

Open the [issue chooser](https://github.com/momenty-lab/MomentySkills/issues/new/choose) for bugs, experience reports, or skill proposals. Use [Discussions](https://github.com/momenty-lab/MomentySkills/discussions) for questions and ideas that are not ready to become a tracked issue.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [the evaluation protocol](docs/evaluation.md), and [provenance policy](docs/provenance.md) before opening a pull request. New skills should solve a repeatable problem, declare their boundaries, and include a way to inspect their observable behavior.

## Develop locally

Use Python 3.11 or newer. The development dependency is pinned in `requirements-dev.txt`.

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks YAML and JSON syntax, required skill frontmatter and names, repository metadata, and local Markdown links. It does not simulate Codex or prove that routing recommendations are effective.

## License

Code and documentation are available under the [MIT License](LICENSE).
