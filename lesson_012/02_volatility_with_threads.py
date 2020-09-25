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
from datetime import datetime
from threading import Thread


class Volatility(Thread):
    volatility_list = []
    null_volatility = []


    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.ticker_name = ''
        self.volatility = 0
        self.ticker_prices = []

    def run(self):
        self.file_name = f'trades\\\{self.file_name}'
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                line = (line.split(','))
                self.ticker_name = line[0]
                price = line[2]
                if price[0].isnumeric():
                    price = float(price)
                    self.ticker_prices.append(price)
            half_sum = (max(self.ticker_prices) + min(self.ticker_prices)) / 2
            self.volatility = (max(self.ticker_prices) - min(self.ticker_prices)) / half_sum * 100
            if self.volatility == 0.0:
                self.null_volatility.append(self.ticker_name)
            else:
                self.volatility_list.append((self.ticker_name, self.volatility))
        return self.volatility_list, self.null_volatility


class Tickers():
    directory = 'trades'
    files = os.listdir(directory)

    def __init__(self):
        self.min_volatility = {}
        self.max_volatility = {}

    def main(self):
        my_threads = [Volatility(file_name=file_name) for file_name in self.files]
        for my_thread in my_threads:
            my_thread.start()
        for my_thread in my_threads:
            my_thread.join()
            Volatility.volatility_list.sort(key=lambda i: i[1])
        self.min_volatility = dict(Volatility.volatility_list[2::-1])
        self.max_volatility = dict(Volatility.volatility_list[:-4:-1])
        print('Максимальная волатильность:')
        for key, val in self.max_volatility.items():
            print(key, val)
        print('Минимальная волатильность:')
        for key, val in self.min_volatility.items():
            print(key, val)
        print('Нулевая волатильность:')
        print(Volatility.null_volatility)


start_time = datetime.now()
all_threads = Tickers()
all_threads.main()
end_time = datetime.now()
print("Время выполнения: ", end_time - start_time)