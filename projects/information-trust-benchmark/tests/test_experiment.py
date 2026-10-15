from src.experiment import generate, evaluate, ALL

def test_reproducibility():
    assert generate(50, 12).equals(generate(50, 12))

def test_bounds():
    df = generate(100)
    assert df[ALL].ge(0).all().all() and df[ALL].le(1).all().all()

def test_evaluation():
    results, coefficients = evaluate(generate(300))
    assert len(results) == 3 and len(coefficients) == 10
    assert results['roc_auc'].between(0, 1).all()
