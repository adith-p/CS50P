import argparse

parser = argparse.ArgumentParser(description="A module that meows")
parser.add_argument(
    "-n", default=1, help="number of time the function meows", type=int)
arg = parser.parse_args()

for _ in range(arg.n):
    print("Meow")
