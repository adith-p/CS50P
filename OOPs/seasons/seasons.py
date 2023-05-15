import sys
from datetime import date, datetime
import inflect


class Dob:

    def __init__(self, dob, current) -> None:
        self.dob = dob
        self.current = current
        self.difference()
        self.convert()

    def __str__(self) -> str:
        return f"{self.dob_words.capitalize()} minutes"

    def convert(self):
        p = inflect.engine()
        min_words = p.number_to_words(self.dob_mins, andword="")
        self.dob_words = min_words

    def difference(self):
        d1 = datetime.strptime(str(date.today()), "%Y-%m-%d")
        d2 = datetime.strptime(self.dob, "%Y-%m-%d")
        delta = d1-d2
        self.dob_mins = round(delta.days*24*60)

    @classmethod
    def get(cls, brith_date):

        try:
            date.fromisoformat(brith_date)
        except ValueError:
            sys.exit("Invalid date")

        return cls(brith_date, date.today())


def main():
    brith_date = input("Date of Birth: ")
    dob = Dob.get(brith_date)
    print(dob)


if __name__ == "__main__":
    main()
