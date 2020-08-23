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

def one_day():
    global carma  # TODO: это можно убрать из глобального состояния.
    a = randint(1, 8)
    carma += a
    print(carma)
    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        print('Уровень кармы 777!')
    else:
        b = randint(1, 14)
        if b == 1:
            expression = f'Я Бог! при уровне кармы {carma}'
            expression_list.append(expression)
            raise IamGodError
        elif b == 2:
            expression = f'Я пьян!при уровне кармы {carma}'
            expression_list.append(expression)
            raise DrunkError
        elif b == 3:
            expression = f'Я разбился в автокатастрофе! при уровне кармы {carma}'
            expression_list.append(expression)
            raise CarCrashError
        elif b == 4:
            expression = f'Я объелся! при уровне кармы {carma}'
            expression_list.append(expression)
            raise GluttonyError
        elif b == 5:
            expression = f'Я в депрессии! при уровне кармы {carma}'
            expression_list.append(expression)
            raise DepressionError
        elif b == 6:
            expression = f'Я самоубился! при уровне кармы {carma}'
            expression_list.append(expression)
            raise SuicideError
    # TODO: не настаиваю, но давайте попробуем сделать красиво.
    # TODO: положите классы исключений в словарь, в котором цифры будут ключами,
    # TODO: и райзите эти исключения прямо из словаря, используя b как ключ.
    return carma

file_name = 'log.txt'

def file_write(expression):  #Запись в лог-файл
    file = open(file_name, mode='w', encoding='utf8')
    file.write(expression)
    file.close()


while True:
    try:
        if one_day() >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except IamGodError:
        print(f'Я Бог! при уровне кармы {carma}')
    except DrunkError:
        print(f'Я пьян! при уровне кармы {carma}')
    except CarCrashError:
        print(f'Я разбился в автокатастрофе! при уровне кармы {carma}')
    except GluttonyError:
        print(f'Я объелся! при уровне кармы {carma}')
    except DepressionError:
        print(f'Я в депрессии! при уровне кармы {carma}')
    except SuicideError:
        print(f'Я самоубился! при уровне кармы {carma}')
    file_write('\n'.join(expression_list) + '\n' + f'Общее количество исключений {len(expression_list)}')


