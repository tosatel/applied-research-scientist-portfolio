# Research Protocol

## Primary question
How effectively can ML-based anomaly detection identify suspicious security events while preserving interpretability and operationally useful false-positive behavior?

## Hypotheses
1. Supervised models will outperform an unsupervised anomaly detector when representative labels are available.
2. A nonlinear model may improve detection but reduce direct interpretability relative to logistic regression.
3. Accuracy alone will obscure operational differences visible in precision, recall, false-positive rate, and alert volume.
4. Feature-level explanations can reveal whether models rely on security-relevant signals or undesirable shortcuts.

## Experimental design
- Stratified 70/30 train/test split with fixed random seed.
- Numeric telemetry features only; event IDs are excluded from modeling.
- Logistic Regression and Random Forest train on labels.
- Isolation Forest trains on normal training events only.
- Metrics are computed on a held-out test set.
- Feature importance is exported for supervised models.

## Threats to validity
Synthetic data simplifies real networks, attacker adaptation, class imbalance, concept drift, logging gaps, and analyst feedback. The experiment demonstrates methodology rather than production efficacy.
