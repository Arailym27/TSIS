import os 
path = input("Path: ")
if os.path.exists(path):
    dir, file = os.path.split(path)
    print(f"Directory name: {dir}")
    print(f"File name: {file}")
else:
    print("The specified path does not exist.")
'''
#OR
import os
path=input()
if os.path.exists(path):
    dir_name=os.path.dirname(path)
    file_name=os.path.basename(path)
    print("DIRECTORY:",dir_name)
    print("File:",file_name)'''
