# Research Protocol

## Objective
Evaluate large language models using a multidimensional, reproducible framework.

## Independent Variables
- model
- prompt condition
- context availability
- prompt wording

## Dependent Variables
- exact match
- token F1
- keyword coverage
- groundedness proxy
- hallucination proxy
- appropriate refusal
- latency
- token usage
- estimated cost

## Controls
- same benchmark across models
- same system instructions where possible
- same decoding settings where possible
- logged model/provider version
- logged run date
- repeated trials for stochastic models

## Repeated Measures
For stochastic models, repeat each item multiple times and report mean, standard deviation, confidence intervals, and failure frequency.

## Human Evaluation Extension
Suggested dimensions: correctness, relevance, completeness, groundedness, clarity, fabrication risk, and deployment acceptability.

## Statistical Analysis
Depending on study size: paired comparisons, bootstrap confidence intervals, effect sizes, non-parametric tests, and multiple-comparison correction where needed.

## Reporting Principle
Do not report only one aggregate score. Always include disaggregated metrics and qualitative error analysis.
