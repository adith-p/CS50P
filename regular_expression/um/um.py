import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    if pattern := re.findall(r"\b(um)\b", s.lower()):
        return len(pattern)
    return 0


if __name__ == "__main__":
    main()
