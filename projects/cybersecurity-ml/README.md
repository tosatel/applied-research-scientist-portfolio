# Explainable Cybersecurity Anomaly Detection Lab

**Focus:** Defensive ML, anomaly detection, explainability, robustness, operational security analytics

## Research Question
How effectively can machine-learning models detect anomalous cybersecurity events while maintaining interpretability, robustness, and operationally useful false-positive rates?

## Study Design
This project uses a benign synthetic security-event dataset representing routine and anomalous authentication/network telemetry. It compares supervised and unsupervised detection approaches under a reproducible train/test protocol.

Models:
- Logistic Regression (interpretable supervised baseline)
- Random Forest (nonlinear supervised baseline)
- Isolation Forest (unsupervised anomaly detector)

Metrics:
- Precision, Recall, F1
- PR-AUC and ROC-AUC where score outputs are available
- False-positive rate
- Detection rate
- Alerts per 1,000 events

Explainability is provided through standardized logistic-regression coefficients and random-forest feature importance. The study is defensive and contains no exploitation, malware, credential theft, or evasion procedures.

## Reproduce
```bash
pip install -r requirements.txt
python src/experiment.py --data data/security_events.csv --output results/sample_results.csv
python src/figures.py --results results/sample_results.csv --importance results/feature_importance.csv --output-dir results/figures
pytest -q
```

## Limitations
The included dataset is synthetic and intended to validate research methodology, code, and reporting. Results must not be interpreted as production detection performance. Future work should validate on appropriately licensed real-world defensive datasets and examine temporal drift, calibration, subgroup behavior, and analyst workload.
