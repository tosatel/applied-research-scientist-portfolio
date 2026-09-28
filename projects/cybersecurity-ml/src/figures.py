import argparse, os, pandas as pd, matplotlib.pyplot as plt

def main(results, importance, output_dir):
    os.makedirs(output_dir,exist_ok=True); r=pd.read_csv(results); imp=pd.read_csv(importance)
    ax=r.set_index('model')[['precision','recall','f1']].plot(kind='bar'); ax.set_ylim(0,1); ax.set_ylabel('Score'); plt.tight_layout(); plt.savefig(os.path.join(output_dir,'model_metric_comparison.png'),dpi=160); plt.close()
    ax=r.set_index('model')['false_positive_rate'].plot(kind='bar'); ax.set_ylim(0,max(.05,r.false_positive_rate.max()*1.2)); ax.set_ylabel('False-positive rate'); plt.tight_layout(); plt.savefig(os.path.join(output_dir,'false_positive_rate.png'),dpi=160); plt.close()
    rf=imp[imp.model=='Random Forest'].sort_values('importance'); ax=rf.set_index('feature')['importance'].plot(kind='barh'); ax.set_xlabel('Feature importance'); plt.tight_layout(); plt.savefig(os.path.join(output_dir,'feature_importance.png'),dpi=160); plt.close()
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--results',required=True); p.add_argument('--importance',required=True); p.add_argument('--output-dir',required=True); a=p.parse_args(); main(a.results,a.importance,a.output_dir)
