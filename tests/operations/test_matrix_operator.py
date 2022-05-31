import unittest

from src.matrix_operator import MatrixOperator
from src.types.axis import Axis2, Axis3
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class TestMatrixOperator(unittest.TestCase):
    # Tests for Matrix Operator
    def test_apply_linear_transformation_2d(self):
        operator = MatrixOperator()

        vector = Vector2(1.5, -2)
        axis = Axis2(Vector2(2, 3), Vector2(-2, 4))

        transformed_vector = operator.apply_linear_transformation(vector, axis)
        self.assertEqual(transformed_vector.x, 7)
        self.assertEqual(transformed_vector.y, -3.5)

    def test_apply_linear_transformation_3d(self):
        operator = MatrixOperator()

        vector = Vector3(1.5, -2, 1)
        axis = Axis3(Vector3(2, 3, 1), Vector3(-2, 4, 6), Vector3(0, 2, 4.2))

        transformed_vector = operator.apply_linear_transformation(vector, axis)
        self.assertEqual(transformed_vector.x, 7)
        self.assertEqual(transformed_vector.y, -1.5)
        self.assertEqual(transformed_vector.z, -6.3)

    def test_apply_linear_transformation_fail(self):
        operator = MatrixOperator()

        vector = Vector2.one()
        axis = Axis3(Vector3.zero(), Vector3.zero(), Vector3.zero())

        with self.assertRaises(TypeError):
            operator.apply_linear_transformation(vector, axis)

    def test_apply_translation_2d(self):
        operator = MatrixOperator()

        vector = Vector2(1, 2)
        translation_vector = Vector2(-4, 2)

        translated_vector = operator.apply_translation(vector, translation_vector)
        self.assertEqual(translated_vector.x, -3)
        self.assertEqual(translated_vector.y, 4)

    def test_apply_translation_3d(self):
        operator = MatrixOperator()

        vector = Vector3(-5, 3, 2)
        translation_vector = Vector3(1, 2.4, 6.2)

        translated_vector = operator.apply_translation(vector, translation_vector)
        self.assertEqual(translated_vector.x, -4)
        self.assertEqual(translated_vector.y, 5.4)
        self.assertEqual(translated_vector.z, 8.2)

    def test_apply_translation_fail(self):
        operator = MatrixOperator()

        vector = Vector2.zero()
        translation_vector = Vector3.zero()

        with self.assertRaises(TypeError):
            operator.apply_translation(vector, translation_vector)

    def test_apply_rotation_2d(self):
        operator = MatrixOperator()

        vector = Vector2.one()
        angle = 90.0

        rotated_vector = operator.apply_rotation(vector, angle)
        self.assertAlmostEqual(rotated_vector.x, -1, 1)
        self.assertAlmostEqual(rotated_vector.y, 1, 1)

    def test_apply_rotation_3d(self):
        operator = MatrixOperator()

        vector = Vector3.one()
        rotation_vector = Vector3(30, 60, -180)

        rotated_vector = operator.apply_rotation(vector, rotation_vector)
        self.assertAlmostEqual(rotated_vector.x, -0.183, 3)
        self.assertAlmostEqual(rotated_vector.y, -1.366, 3)
        self.assertAlmostEqual(rotated_vector.z, 1.049, 3)

    def test_apply_rotation_fail(self):
        operator = MatrixOperator()

        vector = Vector2.zero()
        rotation_vector = Vector3.zero()

        with self.assertRaises(TypeError):
            operator.apply_rotation(vector, rotation_vector)

    def test_apply_scale_2d(self):
        operator = MatrixOperator()

        vector = Vector2(-1.5, 6.24)
        scale_vector = Vector2(2, -2)

        scaled_vector = operator.apply_scale(vector, scale_vector)
        self.assertEqual(scaled_vector.x, -3.0)
        self.assertEqual(scaled_vector.y, -12.48)

    def test_apply_scale_3d(self):
        operator = MatrixOperator()

        vector = Vector3(2.5, 5, -10)
        scale_vector = Vector3(4, 0.5, -0.1)

        scaled_vector = operator.apply_scale(vector, scale_vector)
        self.assertEqual(scaled_vector.x, 10.0)
        self.assertEqual(scaled_vector.y, 2.5)
        self.assertEqual(scaled_vector.z, 1.0)

    def test_apply_scale_fail(self):
        operator = MatrixOperator()

        vector = Vector2.zero()
        scale_vector = Vector3.zero()

        with self.assertRaises(TypeError):
            operator.apply_scale(vector, scale_vector)
