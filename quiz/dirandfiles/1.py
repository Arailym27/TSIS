import os
def listder(path):
    print("Directories:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
            print(i,":")
            for j in os.listdir(os.path.join(path,i)):
                print("    "+j)
        else:
            print(i)
path=input()
listder(path)