import ipaddress
import pandas as pd

def iprange(s):
    ip_list = []
    for line in s:
        ip_list += [str(ip) for ip in ipaddress.IPv4Network(line)]
    filename = input("What to save file as: ")
    df = pd.DataFrame(ip_list)
    df.to_csv(f"{filename}.csv", index=False, header=None)
    return "IP Range file saved to " + filename + ".csv"
