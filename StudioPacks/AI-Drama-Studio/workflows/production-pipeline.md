# 生产流水线与阶段门禁

## 阶段状态

每个阶段使用：not_started → draft → review → approved → stale / blocked。执行任务另用 queued → submitted → running → succeeded / failed / unknown / cancelled。

| 阶段 | 输入 | 交付物 | 进入下一阶段条件 |
|---|---|---|---|
| P0 立项 | 用户需求、素材、授权 | brief、project.json | 来源 / 权利 / 格式清楚 |
| P1 原著与题材分析 | 小说、剧本、创意 | source map、adaptation map、opportunity brief | 事实与推断分离 |
| P2 故事开发 | P1 | story bible、series arc、episode map | 主线、人物动机、集尾承诺成立 |
| P3 单集剧本 | episode map | screenplay、dialogue timeline | 可拍、因果清晰、时长合理 |
| P4 资产定义 | 剧本 | asset registry、角色 / 场景 / 道具圣经 | 身份、外观、状态和授权明确 |
| P5 导演分镜 | 剧本 + 资产 | blocking、shots、keyframe specs | 空间 / 轴线 / 动作 / 时间闭合 |
| P6 模型编译 | shots + model card | image / video / audio jobs | 请求符合当前入口能力 |
| P7 生产 | 已确认 job | media files、job logs | 任务终态且文件可读取 |
| P8 后期 | 已接受媒体 | edit decision list、字幕、音轨、成片 | 交付文件可播放、可定位 |
| P9 审查 | 全部交付物 | qc report、repair list | P0 / P1 问题清零 |
| P10 发布包 | 已通过 QC | master、captions、poster、credits、manifest | 人工确认发布 |

## 依赖失效规则

- 修改 story bible：P2 之后的剧本、资产、分镜、任务和剪辑均 stale。
- 修改单集剧本：该集资产提取、分镜、任务和剪辑 stale；其他集仅在引用了被修改事实时 stale。
- 修改角色身份锚点：所有引用该角色的视觉资产与镜头 stale。
- 修改单个镜头：只使该镜头及其相邻连续性依赖、相关任务和剪辑段 stale。
- 修改 model card：尚未执行的相关任务需重新编译；已生成媒体保留原模型快照。
- 修改 prompt / reference / params / output path：当前 job 的既有确认失效。

## 生产确认

确认对象必须是具体批次，至少包含：
- job 数量与模态；
- 完整 prompt 或 spec；
- model_id、参数和时长；
- 实际参考素材及其用途；
- 预计成本、最大重试数和费用上限；
- 输出路径和覆盖策略；
- adapter 名称与凭据来源说明。

确认只授权当前 job 指纹。不得把“继续”“做完它”当成任意供应商调用的无限授权。

## Auto mode

用户要求全自动时：
- 自动完成不花钱的分析、剧本、资产定义、分镜和编译。
- 可在已明确授权范围内自动执行任务。
- 碰到未验证模型能力、费用超限、真实人物声音 / 肖像、上传第三方素材、发布或不可逆覆盖时阻断。
- 缺少执行器时交付完整 production pack，并标记 waiting_for_executor；绝不声称已经产出视频。