import re
with open ("row.txt",'r') as file:
   txt=file.read()
# Write a Python program to split a string at uppercase letters.
x = re.findall('[A-Z][a-z]*' , txt)
print(x)