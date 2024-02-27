import re
with open ("row.txt",'r') as file:
   txt=file.read()
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
x = re.sub( '\s', ',' , txt)
print(x)