from shape import Shape


class Square(Shape):
    def __init__(self, s):
        super().__init__()
        self.s = s

    def area(self):
        return self.s * self.s
