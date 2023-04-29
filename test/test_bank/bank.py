def main():
    user_input = input("Greeting: ")

    print(f"${value(user_input)}")


def value(usr_input):
    usr_input = usr_input.lower().strip()

    if usr_input in ["hello"]:
        money = 0
        return money
    if usr_input.startswith("h"):
        money = 20
        return money

    money = 100
    return money


if __name__ == "__main__":

    main()
