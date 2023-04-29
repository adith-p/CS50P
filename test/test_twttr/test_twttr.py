"""twttr.py testing file"""
from twttr import shorten


def test_numeric():
    """test numeric imput"""
    assert shorten("100") == "100"


def test_upper():
    """test upper text input"""
    assert shorten("HELLO,WORLD") == "HLL,WRLD"


def test_lower():
    """test lower text input"""
    assert shorten("hello,world") == "hll,wrld"


def test_mixed():
    """test mixed text input"""
    assert shorten("HELLo,wORlD") == "HLL,wRlD"
