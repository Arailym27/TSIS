import os
print("Path:")
def check(path):
    if os.path.exists(path):
          print("Exists")
    else:
          print("Not exists")
    
    if os.access(path,os.R_OK):
         print("Readable")
    else:
         print("NOT Readable")
        
    if os.access(path,os.W_OK):
         print("Writeable")
    else:
         print("NOT writeable")
    
    if os.access(path,os.X_OK):
         print("Executable")
    else:
         print("NOT executeable")
path=input()
check(path)