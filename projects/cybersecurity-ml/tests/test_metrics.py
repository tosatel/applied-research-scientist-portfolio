import sys; sys.path.insert(0,'src')
from metrics import evaluate_binary

def test_perfect_metrics():
    m=evaluate_binary([0,0,1,1],[0,0,1,1],[.1,.2,.8,.9]); assert m['f1']==1 and m['false_positive_rate']==0
