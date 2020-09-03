# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

file_name = 'function_errors.log'


def log_errors(func):
    log = []

    def wrapper(*args):
        try:
            func(*args)
        except Exception as exc:
            log.append(f' {func.__name__:15} {str(args)[1:-2]:32} {str(exc.__class__):25} {exc}')
            raise  # TODO: получается, если произошло исключение, то не произойдет запись в лог
        # TODO: почему не произойдет? Она же реально производится. В предыдущей строке исключение добавляется в log, а в следующих log записывается в файл.
        file = open(file_name, mode='w', encoding='utf8')
        file.write(str('\n'.join(log)))
        file.close()

    return wrapper


# Проверить работу на следующих функциях

@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslz@pmail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
# perky(42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#


# @log_errors('function_errors.log')
# def func():
#     pass
