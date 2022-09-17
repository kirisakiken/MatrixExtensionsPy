import unittest

from src.extensions.vector_extensions import VectorExtensions
from src.types.line2 import Line2
from src.types.line3 import Line3
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class TestVectorExtensions(unittest.TestCase):
    # Tests for Vector Extensions
    def test_vector2_to_matrix_1x2(self):
        vector = Vector2(1.2, -6.2)
        matrix = VectorExtensions.vector2_to_matrix_1x2(vector)

        self.assertEqual(matrix[0][0], vector.x)
        self.assertEqual(matrix[1][0], vector.y)

    def test_vector2_to_matrix_1x3(self):
        vector = Vector2(5.123, -0.52)
        matrix = VectorExtensions.vector2_to_matrix_1x3(vector)

        self.assertEqual(matrix[0][0], vector.x)
        self.assertEqual(matrix[1][0], vector.y)
        self.assertEqual(matrix[2][0], 1)

    def test_vector3_to_matrix_1x3(self):
        vector = Vector3(3, 2.11, -0.13)
        matrix = VectorExtensions.vector3_to_matrix_1x3(vector)

        self.assertEqual(matrix[0][0], vector.x)
        self.assertEqual(matrix[1][0], vector.y)
        self.assertEqual(matrix[2][0], vector.z)

    def test_vector3_to_matrix_1x4(self):
        vector = Vector3(-1.24, 10, 5.21)
        matrix = VectorExtensions.vector3_to_matrix_1x4(vector)

        self.assertEqual(matrix[0][0], vector.x)
        self.assertEqual(matrix[1][0], vector.y)
        self.assertEqual(matrix[2][0], vector.z)
        self.assertEqual(matrix[3][0], 1)

    def test_get_dot_product_2d(self):
        a = Vector2(1, 2)
        b = Vector2(5, 10)

        dot = VectorExtensions.get_dot_product(a, b)
        self.assertEqual(dot, 25)

    def test_get_dot_product_3d(self):
        a = Vector3(1, 2, -1)
        b = Vector3(5, 4, 1.1)

        dot = VectorExtensions.get_dot_product(a, b)
        self.assertEqual(dot, 11.9)

    def test_get_dot_product_fail(self):
        a = Vector2(1, 5)
        b = Vector3(3, 5, 1)

        with self.assertRaises(TypeError):
            VectorExtensions.get_dot_product(a, b)

    def test_get_cross_product_2d(self):
        a = Vector2(1, 2)
        b = Vector2(5, -5)

        cross = VectorExtensions.get_cross_product(a, b)
        self.assertEqual(cross, -15)

    def test_get_cross_product_3d(self):
        expected = Vector3(-9, -15, 13)
        a = Vector3(1, 2, 3)
        b = Vector3(-4, 5, 3)

        cross = VectorExtensions.get_cross_product(a, b)
        self.assertEqual(cross, expected)

    def test_get_cross_product_fail(self):
        a = Vector2(1, 5)
        b = Vector3(3, 5, 1)

        with self.assertRaises(TypeError):
            VectorExtensions.get_cross_product(a, b)

    def test_get_distance_2d(self):
        a = Vector2(1, 2)
        b = Vector2(-5, 10)

        distance = VectorExtensions.get_distance(a, b)
        self.assertEqual(distance, 10)

    def test_get_distance_3d(self):
        a = Vector3(1, 2, -1)
        b = Vector3(5, 3, 1)

        distance = VectorExtensions.get_distance(a, b)
        self.assertAlmostEqual(distance, 4.12, 2)

    def test_get_distance_fail(self):
        a = Vector2(1, 5)
        b = Vector3(3, 5, 1)

        with self.assertRaises(TypeError):
            VectorExtensions.get_distance(a, b)

    def test_get_lerp_2d(self):
        a = Vector2(1, 5)
        b = Vector2(15, 15)
        t_1 = 0.5
        t_2 = 2

        lerp_clamped = VectorExtensions.get_lerp(a, b, t_1)
        self.assertEqual(lerp_clamped.x, 8)
        self.assertEqual(lerp_clamped.y, 10)

        lerp_unclamped = VectorExtensions.get_lerp(a, b, t_2, True)
        self.assertEqual(lerp_unclamped.x, 29)
        self.assertEqual(lerp_unclamped.y, 25)

    def test_get_lerp_3d(self):
        a = Vector3(14, 50, -24)
        b = Vector3(-38, 52, 14)
        t_1 = 0.5
        t_2 = 4

        lerp_clamped = VectorExtensions.get_lerp(a, b, t_1)
        self.assertEqual(lerp_clamped.x, -19)
        self.assertEqual(lerp_clamped.y, 26)
        self.assertEqual(lerp_clamped.z, 7)

        lerp_unclamped = VectorExtensions.get_lerp(a, b, t_2, True)
        self.assertEqual(lerp_unclamped.x, -152)
        self.assertEqual(lerp_unclamped.y, 208)
        self.assertEqual(lerp_unclamped.z, 56)

    def test_get_lerp_fail(self):
        a = Vector2(1, 5)
        b = Vector3(3, 5, 1)

        with self.assertRaises(TypeError):
            VectorExtensions.get_lerp(a, b, 1)

    def test_get_perpendicular_distance_2d(self):
        a = Vector2(1, 2)
        b = Line2(1, -1, 2)

        distance = VectorExtensions.get_perpendicular_distance(a, b)
        self.assertAlmostEqual(distance, 0.707, 3)

    def test_get_perpendicular_distance_3d(self):
        a = Vector3(1, 2, -1)
        b = Line3(1, 5, 1.33, -6)

        distance = VectorExtensions.get_perpendicular_distance(a, b)
        self.assertAlmostEqual(distance, 0.696, 3)

    def test_get_perpendicular_distance_fail(self):
        a = Vector2(0, 5)
        b = Line3(55, 1.2, 5)

        with self.assertRaises(TypeError):
            VectorExtensions.get_perpendicular_distance(a, b)
