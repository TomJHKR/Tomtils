#!/usr/bin/python
import sys, select, os
from Tomaters.Defang import defang
from Tomaters.Fang import fang
from Tueries.IPsearches import *

def main():
    print(f"Welcome to TomTils")
    print(f"Please enter the your values you are wanting to perform")
    #val = input("Enter args: ") 
    
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    while True:
        perform = input(f"What to do: ")
        print(f"")
        if perform == "exit":
            break
        lines = globals()[perform](lines)
    
    




if __name__ == '__main__':
    main()  