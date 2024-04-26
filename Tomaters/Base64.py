import base64
import sys

def decode64(s):
    charset = input("1 - UTF-8\n2 - ascii\n")
    to_use = ""
    match charset:
        case "1":
            to_use = "utf-8"
        case "2":
            to_use = "ascii"
    base64_bytes = str(s).encode(to_use) 
    decode_bytes = base64.b64decode(base64_bytes) 
    decoded_string = decode_bytes.decode(to_use) 
    print(f"Decoded String = {decoded_string}\n")
    return decoded_string
    
def encode64(s):
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
    print(f"Encoded String = {base64_string}\n")
    return base64_string
    