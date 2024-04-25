#!/usr/bin/python
import sys
import json

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