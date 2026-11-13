# 生产执行、任务账本与恢复

每个任务记录 job_id、幂等键、模型快照、prompt/reference/params 哈希、provider job ID、状态、费用和输出路径。状态为 queued、prepared、confirmed、submitted、running、succeeded、failed、unknown、cancelled。unknown 先查询和收集，不盲目重提。重试记录 retry_of。GPU 批次复用实例，任务收集完成后关机。凭据保存在项目外，费用估算注明来源和日期。
