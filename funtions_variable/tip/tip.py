def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    D = d.replace("$", " ")
    D.strip()

    D = float(D)

    return D


def percent_to_float(p):
    P = p.replace("%", " ")
    P.strip()

    P = float(P)

    return P / 100


main()
