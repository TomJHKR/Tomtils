#!/usr/bin/python
import sys
import json
import requests
from dotenv import load_dotenv
import os
import time
import base64
import re

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
    url = f'https://www.virustotal.com/api/v3/ip_addresses/' + s
    api_key = os.getenv('VTKEY')
    headers = {
            "accept": "application/json",
            'x-apikey': api_key,
            
    }
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    stats = response_json['data']['attributes']['last_analysis_stats']
    format_print(stats,s)

def searchURL(s):
    url_id = base64.urlsafe_b64encode(s.encode()).decode().strip("=")
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
        format_print(stats,s)
    except:
        error_print(s)

def searchHash(s):
    url = f'https://www.virustotal.com/api/v3/files/' + s
    api_key = os.getenv('VTKEY')
    headers = {
            "accept": "application/json",
            'x-apikey': api_key,
            
    }
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    stats = response_json['data']['attributes']['last_analysis_stats']
    format_print(stats,s)

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


def scan(s):
    for i in s:
        i.replace(" ","")
        determine_type(i)

def determine_type(s):
    if validate_ip(s):
        searchIP(s)
    elif validate_url(s):
        searchURL(s)
    else:
        searchHash(s)


def validate_url(s):
    domain_regex = r'(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))'
    url_regex = r'''(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))'''
    valid_domain_name_regex = re.compile(url_regex, re.IGNORECASE)
    if re.match(valid_domain_name_regex, s):
        return True
    else:
        return False

def validate_ip(ip_str):
    reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(reg, ip_str):
        return True
    else:
        return False

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
