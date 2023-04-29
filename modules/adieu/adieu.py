""" Program that greet accrding to the number of input"""
name_list = []
while True:
    try:
        user_name = input("Name: ")
        name_list.append(user_name)
    except EOFError:
        print("Adieu, adieu, to ", end="")
        break


if len(name_list) == 1:
    print(f"{name_list[0]}")
elif len(name_list) == 2:
    print(f"{name_list[0]} and {name_list[1]}")
else:
    i = 0
    name_string = ""
    while i < len(name_list)-1:
        name_string = name_string + f"{name_list[i]}, "
        i += 1

    last_name = f"and {name_list[len(name_list)-1]}"

    if len(name_list) >= 3:
        print(f"{name_string}{last_name}")
