from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
def main():
    df = pd.read_csv(ROOT / 'results' / 'sample_results.csv')
    out = ROOT / 'results' / 'figures'
    out.mkdir(parents=True, exist_ok=True)
    for metric in ['f1', 'roc_auc', 'brier_score']:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.bar(df['model'], df[metric])
        ax.set_ylabel(metric.replace('_', ' ').title())
        ax.set_title('Synthetic benchmark: ' + metric.replace('_', ' ').title())
        ax.tick_params(axis='x', rotation=12)
        fig.tight_layout()
        fig.savefig(out / f'{metric}.png', dpi=150)
        plt.close(fig)
if __name__ == '__main__':
    main()
