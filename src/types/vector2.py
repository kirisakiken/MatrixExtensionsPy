import math


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0, 0)

    @staticmethod
    def one():
        return Vector2(1, 1)

    # region Operators

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self.x == other.x and self.y == other.y)

    # endregion

    def get_magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self):
        v_len = self.get_magnitude()
        if v_len == 0:
            return Vector2.zero()

        return Vector2(self.x / v_len, self.y / v_len)
