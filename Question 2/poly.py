#Caleb Biluts
#13229041
#Q.2 Assignment 1

import math
import cmath
from math import radians
from cmath import sqrt,tan
class Polygon:
    def __init__(self,n):
        self.n = n

    def type(self):
        if self.n == 3:
            return "Triangle"
        elif self.n == 4:
            return "Rectangle"
        elif self.n == 5:
            return "Pentagon"
        elif self.n == 6:
            return "Hexagon"
        elif self.n == 8:
            return "Octagon"
        else: return "Polygon"

    def howmanysides(self):
        return self.n

    def area(self):
        pass

    def perimeter(self):
        pass



class Triangle(Polygon):
    def __init__(self,a,b,c):
        Polygon.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c)/2.0
        area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
        return area

    def perimeter(self):
        return self.a + self.b + self.c

class Isosceles(Triangle):
    def __init__(self,a,b):
        Triangle.__init__(self, a,a,b)

class EquilateralTriangle(Triangle):
    def __init__(self,a):
        Triangle.__init__(self, a,a,a)

class Quadrilateral(Polygon):
    def __init__(self,breadth,length):
        Polygon.__init__(self, 4)
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Rectangle(Quadrilateral):
    def __init__(self,breadth,length):
        Polygon.__init__(self, 4)
        self.breadth = breadth
        self.length = length

class Pentagon(Polygon):
    def __init__(self, size):
        Polygon.__init__(self, 5)
        self.size = size
  
    def area(self):
        angle = radians(180/5);
        return self.size*self.size*5/(4*tan(angle));

    def perimeter(self):
        return self.size*5

class Hexagon(Polygon):
    def __init__(self, size):
        Polygon.__init__(self, 6)
        self.size = size
  
    def area(self):
        angle = radians(180/6);
        return self.size*self.size*6/(4*tan(angle));
  
    def perimeter(self):
        return self.size*6   

class Octagon(Polygon):
   def __init__(self, size):
       Polygon.__init__(self, 8)
       self.size = size

   def area(self):
       angle = radians(180/8);
       return self.size*self.size*8/(4*tan(angle));

   def perimeter(self):
       return self.size*6


def main():
    tri1=Triangle(2,2,2)
    rect=Rectangle(2,3)
    tri2=Triangle(3,3,3)
    pent1 = Pentagon(4)
    figures = [tri1,rect,tri2,pent1]
    for i in figures:
        print ("Type of Polygon =>", i.type())
        print ("Sides =", i.howmanysides())
        print ("Area =", i.area())
        print ("Perimeter =", i.perimeter())
main()
