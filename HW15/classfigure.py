import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v
    def perimeter(self):
        return 2*self.h + 2*self.v

class Triangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v * 0.5
    def perimeter(self):
        return self.h + self.v + math.sqrt(self.h^2 + self.v^2)

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r * self.r * math.pi
    def perimeter(self):
        return 2 * math.pi * self.r

class RegularHexagon(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r * self.r * math.sqrt(3)* 1.5
    def perimeter(self):
        return 6*self.r



def main():
    shapes = [
        Rectangle(3,4),
        Rectangle(7,2),
        Triangle(5,2),
        Triangle(4,6),
        Circle(2),
        Circle(7),
        RegularHexagon(2),
        RegularHexagon(5)
    ]
    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())

if __name__ == '__main__':
    main()

