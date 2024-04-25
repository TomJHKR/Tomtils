#!/usr/bin/python
import sys


# Take in list of strings as argument and output a defanged version

# arguments = sys.argv
# fanged = arguments[1]
def defang(s):
    defanged = []
    for line in s:
        fanged = line
        fanged = fanged.replace("hxxp", "http")
        fanged = fanged.replace("[", "")
        fanged = fanged.replace("]", "")
        defanged.append(fanged)

    print(f"Outputting Defanged\n")
    print(*defanged, sep=", ")
    print("")
    return defanged
