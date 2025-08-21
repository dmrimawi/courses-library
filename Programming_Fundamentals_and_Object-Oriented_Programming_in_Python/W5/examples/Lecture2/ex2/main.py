import sys

from circle import Circle
from square import Square
from rectangle import Rectangle


class Main:
    def run(self):
        c = Circle(5)
        s = Square(4)
        r = Rectangle(3, 4)
        shapes = [c, s, r]
        for shape in shapes:
            self.describe_shape(shape)
        return 0

    def describe_shape(self, shape):
        a = shape.area()
        t = type(shape)
        print(f"The area of {t} is {a}")


if __name__ == "__main__":
    main = Main()
    code = main.run()
    sys.exit(code)
