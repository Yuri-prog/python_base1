# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
from threading import Thread
from datetime import datetime

class Volatility:

    def __init__(self, file_name):
        self.ticker_name = ''
        self.volatility = 0
        self.file_name = file_name

    def run(self):

        self.ticker_prices = []
        file = open(self.file_name, 'r', encoding='utf8')
        for line in file:
            line = (line.split(','))
            self.ticker_name = line[0]
            price = line[2]
            if price[0].isnumeric():
                price = float(price)
                self.ticker_prices.append(price)
        half_sum = (max(self.ticker_prices) + min(self.ticker_prices)) / 2
        self.volatility = (max(self.ticker_prices) - min(self.ticker_prices)) / half_sum * 100
        self.volatility = round((self.volatility), 5)
        return self.volatility


class Tickers(Thread):
    directory = 'trades'
    files = os.listdir(directory)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_volatility = {}
        self.max_volatility = {}
        self.null_volatility = []
        self.volatility_list = []

    def run(self):

        for file_name in self.files:
            file_name = f'trades\\\{file_name}'
            one_file = Volatility(file_name)
            one_file.run()
            if one_file.volatility == 0.0:
                self.null_volatility.append(one_file.ticker_name)
            else:
                self.volatility_list.append((one_file.ticker_name, one_file.volatility))
                self.volatility_list.sort(key=lambda i: i[1])
            self.min_volatility = dict(self.volatility_list[2::-1])
            self.max_volatility = dict(self.volatility_list[:-4:-1])


def print_result():
    print('Максимальная волатильность:')
    for key, val in first.max_volatility.items():
        print(key, val)
    print('Минимальная волатильность:')
    for key, val in first.min_volatility.items():
        print(key, val)
    print('Нулевая волатильность:')
    print(first.null_volatility)


first = Tickers()
second = Tickers()

startTime = datetime.now()

first.start()
second.start()

first.join()
second.join()

print_result() #TODO: Время выполнения двух потоков в два раза больше времени выполнения одного. Потоки действительно работают
               # параллельно или я что-то не так сделал? Или GIL мешает?

endTime = datetime.now()
print("Время выполнения: ", endTime - startTime)