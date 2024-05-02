import sys

# Converting time strings
def time(s):
    s = input(f"\nEnter time string to format")
    form = input(f"""\nWhat format type\n
                 1 - HH:MM\n
                 2 - HH:MM:SS\n
                 3 - HH:MM:SS:mm\n
                 4 - \n""")
    