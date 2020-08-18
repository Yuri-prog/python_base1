# -*- coding: utf-8 -*-

from collections import Counter

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

file_name = 'events.txt'


class Parser:

    def __init__(self, file_name, new_file_name):
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.new_pair_list = []

    def count_events(self):
        a = []
        with open(file_name, 'r', encoding='cp1251') as file:
            for i, line in enumerate(file):
                if line.count('NOK'):
                    line = line[0:17] + ']'
                    a.append(line)
                    a.append(str(line) + ' ' + str(a.count(line)))
            i = 1
            while i < (len(a)):  # TODO: здесь всё равно происходит проход по всем ранее найденным строчками
                if a[i - 1][0:18] != a[i][0:18]:
                    self.new_pair_list.append(a[i - 1])
                i += 1
            print('\n'.join(self.new_pair_list))
            return str('\n'.join(self.new_pair_list))

    def file_write(self):
        new_file = open(self.new_file_name, mode='w', encoding='utf8')
        new_file.write(self.count_events())
        new_file.close()


file = Parser('events.txt', 'new_events.txt')
# file.count_events()
# file.file_write()

#TODO С ключами словаря у меня не получается посчитать количество повторений ключей за минуту за один проход. Сделал, как смог.

# TODO: давайте попробуем решить задачу попроще.
# TODO: надо посчитать ноки для каждой цифры:
payload = {
    '1 a': 'NOK',
    '1 b': 'NOK',
    '1 c': 'OK',
    '2 d': 'NOK',
    '2 e': 'NOK',
    '2 f': 'OK',
    '2 g': 'NOK',
    '3 h': 'NOK',
    '3 i': 'OK',
    '3 j': 'OK',
    '1 k': 'NOK',
    '3 l': 'NOK',
    '2 m': 'OK',
    '2 n': 'NOK',
}
quant = 1

result = {}  # TODO: результат записать сюда

for key, value in payload.items():

    num = key[0]  # TODO: num можно использовать как ключ для result
    # TODO: дальше ваш код
    # TODO: Извините, все равно непонятно. Если значениями словаря является счетчик, он считает весь цикл и после первой цифры
    # TODO получаются неправильные значения. То есть после каждой цифры его надо обнулять, при этом он перестает считать.
    # TODO Для того, чтобы работал, нужно запускать цикл заново для каждой цифры, либо для каждой цифры заводить свою
    # TODO переменную счетчика. Как по-другому?

    # TODO: Если мы нашли NOK, и ключа нет в словаре, то надо по этому значению записать 1.
    # TODO: Если ключ есть, то прибавить значение по этому ключу на 1.
    if value == 'NOK':
        result[key[0]] = quant
        quant += 1
        print(result)
quant = 1

print(result)

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу