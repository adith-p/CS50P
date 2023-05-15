import re

email = input("what's your email ")


if re.search(r"^\w+@+(\w+\.)?.*\w+\.edu", email):
    print("Valid")
else:
    print("Invalid")


#
