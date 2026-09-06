import argparse, csv
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path,newline="",encoding="utf-8") as f: return list(csv.DictReader(f))

def avg_by(rows,key,metric):
    d=defaultdict(list)
    for r in rows:
        if r.get(metric,"")!="": d[r[key]].append(float(r[metric]))
    return {k:sum(v)/len(v) for k,v in d.items()}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--results",required=True); ap.add_argument("--output-dir",required=True); args=ap.parse_args()
    rows=read_csv(args.results); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    models=sorted({r["model"] for r in rows}); metrics=["token_f1","keyword_coverage","appropriate_refusal"]; x=list(range(len(models))); width=.22
    fig,ax=plt.subplots(figsize=(9,5))
    for i,metric in enumerate(metrics):
        vals=avg_by(rows,"model",metric); ax.bar([p+(i-1)*width for p in x],[vals.get(m,0) for m in models],width=width,label=metric.replace("_"," ").title())
    ax.set_xticks(x); ax.set_xticklabels(models); ax.set_ylim(0,1.05); ax.set_ylabel("Score"); ax.set_title("Model Metric Comparison"); ax.legend(); fig.tight_layout(); fig.savefig(out/"model_metric_comparison.png",dpi=180); plt.close(fig)
    conditions=sorted({r["condition"] for r in rows}); vals=avg_by(rows,"condition","token_f1")
    fig,ax=plt.subplots(figsize=(8,5)); ax.bar(conditions,[vals.get(c,0) for c in conditions]); ax.set_ylim(0,1.05); ax.set_ylabel("Average Token F1"); ax.set_title("Performance by Prompt Condition"); ax.tick_params(axis="x",rotation=20); fig.tight_layout(); fig.savefig(out/"condition_performance.png",dpi=180); plt.close(fig)
    latency=avg_by(rows,"model","latency_ms"); quality=avg_by(rows,"model","token_f1")
    fig,ax=plt.subplots(figsize=(7,5))
    for m in models:
        ax.scatter([latency[m]],[quality[m]],s=70); ax.annotate(m,(latency[m],quality[m]),xytext=(5,5),textcoords="offset points")
    ax.set_xlabel("Average Latency (ms)"); ax.set_ylabel("Average Token F1"); ax.set_title("Latency–Quality Trade-off"); fig.tight_layout(); fig.savefig(out/"latency_quality_tradeoff.png",dpi=180); plt.close(fig)
    print(f"Figures written to {out}")
if __name__=="__main__": main()
