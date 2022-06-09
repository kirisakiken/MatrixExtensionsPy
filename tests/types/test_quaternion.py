import unittest

from src.types.quaternion import Quaternion
from src.types.vector3 import Vector3


class TestQuaternion(unittest.TestCase):
    # Tests for Quaternion
    def test_instantiate_quaternion(self):
        x, y, z, w = 0.62, -0.56, 1, 0.22
        quaternion = Quaternion(x, y, z, w)

        self.assertEqual(x, quaternion.x)
        self.assertEqual(y, quaternion.y)
        self.assertEqual(z, quaternion.z)
        self.assertEqual(w, quaternion.w)

    def test_get_identity(self):
        quaternion = Quaternion.identity()

        self.assertEqual(quaternion.x, 0)
        self.assertEqual(quaternion.y, 0)
        self.assertEqual(quaternion.z, 0)
        self.assertEqual(quaternion.w, 1)

    def test_from_vector3(self):
        vector = Vector3(30, 45, -60)
        quaternion = Quaternion.from_vector3(vector)

        self.assertAlmostEqual(quaternion.x, 0.704, 3)
        self.assertAlmostEqual(quaternion.y, -0.504, 3)
        self.assertAlmostEqual(quaternion.z, -0.453, 3)
        self.assertAlmostEqual(quaternion.w, -0.211, 3)
