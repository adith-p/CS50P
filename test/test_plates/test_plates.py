"""test cases for the program plates"""

from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


def test_digit():
    assert is_valid("A2") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AAAAAA") == True

    assert is_valid("55") == False
    assert is_valid("50") == False


def test_special_chars():
    assert is_valid("AA..AA") == False
    assert is_valid("AA AA") == False

    assert is_valid("!@#$%") == False
    assert is_valid("AX@24") == False


def test_zero_placement():
    assert is_valid("A01") == False
    assert is_valid("A001") == False
    assert is_valid("AA01") == False


def test_correct_values():
    assert is_valid("AAA222") == True
    assert is_valid("CS50") == True
