#!/usr/bin/python
import sys
import json
import requests
from dotenv import load_dotenv
import os
import time
import base64

def lolbas(inp=None):
    url = "https://lolbas-project.github.io/api/lolbas.json"
    if not inp:
        lol = input("\nWhat DLL/EXE: ")
    else:
        lol = inp
    print("")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            lolbas_data = response.json()
            entry_found = False
            for entry in lolbas_data:
                try_entry = entry["Name"].lower()
                if try_entry == lol.lower():
                    entry_found = True
                    for k, v in entry.items():
                        if isinstance(v, list):
                            print(f"{k} : ")
                            for item in v:
                                print("    -", item)
                        else:
                            print(f"{k} : {v}")
                    break  # Stop iterating once the entry is found
            if not entry_found:
                print("Entry not found.")
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return f"Performed function lolbas\nSearched for {lol}"
