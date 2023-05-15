class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self) -> str:

        return f"{self.name} from {self.house}"

    @classmethod
    def get_student(cls):
        name = input("Name: ")
        house = input("Class: ")
        return cls(name, house)


def main():
    student = Student.get_student()
    print(student)


if __name__ == "__main__":
    main()
