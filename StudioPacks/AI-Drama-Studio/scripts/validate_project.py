#!/usr/bin/env python3
import argparse,csv,json,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument("project");a=p.parse_args();root=Path(a.project);errors=[];warnings=[]
    try: data=json.loads((root/"project.json").read_text(encoding="utf-8"))
    except Exception as e: print(f"ERROR project.json: {e}");return 2
    for k in ["project_id","title","status","format_profile","source","assets","episodes"]:
        if k not in data: errors.append(f"missing project field: {k}")
    ids=set()
    for asset in data.get("assets",[]):
        aid=asset.get("id")
        if not aid: errors.append("asset missing id");continue
        if aid in ids: errors.append(f"duplicate asset id: {aid}")
        ids.add(aid)
        if asset.get("status")=="accepted" and not asset.get("reference_files") and asset.get("kind") in ["character","location","prop","reference_frame"]:
            warnings.append(f"{aid} marked accepted without reference_files")
    for ep in data.get("episodes",[]):
        shots=ep.get("shots",[]); cursor=0.0
        for s in sorted(shots,key=lambda x:x.get("start_seconds",0)):
            sid=s.get("shot_id","<missing>")
            for k in ["start_seconds","duration_seconds","observable_action","start_state","end_state","entity_ids"]:
                if k not in s: errors.append(f"{sid}: missing {k}")
            start=float(s.get("start_seconds",0));dur=float(s.get("duration_seconds",0))
            if dur<=0: errors.append(f"{sid}: duration must be > 0")
            if start < cursor-0.001: errors.append(f"{sid}: overlap or out-of-order timeline")
            if start > cursor+0.001: warnings.append(f"{sid}: unexplained timeline gap {cursor:.3f}-{start:.3f}")
            cursor=start+dur
            for ref in s.get("entity_ids",[]):
                if ref not in ids: errors.append(f"{sid}: unknown entity id {ref}")
        target=ep.get("target_duration_seconds")
        if target and shots and abs(cursor-float(target))>0.05: warnings.append(f"{ep.get('episode_id')}: timeline ends at {cursor:.2f}s, target {target}s")
    for f in ["continuity-ledger.csv","generation-jobs.csv"]:
        if (root/f).exists():
            try:
                with (root/f).open(encoding="utf-8-sig",newline="") as h: list(csv.DictReader(h))
            except Exception as e: errors.append(f"{f}: {e}")
    for x in warnings: print("WARN",x)
    for x in errors: print("ERROR",x)
    print(f"Validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0
if __name__=="__main__": sys.exit(main())
