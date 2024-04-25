#!/usr/bin/python
import sys


# Take in list of strings as argument and output a defanged version
def fang(s):
    fanged = []
    for line in s:
        defanged = line
        defanged = defanged.replace("http", "hxxp")
        defanged = defanged.replace(".", "[.]")
        fanged.append(defanged)

    print(f"Outputting Fanged\n")
    print(*fanged, sep=", ")
    print("")
    return fanged