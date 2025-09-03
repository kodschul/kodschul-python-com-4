class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add_point(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def to_string(self):
        return f"({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # def __mul__(self, other_point):
    #     return self.x + self.y + other_point.x + other_point.y

    def __mul__(self, number):
        return number


a = Point(1, 2)
b = Point(3, 4)

c = a.add_point(b)
c = a + b

ans = a * 1
print(ans)

# product = a * b

# print(c)
# print(product)
