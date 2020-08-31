# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

file_name = 'events.txt'


def count_events():
    new_pair_dict = {}
    new_pair_list = []
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            if 'NOK' in line:
                line = line[0:17] + ']'
                if line not in new_pair_dict:
                    new_pair_dict[line] = 1
                else:
                    new_pair_dict[line] += 1
            else:
                continue
        for key, value in new_pair_dict.items():
            new_pair_list.append(key + ' ' + str(value))
        yield str('\n'.join(new_pair_list))  # TODO: так не интересно. Из генератора выдается единственная строка, и смысла от генератора в общем-то нет.
                                             # TODO: Сделайте так, чтобы за очередной промежуток времени результат выдавался "на лету", то есть до того, как станут известны результаты для
                                             # TODO: следующих промежутков.


grouped_events = count_events()
for group_time in grouped_events:
    print(f'{group_time}')
