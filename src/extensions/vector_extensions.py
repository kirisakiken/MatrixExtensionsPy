import numpy as np

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class VectorExtensions:
    def __init__(self):
        pass

    @staticmethod
    def vector2_to_matrix_1x2(vector_2: Vector2):
        return np.array([[vector_2.x],
                         [vector_2.y]])

    @staticmethod
    def vector2_to_matrix_1x3(vector_2: Vector2):
        return np.array([[vector_2.x],
                         [vector_2.y],
                         [1]])

    @staticmethod
    def vector3_to_matrix_1x3(vector_3: Vector3):
        return np.array([[vector_3.x],
                         [vector_3.y],
                         [vector_3.z],
                         [1]])

    @staticmethod
    def vector3_to_matrix_1x4(vector_3: Vector3):
        return np.array([[vector_3.x],
                         [vector_3.y],
                         [vector_3.z],
                         [1]])
