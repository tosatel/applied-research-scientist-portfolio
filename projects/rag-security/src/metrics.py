def relevant_coverage(r,target): return float(any(d["doc_id"]==target for d in r))
def poison_exposure(r): return sum(int(d["is_trusted"])==0 for d in r)/len(r) if r else 0.0
def poison_top1(r): return float(bool(r) and int(r[0]["is_trusted"])==0)
def trusted_ratio(r): return sum(int(d["is_trusted"])==1 for d in r)/len(r) if r else 0.0
def mean_trust(r): return sum(float(d["trust_score"]) for d in r)/len(r) if r else 0.0
def precision_at_k(r,target): return sum(d["doc_id"]==target for d in r)/len(r) if r else 0.0
def trust_weighted_quality(r,target):
    for rank,d in enumerate(r,1):
        if d["doc_id"]==target: return float(d["trust_score"])/rank
    return 0.0
def security_utility(r,target):
    s=1-poison_exposure(r); u=relevant_coverage(r,target)
    return 2*s*u/(s+u) if s+u else 0.0
