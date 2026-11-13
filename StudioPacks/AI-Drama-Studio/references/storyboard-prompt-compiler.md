# 导演分镜与模型提示词编译

## 镜头合同

每个镜头必须写明：
- shot_id、episode_id、场景与资产 ID；
- start_seconds、duration_seconds；
- shot_size、camera_angle、camera_move；
- screen_direction、blocking；
- observable_action、performance、start_state、end_state；
- dialogue、speaker_id、voice_mode；
- sound_design、lighting、transition；
- visual_evidence、reference_bindings；
- generation_mode、risk_level。

景别、机位和运镜分栏存储，不把三个概念混成一个自由文本字段。

## 先空间后镜头

多角色、追逐、打斗、镜面、巨物或复杂场景先画俯视 blocking：
- 场景原点；
- 角色初始位置；
- 目标路径；
- 摄影机位置与运动；
- 视线和轴线；
- 道具接触点；
- 镜头终态。

没有空间解释的瞬移、左右互换、道具换手和镜头穿墙，视为待修复。

## 时间轴

镜头区间采用 [start, end)：
- start_seconds 从 0 开始；
- 同一 episode 的镜头顺序无重叠、无未解释空档；
- duration_seconds 必须大于 0；
- 总时长与目标片长一致，允许的误差由项目配置明确；
- 单镜时长不得超过当前 model card 的已验证上限。

## 提示词编译顺序

模型提示词按以下优先级拼装：
1. 场景 / 世界上下文；
2. 参考素材映射与控制职责；
3. 起始构图、人物身份和空间关系；
4. 单一主要动作与时间节拍；
5. 表演、视线、接触和物理结果；
6. 摄影机、焦段、景别和运动；
7. 光线、色彩、材质和风格；
8. 声音 / 对白 / 口型策略；
9. 终态与下一镜可承接状态；
10. 负向约束，只写本镜真实风险。

## 多模态参考

不要假设每个模型支持相同数量或类型的图片 / 视频 / 音频。先读取 model card。每个素材必须标注角色，例如：
- REF-CHAR-001：控制人物身份，不控制表情；
- REF-LOC-001：控制空间和材质，不控制镜头构图；
- REF-ACTION-001：只参考动作节奏；
- REF-VOICE-001：仅在授权并被入口支持时控制声线。

## 输出模式

- shot_by_shot：适合精确角色、逐镜重试和素材绑定。
- timeline：适合模型可稳定理解时间码的长段。
- hybrid：保留导演时间线，同时导出逐镜任务。

每次编译必须输出 model_id、capability_snapshot_id、prompt_version、reference_ids、参数、预计时长、风险和输出路径。