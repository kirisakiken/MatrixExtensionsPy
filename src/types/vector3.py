import math


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)

    @staticmethod
    def one():
        return Vector3(1, 1, 1)

    # region Operators

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not (self.x == other.x and self.y == other.y and self.z == other.z)

    # endregion

    def get_magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def get_normalized(self):
        v_len = self.get_magnitude()
        if v_len == 0:
            return Vector3.zero()

        return Vector3(self.x / v_len, self.y / v_len, self.z / v_len)
