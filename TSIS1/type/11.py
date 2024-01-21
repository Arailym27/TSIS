x = 1
y = 35656222554887711
z = -3255522

print(type(x))#they are all integers no matter which type of numbers/positive/negative/without decimals, of unlimited length
print(type(y))
print(type(z))

a = 1.10
b = 1.0
c = -35.59

print(type(x))#same
print(type(y))
print(type(z))

d = 35e3
e = 12E4
f = -87.7e100

print(type(x))
print(type(y))
print(type(z))

g = 3+5j
h = 5j
i = -5j

print(type(g))
print(type(h))
print(type(i))

x = 1    
y = 2.8  
z = 1j   

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))