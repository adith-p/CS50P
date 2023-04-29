def main():
    user_string = input("Input: ")

    print(f"Output: {shorten(user_string)}")


def shorten(user_string):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new_string = ""

    for char in user_string:
        if char not in vowels:
            new_string += char

    return new_string


if __name__ == "__main__":

    main()
