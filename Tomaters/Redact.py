#!/usr/bin/python
import sys

def redact(s):
    redacted = []
    to_redact = input("1 : redact by string\n2 : redact by position\n")
    match to_redact:
        case "1":
            rem = input("String to remove: ")
            rep = "*" * len(rem)
            print(rep)
            print("")
            for line in s:
               unredacted = line
               unredacted = unredacted.replace(rem, rep)
               redacted.append(unredacted)             
        case "2":
            rem = input("char postion/s to remove: ")
            it = rem.split(" ")
            for line in s:
                current = line
                for i in it:
                    unredacted = list(current)
                    unredacted[int(i)-1] = "*"
                    current = "".join(unredacted)
                redacted.append(current)
    print(redacted)
    return redacted
