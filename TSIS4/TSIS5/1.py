#Write a Python program that matches a string that has an
# 'a' followed by zero or more 'b''s.
import re
with open ("row.txt","r") as file:
    txt=file.read()

letter = r'ab*'
matches = re.findall(letter, txt)

if matches:
    for i in matches:
        print(i)
else:
    print("Совпадений не найдено.")