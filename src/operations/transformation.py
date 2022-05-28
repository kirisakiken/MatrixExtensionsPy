import numpy as np

from src.types.axis import Axis2
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

    # linear transformation
    def get_transformation_2d(self, vector_2: Vector2, transformation_axis: Axis2):
        position_matrix = VectorExtensions.vector2_to_matrix_1x2(vector_2)
        transformation_matrix = self.get_transformation_matrix_2d(transformation_axis)
        result = np.matmul(transformation_matrix, position_matrix)
        return Vector2(result[0][0], result[1][0])
