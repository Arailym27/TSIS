import math
def area(a,b):
    s=(a*b**2)/(4*math.tan(math.pi/a))
    return s
    
a=int(input("Input number of sides:"))
b=int(input("Input the length of a side:"))

res=int(area(a,b))
print("The area of the polygon is:",res)
