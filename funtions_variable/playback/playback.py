def main():
    user_str = input()
    print(period(user_str))


def period(user_str):
    new_str = user_str.replace(" ", "...")
    return new_str


main()
