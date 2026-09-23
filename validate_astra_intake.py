from __future__ import annotations
import hashlib,json,pathlib,sys

ROOT=pathlib.Path(__file__).resolve().parent
AGORA=ROOT/"agora"/"AGORA-ELYSION-001"
ASTRA=AGORA/"astra"
EXPECTED=["ASTRA-A","ASTRA-B","ASTRA-C","ASTRA-D","ASTRA-E","ASTRA-F"]

def sha256_text(s:str)->str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    rows=[]
    for aid in EXPECTED:
        hits=sorted(ASTRA.glob(aid+"*.json")) if ASTRA.exists() else []
        if not hits:
            rows.append({"agent_id":aid,"status":"MISSING"})
            continue
        p=hits[-1]
        try:
            d=json.loads(p.read_text())
        except Exception as e:
            rows.append({"agent_id":aid,"status":"INVALID_JSON","file":str(p),"error":type(e).__name__})
            continue
        required=["agent_id","status","task_id","model_id","model_revision","execution_id","result_sha256","provenance","summary","evidence","open_blocks","next_action"]
        missing=[k for k in required if k not in d]
        status="VALID_FORMAT" if not missing else "MISSING_FIELDS"
        rows.append({"agent_id":aid,"status":status,"file":str(p.relative_to(ROOT)),"missing":missing})
    complete=all(x["status"]=="VALID_FORMAT" for x in rows)
    out={"schema":"ELYSION_ASTRA_INTAKE_V1","complete":complete,"agents":rows}
    out["receipt_sha256"]=sha256_text(json.dumps(out,sort_keys=True,separators=(",",":")))
    print(json.dumps(out,indent=2))
    return 0 if complete else 2

if __name__=="__main__":
    raise SystemExit(main())
