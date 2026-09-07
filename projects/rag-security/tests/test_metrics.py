import sys;from pathlib import Path;sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"));from metrics import poison_exposure,trusted_ratio
def test_metrics():
 r=[{"is_trusted":"1"},{"is_trusted":"0"}];assert poison_exposure(r)==.5 and trusted_ratio(r)==.5
