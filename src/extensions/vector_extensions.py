import math
import numpy as np

from src.types.line2 import Line2
from src.types.line3 import Line3
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class VectorExtensions:
    def __init__(self):
        pass

    @staticmethod
    def get_dot_product(a: Vector2 or Vector3, b: Vector2 or Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            v_1_matrix = np.array([[a.x, a.y]])
            v_2_matrix = np.array([[b.x],
                                   [b.y]])
            return np.matmul(v_1_matrix, v_2_matrix)[0][0]
        elif type(a) == Vector3 and type(b) == Vector3:
            v_1_matrix = np.array([[a.x, a.y, a.z]])
            v_2_matrix = np.array([[b.x],
                                   [b.y],
                                   [b.z]])
            return np.matmul(v_1_matrix, v_2_matrix)[0][0]
        else:
            raise TypeError("Invalid argument types for method get_dot_product. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_cross_product(a: Vector2 or Vector3, b: Vector2 or Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            return np.linalg.det(np.array([[a.x, a.y],
                                           [b.x, b.y]]))
        elif type(a) == Vector3 and type(b) == Vector3:
            return np.linalg.det(np.array([[1, 1, 1],
                                           [a.x, a.y, a.z],
                                           [b.x, b.y, b.z]]))
        else:
            raise TypeError("Invalid argument types for method get_dot_product. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_distance(a: Vector2 or Vector3, b: Vector2 or Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2))
        elif type(a) == Vector3 and type(b) == Vector3:
            return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z + b.z) ** 2))
        else:
            raise TypeError("Invalid argument types for method get_distance. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_lerp(a: Vector2 or Vector3, b: Vector2 or Vector3, t: float, unclamped: bool = False) -> Vector2 or Vector3:
        t_value = max(min(t, 1), 0) if not unclamped else t
        if type(a) == Vector2 and type(b) == Vector2:
            return Vector2(a.x + (b.x - a.x) * t_value, a.y + (b.y - a.y) * t_value)
        elif type(a) == Vector3 and type(b) == Vector3:
            return Vector3((a.x + (b.x - a.x)) * t_value, (a.y + (b.y - a.y)) * t_value, (a.z + (b.z - a.z)) * t_value)
        else:
            raise TypeError("Invalid argument types for method get_lerp. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_perpendicular_distance(vector: Vector2 or Vector3, line: Line2 or Line3) -> float:
        if type(vector) == Vector2 and type(line) == Line2:
            return abs((vector.x * line.a) + (vector.y * line.b) + line.c) / line.get_magnitude()
        elif type(vector) == Vector3 and type(line) == Line3:
            return abs((vector.x * line.a) + (vector.y * line.b) + (vector.z * line.c) + line.d) / line.get_magnitude()
        else:
            raise TypeError("Invalid argument types for method get_perpendicular_distance. Expected types: (Vector2 "
                            "and Line2) or (Vector3 and Line3)")

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
                         [vector_3.z]])

    @staticmethod
    def vector3_to_matrix_1x4(vector_3: Vector3):
        return np.array([[vector_3.x],
                         [vector_3.y],
                         [vector_3.z],
                         [1]])
