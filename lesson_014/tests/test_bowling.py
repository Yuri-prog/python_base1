import unittest
# import sys
# sys.path.insert(0, "C:\Users\asus\PycharmProjects\python_base1\lesson_014")
#import myfile
#C:\Users\asus\PycharmProjects\python_base1\lesson_014\take frm here> bowling.py

from lesson_014.bowling import get_score  # TODO: Так должно заработать по идее


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

    # TODO: нужно добавить тесты на некорректные строки + те случаи по которым я написал замечания + может еще какие придумаете


if __name__ == '__main__':
    unittest.main()