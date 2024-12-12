import base64
import sys

def decode64(s=None):
    if not s:
        s = input(f"\nEnter string to decode: ")
    charset = input("1 - UTF-8\n2 - ascii\n")
    to_use = ""
    match charset:
        case "1":
            to_use = "utf-8"
        case "2":
            to_use = "ascii"
    try:
        base64_bytes = str(s).encode(to_use) 
        decode_bytes = base64.b64decode(base64_bytes) 
        decoded_string = decode_bytes.decode(to_use) 
        print(f"\nDecoded String = {decoded_string}\n")
        return s,decoded_string
    except:
        print(f"\nUnable to decode\n")
        return ""

def encode64(s=None):
    if not s:
        s = input(f"\nEnter string to encode: ")
    charset = input("1 - UTF-8\n2 - ascii\n")
    to_use = ""
    match charset:
        case "1":
            to_use = "utf-8"
        case "2":
            to_use = "ascii"
    string_bytes = str(s).encode(to_use) 
    base64_bytes = base64.b64encode(string_bytes) 
    base64_string = base64_bytes.decode(to_use) 
    print(f"\nEncoded String = {base64_string}\n")
    return [s,base64_string]
    
