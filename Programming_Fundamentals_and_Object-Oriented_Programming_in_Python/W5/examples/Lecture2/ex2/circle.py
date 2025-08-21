from shape import Shape


PI = 3.14

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return PI * self.r * self.r

