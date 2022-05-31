import unittest

from src.extensions.axis_extensions import AxisExtensions
from src.types.axis import (
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class TestAxisExtensions(unittest.TestCase):
    # Tests for Axis Extensions
    def test_axis2_to_matrix_2x2(self):
        axis = Axis2(Vector2(3, 4), Vector2(-1, 5))
        matrix = AxisExtensions.axis2_to_matrix_2x2(axis)

        self.assertEqual(matrix[0][0], axis.x_axis.x)
        self.assertEqual(matrix[1][0], axis.x_axis.y)
        self.assertEqual(matrix[0][1], axis.y_axis.x)
        self.assertEqual(matrix[1][1], axis.y_axis.y)

    def test_axis3_to_matrix_3x3(self):
        axis = Axis3(Vector3(1, 0, 5), Vector3(-2, 5, 3.2), Vector3(2, 1, -6.22))
        matrix = AxisExtensions.axis3_to_matrix_3x3(axis)

        self.assertEqual(matrix[0][0], axis.x_axis.x)
        self.assertEqual(matrix[1][0], axis.x_axis.y)
        self.assertEqual(matrix[2][0], axis.x_axis.z)

        self.assertEqual(matrix[0][1], axis.y_axis.x)
        self.assertEqual(matrix[1][1], axis.y_axis.y)
        self.assertEqual(matrix[2][1], axis.y_axis.z)

        self.assertEqual(matrix[0][2], axis.z_axis.x)
        self.assertEqual(matrix[1][2], axis.z_axis.y)
        self.assertEqual(matrix[2][2], axis.z_axis.z)
