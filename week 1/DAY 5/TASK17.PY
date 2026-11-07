class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(5, 15)

print("Point 1:", p1)
print("Point 2:", p2)
print("Point 3:", p3)

print("P1 == P2:", p1 == p2)
print("P1 == P3:", p1 == p3)