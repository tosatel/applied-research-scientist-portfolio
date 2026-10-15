from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, brier_score_loss, log_loss

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ['language_consistency', 'claim_specificity']
SOURCE = ['source_history', 'provenance_quality']
ALL = CONTENT + SOURCE + ['independent_corroboration', 'context_alignment']


def generate(n=1200, seed=42):
    rng = np.random.default_rng(seed)
    latent = rng.normal(size=n)
    data = {}
    for name, loading in zip(ALL, [0.6, 0.45, 0.65, 0.7, 0.8, 0.75]):
        data[name] = np.clip(1 / (1 + np.exp(-(loading * latent + rng.normal(0, 1, n)))), 0, 1)
    frame = pd.DataFrame(data)
    logits = (0.5 * frame[CONTENT].mean(axis=1) + 0.7 * frame[SOURCE].mean(axis=1)
              + 1.2 * frame['independent_corroboration'] + 1.0 * frame['context_alignment'] - 1.7) * 3
    probs = 1 / (1 + np.exp(-logits))
    frame['label'] = rng.binomial(1, probs)
    return frame


def evaluate(frame):
    train, test = train_test_split(frame, test_size=0.25, random_state=42, stratify=frame['label'])
    rows, coefficients = [], []
    for name, columns in [('Content-only', CONTENT), ('Source-only', SOURCE), ('Multidimensional', ALL)]:
        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
        model.fit(train[columns], train['label'])
        prob = model.predict_proba(test[columns])[:, 1]
        pred = (prob >= 0.5).astype(int)
        rows.append({'model': name, 'precision': precision_score(test['label'], pred, zero_division=0),
                     'recall': recall_score(test['label'], pred, zero_division=0),
                     'f1': f1_score(test['label'], pred, zero_division=0),
                     'roc_auc': roc_auc_score(test['label'], prob),
                     'brier_score': brier_score_loss(test['label'], prob),
                     'log_loss': log_loss(test['label'], prob)})
        coefficients.extend({'model': name, 'feature': feature, 'standardized_coefficient': float(value)}
                            for feature, value in zip(columns, model[-1].coef_[0]))
    return pd.DataFrame(rows), pd.DataFrame(coefficients)


def main():
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'results').mkdir(exist_ok=True)
    frame = generate()
    frame.to_csv(ROOT / 'data' / 'synthetic_information_signals.csv', index=False)
    metrics, coefficients = evaluate(frame)
    metrics.to_csv(ROOT / 'results' / 'sample_results.csv', index=False)
    coefficients.to_csv(ROOT / 'results' / 'coefficients.csv', index=False)
    print(metrics.round(3).to_string(index=False))

if __name__ == '__main__':
    main()
