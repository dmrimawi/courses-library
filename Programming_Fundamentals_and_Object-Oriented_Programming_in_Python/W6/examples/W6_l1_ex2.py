from abc import ABC, abstractmethod
class Shape(ABC):
    PI = 3.14159 # Constant to simulate Java-style interface constant
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Shape.PI * self.radius ** 2
    def perimeter(self):
        return 2 * Shape.PI * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
# Usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = \
            {shape.perimeter():.2f}")
