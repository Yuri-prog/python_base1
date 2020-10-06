# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
import multiprocessing
import os
from queue import Empty


class Volatility(multiprocessing.Process):
    volatility_list = []
    null_volatility = []

    def __init__(self, file_name, collector, *args, **kwargs):
        super(Volatility, self).__init__(*args, **kwargs)
        self.file_name = file_name
        self.ticker_name = ''
        self.volatility = 0
        self.ticker_prices = []
        self.collector = collector

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
            self.collector.put(self.ticker_name)
            self.collector.put(self.volatility)
            if self.collector.full():
                print('Очередь заполнена', flush=True)
            print(f'Значение {self.ticker_name, self.volatility} загружено в очередь')


directory = 'trades'
files = os.listdir(directory)


class Tickers(multiprocessing.Process):

    def __init__(self, files, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_volatility = {}
        self.max_volatility = {}
        self.collector = multiprocessing.Queue()
        self.files = files
        self.my_processes = []

    def run(self):

        for file_name in self.files:
            my_process = Volatility(file_name=file_name, collector=self.collector)
            self.my_processes.append(my_process)
        for my_process in self.my_processes:
            my_process.start()

        while True:
            try:
                Volatility.ticker_name = self.collector.get(timeout=1)
                Volatility.volatility = self.collector.get(timeout=1)
                print(f'Принято из очереди {Volatility.ticker_name, Volatility.volatility}', flush=True)
                if Volatility.volatility == 0.0:
                    Volatility.null_volatility.append(Volatility.ticker_name)
                else:
                    Volatility.volatility_list.append((Volatility.ticker_name, Volatility.volatility))
            except Empty:
                print('Очередь пуста', flush=True)
                if not any(my_process.is_alive() for my_process in self.my_processes):
                    break
        for my_process in self.my_processes:
            my_process.join()
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


if __name__ == '__main__':
    tickers = Tickers(files=files)
    tickers.start()
    tickers.join()

# зачет!
