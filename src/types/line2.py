import math


"""
Represents a linear function that can be described as
ax + by = c
"""


class Line2:
    def __init__(self, a: float, b: float, c: float = 0):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def zero():
        return Line2(0, 0, 0)

    def get_magnitude(self):
        return math.sqrt((self.a ** 2) + (self.b ** 2))

    def get_normalized(self):
        v_len = self.get_magnitude()
        if v_len == 0:
            return Line2.zero()

        return Line2(self.a / v_len, self.b / v_len, 0)

