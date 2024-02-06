a=int(input())
b=int(input())
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def compute_area(self):
        return self.a*self.b

rec=Rectangle(a,b)
arearec=rec.compute_area()
print(arearec)

