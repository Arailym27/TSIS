import os 
path = input("каталог: ")
with open(r"TSIS-6/exaples/demofile.txt", 'r') as file:
    lines = len(file.readlines())
    print('Number of lines:', lines)