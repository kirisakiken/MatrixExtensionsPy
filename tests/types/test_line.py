import unittest

from src.types.line2 import Line2
from src.types.line3 import Line3


class TestLine2(unittest.TestCase):
    # Tests for Line2
    def test_instantiate_line2(self):
        a, b, c = 5.2, -0.2534, 5
        line = Line2(a, b, c)

        self.assertEqual(line.a, a)
        self.assertEqual(line.b, b)
        self.assertEqual(line.c, c)

    def test_get_zero(self):
        line = Line2.zero()

        self.assertEqual(line.a, 0)
        self.assertEqual(line.b, 0)
        self.assertEqual(line.c, 0)

    def test_get_magnitude(self):
        line = Line2(3, 4, 5)
        magnitude = line.get_magnitude()

        self.assertEqual(magnitude, 5)

    def test_get_normalized(self):
        line = Line2(-0.25, 3.21, 5.632)
        normalized = line.get_normalized()

        self.assertAlmostEqual(normalized.a, -0.0776, 4)
        self.assertAlmostEqual(normalized.b, 0.99698, 5)
        self.assertEqual(normalized.c, 0)


class TestLine3(unittest.TestCase):
    # Tests for Line3
    def test_initialize_line3(self):
        line = Line3(3.2, -0.366, 12, 5)

        self.assertEqual(line.a, 3.2)
        self.assertEqual(line.b, -0.366)
        self.assertEqual(line.c, 12)
        self.assertEqual(line.d, 5)

    def test_get_zero(self):
        line = Line3.zero()

        self.assertEqual(line.a, 0)
        self.assertEqual(line.b, 0)
        self.assertEqual(line.c, 0)
        self.assertEqual(line.d, 0)

    def test_get_magnitude(self):
        line = Line3(3, 4, 5, 6)
        magnitude = line.get_magnitude()

        self.assertAlmostEqual(magnitude, 7.07, 2)

    def test_get_normalized(self):
        line = Line3(0.12, -4.2, 1.63, 9)
        normalized = line.get_normalized()

        self.assertAlmostEqual(normalized.a, 0.026, 2)
        self.assertAlmostEqual(normalized.b, -0.93, 2)
        self.assertAlmostEqual(normalized.c, 0.36, 2)
        self.assertEqual(normalized.d, 0)
