import argparse,csv
from pathlib import Path
from collections import defaultdict
from defenses import retrieve
from metrics import *
CONDS=["clean_rag","poisoned_rag","naive_defense","trust_aware_rag"]
def read(p):
    with open(p,newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def write(p,rows):
    with open(p,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def run(docs,queries):
    rows=[]
    for q in queries:
        for c in CONDS:
            r=retrieve(q["query"],docs,c)
            rows.append({"query_id":q["query_id"],"condition":c,"retrieved_doc_ids":"|".join(d["doc_id"] for d in r),
            "precision_at_k":round(precision_at_k(r,q["relevant_doc_id"]),4),"relevant_evidence_coverage":relevant_coverage(r,q["relevant_doc_id"]),
            "poisoned_context_exposure":round(poison_exposure(r),4),"poisoned_top1":poison_top1(r),"trusted_context_ratio":round(trusted_ratio(r),4),
            "mean_retrieved_trust":round(mean_trust(r),4),"trust_weighted_retrieval_quality":round(trust_weighted_quality(r,q["relevant_doc_id"]),4),
            "security_utility_score":round(security_utility(r,q["relevant_doc_id"]),4)})
    return rows
def summary(rows):
    ms=["precision_at_k","relevant_evidence_coverage","poisoned_context_exposure","poisoned_top1","trusted_context_ratio","mean_retrieved_trust","trust_weighted_retrieval_quality","security_utility_score"]
    g=defaultdict(list)
    for r in rows:g[r["condition"]].append(r)
    return [{"condition":c,"n_queries":len(rs),**{m:round(sum(float(x[m]) for x in rs)/len(rs),4) for m in ms}} for c,rs in g.items()]
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--documents",required=True);a.add_argument("--queries",required=True);a.add_argument("--output",required=True);x=a.parse_args()
    rows=run(read(x.documents),read(x.queries));write(x.output,rows);write(str(Path(x.output).with_name(Path(x.output).stem+"_summary.csv")),summary(rows))
