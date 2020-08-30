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

exceptions = {1:IamGodError, 2:DrunkError, 3:CarCrashError, 4:GluttonyError, 5:DepressionError, 6:SuicideError}

carma = 0

def one_day():
    global carma # TODO: это можно убрать из глобального состояния.
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
            raise exceptions[b]
        elif b == 2:
            expression = f'Я пьян!при уровне кармы {carma}'
            expression_list.append(expression)
            raise exceptions[b]
        elif b == 3:
            expression = f'Я разбился в автокатастрофе! при уровне кармы {carma}'
            expression_list.append(expression)
            raise exceptions[b]
        elif b == 4:
            expression = f'Я объелся! при уровне кармы {carma}'
            expression_list.append(expression)

            # -*- coding: utf-8 -*-

            # Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
            # Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
            # Например:
            # Василий test@test.ru 27
            #
            # Надо проверить данные из файла, для каждой строки:
            # - присутсвуют все три поля
            # - поле имени содержит только буквы
            # - поле емейл содержит @ и .
            # - поле возраст является числом от 10 до 99
            #
            # В результате проверки нужно сформировать два файла
            # - registrations_good.log для правильных данных, записывать строки как есть
            # - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
            #
            # Для валидации строки данных написать метод, который может выкидывать исключения:
            # - НЕ присутсвуют все три поля: ValueError
            # - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
            # - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
            # - поле возраст НЕ является числом от 10 до 99: ValueError
            # Вызов метода обернуть в try-except.

            class NotNameError(Exception):

                def __str__(self):
                    return 'Ошибка имени'

            class NotEmailError(Exception):

                def __str__(self):
                    return 'Ошибка e-mail'

            file_name = 'registrations.txt'
            good_log_name = 'registrations_good.log'
            bad_log_name = 'registrations_bad.log'
            good_log = []
            bad_log = []

            def write_file(log_name, log):
                file_log = open(log_name, mode='w', encoding='utf8')
                if log == good_log:
                    x = 'абонентов'
                else:
                    x = 'ошибочных записей'
                file_log.write(str('\n'.join(log) + '\n' + f'Общее количество {x} {len(log)}'))
                file_log.close()

            def sort_mistakes():
                file = open(file_name, mode='r', encoding='utf8')
                for line in file:
                    try:
                        name, email, age = line.split()
                        if name.isalpha() is False:
                            raise NotNameError
                        elif '@' not in email or '.' not in email:
                            raise NotEmailError
                        elif age.isdigit() is False:
                            raise ValueError
                        elif age.isdigit() is True:
                            if int(age) < 10 or int(age) > 99:
                                raise ValueError
                        good_log.append(line)
                        write_file(good_log_name, good_log)
                    except ValueError:  # TODO: давайте ловить исключения при вызове этой функции, а то так получается довольно бессмысленная конструкция
                        if age.isdigit() is False:
                            expression = f'Возраст в строке {line} не является числом, ошибка {ValueError}'
                            print(expression)
                            bad_log.append(expression)
                        elif int(age) < 10 or int(age) > 99:
                            expression = f'Возраст  в строке {line} не находится в допустимых пределах, ошибка {ValueError}'
                            print(expression)
                            bad_log.append(expression)
                        else:
                            expression = f'Несоответствие количества элементов в строке {line}, ошибка {ValueError}'
                            print(expression)
                            bad_log.append(expression)
                    except NotNameError:
                        expression = f'Имя {name} содержит не только буквы, ошибка {NotNameError}'
                        print(expression)
                        bad_log.append(expression)
                    except NotEmailError:
                        expression = f'E-mail {email} не содержит элементов @ или ., ошибка {NotEmailError}'
                        print(expression)
                        bad_log.append(expression)
                    write_file(bad_log_name, bad_log)

            sort_mistakes()
