import numpy as np
import math

from src.types.axis import AXIS
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.vector_extensions import VectorExtensions


class RotationOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_rotation_matrix_2d(degree: float):
        rad = math.radians(degree)
        return np.array([[math.cos(rad), -math.sin(rad)],
                         [math.sin(rad), math.cos(rad)]])

    @staticmethod
    def get_rotation_matrix_3d(degree: float, axis: AXIS):
        rad = math.radians(degree)
        if axis == AXIS.X:
            return np.array([[1, 0, 0, 0],
                             [0, math.cos(rad), -math.sin(rad), 0],
                             [0, math.sin(rad), math.cos(rad), 0],
                             [0, 0, 0, 1]])
        elif axis == AXIS.Y:
            return np.array([[math.cos(rad), 0, math.sin(rad), 0],
                             [0, 1, 0, 0],
                             [-math.sin(rad), 0, math.cos(rad), 0],
                             [0, 0, 0, 1]])
        elif axis == AXIS.Z:
            return np.array([[math.cos(rad), -math.sin(rad), 0, 0],
                             [math.sin(rad), math.cos(rad), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        else:
            raise SyntaxError(f"{AXIS.name} is out of range")

    def get_rotation_2d(self, vector_2: Vector2, degree: float) -> Vector2:
        rotation_matrix = self.get_rotation_matrix_2d(degree)
        vector_2_matrix = VectorExtensions.vector2_to_matrix_1x2(vector_2)
        result = np.matmul(rotation_matrix, vector_2_matrix)
        return Vector2(result[0][0], result[1][0])

    def get_rotation_3d(self, vector_3: Vector3, rotation_vector_3: Vector3) -> Vector3:
        rotation_matrix_x = self.get_rotation_matrix_3d(rotation_vector_3.x, AXIS.X)
        rotation_matrix_y = self.get_rotation_matrix_3d(rotation_vector_3.y, AXIS.Y)
        rotation_matrix_z = self.get_rotation_matrix_3d(rotation_vector_3.z, AXIS.Z)

        vector_3_matrix = VectorExtensions.vector3_to_matrix_1x4(vector_3)

        result = np.matmul(rotation_matrix_z, vector_3_matrix)
        result = np.matmul(rotation_matrix_x, result)
        result = np.matmul(rotation_matrix_y, result)

        return Vector3(result[0][0], result[1][0], result[2][0])
