import os
path = 'X.txt'
path_bool = os.access(path, os.F_OK) #проверяет существование файла

if path_bool == False:
    print("Не существует")
    
elif path_bool == True:
    os.remove(path)
    print("Удален")