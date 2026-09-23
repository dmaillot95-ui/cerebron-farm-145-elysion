from __future__ import annotations
import json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parent
required=[
  ROOT/"architecture"/"ELYSION_ARCHITECTURE_V1.json",
  ROOT/"memory"/"ELYSION_MEMORY_CONTRACT_V1.json",
  ROOT/"benchmarks"/"ELYSION_BENCHMARK_V1.json",
  ROOT/"agora"/"AGORA-ELYSION-001"/"ASTRA_ASSIGNMENTS_V1.json",
]

def main():
    missing=[str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        print(json.dumps({"status":"FAIL","missing":missing}))
        return 1
    b=json.loads((ROOT/"benchmarks"/"ELYSION_BENCHMARK_V1.json").read_text())
    m=json.loads((ROOT/"memory"/"ELYSION_MEMORY_CONTRACT_V1.json").read_text())
    assert b["m6_rule"]=="M6_NEVER_IN_TRAIN"
    assert "M6_COLD_BENCHMARK" in m["training_forbidden"]
    print(json.dumps({"status":"PASS","m6_guard":True,"required_files":len(required)}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
