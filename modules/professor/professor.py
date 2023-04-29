# The program should ultimately output the user’s score: the number of correct answers out of 10.
from random import randint


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    # Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
        except ValueError:
            continue

        return level


def generate_integer(level):
    # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+)
    x_values = []
    y_values = []
    i = 0
    while i < 10:
        if level == 1:
            x_temp = randint(0, 9)
            y_temp = randint(0, 9)
        elif level == 2:
            x_temp = randint(10, 99)
            y_temp = randint(10, 99)
        else:
            x_temp = randint(100, 999)
            y_temp = randint(100, 999)

        x_values.append(x_temp)
        y_values.append(y_temp)
        i += 1
        sum_values = []
    for i in range(10):
        sum_values.append(x_values[i] + y_values[i])
        # Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again
    i = 0
    score = 10
    while True:
        while i < 10:
            try:
                user_sum = int(input(f"{x_values[i]} + {y_values[i]} = "))
                act_sum = sum_values[i]
                break

            except ValueError:
                break

        if user_sum != act_sum:
            print("EEE")
            count = 0
            score -= 1

            while count <= 3:
                try:
                    user_sum = int(input(f"{x_values[i]} + {y_values[i]} ="))
                except ValueError:
                    print("EEE")

                if count == 1:
                    print("EEE")
                    print(f"{x_values[i]} + {y_values[i]} = {act_sum}")
                    i += 1
                    break
                if user_sum == act_sum:
                    i += 1

                    break

                print("EEE")
                count += 1
                continue

        else:
            if i == 10:
                print(f"Score: {score}")
                break
            i += 1
            continue


if __name__ == "__main__":
    main()
