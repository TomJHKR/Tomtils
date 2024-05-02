#!/usr/bin/python
import sys
import json
import requests
from dotenv import load_dotenv
import os
import time
import base64

load_dotenv()

def create(s):
    f = open("Tueries/Masterlist.json")
    data = json.load(f)
    print(data)

def source(s):
    q = f"""in(field="SourceIP", values=[{', '.join(s)}])\n"""
    print(q)
    return q

def remote(s):
    q = f"""in(field="RemoteIP", values=[{', '.join(s)}])\n"""
    print(q)
    return q

def searchIP(s):
    for i in s:
        i.replace(" ", "")
        url = f'https://www.virustotal.com/api/v3/ip_addresses/' + i
        api_key = os.getenv('VTKEY')
        headers = {
            "accept": "application/json",
            'x-apikey': api_key,
            
        }
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        stats = response_json['data']['attributes']['last_analysis_stats']
        format_print(stats,i)

def searchURL(s):
    for i in s:
        i.replace(" ", "")
        url_id = base64.urlsafe_b64encode(i.encode()).decode().strip("=")
        # bytes = i.encode("ascii") 
        # encoded = base64.b64encode(bytes)
        url = f'https://www.virustotal.com/api/v3/urls/' + url_id
        api_key = os.getenv('VTKEY')
        headers = {
            "accept": "application/json",
            'x-apikey': api_key,
            
        }
        try:
            response = requests.get(url, headers=headers)
            response_json = json.loads(response.text)
            stats = response_json['data']['attributes']['last_analysis_stats']
            format_print(stats,i)
        except:
            error_print(i)

def format_print(s,ip):
    mal = s.get('malicious')
    sus = s.get('suspicious')
    harmless = s.get('harmless')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}Look up for : {bcolors.ENDC}{ip}')
    print(f'{bcolors.RED}{bcolors.BOLD}Malicious : {bcolors.ENDC}{mal}')
    print(f'{bcolors.YELLOW}{bcolors.BOLD}Suspicious : {bcolors.ENDC}{sus}')
    print(f'{bcolors.OKGREEN}{bcolors.BOLD}Clean : {bcolors.ENDC}{harmless}')

def error_print(ip):
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}Error for looking up : {bcolors.ENDC}{ip}')
    print(f'{bcolors.RED}{bcolors.BOLD}Not Found :({bcolors.ENDC}')



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