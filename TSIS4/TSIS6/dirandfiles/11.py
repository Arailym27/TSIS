import os
def listder(a):
    print("Directories:")
    for i in os.listdir(a):
        if os.path.isdir(os.path.join(a,i)):
            print(i)
def listfile(a):
    print("Files:")
    for i in os.listdir(a):
        if os.path.isfile(os.path.join(a,i)):
            print(i)
def listall(a):
    print("All:")
    for i in os.listdir(a):
        print(i)


a=input()

listder(a)
listfile(a)
listall(a)