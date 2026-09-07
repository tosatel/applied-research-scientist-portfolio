Applied Research Portfolio — AI, ML & Cybersecurity

Tosan Atele-Williams, Ph.D.
Computer Science | Applied AI/ML | Trustworthy AI | Cybersecurity | Computational Trust

This repository showcases applied research and research-engineering projects at the intersection of Artificial Intelligence, Machine Learning, Large Language Models, Trustworthy AI, Computational Trust, and Cybersecurity.

My goal is to investigate not only whether AI systems perform well, but whether they are reliable, grounded, secure, trustworthy, explainable, and suitable for real-world deployment.

Research Profile

I am a computer scientist and applied researcher working on trustworthy, secure, and useful AI systems.

My research interests include:

Large Language Model evaluation
Prompt engineering and prompt robustness
Trustworthy AI
Computational trust
AI governance
Retrieval-Augmented Generation (RAG)
LLM safety and robustness
AI and cybersecurity
Privacy and security
Human-centred and socio-technical AI systems
Translation of research into deployable AI prototypes

This portfolio is designed to test capabilities relevant to Applied Research, AI/ML, Trustworthy AI, Generative AI, and AI Security.

Featured Research Projects

1. LLM Evaluation Lab

Status: Active / Initial reproducible framework completed

A reproducible experimental framework for evaluating Large Language Models beyond conventional accuracy metrics.

Primary Research Question

How reliably can large language models answer questions when evaluated across correctness, groundedness, hallucination risk, robustness, and operational efficiency rather than a single accuracy score?

Research Objectives

The project investigates:

whether relevant context improves groundedness;
whether context reduces hallucination risk;
how sensitive LLMs are to semantically equivalent prompt variations;
whether models appropriately refuse to answer when evidence is insufficient;
trade-offs between response quality, latency, token usage, and cost; and
why accuracy alone is insufficient for evaluating deployment readiness.
Experimental Conditions

Three initial experimental conditions are implemented:

Baseline — question without supporting context
Context-Augmented — question with relevant supporting evidence
Prompt Variant — semantically equivalent reformulation of the original question
Evaluation Metrics

The evaluation pipeline currently measures:

Exact Match
Token F1
Keyword Coverage
Groundedness Proxy
Hallucination Proxy
Appropriate Refusal
Response Latency
Input Token Usage
Output Token Usage
Estimated Cost
Research Artifacts

The project includes:

research protocol;
benchmark dataset;
sample model outputs;
Python evaluation pipeline;
reusable evaluation metrics;
Jupyter notebook;
automated tests;
results templates;
model-comparison figures;
condition-performance analysis; and
latency-versus-quality analysis.
Reproducibility

The starter experiment uses transparent sample data and simulated model outputs, allowing the entire evaluation pipeline to be reproduced without requiring proprietary API credentials.

The next research phase will replace the outputs with controlled experiments involving real LLMs and repeated trials.

Project: projects/llm-evaluation-lab/

2. Trust-Aware RAG Security Lab

Status: Active / Initial reproducible framework completed

A reproducible research framework for studying security, provenance, and trust risks in Retrieval-Augmented Generation systems.

Primary Research Question

How vulnerable are Retrieval-Augmented Generation systems to malicious, low-trust, or poisoned retrieved content, and can provenance- and trust-aware retrieval reduce attack exposure while preserving useful evidence?

Research Objectives

The project investigates:

how poisoned or misleading documents can enter the retrieval context;
whether relevance-only retrieval can rank untrustworthy evidence highly;
whether source provenance and computational trust can improve retrieval security;
how minimum-trust filtering affects retrieval utility;
whether combined relevance-and-trust ranking reduces poisoned-context exposure; and
the trade-off between retrieval security and useful evidence coverage.
Experimental Conditions

Four initial experimental conditions are implemented:

Clean RAG — retrieval from trusted documents only
Poisoned RAG — relevance-only retrieval over trusted and poisoned documents
Naive Defence — minimum-trust filtering before relevance ranking
Trust-Aware RAG — joint relevance and trust-based ranking
Trust Model

The project models document trust using:

[
Trust(d)=w_pP(d)+w_aA(d)+w_rR(d)+w_cC(d)
]

where trust can incorporate:

provenance;
authority;
historical reliability; and
consistency.

Trust-aware retrieval combines trust and relevance:

[
Score(d,q)=\alpha Relevance(d,q)+(1-\alpha)Trust(d)
]

Evaluation Metrics

The evaluation pipeline currently measures:

Precision@k
Relevant Evidence Coverage
Poisoned Context Exposure
Poisoned Top-1 Rate
Trusted Context Ratio
Mean Retrieved Trust
Trust-Weighted Retrieval Quality
Security–Utility Score
Research Artifacts

The project includes:

formal threat model;
research protocol;
synthetic mixed-trust corpus;
labeled attack scenarios;
document trust scoring;
relevance-only retrieval baseline;
minimum-trust defense;
trust-aware retrieval strategy;
Python experiment pipeline;
Jupyter notebook;
automated tests;
result templates; and
security/utility comparison figures.
Reproducibility

The starter experiment uses benign synthetic attack scenarios and transparent lexical retrieval so that the security behavior can be independently inspected without requiring proprietary APIs.

Future phases will extend the work to embedding-based retrieval, larger corpora, repeated trials, real LLMs, downstream attack-success evaluation, groundedness, and answer-quality analysis.

Project: projects/rag-security/

3. Trustworthy AI

Status: Planned

Research into practical methods for designing and evaluating AI systems that are:

reliable;
transparent;
accountable;
privacy-aware;
robust;
explainable; and
aligned with organizational governance requirements.

The project will connect technical evaluation with AI governance, risk management, computational trust, and socio-technical considerations.

4. Cybersecurity + Machine Learning

Status: Planned

Applied machine-learning research for cybersecurity problems including:

anomaly detection;
phishing detection;
malicious-behaviour detection;
security analytics;
threat prioritization;
AI-assisted cyber defence; and
adversarial machine learning.

The research will examine both predictive performance and the operational limitations, adversarial risks, explainability, and trustworthiness of ML-based security systems.

Research Themes
Research
│
├── LLM Evaluation
│   ├── Groundedness
│   ├── Hallucination
│   ├── Robustness
│   └── Model Comparison
│
├── Prompt Engineering
│   ├── Prompt Sensitivity
│   ├── Prompt Robustness
│   └── Evaluation
│
├── Trustworthy AI
│   ├── Reliability
│   ├── Transparency
│   ├── Accountability
│   └── Computational Trust
│
├── AI Governance
│   ├── Risk
│   ├── Privacy
│   ├── Responsible AI
│   └── Deployment Governance
│
├── RAG
│   ├── Retrieval Quality
│   ├── Provenance
│   ├── Groundedness
│   └── Trust-Aware Retrieval
│
└── AI + Cybersecurity
    ├── Prompt Injection
    ├── RAG Security
    ├── Adversarial ML
    └── Security Analytics
Repository Structure
applied-research-scientist-portfolio/
│
├── research/
│   ├── research-agenda.md
│   ├── publications.md
│   └── experiment-template.md
│
├── projects/
│   ├── llm-evaluation-lab/
│   ├── rag-security/
│   ├── trustworthy-ai/
│   └── cybersecurity-ml/
│
├── notebooks/
├── src/
├── tests/
├── data/
├── docs/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── LICENSE
└── README.md

Each major research project is designed as an independent experimental study with its own research question, methodology, data, code, evaluation, results, and documentation.

Research Methodology

Projects in this repository generally follow the research lifecycle:

Research Question → Hypothesis → Experimental Design → Data → Implementation → Evaluation → Statistical Analysis → Error Analysis → Interpretation → Reproducibility

Each project should document:

Problem statement
Research question
Hypotheses
Dataset
Experimental design
Baselines
Evaluation metrics
Results
Statistical analysis
Error analysis
Threats to validity
Security and privacy considerations
Ethical considerations
Reproduction instructions
Deployment implications
Methods & Technical Skills
AI / Machine Learning

Python • NumPy • Pandas • scikit-learn • PyTorch • Hugging Face • NLP • Generative AI

Large Language Models

LLM Evaluation • Prompt Engineering • RAG • Groundedness Evaluation • Hallucination Analysis • Model Comparison • Robustness Testing

Trustworthy AI

Computational Trust • Responsible AI • AI Governance • Privacy • Reliability • Transparency • Risk Analysis

Cybersecurity

AI Security • Security Analytics • Adversarial ML • Prompt Injection • RAG Security • Threat Detection

Research

Experimental Design • Benchmark Development • Statistical Analysis • Reproducible Research • Error Analysis • Technical Writing

Reproducibility Principles

Research projects should be:

Transparent — assumptions and limitations are explicitly documented.

Reproducible — experiments include code, data schemas, configurations, and execution instructions.

Measurable — conclusions are supported by defined evaluation metrics.

Auditable — experimental decisions and model configurations are documented.

Responsible — security, privacy, bias, ethical, and governance considerations are included where appropriate.

Getting Started

Clone the repository:

git clone https://github.com/tosatel/applied-research-scientist-portfolio.git
cd applied-research-scientist-portfolio

Create a Python environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest

Individual projects may contain additional dependencies and execution instructions.

For example:

cd projects/llm-evaluation-lab
pip install -r requirements.txt
pytest -q
Research Roadmap
LLM Evaluation

Define multidimensional LLM evaluation framework

Create benchmark dataset

Implement evaluation metrics

Add hallucination and groundedness evaluation

Add prompt-variation experiment

Add refusal-behaviour evaluation

Build reproducible Python evaluation pipeline

Add Jupyter analysis notebook

Add automated tests

Generate initial research figures

Evaluate real LLMs

Add repeated trials and confidence intervals

Add human evaluation

Add semantic and factuality metrics

RAG & AI Security

Build trust-aware RAG prototype

Add prompt-injection evaluation suite

Add retrieval-poisoning experiments

Add source-provenance evaluation

Investigate trust-aware retrieval ranking

Trustworthy AI

Develop AI trust evaluation framework

Add responsible-AI model cards

Connect technical metrics with governance controls

Develop deployment-readiness scorecard

Cybersecurity + ML

Add cybersecurity anomaly-detection study

Add phishing-detection experiment

Evaluate adversarial robustness

Investigate explainability for security models

Research Dissemination

Add technical reports

Add research papers/preprints

Add conference posters

Add experiment reproducibility reports

Add CI for automated research tests

Current Research Direction

The broader research program asks:

How can we design, evaluate, and govern AI systems so that humans and organizations can make justified decisions about when those systems should be trusted?

The portfolio approaches this problem through LLM evaluation, computational trust, trustworthy AI, RAG, AI governance, and cybersecurity.

Contact

Tosan Atele-Williams, Ph.D.

Computer Science | Applied AI/ML | Trustworthy AI | Cybersecurity | Computational Trust
