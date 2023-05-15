from um import count


def main():
    test_values()
    test_spaces()
    test_case()


def test_values():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_spaces():
    assert count(" um ") == 1
    assert count("um ") == 1
    assert count(" um") == 1


def test_case():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("UM um") == 2


if __name__ == "__main__":
    main()
