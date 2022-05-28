import numpy as np
import math

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.vector_extensions import VectorExtensions


class RotationOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_rotation_matrix_2d(degree):
        rad = math.radians(degree)
        return np.array([[math.cos(rad), -math.sin(rad)],
                         [math.sin(rad), math.cos(rad)]])

    def get_rotation_2d(self, vector_2: Vector2, degree: float) -> Vector2:
        rotation_matrix = self.get_rotation_matrix_2d(degree)
        vector_2_matrix = np.array([[vector_2.x],
                                    [vector_2.y]])
        result = np.matmul(rotation_matrix, vector_2_matrix)
        return Vector2(result[0][0], result[1][0])
