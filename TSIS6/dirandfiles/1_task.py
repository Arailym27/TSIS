import os
def list_direc(path):
    print("Directories:")
    for i in os.listdir(path):
        #выводит все файлы и папки в каталоге
        if os.path.isdir(os.path.join(path,i)):
            #проверка является ли наша ссылка которая 
            #os.path.join(path,i)-которая например path=/Users/arajlymkabykenova/Desktop/PP2/TSIS3  i=Classes и тогда является ли /Users/arajlymkabykenova/Desktop/PP2/TSIS3/Classes она папкой 
            #
            print(i)
def list_files(path):
    print("\nFiles:")
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)):
            print(i)
def list_all(path):
    print("\nСписок всех каталогов и файлов:")
    for i in os.listdir(path):
        print(i)

path=input("Path for check:")

print(path)
list_direc(path)
list_files(path)
list_all(path)

"""import os
path=input()#ввели TSIS3
content=os.listdir(path)#файлы и папки в папке
for i in content:#смотрим эти папки 
    path_current=path+ '/' + i
    if os.path.isdir(path_current):
        print(i,":")
        for j in os.listdir(path_current):
            print("      "+j)

    else:
        print(i)"""

