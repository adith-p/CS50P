# while True:
#     try:
#         name = input("What's your name: ")
#     except EOFError:
#         break

# with open("name.txt", "r", encoding="UTF-8") as file:
#     for name in file:
#         print(f"{name}".rstrip())

# names = []

# with open("name.txt", "r") as file:
#     for name in file:
#         names.append(name.rstrip())


# for name_s in sorted(names):
#     print(f"Hi, {name_s}")

import csv
students_list = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students_list.append({"name": row["name"], "home": row["dept"]})


for student in sorted(students_list, key=lambda student: student["name"]):
    print(f"Name: {student['name']} Dept: {student['home']}")
