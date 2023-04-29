def main():
    input_string = input("What time is it? ")
    time = convert(input_string)

    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hour, minu = time.split(":")
    hour = float(hour)
    minu = float(minu)/60
    new_time = hour+minu

    return new_time


if __name__ == "__main__":
    main()
