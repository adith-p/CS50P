def main():
    user_input = input("Greeting: ")

    check(user_input.lower().strip())


def check(usr_input):
    if "hello" in usr_input:
        print("$0")
    elif usr_input[0] == "h" and usr_input != "hello":
        print("$20")
    elif usr_input[0] == "w":
        print("$100")


main()
