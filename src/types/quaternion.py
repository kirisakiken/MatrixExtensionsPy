from math import (
    sin,
    cos,
)
from src.types.vector3 import Vector3


class Quaternion:
    def __init__(self, x, y, z, w):
        self.x, self.y, self.z, self.w = x, y, z, w

    @staticmethod
    def identity():
        return Quaternion(0, 0, 0, 1)

    @staticmethod
    def from_vector3(vector: Vector3):
        cy = cos(vector.x * 0.5)
        sy = sin(vector.x * 0.5)
        cp = cos(vector.y * 0.5)
        sp = sin(vector.y * 0.5)
        cr = cos(vector.z * 0.5)
        sr = sin(vector.z * 0.5)

        return Quaternion(
            sr * cp * cy - cr * sp * sy,
            cr * sp * cy + sr * cp * sy,
            cr * cp * sy - sr * sp * cy,
            cr * cp * cy + sr * sp * sy,
        )
