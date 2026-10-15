# Information Trust & Misinformation Detection Benchmark

**Project 5 | Computational Trust · NLP/ML · Responsible AI**

## Research question
Can multidimensional information-trust signals improve classification and calibration compared with content-only and source-only baselines?

## Scope
This is a **synthetic methodological benchmark**, not a fact-checker. Labels are simulated and are not verified claims. Source attributes are illustrative signals, not judgments about real publishers. No actual misinformation claims are distributed.

## Baselines
1. Content-only: linguistic and consistency proxies.
2. Source-only: provenance and source-history proxies.
3. Multidimensional: content, provenance, corroboration, and contextual signals.

## Reproduce
```bash
python -m pip install -r requirements.txt
python src/experiment.py
python src/figures.py
python -m pytest -q
```
Outputs are written to `results/`. All models use a stratified held-out test split. Scores are illustrative and cannot establish real-world generalization.

## Metrics
Precision, recall, F1, ROC-AUC, Brier score, and log loss. Coefficients are reported for interpretability, but correlated inputs can make individual coefficient interpretation unstable.

## Limitations and next steps
Synthetic labels are generated from the same underlying signal families as the features, which may favor the combined model. Evaluate on independently annotated, licensed datasets with temporal/source holdouts; add annotator disagreement, subgroup and distribution-shift analysis, confidence intervals, and qualitative error review before making real-world claims.
