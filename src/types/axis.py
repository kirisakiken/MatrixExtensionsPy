from enum import Enum

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class AXIS(Enum):
    X = 1,
    Y = 2,
    Z = 3,


class Axis2:
    def __init__(self, x_axis: Vector2, y_axis: Vector2):
        self.x_axis = x_axis
        self.y_axis = y_axis


class Axis3:
    def __init__(self, x_axis: Vector3, y_axis: Vector3, z_axis: Vector3):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis
