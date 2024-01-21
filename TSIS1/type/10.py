z1 = complex(2, 3)  # 2 + 3j
a = ["apple", "banana", "cherry"]

print(a)
print(type(a)) #list-изменяемый можно добавлять удалять

b = ("apple", "banana", "cherry")
print(b)
print(type(b)) #tuple-не меняеться

c = {"name" : "John", "age" : 36}
print(c)
print(type(c)) #dict

x = range(6)
print(x)
print(type(x)) 

y = {"apple", "banana", "cherry"}
print(y)
print(type(y))#set - изменяемый

u = True #bool
print(u)
print(type(u))

k = frozenset({"apple", "banana", "cherry"})#неизменяемый
print(k)
print(type(k))

w = None
print(w)
print(type(w))

n = b"Hello"
print(n)
print(type(n)) 

f = bytearray(5)
print(f)
print(type(f))

q = memoryview(bytes(5))
print(q)
print(type(q)) 
