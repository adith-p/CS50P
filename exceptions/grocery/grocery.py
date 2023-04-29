def main():

    final_list = occurence(menus())

    print_list(final_list)


def menus():
    item_list = []

    while True:

        try:
            item = input()
        except EOFError:
            break

        item_list.append(item)

    sorted_list = sorted(item_list)
    return sorted_list


def occurence(sorted_list):
    occur = {}

    for fruits in sorted_list:
        if fruits not in occur:
            occur[fruits] = 1
        else:
            occur[fruits] += 1

    return occur


def print_list(final_list):
    for keys, values in final_list.items():
        print(f"{values} {keys.upper()}")


main()
