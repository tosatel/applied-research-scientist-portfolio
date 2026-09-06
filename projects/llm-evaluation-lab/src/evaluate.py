import argparse, csv
from pathlib import Path
from collections import defaultdict
from metrics import exact_match, token_f1, keyword_coverage, groundedness, hallucination_proxy, appropriate_refusal

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    if not rows: return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def evaluate(benchmark_rows, prediction_rows):
    benchmark = {r["id"]: r for r in benchmark_rows}; out=[]
    for p in prediction_rows:
        b=benchmark[p["id"]]; answerable=b["answerable_from_context"].lower()=="true"
        use_context=p["condition"]=="context_augmented"
        g=groundedness(b["context"],p["prediction"]) if use_context else ""
        h=hallucination_proxy(b["context"],p["prediction"]) if use_context else ""
        out.append({**p,"category":b["category"],"reference_answer":b["reference_answer"],"exact_match":round(exact_match(b["reference_answer"],p["prediction"]),4),"token_f1":round(token_f1(b["reference_answer"],p["prediction"]),4),"keyword_coverage":round(keyword_coverage(b["keywords"],p["prediction"]),4),"groundedness":round(g,4) if g!="" else "","hallucination_proxy":round(h,4) if h!="" else "","appropriate_refusal":round(appropriate_refusal(answerable,p["prediction"]),4)})
    return out

def summarize(rows):
    metrics=["exact_match","token_f1","keyword_coverage","groundedness","hallucination_proxy","appropriate_refusal"]
    groups=defaultdict(list)
    for r in rows: groups[(r["model"],r["condition"])].append(r)
    summary=[]
    for (model,condition),rs in sorted(groups.items()):
        item={"model":model,"condition":condition,"n":len(rs)}
        for m in metrics:
            vals=[float(r[m]) for r in rs if r[m]!=""]
            item[m]=round(sum(vals)/len(vals),4) if vals else ""
        for m in ["latency_ms","input_tokens","output_tokens","estimated_cost_usd"]:
            vals=[float(r[m]) for r in rs]; item[f"avg_{m}"]=round(sum(vals)/len(vals),4)
        summary.append(item)
    return summary

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--benchmark",required=True); ap.add_argument("--predictions",required=True); ap.add_argument("--output",required=True); args=ap.parse_args()
    results=evaluate(read_csv(args.benchmark),read_csv(args.predictions)); write_csv(args.output,results)
    summary_path=Path(args.output).with_name(Path(args.output).stem+"_summary.csv"); write_csv(summary_path,summarize(results))
    print(f"Wrote {args.output}"); print(f"Wrote {summary_path}")
if __name__=="__main__": main()
