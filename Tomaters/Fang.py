#!/usr/bin/python
import sys

from typing import Optional
import re

from Schemes import URI_SCHEMES_DEFANGED_MAP_REV
from Uri import extract_scheme

# Take in list of strings as argument and output a fanged version


# Defang dot only if they have not already been defanged
REFANG_DOT_PATTERN = re.compile(r"\[([\.\+-])\]")


def fang(s):
    fanged_list = []
    for line in s:
        fanged = line
        fanged = refang_scheme(fanged) or fanged
        fanged = REFANG_DOT_PATTERN.sub(r"\1", fanged)
        fanged_list.append(fanged)

    print(f"Outputting Fanged\n")
    print(*fanged_list, sep=", ")
    print("")
    return fanged_list


def refang_scheme(s: str) -> Optional[str]:
    if not (scheme := extract_scheme(s)):
        return None

    # Special case for HXXP[S]
    if scheme == "hxxp" or scheme == "hxxps":
        defanged_scheme = "http" + ("s" * scheme.endswith("s"))
    elif not (defanged_scheme := URI_SCHEMES_DEFANGED_MAP_REV.get(scheme)):
        return None

    return s.replace(scheme, defanged_scheme, 1)
