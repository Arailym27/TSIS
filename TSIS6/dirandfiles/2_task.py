import os 
def check(path):
    if os.path.exists(path):
        print("Exists")
    else:
        print('It does not exist')
    
    if os.access(path,os.R_OK):
        print("Readable")
    else:
        print("Not readable")
    
    if os.access(path,os.W_OK):
        print("Writeable")
    else:
        print('NOT Writeable')
    
    if os.access(path,os.X_OK):
        print("Executable")
    else:
        print('NOT Executable')

path=input()
check(path)