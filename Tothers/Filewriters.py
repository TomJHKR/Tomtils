import sys

def writetxt(s):
    file_name = input("Please enter File Name: ")
    print("")
    f = open(file_name+".txt", "w")
    f.write(str(s))
    f.close()