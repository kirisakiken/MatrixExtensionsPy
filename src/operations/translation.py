import numpy as np

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.vector_extensions import VectorExtensions


class TranslationOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_translation_matrix_2d(translation_vector_2d: Vector2):
        arr = np.identity(3)
        arr[0:2, 2] = [translation_vector_2d.x, translation_vector_2d.y]
        return arr

    def get_translation_2d(self, vector_2: Vector2, translation_vector: Vector2) -> Vector2:
        translation_matrix = self.get_translation_matrix_2d(translation_vector)
        position_matrix = VectorExtensions.vector2_to_matrix3x3(vector_2)
        result = np.matmul(translation_matrix, position_matrix)
        return Vector2(result[0][0], result[1][0])
