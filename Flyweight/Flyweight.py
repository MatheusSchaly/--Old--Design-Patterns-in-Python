"""
Created on Tue Jun 19 10:09:05 2018

@author: Matheus Schaly
"""


from abc import ABC, abstractmethod
import copy


# Flyweight Factory
class Shape_Factory:
    
    circle_map = {}
    
    def get_circle(cls, color):
        
        circle = cls.circle_map.get(color)
        
        if (circle == None):
            circle = Circle(color)
            cls.circle_map[color] = circle
            print("Creating circle of color: " + color)
        
        return copy.deepcopy(circle) # Should it be a copy?
    
    
# Flyweight
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass
    
    
# Concrete Flyweight
class Circle(Shape):
    
    _color = ''
    _x = 0
    _y = 0
    _radius = 0
    
    def __init__(self, color):
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        
    def draw(self):
        print("Circle: \ncolor:", self.color, "\nx:", self.x, "\ny:", self.y, "\nradius:", self.radius)

my_circles = []

circle = Shape_Factory.get_circle(Shape_Factory, "black")
circle.draw()
my_circles.append(circle)
print()

circle = Shape_Factory.get_circle(Shape_Factory, "black")
circle.x = 10
circle.y = 20
circle.radius = 5
circle.draw()
my_circles.append(circle)
print()

circle = Shape_Factory.get_circle(Shape_Factory, "black")
circle.draw()
my_circles.append(circle)
print()

circle = Shape_Factory.get_circle(Shape_Factory, "red")
circle.draw()
my_circles.append(circle)
print()

print("My circles:")
for circle in my_circles:
    circle.draw()
    print()

