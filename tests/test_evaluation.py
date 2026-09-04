from src.evaluation import accuracy, exact_match


def test_accuracy():
    assert accuracy([1, 0, 1], [1, 0, 0]) == 2 / 3


def test_exact_match():
    assert exact_match("Trustworthy AI", "  trustworthy   ai ") == 1
