import unittest

from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class TestVector2(unittest.TestCase):
    # Tests for Vector2
    def test_instantiate_vector2(self):
        x, y = 1.562, -1.25

        vector = Vector2(x, y)

        self.assertEqual(x, vector.x)
        self.assertEqual(y, vector.y)

    def test_get_zero(self):
        vector = Vector2.zero()

        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 0)

    def test_get_one(self):
        vector = Vector3.one()

        self.assertEqual(vector.x, 1)
        self.assertEqual(vector.y, 1)

    def test_get_magnitude(self):
        vector_1 = Vector2(3, 4)
        vector_2 = Vector2(-3, 4)
        magnitude_1 = vector_1.get_magnitude()
        magnitude_2 = vector_2.get_magnitude()

        self.assertEqual(magnitude_1, 5)
        self.assertEqual(magnitude_2, 5)

    def test_get_normalized(self):
        vector_1 = Vector2(10, 10)
        vector_2 = Vector2(-10, 10)
        normalized_1 = vector_1.get_normalized()
        normalized_2 = vector_2.get_normalized()

        self.assertAlmostEqual(normalized_1.x, 0.707, 3)
        self.assertAlmostEqual(normalized_1.y, 0.707, 3)

        self.assertAlmostEqual(normalized_2.x, -0.707, 3)
        self.assertAlmostEqual(normalized_2.y, 0.707, 3)

    # region Operator Tests

    def test_add(self):
        vector_1 = Vector2(1.5, -6.1)
        vector_2 = Vector2(-12.53, 4)

        result = vector_1 + vector_2
        self.assertAlmostEqual(result.x, -11.03, 2)
        self.assertAlmostEqual(result.y, -2.1, 2)

    def test_subtract(self):
        vector_1 = Vector2(4, -2)
        vector_2 = Vector2(-12, 1)

        result = vector_1 - vector_2
        self.assertEqual(result.x, 16)
        self.assertEqual(result.y, -3)

    def test_multiply(self):
        vector_1 = Vector2(2.5, -2)
        vector_2 = Vector2(4, 1)

        result = vector_1 * vector_2
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, -2)

    def test_equal(self):
        vector_1 = Vector2(3.22, 1)
        vector_2 = Vector2(3.22, 1)
        result_1 = vector_1 == vector_2
        self.assertEqual(result_1, True)

        vector_3 = Vector2(-2, 0)
        vector_4 = Vector2(-2, 0.12)
        result_2 = vector_3 == vector_4
        self.assertEqual(result_2, False)

    def test_not_equal(self):
        vector_1 = Vector2(3.22, 1)
        vector_2 = Vector2(3.22, 1)
        result_1 = vector_1 != vector_2
        self.assertEqual(result_1, False)

        vector_3 = Vector2(1, 2)
        vector_4 = Vector2(1, 1)
        result_2 = vector_3 != vector_4
        self.assertEqual(result_2, True)

        vector_5 = Vector2(1, 2)
        vector_6 = Vector2(2, 1)
        result_3 = vector_5 != vector_6
        self.assertEqual(result_3, True)

        vector_7 = Vector2(1, 1)
        vector_8 = Vector2(2, 1)
        result_4 = vector_7 != vector_8
        self.assertEqual(result_4, True)

    # endregion


class TestVector3(unittest.TestCase):
    # Tests for Vector3
    def test_instantiate_vector3(self):
        x, y, z = 3.1152, 0.25, -6

        vector = Vector3(x, y, z)

        self.assertEqual(x, vector.x)
        self.assertEqual(y, vector.y)
        self.assertEqual(z, vector.z)

    def test_get_zero(self):
        vector = Vector3.zero()

        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 0)
        self.assertEqual(vector.z, 0)

    def test_get_one(self):
        vector = Vector3.one()

        self.assertEqual(vector.x, 1)
        self.assertEqual(vector.y, 1)
        self.assertEqual(vector.z, 1)

    def test_get_magnitude(self):
        vector_1 = Vector3(3, 4, 5)
        vector_2 = Vector3(3, -4, 5)
        magnitude_1 = vector_1.get_magnitude()
        magnitude_2 = vector_2.get_magnitude()

        self.assertAlmostEqual(magnitude_1, 7.07, 2)
        self.assertAlmostEqual(magnitude_2, 7.07, 2)

    def test_get_normalized(self):
        vector_1 = Vector3(5, -7, 1.12)
        vector_2 = Vector3(-5.12, 6.1669, -0.35)
        normalized_1 = vector_1.get_normalized()
        normalized_2 = vector_2.get_normalized()

        self.assertAlmostEqual(normalized_1.x, 0.576, 3)
        self.assertAlmostEqual(normalized_1.y, -0.8069, 3)
        self.assertAlmostEqual(normalized_1.z, 0.129, 3)

        self.assertAlmostEqual(normalized_2.x, -0.638, 3)
        self.assertAlmostEqual(normalized_2.y, 0.7686, 3)
        self.assertAlmostEqual(normalized_2.z, -0.0436, 3)

    # region Operator Tests

    def test_add(self):
        vector_1 = Vector3(1.5, -6.1, 2.5)
        vector_2 = Vector3(-12.53, 4, -2.5)

        result = vector_1 + vector_2
        self.assertAlmostEqual(result.x, -11.03, 2)
        self.assertAlmostEqual(result.y, -2.1, 2)
        self.assertAlmostEqual(result.z, 0, 2)

    def test_subtract(self):
        vector_1 = Vector3(4, -2, 5)
        vector_2 = Vector3(-12, 1, 1)

        result = vector_1 - vector_2
        self.assertEqual(result.x, 16)
        self.assertEqual(result.y, -3)
        self.assertEqual(result.z, 4)

    def test_multiply(self):
        vector_1 = Vector3(2.5, -2, 2)
        vector_2 = Vector3(4, 1, -3)

        result = vector_1 * vector_2
        self.assertEqual(result.x, 10)
        self.assertEqual(result.y, -2)
        self.assertEqual(result.z, -6)

    def test_equal(self):
        vector_1 = Vector3(3.22, 1, 2)
        vector_2 = Vector3(3.22, 1, 2)
        result_1 = vector_1 == vector_2
        self.assertEqual(result_1, True)

        vector_3 = Vector3(-2, 0, 1)
        vector_4 = Vector3(-2, 0.12, 1)
        result_2 = vector_3 == vector_4
        self.assertEqual(result_2, False)

    def test_not_equal(self):
        vector_1 = Vector3(3.22, 1, 2)
        vector_2 = Vector3(3.22, 1, 2)
        result_1 = vector_1 != vector_2
        self.assertEqual(result_1, False)

        vector_3 = Vector3(1, 1, 1)
        vector_4 = Vector3(1, 1, 2)
        result_2 = vector_3 != vector_4
        self.assertEqual(result_2, True)

        vector_5 = Vector3(1, 2, 1)
        vector_6 = Vector3(1, 1, 1)
        result_3 = vector_5 != vector_6
        self.assertEqual(result_3, True)

        vector_7 = Vector3(1, 1, 1)
        vector_8 = Vector3(2, 1, 1)
        result_4 = vector_7 != vector_8
        self.assertEqual(result_4, True)

    # endregion
