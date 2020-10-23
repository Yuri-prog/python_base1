import unittest
from bowling import get_score #TODO Спасибо, заработало


# Сейчас при попытке запуска теста из под командной строки не находит lesson_014
#  Пути старайтесь указывать относительно рабочей директории (той, в которой лежит главный запускаемый файл)
#  т.к. здесь у нас проект состоит из нескольких "мини"-проектов, то можно выполнить хитрый приём, явно указав
#  на рабочую директорию.
#  Сделать это можно либо в Run - Edit configurations
#  Либо можно просто выделить нужную папку как source root
#  для этого надо нажать на неё правой кнопкой - mark directory as - source root
#  Пробовал ставить в командной строке основным каталогом и lesson_014 и tests,
#  указывал на рабочую директорию, ничего не помогает.
#  Заработало только когда скопировал файл bowling в папку tests.

class MySortTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('547/23XX-3X81453-')
        self.assertEqual(result, 113)
        with self.assertRaises(ValueError):
            get_score('547/23XX-3X81453')
        with self.assertRaises(ValueError):
            get_score('547/23XX-3X81453-5')

    def test_wrong_symbol(self):
        with self.assertRaises(ValueError):
            get_score('547/23XX-3y81453-')
        with self.assertRaises(ValueError):
            get_score('547/23XX-3x8140-')

    def test_lower_case(self):
        result = get_score('547/23Xx-3x81453-')
        self.assertEqual(result, 113)

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
        result = get_score('12345463728121341812')
        self.assertEqual(result, 68)
        with self.assertRaises(ValueError):
            get_score('12345564738291343912')


if __name__ == '__main__':
    unittest.main()
