"""
a program that return the price of the bitcoin based on the input quantity of the coin 
"""
import sys
import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    if True:
        float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5)

except requests.RequestException:
    sys.exit()

coin = r.json()
price = coin["bpi"]["USD"]["rate_float"]

print(f"${price*float(sys.argv[1]):,.4f}")
