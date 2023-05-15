from seasons import Dob
import pytest


def main():
    test_correct_format()
    test_incorrect_format()


def test_correct_format():
    assert str(Dob.get(
        "2022-01-01")) == "Seven hundred eleven thousand, three hundred sixty minutes"


def test_incorrect_format():
    with pytest.raises(SystemExit):
        Dob.get("202-01-02")
        Dob.get("2021-1-01")
        Dob.get("2022-01-6")


if __name__ == "__main__":
    main()
