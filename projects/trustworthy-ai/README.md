# Trustworthy AI Evaluation Framework
**Applied Research Scientist Portfolio — Project 3**

## Research Question
> How can AI trustworthiness be evaluated across multiple technical and governance dimensions without allowing strength in one area to conceal a critical weakness in another?

## Dimensions
Reliability, Robustness, Transparency, Privacy, Fairness, Governance.

## Design
The framework preserves dimension-level evidence and computes an explicitly weighted comparative indicator:

`CompositeTrust = sum(weight_i * score_i) / sum(weight_i)`

A separate critical-risk gate prevents the aggregate score from masking a dimension below its required threshold.

## Hypotheses
- Task performance alone is insufficient for deployment-readiness assessment.
- Multi-dimensional evaluation reveals risks hidden by a single metric.
- Critical gates prevent strong averages from masking unacceptable weaknesses.
- Explicit weights and thresholds improve auditability.

## Outputs
Dimension scores, composite indicator, weakest dimension, gate failures, readiness category, and research figures.

## Run
```bash
pip install -r requirements.txt
python src/evaluate.py --systems data/systems.csv --thresholds data/dimension_thresholds.csv --output results/sample_results.csv
python src/figures.py --results results/sample_results.csv --output-dir results/figures
pytest -q
```

## Interpretation
The composite indicator is a comparison aid, not a declaration that a system is intrinsically trustworthy. Dimension evidence and critical failures remain primary.

## Limitations
Starter data are synthetic and normalized. Real assessments require domain-specific evidence, uncertainty analysis, stakeholder-defined thresholds, subgroup analysis, monitoring, and governance review.

## Roadmap
- [x] Multi-dimensional scoring
- [x] Explicit weights and thresholds
- [x] Critical-risk gates
- [x] Deployment-readiness logic
- [x] Reproducible pipeline, notebook, tests, figures
- [ ] Connect LLM Evaluation Lab evidence
- [ ] Connect RAG Security Lab evidence
- [ ] Add confidence intervals and measurement uncertainty
- [ ] Add stakeholder weighting profiles
- [ ] Add governance evidence checklist
- [ ] Validate on real AI systems

## Author
**Tosan Atele-Williams, Ph.D.**  
Computer Science | Applied AI/ML | Trustworthy AI | Cybersecurity | Computational Trust
