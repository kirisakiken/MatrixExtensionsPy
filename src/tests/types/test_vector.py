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

        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 0)
        self.assertEqual(vector.z, 0)

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
