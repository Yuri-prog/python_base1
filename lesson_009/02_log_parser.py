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
            while i < (len(a)):
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
file.count_events()
file.file_write()

#TODO С ключами словаря у меня не получается посчитать количество повторений ключей за минуту за один проход. Сделал, как смог.
#TODO Почему то не происходит запись в файл, хотя выдает код процесса 0. Даже при запуске первого рабочего коммита.


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
