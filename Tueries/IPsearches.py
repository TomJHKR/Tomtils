#!/usr/bin/python
import sys

def source(s):
    print(f"""in(field="SourceIP", values=[{', '.join(s)}])\n""")
    return s

def remote(s):
    print(f"""in(field="RemoteIP", values=[{', '.join(s)}])\n""")
    return s