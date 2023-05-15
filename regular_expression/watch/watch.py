import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = re.search("iframe.+embed/([^\"]+)", s)
    try:
        if pattern.groups():
            shorten = f"https://youtu.be/{pattern.group(1)}"
            return shorten
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
