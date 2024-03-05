import os
f=open("/Users/arajlymkabykenova/Desktop/kerek/a.txt",'w')
f.write("Woops! I have deleted the content!")
f.close()
f=open("/Users/arajlymkabykenova/Desktop/kerek/a.txt",'r')
print(f.read())
f.seek(0)
#переводим курсор на нчало 
#так как тут у нас в read он читает все и курсор на пустоте
print(f.read(6))
if not os.path.exists('newfilee.txt'):
    with open ("newfilee.txt",'x') as f:
        f.write("Text")
else:
    os.remove("newfilee.txt")
#был удалена папка kerekemes
'''import os
os.rmdir("/Users/arajlymkabykenova/Desktop/kerekemes")
'''