import math
from engine.functions import lookat


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dir(self):
        return lookat(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other, self.y / other)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __str__(self): return f'({self.x};{self.y})'
