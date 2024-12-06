import ipaddress
import pandas as pd

def iprange(s=None):
    if not s:
        s = input("Enter IP Subnet : ")
    ip_list = []
    ip_list += [str(ip) for ip in ipaddress.IPv4Network(s)]
    filename = input("What to save file as: ")
    df = pd.DataFrame(ip_list)
    df.to_csv(f"{filename}.csv", index=False, header=None)
    print(f"IP Range file saved to {filename}.csv")
    return f"Performed function iprange\nRange {s} Saved to {filename}.csv"
