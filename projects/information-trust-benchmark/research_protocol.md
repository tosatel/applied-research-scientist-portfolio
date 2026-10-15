# Research protocol

**Hypothesis:** Joint content, provenance, corroboration, and context features improve held-out discrimination and probability calibration versus narrower baselines in a synthetic benchmark.

**Design:** Reproducibly generate 1,200 synthetic observations using a fixed seed. Stratified train/test split (75/25). Fit standardized logistic-regression pipelines to identical splits. No test-set tuning. Evaluate precision, recall, F1, ROC-AUC, Brier score, log loss, and inspect model coefficients.

**Validity threats:** Labels are simulated from feature families, feature correlations, source-proxy confounding, threshold dependence, artificial data balance, and lack of independent real-world annotations.

**Ethics:** Avoid automated censorship, source stigmatization, or using a model score as a definitive truth label. Human review and evidence verification are required for real applications.
