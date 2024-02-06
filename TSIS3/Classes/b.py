class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    
    def area(self):
        return self.length**2
    
l=float(input())
square=Square(l)
print(square.area())