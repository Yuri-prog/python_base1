# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе


# quantity = 0
# price = 0
# common_price = 0
# common_quantity = 0
# for numbers in store:
#
#     # for  in range(len(store[numbers])):
#         quantity_store = store[numbers][i]['quantity']
#         summa = store[numbers][i]['quantity'] * store[numbers][i]['price']
#         common_quantity += quantity_store
#         common_price += summa
#
# print('Количество единиц мебели', common_quantity, 'шт. на общую сумму', common_price, 'руб.')



quantity = 0
price = 0
common_quant = 0
common_sum = 0
for numbers in goods:
    print(numbers,  goods[numbers])


for numbers in store:

    common_quant = 0
    common_sum = 0
    for substore in store[numbers]:
         common_quant += substore['quantity']
         common_sum += substore['quantity'] * substore['price']

    print(f'{numbers}: {common_quant} шт. на общую сумму {common_sum} руб.')  # TODO: как-то так

# зачет!



