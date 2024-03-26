import os 
path = input("каталог: ")
with open(path, 'r') as file:
    lines = len(file.readlines())
    print('Number of lines:', lines)