class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self._name} from {self._house}"

    @property
    def get_name(self):
        return self._name

    @property
    def get_house(self):
        return self.house

    @get_name.setter
    def name(self, name):
        self._name = name

    @get_house.setter
    def house(self, house):
        if house not in ["cs", "bca", "bcom"]:
            raise ValueError("Incorrect value")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    stream = input("Class: ")
    return Student(name, stream)


if __name__ == "__main__":
    main()
