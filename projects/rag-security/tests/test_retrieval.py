import sys;from pathlib import Path;sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"));from retrieval import relevance_score,rank_documents
def test_relevance(): assert relevance_score("queue fifo","queue uses fifo")>0
def test_trust_rank():
 d=[{"doc_id":"good","text":"queue fifo","is_trusted":"1","provenance":.9,"authority":.9,"reliability":.9,"consistency":.9},{"doc_id":"bad","text":"queue fifo","is_trusted":"0","provenance":.1,"authority":.1,"reliability":.1,"consistency":.1}]
 assert rank_documents("queue fifo",d,"trust_aware",1)[0]["doc_id"]=="good"
