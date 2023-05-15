"""Regualr exp module"""
import re

name = input("enter the name ")

if names := re.search(r"^(.+), *(.+)$", name):

    last, first = names.groups()

    name = f"{first} {last}"

print("hello ", name)
