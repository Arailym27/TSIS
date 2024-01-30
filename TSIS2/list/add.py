thislist = ["apple", "banana", "cherry"]#move(and add)-safe-insert(USE INDEX)
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("orange")#add at the end
print(thislist)
list=[1,2,3]
list_1=[4,5,6]#union-add-in the end
#iterable object(set,dict,list,tuple)
list.extend(list_1)
print(list)