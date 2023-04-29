def main():

    convert()


def convert():

 # while(true)
    while True:

        value = input("Fraction: ")

        if "/" not in value:
            continue
        words = value.split("/")
        x = words[0]
        z = words[1]
        try:

            x = int(x)
            z = int(z)
            if x > z:
                continue

            fraction = x/z

        except (ZeroDivisionError, ValueError):
            pass
        else:
            break

    percent = int(round(fraction*100))

    if fraction > 0.9:
        print("F")
    elif fraction < 0.1:
        print("E")
    else:
        print(str(percent)+"%")


main()
