import argparse,csv
from pathlib import Path
from scoring import DIMENSIONS,composite,weakest
from gates import failures,readiness
def read(p):
    with open(p,newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def cfg(rows):
    return ({r["dimension"]:float(r["critical_threshold"]) for r in rows},{r["dimension"]:float(r["weight"]) for r in rows})
def run(systems,t,w):
    out=[]
    for s in systems:
        c=composite(s,w); d,m=weakest(s); f=failures(s,t)
        out.append({"system":s["system"],**{x:float(s[x]) for x in DIMENSIONS},"composite_trust":round(c,4),"minimum_dimension":d,"minimum_score":m,"gate_failures":"|".join(f),"critical_gate_pass":not bool(f),"readiness":readiness(c,f)})
    return out
def write(p,rows):
    Path(p).parent.mkdir(parents=True,exist_ok=True)
    with open(p,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--systems",required=True);p.add_argument("--thresholds",required=True);p.add_argument("--output",required=True);a=p.parse_args()
    t,w=cfg(read(a.thresholds));write(a.output,run(read(a.systems),t,w))
