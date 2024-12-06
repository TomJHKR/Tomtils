#!/usr/bin/python
import sys, select, os, tempfile, json

from Tomaters.Defang import defang
from Tomaters.Fang import fang
from Tomaters.Redact import redact
from Tomaters.Base64 import *
from Tomaters.Iprange import *

from Tueries.IPsearches import *
from Tueries.Concat import *
from Tueries.Port import *
from Tueries.Tilers import *

from Tothers.Filewriters import *

from helpers import help,parse_arguments

## Main for determining what function to use
def main():
    args = parse_arguments()
    help()
    global history_temp_file
    history_temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".json")

    if args.method:
        if args.input:
            current = globals()[args.method](args.input)
        else:
            current = globals()[args.method]()
    while True:
        perform = input(f"\nWhat to do: ")
        match perform:
            case "exit":
                break
            case "writetxt":
                history = load_history(history_temp_file)
                writetxt(history)
            case _ if perform.split(" ")[0] == "use":
                use = perform.split(" ")[1]
                history = load_history(history_temp_file)
                lines = history.get(use)
                print(f"\nUsing : {use} - {history[use]}\n")
                continue
            case "hist":
                history_print(history_temp_file)
            case "help":
                help()
            case _:
                try:
                    current = globals()[perform]()
                    if isinstance(current, list):
                        save_history(format_history_entry(current[0], current[1], perform),history_temp_file)
                    else:
                        save_history(current, history_temp_file)
                except Exception as e:
                    print(e)
                    continue




def change(s):
    print(f"Please enter the your values (or not): ")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    if line == None:
        return ""
    return lines


def current(s):
    print(f"\nCurrent string/list being used: {s}\n")



if __name__ == '__main__':
    main()  
