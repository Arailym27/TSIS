# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
with open ("row.txt",'r') as file:
   txt=file.read()
x = re.findall( r"a.*b\b"  , txt)
print(x)
