# test_app.py

import unittest
from app import main
from io import StringIO
import sys

class TestApp(unittest.TestCase):

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        self.assertIn("Hello this is latashree", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
