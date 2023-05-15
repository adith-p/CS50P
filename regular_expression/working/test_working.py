import pytest
from working import convert


def main():
    test_omit()
    test_out_of_range()
    test_off_time()


def test_omit():
    with pytest.raises(ValueError):
        convert("9 AM - 10 AM")
    with pytest.raises(ValueError):
        convert("9 AM @ 10 AM")
    with pytest.raises(ValueError):
        convert("9 AM = 10 AM")


def test_out_of_range():
    with pytest.raises(ValueError):
        convert("15 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("24 AM to 15 PM")
    with pytest.raises(ValueError):
        convert("1:65 AM to 2:90 PM")


def test_off_time():
    assert convert("9 AM to 5 PM") != "10:00 to 17:00"
    assert convert("10 AM to 5 PM") != "11:00 to 17:00"
    assert convert("11 PM to 5 AM") != "24:00 to 05:00"
    assert convert("11:30 PM to 5:30 AM") != "23:35 to 05:40"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


if __name__ == "__main__":
    main()
