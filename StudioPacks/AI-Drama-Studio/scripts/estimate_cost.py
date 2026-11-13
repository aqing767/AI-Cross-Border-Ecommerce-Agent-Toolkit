#!/usr/bin/env python3
import argparse,csv,collections
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument("jobs_csv");a=p.parse_args()
 totals=collections.defaultdict(float);counts=collections.Counter();unknown=0
 with Path(a.jobs_csv).open(encoding="utf-8-sig",newline="") as f:
  for row in csv.DictReader(f):
   cur=(row.get("currency") or "UNKNOWN").upper();status=row.get("status","")
   counts[(cur,status)]+=1
   raw=row.get("cost_estimate") or ""
   try: totals[cur]+=float(raw)
   except (ValueError,TypeError): unknown+=1
 print("Estimated totals by currency:")
 for cur,val in sorted(totals.items()): print(f"  {cur}: {val:.4f}")
 print("Job counts:")
 for (cur,status),n in sorted(counts.items()): print(f"  {cur} / {status or 'unspecified'}: {n}")
 print(f"Unknown estimates: {unknown}")
 print("Note: estimates are only as reliable as the price source and verification date recorded in each job.")
if __name__=="__main__":main()
