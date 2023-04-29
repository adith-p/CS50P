import sys
from pyfiglet import Figlet

# Expects zero or two command-line arguments:

if len(sys.argv) == 1:
    sys.exit("invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            f = Figlet(font=sys.argv[2])
            text = input("Input: ")
            print(f.renderText(text))
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
