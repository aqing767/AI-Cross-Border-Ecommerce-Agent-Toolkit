# AI Drama Studio

个人专属 AI 漫剧 / 微短剧 / 小说改编生产套件。它是一个独立 Skill Pack，采用文件优先、模型无关、可审计、可恢复的方式，把创意转成可生产、可剪辑、可复核的项目包。

## 目标

- 一条总控 Skill 自动路由 12 个专业能力域。
- 21 个参考仓库逐项建立来源映射；只吸收可泛化的方法，不复制未获许可的代码、提示词原文、素材或品牌。
- 以项目文件作为唯一事实源；聊天上下文不是项目数据库。
- 先做文本与资产计划，再编译镜头和模型任务。
- 任何付费媒体任务先预览，再按授权范围执行。
- 用确定性脚本检查 ID、引用、时间线、能力边界和任务账本。
- 附带离线浏览器工作台原型，可导入 / 导出项目 JSON。

## 目录

- SKILL.md：唯一自然语言入口与总控路由。
- references/：故事开发、资产一致性、分镜编译、模型路由、生产运维和质量闸门。
- workflows/：生产状态机与阶段交接。
- schemas/：项目与镜头 JSON Schema。
- templates/：项目、故事圣经、角色圣经和台账模板。
- scripts/：标准库 Python 脚手架、校验和成本估算。
- tests/：离线单元测试。
- workbench/：本地静态看板原型。

## 安装到 Codex Skill 目录

把整个 AI-Drama-Studio 文件夹复制到：

- Windows：%USERPROFILE%\.codex\skills\ai-drama-studio
- macOS / Linux：$CODEX_HOME/skills/ai-drama-studio（未设置时为 ~/.codex/skills/ai-drama-studio）

其他兼容 Agent 可将该目录放进其 skills 目录。入口文件必须保留为 SKILL.md。

## 新建项目

在本目录执行：

~~~bash
python scripts/scaffold_project.py --name "项目名称" --slug "project-slug" --output ./projects
~~~

## 校验项目

~~~bash
python scripts/validate_project.py ./projects/project-slug
~~~

校验只报告结构和确定性问题，不宣称模型生成的画面已经通过审片。

## 成本估算

~~~bash
python scripts/estimate_cost.py ./projects/project-slug/generation-jobs.csv
~~~

## 启动离线工作台

~~~bash
python -m http.server 8765 --directory workbench
~~~

浏览器打开 http://127.0.0.1:8765。工作台数据默认保存在当前浏览器 localStorage；需要跨设备或交给 Agent 时，使用导出 / 导入项目 JSON。它目前不是远程生成服务，也不会自动调用供应商 API。

## 生产原则

1. 原著事实、创作推断、用户决定和未决事项必须分开。
2. 角色身份、角色状态、服装变体、声音锚点分别管理。
3. 参考素材必须登记真实文件；未上传素材只能标为计划项，不能伪称已核验。
4. 模型能力以本次实际入口的 schema 和实测为准，不从旧版本照搬限制。
5. 上游内容修改后，所有受影响的下游产物标记为 stale。
6. 生成任务超时先找回任务状态，不盲目重提。
7. 项目凭据保存在项目目录之外。
8. 交付包含可编辑源文件、素材清单、镜头清单、任务记录、质检报告和版本信息。

## 参考来源

见 SOURCES.md。各仓库许可证与第三方素材边界必须在复用具体代码或文本前再次核对。