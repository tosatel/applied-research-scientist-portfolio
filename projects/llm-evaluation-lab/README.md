# LLM Evaluation Lab

**Applied Research Scientist Portfolio Project**  
**Focus:** Large Language Model Evaluation, Trustworthy AI, RAG, Robustness, and Hallucination Analysis

## Abstract
Large language models often produce fluent responses that may still be incomplete, unsupported, inconsistent, or factually incorrect. This project provides a reproducible framework for evaluating LLMs across correctness, lexical answer quality, groundedness, hallucination risk, prompt robustness, refusal behavior, latency, token usage, and cost.

The starter version uses a transparent benchmark and simulated model outputs so the full pipeline can be run locally without API credentials. The framework is intentionally model-agnostic and can later be connected to commercial APIs or local/open-source models.

## 1. Research Question
> How reliably can large language models answer questions when evaluated across correctness, groundedness, hallucination risk, robustness, and operational efficiency rather than a single accuracy score?

### Secondary Questions
1. Does relevant supporting context improve groundedness and reduce unsupported claims?
2. How sensitive is performance to semantically equivalent prompt variations?
3. How often does a model fabricate information when context is insufficient?
4. What trade-offs emerge between quality, latency, token usage, and cost?
5. Which metrics are most useful for determining deployment readiness?

## 2. Hypotheses
**H1 — Context improves groundedness.** Responses produced with relevant context will be more grounded and contain fewer unsupported claims.

**H2 — Prompt wording affects performance.** Semantically similar prompts can produce measurably different outputs.

**H3 — Accuracy is not enough.** Models with similar correctness scores may differ significantly in groundedness, robustness, refusal behavior, latency, and cost.

## 3. Experimental Methodology

| Condition | Description |
|---|---|
| `baseline` | Question only |
| `context_augmented` | Question plus supporting context |
| `prompt_variant` | Semantically equivalent reworded prompt |

**Independent variables:** model, prompt condition, context availability, prompt wording.  
**Dependent variables:** exact match, token F1, keyword coverage, groundedness, hallucination proxy, appropriate refusal, latency, token usage, estimated cost.

## 4. Dataset Structure

### Benchmark schema
| Field | Description |
|---|---|
| `id` | Unique benchmark ID |
| `category` | Topic/domain |
| `question` | Primary evaluation prompt |
| `reference_answer` | Expected answer |
| `context` | Optional supporting evidence |
| `answerable_from_context` | Whether the context is sufficient |
| `prompt_variant` | Alternative wording |
| `keywords` | Expected concepts |

### Model-output schema
| Field | Description |
|---|---|
| `id` | Benchmark ID |
| `condition` | Experimental condition |
| `model` | Model identifier |
| `prediction` | Model output |
| `latency_ms` | Response latency |
| `input_tokens` | Input token count |
| `output_tokens` | Output token count |
| `estimated_cost_usd` | Optional estimated cost |

## 5. Metrics
- **Exact Match** — normalized string equality.
- **Token F1** — lexical precision/recall overlap.
- **Keyword Coverage** — fraction of expected concepts present.
- **Groundedness Proxy** — fraction of substantive answer tokens supported by supplied context.
- **Hallucination Proxy** — `1 - groundedness` for context-augmented responses.
- **Appropriate Refusal** — whether insufficient context triggers a proper refusal.
- **Operational Metrics** — latency, token usage, and estimated cost.

> These are transparent research proxies, not perfect measures of factuality or trustworthiness. A mature study should add human evaluation and stronger semantic/factuality metrics.

## 6. Project Structure
```text
llm-evaluation-lab/
├── README.md
├── research_protocol.md
├── requirements.txt
├── data/
│   ├── benchmark.csv
│   └── sample_model_outputs.csv
├── src/
│   ├── metrics.py
│   ├── evaluate.py
│   └── figures.py
├── notebooks/
│   └── 01_llm_evaluation_lab.ipynb
├── results/
│   ├── results_template.csv
│   ├── summary_template.md
│   └── figures/
└── tests/
    └── test_metrics.py
```

## 7. Running the Project
```bash
pip install -r requirements.txt
python src/evaluate.py --benchmark data/benchmark.csv --predictions data/sample_model_outputs.csv --output results/sample_results.csv
python src/figures.py --results results/sample_results.csv --output-dir results/figures
pytest -q
```

## 8. Analysis Plan
1. Compute item-level metrics.
2. Aggregate by model and condition.
3. Compare baseline vs. context-augmented responses.
4. Compare original vs. prompt-variant responses.
5. Inspect hallucination/refusal failures.
6. Examine latency/cost trade-offs.
7. Conduct qualitative error analysis.
8. Document threats to validity.
9. Translate findings into deployment recommendations.

## 9. Threats to Validity
- **Construct validity:** automated metrics approximate, but do not fully capture, human judgments.
- **Internal validity:** model versions, prompt wording, decoding settings, and sampling affect outcomes.
- **External validity:** a small benchmark cannot establish general performance across all domains.
- **Reproducibility:** hosted models may change over time.

## 10. Ethics, Security, and Privacy
- Do not commit confidential or personal data.
- Do not commit API keys.
- Document provider/model versions.
- Treat automated evaluators as fallible.
- Report limitations explicitly.
- Evaluate prompt injection and data leakage separately.

## 11. Extension Roadmap
- [x] benchmark schema
- [x] transparent metrics
- [x] sample model outputs
- [x] reproducible analysis
- [x] figure generation
- [x] notebook
- [x] tests
- [ ] connect 3–5 current LLMs
- [ ] repeated trials and confidence intervals
- [ ] human evaluation rubric
- [ ] calibrated LLM-as-judge
- [ ] prompt injection and RAG security benchmark

## Author
**Tosan Atele-Williams, Ph.D.**  
Computer Science | Applied AI/ML | Trustworthy AI | Computational Trust | Cybersecurity
