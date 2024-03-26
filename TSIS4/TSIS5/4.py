# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
with open ("row.txt",'r') as file:
   txt=file.read()

x = re.findall( r"\b[A-Z][a-z]*\b"  , txt)
print(x)