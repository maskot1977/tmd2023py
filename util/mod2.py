import math

print("Hello world!")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def midpoint(self, p):
        return Point((self.x + p.x) / 2, (self.y + p.y) /2)

    def mdistance(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y)


def my_name(z, w):
    print("I'm", z, w)
