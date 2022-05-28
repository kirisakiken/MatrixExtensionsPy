import numpy as np

from src.types.axis import (
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.extensions.axis_extensions import AxisExtensions
from src.extensions.vector_extensions import VectorExtensions


class TransformationOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_transformation_matrix_2d(transformation_axis: Axis2):
        return AxisExtensions.axis2_to_matrix_2x2(transformation_axis)

    @staticmethod
    def get_transformation_matrix_3d(transformation_axis: Axis3):
        return AxisExtensions.axis3_to_matrix_3x3(transformation_axis)

    # linear transformation 2D
    def get_transformation_2d(self, vector_2: Vector2, transformation_axis: Axis2) -> Vector2:
        position_matrix = VectorExtensions.vector2_to_matrix_1x2(vector_2)
        transformation_matrix = self.get_transformation_matrix_2d(transformation_axis)
        result = np.matmul(transformation_matrix, position_matrix)
        return Vector2(result[0][0], result[1][0])

    # linear transformation 3D
    def get_transformation_3d(self, vector_3: Vector3, transformation_axis: Axis3) -> Vector3:
        position_matrix = VectorExtensions.vector3_to_matrix_1x3(vector_3)
        transformation_matrix = self.get_transformation_matrix_3d(transformation_axis)
        result = np.matmul(transformation_matrix, position_matrix)
        return Vector3(result[0][0], result[1][0], result[2][0])
