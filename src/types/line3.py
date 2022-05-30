import math

"""
Represents a linear function that can be described as
ax + by + cz = d in 3D Space
"""


class Line3:
    def __init__(self, a: float, b: float, c: float, d: float = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @staticmethod
    def zero():
        return Line3(0, 0, 0, 0)

    def get_magnitude(self):
        return math.sqrt((self.a ** 2) + (self.b ** 2) + (self.c ** 2))

    def get_normalized(self):
        v_len = self.get_magnitude()
        if v_len == 0:
            return Line3.zero()

        return Line3(self.a / v_len, self.b / v_len, self.c / v_len, 0)
