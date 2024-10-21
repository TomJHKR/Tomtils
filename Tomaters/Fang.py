#!/usr/bin/python
import sys


# Take in list of strings as argument and output a defanged version
def fang(s):
    fanged_list = []
    for line in s:
        fanged = line
        fanged = defanged.replace("hxxp", "http")
        fanged = defanged.replace("[.]", ".")
        fanged_list.append(fanged)

    print(f"Outputting Fanged\n")
    print(*fanged_list, sep=", ")
    print("")
    return fanged_list
