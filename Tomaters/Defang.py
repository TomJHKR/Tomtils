#!/usr/bin/python
import sys


# Take in list of strings as argument and output a defanged version

# arguments = sys.argv
# fanged = arguments[1]
def defang(s):
    defanged_list = []
    for line in s:
        defanged = line
        defanged = fanged.replace("hxxp", "http")
        defanged = fanged.replace("[", "")
        defanged = fanged.replace("]", "")
        defanged_list.append(defanged)

    print(f"Outputting Defanged\n")
    print(*defanged_list, sep=", ")
    print("")
    return defanged_list
