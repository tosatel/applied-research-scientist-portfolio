import sys;from pathlib import Path;sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"));from gates import failures,readiness
def test_gate():
 s={"reliability":.8,"robustness":.8,"transparency":.8,"privacy":.4,"fairness":.8,"governance":.8};t={k:.6 for k in s};assert failures(s,t)==["privacy"];assert readiness(.82,["privacy"])=="remediation_required"
def test_ready():assert readiness(.84,[])=="ready_for_controlled_pilot"
