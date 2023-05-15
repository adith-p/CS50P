import validators


def main():
    email = input("what's your email address... ")
    if validate(email):
        print("valid")
    else:
        print("invalid")


def validate(email_id):

    return validators.email(email_id)


if __name__ == "__main__":
    main()
