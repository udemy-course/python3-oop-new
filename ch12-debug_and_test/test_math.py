import unittest

from demo.math import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 4), 5)

    def test_add_2(self):
        self.assertEqual(add(10, 20), 30)
        self.assertNotEqual(add(10, 20), 31)

    def test_add_3(self):
        self.assertRaises(ValueError, add, 1, 1.2)


if __name__ == '__main__':
    unittest.main()
