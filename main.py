#!/usr/bin/python
import sys, select, os
from Tomaters.Defang import defang
from Tomaters.Fang import fang
from Tomaters.Redact import redact
from Tomaters.Base64 import *
from Tueries.IPsearches import *




def main():
    help("")
    
    #val = input("Enter args: ") 
    lines = change("")
    global history
    history = {}
    history["original"] = lines
    while True:
        perform = input(f"What to do: ")
        print(f"")
        if perform == "exit":
            break
        if perform.split(" ")[0] == "use":
            use = perform.split(" ")[1]
            lines = history.get(use)
            print(f"Using : {use} - {history[use]}\n")
            continue
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
    f = open('readme.md', 'r')
    fileString = f.read()
    print(fileString)

def change(s):
    print(f"Please enter the your values: ")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return lines

def current(s):
    print(f"Current string/list being used: {s}\n")
if __name__ == '__main__':
    main()  