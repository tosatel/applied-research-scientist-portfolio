# Trust-Aware RAG Security Lab

**Applied Research Scientist Portfolio — Project 2**

## Abstract
RAG systems improve LLM responses with retrieved evidence, but retrieval also creates a security boundary: relevant content may be misleading, poisoned, or poorly sourced. This reproducible research prototype evaluates whether provenance- and trust-aware retrieval can reduce exposure to synthetic poisoned documents while preserving retrieval utility.

## Primary Research Question
> How vulnerable are RAG systems to malicious, low-trust, or poisoned retrieved content, and can provenance- and trust-aware retrieval reduce attack exposure while preserving useful evidence?

## Hypotheses
- **H1:** Trust-aware retrieval reduces poisoned-document exposure relative to relevance-only retrieval.
- **H2:** Lower poisoned-context exposure reduces downstream attack opportunity.
- **H3:** Strict trust filtering can improve security at a cost to retrieval utility.
- **H4:** Joint relevance-and-trust ranking can improve the security–utility trade-off.

## Conditions
1. `clean_rag` — trusted corpus only.
2. `poisoned_rag` — relevance-only retrieval over mixed-trust content.
3. `naive_defense` — minimum trust threshold before relevance ranking.
4. `trust_aware_rag` — combined relevance and trust ranking.

## Trust Model
`Trust(d) = wp*Provenance + wa*Authority + wr*Reliability + wc*Consistency`

Trust-aware ranking:
`Score(d,q) = alpha*Relevance(d,q) + (1-alpha)*Trust(d)`

The weights are experimental parameters, not a claim that trust can be universally reduced to one formula.

## Metrics
- Precision@k
- Relevant Evidence Coverage
- Poisoned Context Exposure
- Poisoned Top-1 Rate
- Trusted Context Ratio
- Mean Retrieved Trust
- Trust-Weighted Retrieval Quality
- Security–Utility Score

## Structure
```text
rag-security/
├── README.md
├── research_protocol.md
├── threat_model.md
├── requirements.txt
├── data/
├── src/
├── notebooks/
├── results/
└── tests/
```

## Run
```bash
pip install -r requirements.txt
python src/experiment.py --documents data/documents.csv --queries data/queries.csv --output results/sample_results.csv
python src/figures.py --summary results/sample_results_summary.csv --output-dir results/figures
pytest -q
```

## Interpretation
The core research problem is not merely whether retrieval finds semantically relevant text. It is whether a RAG system can distinguish **relevant evidence from relevant-but-untrustworthy evidence**.

## Safety and Ethics
The corpus uses benign synthetic poisoning examples for defensive research. It contains no malware, credential theft, destructive instructions, or operational exploitation guidance.

## Limitations
The starter corpus is intentionally small; lexical retrieval is used for transparency; trust attributes are controlled experimental variables; and retrieval exposure is only a proxy for downstream LLM attack success. Later work should use embeddings, larger corpora, repeated trials, real LLMs, confidence intervals, and human evaluation.

## Roadmap
- [x] Synthetic mixed-trust corpus
- [x] Threat model
- [x] Trust scoring
- [x] Relevance baseline
- [x] Threshold defense
- [x] Trust-aware ranking
- [x] Security/utility metrics
- [x] Notebook, tests, and figures
- [ ] Embedding/vector retrieval
- [ ] Larger poisoning benchmark
- [ ] Real multi-LLM downstream evaluation
- [ ] Attack-success, groundedness, and answer-quality evaluation
- [ ] Provenance graph and trust calibration

## Author
**Tosan Atele-Williams, Ph.D.**  
Computer Science | Applied AI/ML | Trustworthy AI | Cybersecurity | Computational Trust
