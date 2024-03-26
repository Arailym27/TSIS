#1 square
def gen(san):
    for i in range(san):
        yield i**2

san=int(input())
for j in gen(san):
    print(j)

#2
def san(n):
 for i in range(n+1):
    if i%2==0:
        yield i

n=int(input())
even=san(n)
res=", ".join(map(str,even))
print(res)

#3
def bol(san):
   for i in range(san+1):
      if i%3==0 and i%4==0:
         yield i
san=int(input())
for j in bol(san):
   print(j)

#4
def sq(a,b):
      for i in range(a,b+1):
         yield i**2
a=int(input())
b=int(input())
for i in sq(a,b):
   print(i)

#5
def san(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
for i in san(n):
    print(i)