import os
i_path=input("Path for check:")
content = os.listdir(i_path)#['classes', 'functionpt1']
for i in content:
    path_current = i_path + '/' + i #/Users/arajlymkabykenova/Desktop/PP2/TSIS3/classes
    if os.path.isdir(path_current):
        print(i + ':')
        for j in os.listdir(path_current):
            print('      ' + j)
    else:
        print(i)