import sys;from pathlib import Path;sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"));from scoring import composite,weakest
def test_composite():
 s={k:.8 for k in ["reliability","robustness","transparency","privacy","fairness","governance"]};w={k:1 for k in s};assert abs(composite(s,w)-.8)<1e-9
def test_weakest():
 s={"reliability":.8,"robustness":.7,"transparency":.6,"privacy":.9,"fairness":.8,"governance":.75};assert weakest(s)==("transparency",.6)
