# MomentySkills

[English](README.md)

MomentySkills 是一个原创、开源的 Codex 可移植技能集合，面向软件开发中反复出现的工作流程。每项技能把聚焦的指令、边界和必要的配套资料组织在一起，便于检查、调整和独立使用，不依赖私有 Momenty 工作区。

## 技能

| 技能 | 用途 |
| --- | --- |
| [`adaptive-dev-routing`](skills/adaptive-dev-routing/SKILL.md) | 为开发任务选择当前环境可用的模型与推理强度，并应用明确的审查和修复关卡。 |
| [`development-task-handoff`](skills/development-task-handoff/SKILL.md) | 在代理、工具、会话或工作区切换时，保存并核验可继续的开发状态。 |

每项技能都以独立目录提供。使用时以其中的 `SKILL.md` 为入口，只在适用时读取配套参考资料。

## 安装

[Codex Skills 官方文档](https://developers.openai.com/codex/skills)列出的发现位置包括用户级 `$HOME/.agents/skills` 和仓库级 `.agents/skills`，也支持通过符号链接连接技能目录。Codex 通常会自动检测变更；安装后仍未出现时可重启 Codex。

先把本仓库克隆到专用源码目录，再链接需要使用的技能。下面的示例会检查仓库目标和所选技能路径；只要任意位置已存在就停止，不会覆盖：

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

如需安装 Development Task Handoff，把变量改为 `skill_name="development-task-handoff"`。如果仓库已经克隆，需要再添加一项技能，保留 `repo_dir`，只调整 `skill_name`：

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

不要删除或覆盖已有的同名个人技能。如果只想在某个仓库内启用，也应先做同样的碰撞检查，再把技能链接到该仓库的 `.agents/skills/` 目录。

## 使用

可以直接向 Codex 提出符合技能范围的开发任务，让每个 `SKILL.md` 的描述参与正常技能发现，也可以显式调用：

```text
$adaptive-dev-routing 为这个实现任务选择配置，并解释需要哪些审查关卡。

$development-task-handoff 为当前开发任务准备一份经过核验的接力记录。
```

`adaptive-dev-routing` 会在当前运行环境可用的模型与推理强度内提出路由建议。它的[配置说明](skills/adaptive-dev-routing/references/profiles.md)介绍了如何复制和调整配置，同时避免把个人路径、账号信息或私有项目规则放入这个公开仓库。

## 反馈与贡献

Bug、经验报告和技能提案请从 [Issue 选择页](https://github.com/momenty-lab/MomentySkills/issues/new/choose)提交；问题和尚未形成明确 Issue 的想法可以放到 [Discussions](https://github.com/momenty-lab/MomentySkills/discussions)。

提交 Pull Request 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)和[来源说明](docs/provenance.md)。涉及性能或效率的经验报告还应遵循[评估协议](docs/evaluation.md)，说明实际测量的内容，未测得的值保持为 `unknown`。

## 本地开发

使用 Python 3.11 或更高版本。开发依赖已固定在 `requirements-dev.txt` 中。

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

验证器会检查 YAML 与 JSON 语法、技能 frontmatter 与名称、仓库元数据和本地 Markdown 链接。它不会模拟 Codex，也不能确认运行时结果。

## 许可证

代码和文档采用 [MIT License](LICENSE)。
