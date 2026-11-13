# 架构

## 七层生产架构

1. **创意与 IP 层**：市场信号、题材、受众承诺、改编权、项目立项。
2. **故事与剧本层**：原著索引、故事圣经、人物弧线、分集图、可拍剧本。
3. **资产与世界层**：角色、服装、场景、道具、声音、关系、空间与时间状态。
4. **导演与分镜层**：blocking、镜头覆盖、关键帧、时间码、动作相位和声音设计。
5. **模型编译层**：能力快照、prompt adapter、参考素材映射、参数校验。
6. **生产执行层**：job queue、预算、授权、幂等、重试、任务找回和文件收集。
7. **后期与质量层**：剪辑、字幕、配音、混音、画面 / 声音 / 连续性 / 合规验收。

## 12 个专业能力模块

- IP Scout：题材与市场研究。
- Novel Analyst：原著拆解、章节索引、改编映射。
- Story Architect：世界观、故事圣经、系列弧线。
- Screenwriter：分集剧本、对白、表演节拍。
- Asset Supervisor：人物 / 场景 / 道具 / 服装 / 声音。
- Continuity Supervisor：跨镜 / 跨集状态与伏笔。
- Director：场面调度、镜头意图和覆盖。
- Storyboard Artist：镜头表、关键帧、宫格与预演。
- Prompt Compiler：按模型能力生成请求。
- Producer：任务队列、费用、授权与恢复。
- Editor：剪辑时间线、字幕、音频与导出。
- QC Reviewer：独立质检、返工定位和验收报告。

## 文件事实源

每个项目至少包含：

- project.json：项目元数据、来源权利、格式配置、模型能力快照。
- story-bible.md：全局事实、世界规则、主题和叙事承诺。
- character-bible.md：角色身份不变量、状态变量和声音。
- assets/registry.json：所有资产唯一 ID、引用文件和审批状态。
- episodes/EPxxx/script.md：单集剧本。
- episodes/EPxxx/shots.json：结构化镜头。
- continuity-ledger.csv：跨集 / 跨镜状态变更。
- generation-jobs.csv：模型任务、幂等键、状态、费用和输出。
- qc/：检查结果、证据、修复和验收。

## 关键设计约束

- 每个阶段只拥有自己的数据字段；后续阶段不能偷偷改写上游事实。
- 上游变化产生版本号，依赖它的下游产物自动标记 stale。
- 角色 ID 不随服装变化；服装是独立 look_id。
- 镜头 ID、资产 ID、任务 ID 永不复用。
- 所有时间以秒为数值，镜头区间采用 [start, end) 语义。
- 生成状态和媒体质量是两件事：任务成功不等于画面合格。
- 所有供应商调用通过 adapter；Skill 不绑定某一家服务。