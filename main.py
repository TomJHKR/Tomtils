#!/usr/bin/python
import sys, select, os
from Tomaters.Defang import defang
from Tomaters.Fang import fang
from Tueries.IPsearches import *




def main():
    help("")
    print(f"Please enter the your values: ")
    #val = input("Enter args: ") 
    lines = []
    global history
    history = {}
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    history["original"] = lines
    while True:
        perform = input(f"What to do: ")
        print(f"")
        if perform == "exit":
            break
        if perform.split(" ")[0] == "use":
            use = perform.split(" ")[1]
            lines = history.get(use)
            print(f"Using : {use}\n")
            continue
        try:
            history[perform] = lines
            lines = globals()[perform](lines)
        except:
            del history[perform]
            continue

def hist(s):
    del history["hist"]
    for key, value in history.items():
        print(f"{key} : {value}\n")

def help(s):
    f = open('readme.md', 'r')
    fileString = f.read()
    print(fileString)





if __name__ == '__main__':
    main()  