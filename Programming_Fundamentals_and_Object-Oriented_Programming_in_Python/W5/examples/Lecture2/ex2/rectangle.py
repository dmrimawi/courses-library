from shape import Shape


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

