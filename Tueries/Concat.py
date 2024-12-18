import sys
from helpers import validate_input

def concat(inp=None):
   s = validate_input(inp)
   complete = ""
   query = input(f"\nPlease enter query string with # where input to be replaced\nFor example ip_src:# OR ip_dst:#\n")
   joiner = input(f"\nEnter query joining string (eg. OR, ||): ")
   for x in range(len(s)):
      st = query.replace("#", s[x])
      complete += st
      if x != (len(s)-1):
         complete += " " + joiner + " "
   print(f"\nComplete query:\n" + complete)
   return f"Perform function concat\n{complete}"
