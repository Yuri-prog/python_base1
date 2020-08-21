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

def one_day():
    carma = 0
    while True:
     a = randint(1, 8)
     carma += a
     print(carma)
     if carma > ENLIGHTENMENT_CARMA_LEVEL:
        break
    b = randint


try:
    one_day()
exept
# https://goo.gl/JnsDqu
