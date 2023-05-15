import random


class Hat:
    dept = ["CS", "BCA", "Bcom"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.dept))


def main():
    name = input("name: ")
    Hat.sort(name)


if __name__ == "__main__":
    main()
