def main():
    yell("This Was CS50")


def yell(*words):
    upperwords = [word.upper() for word in words]
    print(*upperwords)


if __name__ == "__main__":
    main()
