class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"Area of the circle is {3.14 * self.radius * self.radius} cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        print(f"Area of the square is {self.width * self.width} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"Area of the triange is {0.5 * self.width * self.height} cm^2")
        super().describe()

circle = Circle("red", True, 4)
square = Square("blue", False, 2)
triangle = Triangle("green", True, 3, 6)

print(circle.colour)
print(circle.is_filled)
print(circle.radius)
circle.describe()

print(square.colour)
print(square.is_filled)
print(square.width)
square.describe()

print(triangle.colour)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()