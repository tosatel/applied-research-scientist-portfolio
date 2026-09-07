import re
from trust_scoring import trust_score
STOP={"a","an","the","is","are","to","of","and","or","in","on","for","with","what","which","why","does"}
def tokens(s): return {x for x in re.findall(r"[a-z0-9]+",(s or "").lower()) if x not in STOP and len(x)>1}
def relevance_score(q,t):
    a,b=tokens(q),tokens(t)
    return len(a&b)/len(a|b) if a and b else 0.0
def rank_documents(q,docs,strategy="relevance",k=3,alpha=.65,threshold=.55):
    out=[]
    for d in docs:
        r=relevance_score(q,d["text"]); t=trust_score(d)
        if strategy=="threshold" and t<threshold: continue
        score=alpha*r+(1-alpha)*t if strategy=="trust_aware" else r
        out.append({**d,"relevance_score":r,"trust_score":t,"ranking_score":score})
    return sorted(out,key=lambda x:(x["ranking_score"],x["trust_score"]),reverse=True)[:k]
