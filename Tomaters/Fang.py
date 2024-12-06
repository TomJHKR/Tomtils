#!/usr/bin/python
import sys
from helpers import validate_input

# Take in list of strings as argument and output a defanged version
def fang(inp=None):
    s = validate_input(inp)
    fanged_list = []
    for line in s:
        defanged = line
        fanged = defanged.replace("hxxp", "http")
        fanged = defanged.replace("[.]", ".")
        fanged_list.append(fanged)

    print(f"Outputting Fanged\n")
    print(*fanged_list, sep=", ")
    print("")
    return s,fanged_list
