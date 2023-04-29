import pytest

from fuel import gauge, convert


def test_exceptions():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("10/9")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_correct_values():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
