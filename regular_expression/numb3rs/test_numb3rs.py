from numb3rs import validate


def main():
    test_byte()
    test_non_int()
    test_division()


def test_byte():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.1") == True
    assert validate("1.1.1.1") == True
    assert validate("300.256.255.1") == False
    assert validate("") == False


def test_non_int():
    assert validate("cat") == False
    assert validate("$%^&@#$") == False
    assert validate("256-963-255-693") == False


def test_division():
    assert validate("8.8.8.") == False
    assert validate("127.0.0") == False
    assert validate("255.255") == False
    assert validate("255.265.275.285.295") == False


def test_range():

    assert validate("512.1.1.1") == False
    assert validate("1.256.3.4") == False
    assert validate("1.2.256.4") == False
    assert validate("1.2.3.256") == False


if __name__ == "__main__":
    main()
