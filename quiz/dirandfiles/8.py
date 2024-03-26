import os
path = 'X.txt'
path_bool = os.path.exists(path) #проверяет существование файла

if path_bool == False:
    print("Не существует")
    
elif path_bool == True:
    os.remove(path)
    print("Удален")