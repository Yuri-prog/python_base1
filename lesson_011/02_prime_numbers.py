# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.number = 1
        self.n = n
        self.prime_numbers = []
        self.prime = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.number < self.n:
            self.number += 1
            for self.prime in self.prime_numbers:
                if self.number % self.prime == 0:
                    break
            else:
                self.prime_numbers.append(self.number)
                return self.prime

        raise StopIteration()


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    prime = 1
    for number in range(1, n + 1):
        number += 1
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield prime


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def summa(i1, i2, number):  # вычисление суммы элементов среза
    sum = 0
    for i in range(i1, i2 + 1):
        sum += int(number[i])
    return sum


def lucky_number(n):
    m = str(n)
    s = len(m)
    if s % 2 == 0:
        return n, (summa(0, (s // 2) - 1, m) == summa(s // 2, s - 1, m))
    else:
        return n, (summa(0, (s // 2) - 1, m) == summa((s // 2) + 1, s - 1, m))


# for i in range(1, 20):
#     print(i, lucky_number(i))

def palyndrome(n):
    result = True
    n = str(n)
    for i in range(0, len(n)):
        result &= (bool(n[i] == n[-i - 1]))
    return n, result


# palyndrome(4567654)


def niven_numbers(n):  # числа Нивена
    n = str(n)
    return n, (int(n) % (summa(0, len(n) - 1, n)) == 0)


# for i in range(1, 100):
#     print(i, niven_numbers(i))


for number in prime_numbers_generator(n=10000):  # первый способ
    print(palyndrome(number))

gen = prime_numbers_generator(100000)  # второй способ
result = map(lucky_number, gen)
for i in result:
    print(i)