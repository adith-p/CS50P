def main():
    user_str = input()
    words = user_str.split()

    print(convert(user_str, words))


def convert(user_str, words):
    if ':)' in words or ':(' in words:
        new_str = user_str.replace(":)", "🙂")
        new1_str = new_str.replace(":(", "🙁")

    return new1_str


main()
