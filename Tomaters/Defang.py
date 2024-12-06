#!/usr/bin/python
import sys
from helpers import validate_input


# Take in list of strings as argument and output a defanged version

# arguments = sys.argv
# fanged = arguments[1]
def defang(inp=None):
    s = validate_input(inp)
    defanged_list = []
    for line in s:
        fanged = line
        defanged = fanged.replace("http", "hxxp")
        defanged = fanged.replace(".", "[.]")
        defanged_list.append(defanged)

    print(f"Outputting Defanged\n")
    print(*defanged_list, sep=", ")
    print("")
    return [s,defanged_list]
