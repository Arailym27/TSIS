import os
def list_der(path):
    print("Derectories:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
          print(i)

def list_files(path):
    print("Files:")
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)):
          print(i)

def list_all(path):
    print("All:")
    for i in os.listdir(path):
          print(i)
    
path=input()
list_der(path)
list_files(path)
list_all(path)