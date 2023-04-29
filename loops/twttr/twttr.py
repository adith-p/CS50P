def main():
    user_string = input("Input: ")

    print(f"Output: {delete(user_string)}")


def delete(user_string):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new_string = ""

    for char in user_string:
        if char not in vowels:
            new_string += char

    return new_string


main()
