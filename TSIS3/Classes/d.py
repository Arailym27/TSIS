
class Point:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def show(self):
        print(self.x1,self.y1,self.x2,self.y2)

    def move(self):
        A = input("""
    If you want to change first coordinates write '1',
    if you want to change second coordinates write '2',
    if you want to change both coordinates write '3',
    if you don't want to change, write '0'
    """)

        if A =="1":
           self.x1 = float(input("x = "))
           self.y1 = float(input("y = "))

        elif A == "2":
            self.x2 = float(input("x = "))
            self.y2 = float(input("y = "))

        elif A == "3":
            
            self.x1 = float(input("x = "))
            self.y1 = float(input("y = "))
            self.x2 = float(input("x = "))
            self.y2 = float(input("y = "))

        else :
            pass

    def dist(self):
        formula = (self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2 
        return formula ** 0.5
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
Geom = Point(x1 , y1, x2, y2)

Geom.show()
Geom.move()

print(Geom.dist())