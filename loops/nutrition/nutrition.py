def main():
    fruit_name = input("Item: ")

    Calories(fruit_name)


def Calories(fruit_name):
    fruits_dict = {
        "apple": "130",
        "avocado": "50",
        "Banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "Honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",


    }
    for i in fruits_dict:
        if i == fruit_name.lower():

            print(f"Calories: {fruits_dict[i]}")

        else:
            print("")


main()
