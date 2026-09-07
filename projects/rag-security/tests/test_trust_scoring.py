import sys;from pathlib import Path;sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"));from trust_scoring import trust_score
def test_trust(): assert abs(trust_score({"provenance":.9,"authority":.9,"reliability":.9,"consistency":.9})-.9)<1e-9
