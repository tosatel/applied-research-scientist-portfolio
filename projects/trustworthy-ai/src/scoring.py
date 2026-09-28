DIMENSIONS=["reliability","robustness","transparency","privacy","fairness","governance"]
def validate(s):
    for d in DIMENSIONS:
        if not 0<=float(s[d])<=1: raise ValueError(f"{d} outside [0,1]")
def composite(s,w):
    validate(s); total=sum(w[d] for d in DIMENSIONS)
    if total<=0: raise ValueError("weights must sum positive")
    return sum(float(s[d])*w[d] for d in DIMENSIONS)/total
def weakest(s):
    validate(s); d=min(DIMENSIONS,key=lambda x:float(s[x])); return d,float(s[d])
