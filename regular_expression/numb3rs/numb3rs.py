import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if pattern := re.search(r"^(\d{0,3}).(\d{0,3}).(\d{0,3}).(\d{0,3})$", ip):

        if len(pattern.groups()) == 4:

            for i in pattern.groups():

                try:
                    if int(i) <= 255:
                        flag = True
                    else:
                        return False
                except ValueError:
                    return False
            return flag
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
