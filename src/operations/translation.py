import numpy as np

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.vector_extensions import VectorExtensions


class TranslationOperator:
    def __init__(self):
        pass

    @staticmethod
    def __get_translation_matrix_2d(translation_vector_2: Vector2):
        arr = np.identity(3)
        arr[0:2, 2] = [translation_vector_2.x, translation_vector_2.y]
        return arr

    @staticmethod
    def __get_translation_matrix_3d(translation_vector_3: Vector3):
        arr = np.identity(4)
        arr[0:3, 3] = [translation_vector_3.x, translation_vector_3.y, translation_vector_3.z]
        return arr

    def get_translation_2d(self, vector_2: Vector2, translation_vector: Vector2) -> Vector2:
        translation_matrix = self.__get_translation_matrix_2d(translation_vector)
        position_matrix = VectorExtensions.vector2_to_matrix_1x3(vector_2)
        result = np.matmul(translation_matrix, position_matrix)
        return Vector2(result[0][0], result[1][0])

    def get_translation_3d(self, vector_3: Vector3, translation_vector: Vector3) -> Vector3:
        translation_matrix = self.__get_translation_matrix_3d(translation_vector)
        position_matrix = VectorExtensions.vector3_to_matrix_1x4(vector_3)
        result = np.matmul(translation_matrix, position_matrix)
        return Vector3(result[0][0], result[1][0], result[2][0])
