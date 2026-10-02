from examples.quickstart import run_demo


def test_quickstart_is_reproducible():
    first = run_demo(seed=42)
    second = run_demo(seed=42)

    assert first == second
    assert first["r2"] > 0.95
    assert abs(first["coefficient"] - 3.2) < 0.2
