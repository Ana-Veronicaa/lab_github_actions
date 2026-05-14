def test_example():
    """Test simplu care verifica ca 1 + 1 = 2."""
    assert 1 + 1 == 2


def test_salut():
    """Test care verifica ca functia salut returneaza un string."""
    from script import salut
    assert salut() == "Hello, GitHub Actions! Workflow test successful!"