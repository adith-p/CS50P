def main():

    menus()


def menus():
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    sale = 0
    while True:

        try:
            item = input("Item: ").title()
        except EOFError:
            break

        for i in menu_items:
            if i == item:
                sale += float(menu_items[i])
                sale_formated = format(sale, ".2f")
                print(f"Total: ${sale_formated}")
                break

            else:
                continue


main()
