import unittest

from src.types.axis import Axis2, Axis3
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class TestAxis2(unittest.TestCase):
    # Tests for Axis2
    def test_instantiate_axis2(self):
        x_axis = Vector2(1.2425, -0.41)
        y_axis = Vector2(661.2, 4.241)

        axis = Axis2(x_axis, y_axis)

        self.assertEqual(x_axis.x, axis.x_axis.x)
        self.assertEqual(x_axis.y, axis.x_axis.y)

        self.assertEqual(y_axis.x, axis.y_axis.x)
        self.assertEqual(y_axis.y, axis.y_axis.y)


class TestAxis3(unittest.TestCase):
    # Tests for Axis3
    def test_instantiate_axis3(self):
        x_axis = Vector3(-2.1, 61, -6.123)
        y_axis = Vector3(11.245661, -4, 6.145)
        z_axis = Vector3(-0.41, 38, 8.75)

        axis = Axis3(x_axis, y_axis, z_axis)

        self.assertEqual(x_axis.x, axis.x_axis.x)
        self.assertEqual(x_axis.y, axis.x_axis.y)
        self.assertEqual(x_axis.z, axis.x_axis.z)

        self.assertEqual(y_axis.x, axis.y_axis.x)
        self.assertEqual(y_axis.y, axis.y_axis.y)
        self.assertEqual(y_axis.z, axis.y_axis.z)

        self.assertEqual(z_axis.x, axis.z_axis.x)
        self.assertEqual(z_axis.y, axis.z_axis.y)
        self.assertEqual(z_axis.z, axis.z_axis.z)
