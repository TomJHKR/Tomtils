#!/usr/bin/python
import sys
import json
import os

def port(inp=None):
    if not inp:
        port = input(f"What port: ")
    else:
        port = inp
    f = open("Tueries/PortList.json")
    data = json.load(f)
    try:
        for i in data[port]:
            format_print(i)
    except:
        print(f"{bcolors.BOLD}{bcolors.HEADER}{bcolors.RED}ERROR: PORT not found{bcolors.ENDC}")
    return f"Perfomed function port\n{port}"

def format_print(s):
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{bcolors.OKBLUE}Port : {bcolors.ENDC}{s["port"]}')
    print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.OKBLUE}Descripton : {bcolors.ENDC}{s["description"]}')
    if s["udp"]:
        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.OKGREEN}UDP : {bcolors.ENDC}{s["udp"]}')
    else:
        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.RED}UDP : {bcolors.ENDC}{s["udp"]}')
    if s["tcp"]:
        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.OKGREEN}TCP : {bcolors.ENDC}{s["tcp"]}')
    else:
        print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.RED}TCP : {bcolors.ENDC}{s["tcp"]}')
    print(f'{bcolors.HEADER}{bcolors.BOLD}{bcolors.OKBLUE}Status : {bcolors.ENDC}{s["status"]}')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
