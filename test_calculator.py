import unittest
from calculator import add, percent


class T(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_percent(self):
        self.assertEqual(percent(1, 4), 25.0)
        self.assertEqual(percent(3, 3), 100.0)
