import re
with open ("roww.txt",'r') as file:
   text=file.read()
   pattern = r'\d{4}-\d{2}-\d{2}'
   res=re.findall(pattern,text)
   print(res)