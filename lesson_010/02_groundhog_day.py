# -*- coding: utf-8 -*-
from random import randint, shuffle

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
expression_list = []


class IamGodError(Exception):

    def __str__(self):
        print('Я Бог!')


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

exceptions = {1: IamGodError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError, 5: DepressionError, 6: SuicideError}
phrases = {1: f'Я Бог!', 2: f'Я пьян!', 3: f'Я разбился в автокатастрофе! ', 4: f'Я объелся! ', 5: f'Я в депрессии!',
           6: f'Я самоубился!'}


def rasing(b, expression):
    expression_list.append(expression)
    raise exceptions[b]


def one_day():
    print(carma)
    b = randint(1, 14)
    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        print('Уровень кармы 777!')
    else:
        if b in range(1, 6):
            rasing(b, phrases[b])
    return carma


file_name = 'log.txt'


def file_write(expression):  # Запись в лог-файл
    file = open(file_name, mode='w', encoding='utf8')
    file.write(expression)
    file.close()


while True:
    a = randint(1, 8)
    carma += a
    try:
        if one_day() >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except exceptions[1]:
        print(phrases[1])
    except exceptions[2]:
        print(phrases[2])
    except exceptions[3]:
        print(phrases[3])
    except exceptions[4]:
        print(phrases[4])
    except exceptions[5]:
        print(phrases[5])
    except exceptions[6]:
        print(phrases[6])
    file_write('\n'.join(expression_list) + '\n' + f'Общее количество исключений {len(expression_list)}')
