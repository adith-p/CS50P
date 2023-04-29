"""Test Cases for bank.py"""
from bank import value


def test_zero_case():
    """cases where the output is 0"""
    assert value("hello") == 0
    assert value(" hello ") == 0


def test_20_case():
    """cases where the output is 20"""

    assert value("Hey") == 20
    assert value("HOW ARE YOU DOING") == 20


def test_100_case():
    """cases where the output is 100"""
    assert value("What's happening") == 100
    assert value("What") == 100
