# MomentySkills

[English](README.md)

MomentySkills 是一个原创、开源的 Codex 实验性技能集合。首个技能 `adaptive-dev-routing` 提供一套面向开发任务的实践框架：按任务选择模型与推理强度，并在有需要时加入独立的规格审查、质量审查和修复关卡。

> “Codex 官方用量统计显示我已经使用了 200 亿 tokens 之后，我想更认真地研究如何提升开发效率，也把这些实验分享出来，让社区一起验证、质疑、反馈和受益。”——MomentySkills 创始人

这里的 200 亿来自创始人对 Codex 官方界面显示结果的个人陈述，没有经过独立审计，也不能证明本技能可以提升质量、节省时间或减少 token。MomentySkills 是独立社区项目，与 OpenAI 没有隶属或背书关系。

## 当前状态

仓库中的所有内容都处于实验阶段。首个技能提供的是可以检验的路由假设，不是基准测试结论。生产环境有效性尚未验证，目前也没有群体层面的测量数据。我们希望收集的证据见[评估说明](docs/evaluation.md)。

## 技能

| 技能 | 用途 | 成熟度 |
| --- | --- | --- |
| [`adaptive-dev-routing`](skills/adaptive-dev-routing/SKILL.md) | 为开发任务选择当前环境可用的模型与推理强度，并应用明确的审查和修复关卡。 | 实验性 |

每个技能都是可移植目录，包含自身的 `SKILL.md`，以及确有需要的参考资料、示例或脚本。这个集合不依赖任何 Momenty 应用或私有工作区。

## 安全安装

[Codex Skills 官方文档](https://developers.openai.com/codex/skills)列出的发现位置包括用户级 `$HOME/.agents/skills` 和仓库级 `.agents/skills`，也支持通过符号链接连接技能目录。Codex 通常会自动检测变更；安装后仍未出现时可重启 Codex。

先克隆到专用源码目录，再明确选择是否用符号链接启用技能。下面的示例会先检查克隆目标和同名技能路径；只要任意位置已存在就停止，不会覆盖：

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

不要为了安装本技能而删除或覆盖已有的同名个人技能。如果只想在某个仓库内启用，也应先做同样的碰撞检查，再链接到该仓库的 `.agents/skills/` 目录。

## 使用方式

可以直接向 Codex 提出具体开发任务，让 `SKILL.md` 的描述参与正常技能发现，也可以显式调用：

```text
$adaptive-dev-routing 为这个实现任务选择配置，并解释需要哪些审查关卡。
```

技能返回的是受当前运行环境可用模型与推理强度约束的建议。记录实验时，请把“请求的配置”和“实际观察到的配置”分开填写。

## 自定义配置

先阅读[配置说明](skills/adaptive-dev-routing/references/profiles.md)，把[创始人配置示例](skills/adaptive-dev-routing/examples/founder-profile.json)复制到你自己控制的文件中，再只使用你的 Codex 运行环境支持的值。个人路径、账号信息和私有项目规则应留在这个公开克隆之外。

使用技能时显式选择复制后的配置：

```text
$adaptive-dev-routing 这个任务使用 ./my-routing-profile.json，并报告请求的路由配置。
```

示例配置只是起始假设，不是对模型或推理强度的通用排名。分享结果时，请提供配置文件版本或相关设置，让其他人能理解当时请求了什么。

## 贡献经验和技能

正向、中性、混合和负向结果都同样有价值。提交经验时尽量提供基线与候选方案，分别说明请求配置与观察配置，注明时间或 token 总量的来源；未测得的审查、修复或其他阶段消耗填写 `unknown`。提交前必须移除私有数据。项目不会根据结果是否正向给予奖励。

Bug、经验报告和技能提案请从 [Issue 选择页](https://github.com/momenty-lab/MomentySkills/issues/new/choose)提交；尚未形成明确 Issue 的问题和想法可以放到 [Discussions](https://github.com/momenty-lab/MomentySkills/discussions)。

提交 Pull Request 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)、[评估协议](docs/evaluation.md)和[来源说明](docs/provenance.md)。新技能应解决可重复出现的问题，明确适用边界，并提供可以检查的可观察行为。

## 本地开发

使用 Python 3.11 或更高版本。开发依赖已固定在 `requirements-dev.txt` 中。

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

验证器会检查 YAML 与 JSON 语法、技能 frontmatter 与名称、仓库元数据和本地 Markdown 链接。它不会模拟 Codex，也不能证明路由建议有效。

## 许可证

代码和文档采用 [MIT License](LICENSE)。
