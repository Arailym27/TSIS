import re
with open ("row.txt",'r') as file:
   text=file.read()

   res=re.findall("a.{2,3}b",text)
   print(res)