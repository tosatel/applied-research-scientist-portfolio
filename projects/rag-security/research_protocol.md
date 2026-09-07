# Research Protocol
## Objective
Measure whether explicit trust signals reduce poisoned-context exposure without unacceptable loss of relevant evidence.

## Independent Variables
Corpus condition, defense strategy, trust threshold, alpha, and retrieval depth k.

## Dependent Variables
Precision@k, relevant evidence coverage, poisoned exposure, poisoned top-1 rate, trusted-context ratio, mean retrieved trust, trust-weighted retrieval quality, and security–utility score.

## Starter Configuration
- lexical Jaccard relevance
- k = 3
- equal trust-component weights
- trust threshold = 0.55
- alpha = 0.65

## Procedure
1. Load labeled corpus and queries.
2. Calculate document trust.
3. Execute every query under all four conditions.
4. Record ranked evidence and metrics.
5. Compare query-level and aggregate results.
6. Inspect failures.
7. Extend with parameter sensitivity and statistical testing.

## Statistical Extension
Use paired comparisons, bootstrap confidence intervals, effect sizes, and sensitivity analysis over alpha, threshold, and k on a larger benchmark.
