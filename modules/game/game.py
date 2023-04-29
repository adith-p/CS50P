from random import randrange
# Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
    except ValueError:
        continue

    # Randomly generates an integer between 1 and , inclusive, using the random module.
    that_integer = randrange(level+1)

    # Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
    except ValueError:
        continue

    # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    if guess < that_integer:
        print("Too small!")

    # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    elif guess > that_integer:
        print("Too Large! ")

    # If the guess is the same as that integer, the program should output Just right! and exit.
    else:
        print("Just right!")
        break
