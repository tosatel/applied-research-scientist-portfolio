# Threat Model
## System
A RAG pipeline retrieves external evidence for downstream language-model generation.

## Assets
Evidence integrity, provenance, answer reliability, user trust, and protected information.

## Adversary Goal
Cause low-trust or misleading evidence to be retrieved and potentially influence generation.

## Safe Synthetic Attack Classes
- Corpus poisoning
- Relevance mimicry
- Low-provenance evidence

## Assumptions
Some retrievable content can be influenced; trusted and untrusted sources coexist; trust metadata is available.

## Defenses
Provenance scoring, authority/reliability/consistency signals, minimum-trust filtering, and joint relevance/trust ranking.

## Residual Risk
Trust metadata can be incomplete or manipulated. Trust-aware retrieval reduces exposure; it does not prove retrieved content is safe.
