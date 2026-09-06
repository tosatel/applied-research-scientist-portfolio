import re
from collections import Counter

STOPWORDS = {"a","an","the","is","are","was","were","be","been","being","to","of","and","or","in","on","for","with","that","this","it","as","at","by","from","so","can","could","would","should","may","might","there","which","what","when","where","who","how"}

def normalize_text(text):
    text = (text or "").lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def tokenize(text, remove_stopwords=False):
    tokens = normalize_text(text).split()
    if remove_stopwords:
        tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return tokens

def exact_match(reference, prediction):
    return float(normalize_text(reference) == normalize_text(prediction))

def token_f1(reference, prediction):
    ref, pred = tokenize(reference), tokenize(prediction)
    if not ref or not pred:
        return float(ref == pred)
    overlap = sum((Counter(ref) & Counter(pred)).values())
    if overlap == 0:
        return 0.0
    precision, recall = overlap/len(pred), overlap/len(ref)
    return 2 * precision * recall / (precision + recall)

def keyword_coverage(keywords, prediction):
    expected = [normalize_text(k) for k in (keywords or "").split("|") if k.strip()]
    if not expected:
        return 1.0
    pred = normalize_text(prediction)
    return sum(k in pred for k in expected) / len(expected)

def groundedness(context, prediction):
    pred_tokens = tokenize(prediction, remove_stopwords=True)
    if not pred_tokens:
        return 0.0
    ctx = set(tokenize(context, remove_stopwords=True))
    return sum(t in ctx for t in pred_tokens) / len(pred_tokens)

def hallucination_proxy(context, prediction):
    return 1.0 - groundedness(context, prediction)

REFUSAL_PATTERNS = ("not enough information","cannot determine","can't determine","cannot be determined","not provided","does not provide","insufficient information","not specified","does not name")

def appropriate_refusal(answerable_from_context, prediction):
    pred = normalize_text(prediction)
    refusal = any(normalize_text(p) in pred for p in REFUSAL_PATTERNS)
    return float(not refusal) if answerable_from_context else float(refusal)
