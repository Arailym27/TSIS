import os 
path = input("каталог: ")
if os.path.exists(path):
    dir, file = os.path.split(path)
    print(f"File name: {file}")
    print(f"Part of the catalog: {dir}")
else:
    print("The specified path does not exist.")
