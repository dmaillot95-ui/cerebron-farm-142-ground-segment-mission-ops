import json,hashlib,pathlib,platform
import math
rate=50e6;window=480.;eff=.82;bits=rate*window*eff;gb=bits/8/1e9;out={"downlink_bps":rate,"contact_window_s":window,"efficiency":eff,"delivered_gb":gb};ok=gb>0
out.update({"farm":142,"engine":"python-engineering-batch-canary","engine_version":platform.python_version(),"test":"CONTACT_WINDOW_CAPACITY","status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ENGINEERING_CANARY_NOT_PHYSICAL_VALIDATION"});raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f142_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
