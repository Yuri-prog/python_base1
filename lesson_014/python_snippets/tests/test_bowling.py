import unittest
from ..bowling import get_score

class MySortTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('567/23XX-3X89453-')
        self.assertEqual(result, 123)

    def test_all_strikes(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_all_fails(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_all_spares(self):
        result = get_score('1/2/3/4/5/6/7/8/9/9/')
        self.assertEqual(result, 150)

    def test_all_numbers(self):
        result = get_score('12345678912345678912')
        self.assertEqual(result, 93)


if __name__ == '__main__':
    unittest.main()