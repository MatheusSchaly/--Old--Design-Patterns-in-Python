"""
Created on Thu Jun 14 16:57:02 2018

@author: Matheus Schaly
"""


from abc import ABC, abstractmethod


# Component
class Shape(ABC):
    
    @abstractmethod
    def draw(self, color):
        pass


# Leaf 1
class Triangle(Shape):
    
    def draw(self, color):
        print("Drawing Triangle with color " + color)


# Leaf 2
class Circle(Shape):
    
    def draw(self, color):
        print("Drawing Circle with color " + color)


# Composite
class Drawing(Shape):
    
    def __init__(self):
        self.shapes = []

    def draw(self, color):
        for sh in self.shapes:
            sh.draw(color)

    def add(self, sh):
        self.shapes.append(sh)

    def remove(self, sh):
        self.shapes.remove(sh)

    def clear(self):
        print("Clearing all the shapes from drawing")
        self.shapes = []


tri1 = Triangle()
tri2 = Triangle()
cir  = Circle()

drawing = Drawing()
drawing.add(tri1)
drawing.add(tri2)
drawing.add(cir)

drawing.draw("Red")

drawing.clear()

drawing.add(tri1)
drawing.add(cir)
drawing.draw("Green")