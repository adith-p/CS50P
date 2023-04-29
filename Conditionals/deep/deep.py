def main():
    user_input = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    check(user_input.lower().strip())

# or "forty-two " or "forty two"


def check(usr_input):
    if usr_input == "42" or usr_input == "forty-two" or usr_input == "forty two":

        print("Yes")
    else:
        print("No")


main()
