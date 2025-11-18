import pytest
from app.calculator import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-3, -2) == -5

def test_add_floats():
    assert add(2.5, 1.2) == 3.7

def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("a", 1)
