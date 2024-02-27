import re
with open ("row.txt",'r') as file:
   txt=file.read()
   with open ("row.txt",'r') as file:
     text=file.read()
   txt = input(str())
x = re.sub(r'([a-zA-Z]+)_([a-zA-Z]+)', lambda match: match.group(1).capitalize()+match.group(2).capitalize() , txt)
# sub  выполняет замену в строке
# match возвращает новую строку
# match.group(1)первой группе перед подчеркиванием 
# match.group(2)после подчеркивания
print(x)
