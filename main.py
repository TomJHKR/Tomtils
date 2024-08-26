#!/usr/bin/python
import sys, select, os
from Tomaters.Defang import defang
from Tomaters.Fang import fang
from Tomaters.Redact import redact
from Tomaters.Base64 import *
from Tueries.IPsearches import *
from Tothers.Filewriters import *
from Tueries.Concat import *
from rich.console import Console
from rich.markdown import Markdown
from Tueries.Port import *
from Tueries.Tilers import *




def main():
    help("")
    #val = input("Enter args: ") 
    lines = change("")
    global history
    history = {}
    history["original"] = lines
    while True:
        perform = input(f"\nWhat to do: ")
        if perform == "exit":
            break
        if perform.split(" ")[0] == "use":
            use = perform.split(" ")[1]
            lines = history.get(use)
            print(f"\nUsing : {use} - {history[use]}\n")
            continue
        if perform == "writetxt":
            writetxt(history)
        try:
            lines = globals()[perform](lines)
            if perform != 'help' and perform != 'hist':
                history[perform] = lines
        except:
            del history[perform]
            continue

def hist(s):
    #del history["hist"]
    for key, value in history.items():
        print(f"{key} : {value}\n")

def help(s):
    console = Console()
    with open('readme.md') as f:
        md = Markdown(f.read())
        console.print(md)

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
