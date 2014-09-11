import unittest
from simple_math import SimpleMath


class TestSimpleMath(unittest.TestCase):
    sample_list = (1, 3, 4, 9)

    def setUp(self):
        self.sm = SimpleMath()


    def test_add(self):
        expected = 5
        result = self.sm.add(2, 3)
        self.assertEquals(result, expected)

    def test_total(self):
        expected = 17
        result = self.sm.total(self.sample_list)
        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main()