thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist.pop(0)
print(thislist)
thislist.pop()
print(thislist)
thislist.append('orange')
thislist.insert(0,'orange')
print(thislist)
del thislist[3]
print(thislist)
'''del thislist
print(thislist)
#this will cause an error because you have succsesfully deleted "thislist".'''

thislist.clear()
print(thislist)