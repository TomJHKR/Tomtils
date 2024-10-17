import ipaddress
import pandas as pd

def iprange(s):
    ip_list = []
    if len(s) == 1:
        ip_list += [str(ip) for ip in ipaddress.IPv4Network(s[0])]
    else:
        for line in s:
            ip_list += [str(ip) for ip in ipaddress.IPv4Network(line)]
    filename = input("What to save file as: ")
    df = pd.DataFrame(ip_list)
    df.to_csv(f"{filename}.csv", index=False)
    return "IP Range file saved to " + filename + ".csv"
