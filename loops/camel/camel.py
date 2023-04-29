def main():

    camel_case = input("camelCase: ")

    print(f"snake_case: {snake(camel_case)}")


def snake(camel_case):
    s_case = ""
    for char in camel_case:
        if char.isupper():

            s_case += "_"+char.lower()
        else:
            s_case += char

    return s_case


main()
