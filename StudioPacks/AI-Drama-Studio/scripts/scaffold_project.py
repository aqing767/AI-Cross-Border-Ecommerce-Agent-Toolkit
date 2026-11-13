#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description="Create an AI Drama Studio project")
    p.add_argument("--name",required=True); p.add_argument("--slug",required=True); p.add_argument("--output",default="projects")
    a=p.parse_args()
    slug=a.slug.lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,62}",slug): raise SystemExit("slug must be 2-63 lowercase letters, digits or hyphens")
    root=Path(a.output).resolve()/slug
    if root.exists(): raise SystemExit(f"Refusing to overwrite existing project: {root}")
    for d in ["episodes/EP001","assets/characters","assets/locations","assets/props","assets/references","qc","exports"]: (root/d).mkdir(parents=True,exist_ok=True)
    data={"schema_version":"1.0.0","project_id":slug,"title":a.name,"status":"planning","format_profile":{"id":"serial_episode","aspect_ratio":"9:16","target_duration_seconds":90,"language":"zh-CN"},"source":{"type":"original","rights_status":"pending","source_uri":None,"notes":""},"creative":{"logline":"","genre":[],"audience":"","visual_style":"unselected","tone":"","constraints":[]},"model_capabilities":{"status":"unverified","provider":None,"model_id":None,"max_duration_seconds":None,"max_reference_assets":None,"verified_at":None,"evidence":None},"assets":[],"episodes":[{"episode_id":"EP001","status":"not_started","target_duration_seconds":90,"shots":[]}]}
    (root/"project.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (root/"story-bible.md").write_text("# 故事圣经\n\n待创作\n",encoding="utf-8")
    (root/"continuity-ledger.csv").write_text("episode_id,entity_id,state_before,event,state_after,evidence\n",encoding="utf-8")
    (root/"generation-jobs.csv").write_text("job_id,idempotency_key,episode_id,shot_id,modality,provider,model_id,status,provider_job_id,cost_estimate,cost_actual,currency,prompt_hash,reference_hashes,params_hash,output_paths,error_code,retry_of\n",encoding="utf-8")
    (root/"制作进度.md").write_text("# 制作进度\n\n- brief: draft\n- story: not_started\n- script: not_started\n- assets: not_started\n- storyboard: not_started\n- production: not_started\n- edit: not_started\n- review: not_started\n",encoding="utf-8")
    print(root)
if __name__=="__main__": main()
