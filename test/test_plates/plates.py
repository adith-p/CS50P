def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    truce = True
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) <= 2 or len(s) > 6:
        truce = False
        return truce

    # they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. .”
    if s[:2].isdigit() and s[:-1].isalpha():
        truce = False
        return truce

    # “No periods, spaces, or punctuation marks are allowed.
    if s.isalnum():

        # ”The first number used cannot be a ‘0’"
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i:].isdigit() and s[i] != '0':
                    truce = True
                else:
                    truce = False
                return truce

    else:
        truce = False
        return truce

    return truce


if __name__ == "__main__":
    main()
