
#1 deg->rad

import math
degree=float(input("Input degree:"))
rad=round(degree*3.14/180,6)
print('Output radian:',rad)

#2area trapezoid

import math
h=int(input("height:"))
a=int(input("first value:"))
b=int(input("second value:"))
s=(a+b)/2*h
print("Output:",s)

#3 area of pol
import math
def area(a,b):
    s=(a*b**2)/(4*math.tan(math.pi/a))
    return s
    
a=int(input("sides:"))
b=int(input("length of a side:"))

res=int(area(a,b))
print("The area of the polygon is:",res)

#4 pallal
import math
def area(a,b):
    s=a*b
    print("Output:",float(s))
    
a=int(input("Length:"))
b=int(input("Height:"))
area(a,b)


