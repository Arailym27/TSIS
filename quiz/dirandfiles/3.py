import os
path=input()
if os.path.exists(path):
    dir,file=os.path.split(path)
    print(f"Dir:{dir}")
    print(f"File:{file}")

'''or 
dir=os.path.dirname(path)
file=os.path.basename(path)
print(dir,file)'''