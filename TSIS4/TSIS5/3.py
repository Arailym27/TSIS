import re
with open ("row.txt",'r') as file:
   text=file.read()
x = re.findall(r'\b[a-z]+_[a-z]+',text)
print(x)
if x :
    print("YES")
else:
    print("NO")