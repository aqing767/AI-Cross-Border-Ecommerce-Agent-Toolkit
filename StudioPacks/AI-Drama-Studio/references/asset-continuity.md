# 资产注册与连续性

## 资产类型

character / look / location / prop / costume / voice / style / reference_frame / sound_cue。

每个资产使用唯一稳定 ID，例如 CHAR-001、LOC-004、PROP-012。显示名称可以变化，ID 不变。

## 角色身份与状态分离

身份不变量：
- 面部结构、年龄范围、体型比例、发型基准、辨识标记；
- 核心性格、说话方式、经授权的声音锚点；
- 角色唯一参考图和批准版本。

状态变量：
- 当前服装 look_id；
- 伤势、污渍、湿度、疲惫、情绪；
- 持有道具、所在位置、人物关系阶段；
- 本集新增或消失的状态。

禁止用服装变体创建新角色 ID。禁止将一张多角色拼图误登记为多个角色参考图。

## 场景与空间

每个重要场景登记：
- 坐标原点、入口 / 出口、固定家具和关键道具；
- 时间、天气、主光源方向和色温；
- 人物起始位置、屏幕方向和 180 度轴；
- 镜头可达区域、遮挡和反射规则。

镜头调度使用 start → path → end。跨镜延续时，上一镜终态必须等于下一镜起态，除非剪辑明确表达了时间跳跃或空间转移。

## 道具状态

每个关键道具使用 PROP-ID + STATE-ID。记录持有人、位置、朝向、损坏、开合、数量和可见文字。关键文字 / logo 默认后期合成，不依赖视频模型准确生成。

## 声音身份

声音资产记录来源授权、语言、音域、音色、语速、情绪范围和参考文件。未经明确授权不得克隆或模仿真实人物声音。模型原生对白与后期配音必须区分，并在混音台账中记录。

## 参考素材语义

每个 reference 记录：
- file_path / file_hash；
- controls：该素材控制哪些维度；
- must_not_transfer：禁止从素材继承哪些内容；
- approved_by / approved_at；
- status：planned / received / reviewed / accepted / rejected。

planned 不等于 received；received 不等于 reviewed；只有 accepted 才可用于正式生成。