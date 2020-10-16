import unittest
from lesson_014.bowling import get_score #TODO: Сейчас при попытке запуска теста из под командной строки не находит lesson_014


class MySortTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('557/23XX-3X82453-')
        self.assertEqual(result, 115)
        with self.assertRaises(ValueError):
            get_score('557/23XX-3X82453')
        with self.assertRaises(ValueError):
            get_score('557/23XX-3X82453-5')

    def test_wrong_symbol(self):
        with self.assertRaises(ValueError):
            get_score('557/23XX-3y82453-')

    def test_lower_case(self):
        result = get_score('557/23Xx-3x82453-')
        self.assertEqual(result, 115)

    def test_all_strikes(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_all_fails(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_all_spares(self):
        result = get_score('1/2/3/4/5/6/7/8/9/9/')
        self.assertEqual(result, 150)
        with self.assertRaises(ValueError):
            get_score('1/2/3/4/5/6/7/8/9///')

    def test_all_numbers(self):
        result = get_score('12345564738291341912')
        self.assertEqual(result, 80)
        with self.assertRaises(ValueError):
            get_score('12345564738291343912')


if __name__ == '__main__':
    unittest.main()