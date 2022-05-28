import numpy as np

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.vector_extensions import VectorExtensions


class ScaleOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_scale_matrix_2d(vector_2: Vector2):
        return np.array([[vector_2.x, 0],
                         [0, vector_2.y]])

    def get_scale_2d(self, vector_2: Vector2, scale_vector_2: Vector2):
        scale_matrix = self.get_scale_matrix_2d(scale_vector_2)
        vector_2_matrix = VectorExtensions.vector2_to_matrix_1x2(vector_2)
        result = np.matmul(scale_matrix, vector_2_matrix)
        return Vector2(result[0][0], result[1][0])
