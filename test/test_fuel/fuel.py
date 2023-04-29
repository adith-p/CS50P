def main():

    value = input("Fraction: ")

    print(gauge(convert(value)))


def convert(fraction):
    while True:

        if "/" not in fraction:
            continue
        words = fraction.split("/")
        x = words[0]
        z = words[1]
        try:

            x = int(x)
            z = int(z)

        except ValueError:
            raise ValueError
        try:
            if x > z:
                continue

            fraction = x/z
        except ZeroDivisionError:
            raise ZeroDivisionError

        else:
            break

    return int(round(fraction*100))


def gauge(percentage):

    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"

    return str(percentage)+"%"


if __name__ == "__main__":
    main()
