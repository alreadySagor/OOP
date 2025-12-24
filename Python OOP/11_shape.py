# best example of Polymorphism

# polymorphism maane holo --> eki jinisher bivinno rup thakte pare
# jemon Rectangle & Circle er ekta method (same naam er(area)) area (area duitar khetrei same naam kintu Rectangle er khetre ek rup Circle er khtre ek rup)

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name
    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius
    
# f = Rectangle('ee', 10, 2)
# print(f.area())
# h = Circle('c', 10)
# print(h.area())

# ekhane Rectangle & Circle er moddhe area naam er method ache
# duita method er naam eki kintu ekekta ekek class er tai tader rup'o vinno
