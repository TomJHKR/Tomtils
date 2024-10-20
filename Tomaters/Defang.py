#!/usr/bin/python
import sys
from typing import Optional
import re

from Schemes import URI_SCHEMES_DEFANGED_MAP
from Uri import extract_scheme

# Take in list of strings as argument and output a defanged version


# Defang dot only if they have not already been defanged
DEFANG_DOT_PATTERN = re.compile(r"(?<!\[)\.(?!\])")


# arguments = sys.argv
# fanged = arguments[1]
def defang(s):
    # TODO: support IP addresses
    defanged_list = []
    for line in s:
        defanged = line
        defanged = defang_scheme(defanged) or defanged
        defanged = DEFANG_DOT_PATTERN.sub("[.]", defanged)
        defanged_list.append(defanged)

    print(f"Outputting Defanged\n")
    print(*defanged_list, sep=", ")
    print("")
    return defanged_list


def defang_scheme(s: str) -> Optional[str]:
    if not scheme := extract_scheme(s):
        return None

    if not defanged_scheme := URI_SCHEMES_DEFANGED_MAP.get(scheme):
        return None

    return s.replace(scheme, defanged_scheme, 1)
