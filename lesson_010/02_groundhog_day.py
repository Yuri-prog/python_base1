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



# -*- coding: utf-8 -*-
from random import randint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
expression = ''


class IamGodError(Exception):

    def __str__(self):
        pass


class DrunkError(Exception):

    def __str__(self):
        print('Я пьян!')


class CarCrashError(Exception):

    def __str__(self):
        print('Я разбился в автокатастрофе!')


class GluttonyError(Exception):

    def __str__(self):
        print('Я объелся!')


class DepressionError(Exception):

    def __str__(self):
        print('Я в депрессии!')


class SuicideError(Exception):

    def __str__(self):
        print('Я самоубился!')

carma = 0

def one_day():
    global carma
    global expression
    a = randint(1, 8)
    carma += a
    print(carma)
    if carma > ENLIGHTENMENT_CARMA_LEVEL:
        print('Уровень кармы 777!')
    else:
        b = randint(1, 14)
        print('b = ', b)
        if b == 1:
            expression = 'Я бог'
            file_write(expression)
            raise IamGodError
        elif b == 2:
            expression = 'Я пьян!'
            file_write(expression)
            raise DrunkError
        elif b == 3:
            expression = 'Я разбился в автокатастрофе!'
            file_write(expression)
            raise CarCrashError
        elif b == 4:
            expression = 'Я объелся!'
            file_write(expression)
            raise GluttonyError
        elif b == 5:
            expression = 'Я в депрессии!'
            file_write(expression)
            raise DepressionError
        elif b == 6:
            expression = 'Я самоубился!'
            file_write(expression)
            raise SuicideError
    return carma

file_name = 'log.txt'

def file_write(expression):
    file = open(file_name, mode='w', encoding='utf8')
    file.write(expression)
    file.close()


while True:
    try:
        if one_day() > ENLIGHTENMENT_CARMA_LEVEL:
            break
    except IamGodError:
        print('Я бог')
    except DrunkError:
       print('Я пьян!')
    except CarCrashError:
        print('Я разбился в автокатастрофе!')
    except GluttonyError:
        print('Я объелся!')
    except DepressionError:
        print('Я в депрессии!')
    except SuicideError:
        print('Я самоубился!')

file = open(file_name, mode='w', encoding='utf8')
file.write('ggggggggddddddddddddddd')
file.close()


# https://goo.gl/JnsDqu
#one_day()
