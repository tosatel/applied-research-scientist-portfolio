import sys; sys.path.insert(0,'src')
from models import build_models

def test_model_set():
    assert set(build_models())=={'Logistic Regression','Random Forest','Isolation Forest'}
