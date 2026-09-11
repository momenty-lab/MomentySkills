# MomentySkills

[简体中文](README.zh-CN.md)

MomentySkills is an original, open-source collection of portable Codex skills for recurring software development workflows. Each skill packages focused instructions, boundaries, and supporting resources that can be inspected, adapted, and used without a private Momenty workspace.

## Skills

| Skill | Purpose |
| --- | --- |
| [`adaptive-dev-routing`](skills/adaptive-dev-routing/SKILL.md) | Select an available model and reasoning effort for a development task, then apply explicit review and repair gates. |
| [`development-task-handoff`](skills/development-task-handoff/SKILL.md) | Preserve and verify development state when work moves between agents, tools, sessions, or workspaces. |

Each skill is self-contained in its own directory. Follow its `SKILL.md` for the workflow and read supporting references only when they apply.

## Install

The [Codex skills documentation](https://developers.openai.com/codex/skills) lists `$HOME/.agents/skills` for user skills and `.agents/skills` for repository skills. Symlinked skill directories are supported. Codex normally detects changes automatically; restart it if an installed skill does not appear.

Clone this repository into a dedicated source directory, then link the skill you want to use. This example stops if the repository destination or selected skill path already exists:

```bash
repo_dir="${HOME}/src/MomentySkills"
skill_name="adaptive-dev-routing"
skill_dir="${HOME}/.agents/skills/${skill_name}"

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
  ln -s "$repo_dir/skills/$skill_name" "$skill_dir"
```

Set `skill_name="development-task-handoff"` to install Development Task Handoff instead. To add another skill after the repository is already cloned, keep `repo_dir` and change only `skill_name`:

```bash
repo_dir="${HOME}/src/MomentySkills"
skill_name="development-task-handoff"
skill_dir="${HOME}/.agents/skills/${skill_name}"

if [ ! -f "$repo_dir/skills/$skill_name/SKILL.md" ]; then
  echo "Skill source not found: $repo_dir/skills/$skill_name/SKILL.md" >&2
  exit 1
fi
if [ -e "$skill_dir" ] || [ -L "$skill_dir" ]; then
  echo "Refusing to replace existing skill: $skill_dir" >&2
  exit 1
fi

mkdir -p "$(dirname "$skill_dir")"
ln -s "$repo_dir/skills/$skill_name" "$skill_dir"
```

Do not remove or overwrite an existing personal skill. For repository-only discovery, use the same collision check before linking a skill under that repository's `.agents/skills/` directory.

## Use

Ask Codex for a matching development task and let normal skill discovery use each `SKILL.md` description, or invoke a skill explicitly:

```text
$adaptive-dev-routing choose a configuration for this implementation and explain the review gates.

$development-task-handoff prepare a verified handoff for this development task.
```

`adaptive-dev-routing` proposes routes within the models and reasoning efforts available in your runtime. Its [profile guide](skills/adaptive-dev-routing/references/profiles.md) explains how to copy and customize a profile without putting personal paths, account data, or private project rules in this public repository.

## Feedback and contributions

Use the [issue chooser](https://github.com/momenty-lab/MomentySkills/issues/new/choose) for bugs, experience reports, and skill proposals. Use [Discussions](https://github.com/momenty-lab/MomentySkills/discussions) for questions and early ideas.

Before opening a pull request, read [CONTRIBUTING.md](CONTRIBUTING.md) and the [provenance policy](docs/provenance.md). Performance or efficiency reports should also follow the [evaluation protocol](docs/evaluation.md), identify what was measured, and keep unmeasured values as `unknown`.

## Develop locally

Use Python 3.11 or newer. The development dependency is pinned in `requirements-dev.txt`.

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks YAML and JSON syntax, required skill frontmatter and names, repository metadata, and local Markdown links. It does not simulate Codex or establish runtime outcomes.

## License

Code and documentation are available under the [MIT License](LICENSE).
