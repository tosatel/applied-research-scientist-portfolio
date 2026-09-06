import sys
from pathlib import Path
SRC=Path(__file__).resolve().parents[1]/"src"; sys.path.insert(0,str(SRC))
from metrics import exact_match, token_f1, keyword_coverage, groundedness, appropriate_refusal

def test_exact_match(): assert exact_match("Queue"," queue ")==1.0
def test_token_f1(): assert token_f1("machine learning model","learning model")>0.7
def test_keyword_coverage(): assert keyword_coverage("retrieval|context","Retrieval supplies external context.")==1.0
def test_groundedness(): assert groundedness("A queue follows first in first out order.","A queue follows first in first out.")>0.7
def test_refusal(): assert appropriate_refusal(False,"There is not enough information in the context.")==1.0
