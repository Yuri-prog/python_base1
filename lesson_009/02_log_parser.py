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
new_file_name = 'new_events.txt'


class Parser:
    new_pair_dict = {}
    time = ''

    def __init__(self, file_name, new_file_name):
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.new_pair_list = []

    def count_events(self, time):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    def count_time():  # TODO: дефы внутри дефов без веской причины использовать не нужно.
                                       # TODO: тут веской причины нет.
                        if line not in self.new_pair_dict:
                            self.new_pair_dict[line] = 1
                        else:
                            self.new_pair_dict[line] += 1

                    if time == 'min':
                        line = line[0:17] + ']'
                        count_time()
                    elif time == 'hour':
                        line = line[0:14] + ']'
                        count_time()
                    elif time == 'month':
                        line = line[0:8] + ']'
                        count_time()
                    else:
                        print('Ошибка ввода')
                        break
                else:
                    continue
            for key, value in self.new_pair_dict.items():
                self.new_pair_list.append(key + ' ' + str(value))  # TODO: а дублирование происходит потому что этот массив заполняется два раза.
                                                                   # TODO: Попробуйте найти, где именно. 
            return str('\n'.join(self.new_pair_list))

    def file_write(self):
        new_file = open(self.new_file_name, mode='w', encoding='utf8')
        new_file.write(self.count_events(self.time))
        new_file.close()


file = Parser('events.txt', 'new_events.txt')
file.count_events('hour')
file.file_write()

#TODO: Вопрос. Почему пишет Ошибку ввода и делает двойную запись в файл?
# TODO: Вы написали код, который выводит это сообщение, и спрашиваете меня, почему он его выводит :)
# TODO: Обратите внимание на все вызовы count_events. time и self.time - это разные переменные


# payload = {
#     '1 a': 'NOK',
#     '1 b': 'NOK',
#     '1 c': 'OK',
#     '2 d': 'NOK',
#     '2 e': 'NOK',
#     '2 f': 'OK',
#     '2 g': 'NOK',
#     '3 h': 'NOK',
#     '3 i': 'OK',
#     '3 j': 'OK',
#     '1 k': 'NOK',
#     '3 l': 'NOK',
#     '2 m': 'OK',
#     '2 n': 'NOK',
# }
#
#
# result = {}
#
# for key, value in payload.items():
#
#     num = key[0]
#
#     if value == 'NOK':
#         if  num not in result:
#             result[num] = 1
#         else:
#             result[num] += 1
#         print(result)
#
#
# print(result)
#
# # После зачета первого этапа нужно сделать группировку событий
# #  - по часам
# #  - по месяцу

