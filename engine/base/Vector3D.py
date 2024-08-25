import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, other):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __mul__(self, other):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __str__(self): return f'({self.x};{self.y};{self.z})'
