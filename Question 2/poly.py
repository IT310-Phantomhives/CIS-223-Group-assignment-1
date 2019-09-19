#Caleb Biluts
#B507
from abc import ABCMeta, abstractmethod
from cmath import sqrt, tan
from math import radians


class Polygon :

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):
    def _init_(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Isosceles (Triangle):
    def _init_(slef, x,y):
        Triangle._init_(self, x, x, y)

    def area(self):
        altitude = sqrt(self.x*self.x - self.z*self.z/4);
        return altitude*self.z/2;

    def perimeter(slef):
        return self.x+self.y+self.z

class EquilateralTriangle (Triangle):
    def _init_(self, x):
        Triangle._init_(self, x,x,x)

    def area(self):
        return sqrt(3)*self.x*self.x/4;\
               
    def perimeter(self):
        return self.x+self.y+self.z

class Quadrilateral(Polygon):
    def _init_(slef, x,y):
        self.x = x
        self.y = y

class Rectangle(Quadrilateral):
    def _init_(self, x,y):
        Quadrialterl._init_(self, x,y)
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)

class square(Quadrilateral):
    def _init_(self, x):
        Quadrilateral._init_(self, x, x)
    def area(slef):
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)

class Pentagon(Polygon):
    def _init_(self, size,numberOfSide=5):
        self.size = size
        self.numberOfSide = numberOfSide

    def area(slef):
        angle = radians(180/self.numberOfSide);
        return self.size*self.size* self.numberOfSide/(4*tan(angle));

    def perimeter(slef):
        return self.numberOfSide*self.size;

class Hexagon(Polygon):
    def _init_(self, size,numberOfSide=6):
        self.size = size
        self.numberOfSide = numberOfSide

    def area(self):
        angle = radians(180/self.numberOfSide);
        self.numberOfSide = numberOfSide

    def area(self):
        angle = radians(180/self.numberOfSide);
        return self.size*self.size* self.numberOfSide/(4*tan(angle));
    def perimeter(slef):
        return self.numberOfSide*self.size;

class Octagon(Polygon):
    def _init_(self, size,numberOfSide=8):
        self.size = size
        self.numberOfSide = numberOfSide
    def area(self):
        angle = radians(180/self.numberOfSide);
        return self.size*self.size* self.numberOfSide/(4*tan(angle));

    def perimeter(slef):
        return self.numberOfSide*self.size;
    
