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
        except ValueError:
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
