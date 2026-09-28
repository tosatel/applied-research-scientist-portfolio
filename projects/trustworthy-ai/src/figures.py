import argparse,csv
from pathlib import Path
import matplotlib.pyplot as plt
def read(p):
    with open(p,newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--results",required=True);p.add_argument("--output-dir",required=True);a=p.parse_args()
    r=read(a.results);o=Path(a.output_dir);o.mkdir(parents=True,exist_ok=True);names=[x["system"] for x in r]
    fig,ax=plt.subplots(figsize=(8,5));ax.bar(names,[float(x["composite_trust"]) for x in r]);ax.set_ylim(0,1);ax.set_ylabel("Composite Trust Indicator");ax.set_title("Composite Trust by System");fig.tight_layout();fig.savefig(o/"composite_trust.png",dpi=180);plt.close(fig)
    dims=["reliability","robustness","transparency","privacy","fairness","governance"]
    fig,ax=plt.subplots(figsize=(9,5))
    for x in r:ax.plot(dims,[float(x[d]) for d in dims],marker="o",label=x["system"])
    ax.set_ylim(0,1);ax.set_ylabel("Normalized Score");ax.set_title("Trustworthiness Dimension Profiles");ax.tick_params(axis="x",rotation=20);ax.legend();fig.tight_layout();fig.savefig(o/"dimension_profiles.png",dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5));ax.bar(names,[float(x["minimum_score"]) for x in r]);ax.set_ylim(0,1);ax.set_ylabel("Weakest Dimension Score");ax.set_title("Weakest-Link View");fig.tight_layout();fig.savefig(o/"minimum_dimension_scores.png",dpi=180);plt.close(fig)
