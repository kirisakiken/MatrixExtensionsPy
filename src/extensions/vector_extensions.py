import numpy as np

from src.types.vector2 import Vector2


class VectorExtensions:
    def __init__(self):
        pass

    @staticmethod
    def vector2_to_matrix_1x3(vec_2d: Vector2):
        return np.array([[vec_2d.x],
                         [vec_2d.y],
                         [1]])

    @staticmethod
    def vector2_to_matrix_1x2(vec_2d: Vector2):
        return np.array([[vec_2d.x],
                         [vec_2d.y]])
