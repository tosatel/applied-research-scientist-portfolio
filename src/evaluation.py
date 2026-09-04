"""Small reusable evaluation utilities for portfolio experiments."""

from typing import Iterable


def accuracy(y_true: Iterable, y_pred: Iterable) -> float:
    """Return simple classification accuracy."""
    y_true = list(y_true)
    y_pred = list(y_pred)
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have equal length")
    if not y_true:
        raise ValueError("inputs must not be empty")
    return sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)


def exact_match(reference: str, prediction: str) -> int:
    """Return 1 when normalized strings match exactly, else 0."""
    normalize = lambda s: " ".join(s.strip().lower().split())
    return int(normalize(reference) == normalize(prediction))
