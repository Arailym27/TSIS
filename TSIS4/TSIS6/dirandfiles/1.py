f=open("arai.txt","a")
#with open("arai.txt",'r')as f:
f.write("Жетім шалды бала орнына тербеген.")
f.close()
f=open("arai.txt","r")
print(f.readline())
print(f.readline())
print("Курсив тут\n")
for x in f:
    print(x)
f.close()
