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
    count = 0
    saved_line = ''

    with open(file_name, 'r', encoding='cp1251') as file:
        for file_line in file:
            if 'NOK' in file_line:
                file_line = file_line[1:17]
                if file_line != saved_line and saved_line != '':
                    yield saved_line, count
                    count = 0
                saved_line = file_line
                count += 1
            else:
                continue


grouped_events = count_events()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
# зачет!
