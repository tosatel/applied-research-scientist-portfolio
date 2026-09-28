# Evaluation Framework
## Dimensions
- Reliability: correctness and consistency in intended conditions.
- Robustness: stability under perturbation and relevant adverse conditions.
- Transparency: documentation, explanations, provenance, and limitations.
- Privacy: protection and minimization of sensitive information.
- Fairness: examination of performance and impacts across relevant groups.
- Governance: ownership, monitoring, escalation, auditability, and controls.

## Readiness Rules
- `ready_for_controlled_pilot`: composite >= 0.80 and all gates pass.
- `conditional_review`: composite >= 0.65 and all gates pass.
- `remediation_required`: any gate fails or composite < 0.65.

These are experimental research categories, not regulatory determinations.
