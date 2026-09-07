DEFAULT_WEIGHTS={"provenance":.25,"authority":.25,"reliability":.25,"consistency":.25}
def trust_score(d,weights=None):
    w=weights or DEFAULT_WEIGHTS
    total=sum(w.values())
    if total<=0: raise ValueError("weights must sum positive")
    return sum(float(d[k])*w[k] for k in w)/total
