def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    numeric_date(months)


def numeric_date(months_list):

    while True:

        date = input("Date: ").strip()

        if date.replace("/", "").isdigit():  # MM/DD/YYYY
            words = date.split("/")
            year = int(words[2])
            month = int(words[0])
            day = int(words[1])
        elif "," in date and date[0].isalpha():  # October 9, 1701
            words = date.split(" ")
            year = int(words[2])
            month = words[0]
            day = int(words[1].replace(",", ""))

            if month not in months_list:
                continue
            else:
                month = months_list.index(month)+1
        else:
            continue

        if day < 1 or day > 31:
            continue
        elif month < 1 or month > 12:
            continue

        iso_std = f"{year:04d}-{month:02d}-{day:02d}"  # YYYY-MM-DD

        print(iso_std)
        break


main()
