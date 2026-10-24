import unittest
from feature_a import add

class ScaffoldTest(unittest.TestCase):
    def test_scaffold_exports_callable(self):
        self.assertTrue(callable(add))
