from math import sqrt


class Vector4:
    def __init__(self, x, y, z, w):
        self.x, self.y, self.z, self.w = x, y, z, w

    @staticmethod
    def zero():
        return Vector4(0, 0, 0, 0)

    @staticmethod
    def one():
        return Vector4(1, 1, 1, 1)

    # region Operators

    def __add__(self, other):
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Vector4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        return Vector4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __ne__(self, other):
        return not (self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w)

    # endregion

    def get_magnitude(self):
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2) + (self.w ** 2))

    def get_normalized(self):
        v_len = self.get_magnitude()
        if v_len == 0:
            return Vector4.zero()

        return Vector4(self.x / v_len, self.y / v_len, self.z / v_len, self.w / v_len)
