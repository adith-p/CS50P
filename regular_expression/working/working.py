import re
import sys


def main():
    print(convert(input("Hours: ")))


def get_time(u_time):
    if pattern := re.search(r"(\d+):?(\d*) (AM|PM) to (\d+):?(\d*)? (PM|AM)$", u_time):
        pattern_list = list(pattern.groups())
        if pattern_list[1] == "":
            pattern_list.remove("")
            pattern_list.insert(1, "00")

            pattern_list.remove("")
            pattern_list.insert(4, "00")
        return pattern_list
    else:
        raise ValueError


def check_time(pattern_list):
    if int(pattern_list[0]) not in range(0, 13):
        raise ValueError
    if int(pattern_list[3]) not in range(0, 13):
        raise ValueError
    if int(pattern_list[1]) not in range(0, 60):
        raise ValueError
    if int(pattern_list[4]) not in range(0, 60):
        raise ValueError

    if pattern_list[5] == "AM":
        if int(pattern_list[3]) in range(1, 10):
            pattern_list[3] = "0" + pattern_list[3]
        elif int(pattern_list[1]) in range(1, 10):
            pattern_list[1] = "0" + pattern_list[1]

        if pattern_list[0] != "12":
            pattern_list[0] = str(int(pattern_list[0]) + 12)

        if pattern_list[3] == "12":
            pattern_list[3] = "00"

        return f"{pattern_list[0]}:{pattern_list[1]} to {pattern_list[3]}:{pattern_list[4]}"

    if pattern_list[5] == "PM":
        if int(pattern_list[3]) in range(1, 10):
            pattern_list[3] = "0" + pattern_list[3]
        if int(pattern_list[0]) in range(1, 10):
            pattern_list[0] = "0" + pattern_list[0]

        if pattern_list[3] != '12':
            pattern_list[3] = str(int(pattern_list[3]) + 12)

        if pattern_list[0] == '12':
            pattern_list[0] = "00"

    return f"{pattern_list[0]}:{pattern_list[1]} to {pattern_list[3]}:{pattern_list[4]}"


def convert(s):

    pattern_list = get_time(s)
    return check_time(pattern_list)


if __name__ == "__main__":
    main()
