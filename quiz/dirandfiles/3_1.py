import os
path=input()
if os.path.exists(path):
    dirname=os.path.dirname(path)
    filename=os.path.basename(path)
    print("DIRECTORY:",dirname)
    print("File:",filename)