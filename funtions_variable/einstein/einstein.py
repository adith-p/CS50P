# e= mc**2

def main():
    m = int(input("m: "))
    print(f"E: {calculate(m)}")


def calculate(m):
    C = 300000000
    E = m*C**2

    return E


main()
