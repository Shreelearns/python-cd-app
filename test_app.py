# test_app.py

import unittest
from app import add

class TestAddition(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed(self):
        self.assertEqual(add(-1, 5), 4)

if __name__ == "__main__":
    unittest.main()
