
class Shape:

    def angle(self):
        return 90


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * 22/7


class Rectangle(Shape):

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


# 10 is the radius
circle = Circle(4)
print(circle.angle())
print(f"Area of the circle is: {circle.area()} AU")

# 15 is the length, 25 width
rect = Rectangle(15, 25)
print(rect.angle())
print(f"Area of the rect is: {rect.area()} AU")
