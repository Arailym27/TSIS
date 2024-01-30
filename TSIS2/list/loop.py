list=[1,2,3,4,5]
for x in list:
    print(x)
for i in range(len(list)):
    print(list[i])

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
i=0
while i<len(thislist):
    print (thislist[i])
    print (i)
    i+=1