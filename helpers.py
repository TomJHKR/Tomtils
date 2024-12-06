import os
from print_color import print
from typing import Union

def get_input():
    print("Please enter values seperated by newline: ", color='blue')
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    if line == None:
        return ""
    return lines

def validate_input(inp: Union[str,list]):
    if not inp:
        inp = get_input()
    if isinstance(inp, str):
        inp = [inp]
    return inp
