import sys,tempfile,json
from print_color import print

def writetxt(s):
    file_name = input("Please enter File Name: ")
    print("")
    f = open(file_name+".txt", "w")
    f.write(str(s))
    f.close()

def load_history(filename):
    filename.seek(0)
    try:
        return json.load(filename)
    except json.JSONDecodeError:
        return {}

def save_history(text: str,filename):
    filename.seek(0)
    try:
        history = load_history(filename)
    except:
        history = []
    
    if isinstance(history, list):
        history.append(text)
    else:
        history = [text]
    filename.seek(0)
    json.dump(history, filename)
    filename.truncate()

def format_history_entry(original,modified,function):
    return f"""Performed function {function}\nOriginal : {original}\nModified : {modified}\n"""

def history_print(filename):
    file = load_history(filename)
    print(f"\nHistory File Output\n", format='bold', color='blue')
    for entry in file:
        for line in entry.split("\n"):
            if "Performed function" in line:
                functions = line.split()
                print(f"{functions[0]} {functions[1]} ", end = "")
                print(functions[2], color='cyan', background='black')
            elif "Original" in line:
                functions = line.split(":",1)
                print(functions[0], color='green', end = "")
                print(functions[1])
            elif "Modified" in line:
                functions = line.split(":",1)
                print(functions[0], color='red', end = "")
                print(functions[1])
            else:
                print(line)
        print("")
    

