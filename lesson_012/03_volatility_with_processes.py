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
import os
from datetime import datetime
import multiprocessing


class Volatility(multiprocessing.Process):
    volatility_list = []
    null_volatility = []


    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.ticker_name = ''
        self.volatility = 0
        self.ticker_prices = []
        #self.collector = multiprocessing.Queue()

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
        #self.collector.put(self.volatility_list)
        #print(self.volatility_list)
        return self.volatility_list, self.null_volatility



class Tickers():
    directory = 'trades'
    files = os.listdir(directory)

    def __init__(self):
        self.min_volatility = {}
        self.max_volatility = {}

    def main(self):
        #my_processes = [Volatility(file_name=file_name) for file_name in self.files]
        my_process = Volatility(file_name='TICKER_AFM9.csv')
        #for my_process in my_processes:
        if __name__ == '__main__':
            my_process.start()
        #for my_process in my_processes:
            my_process.join()
            #my_processes.collector.get()
            #print(my_process.volatility_list)  #TODO: В данном случае запущен один поток. Я не понимаю, почему он не передает в main() результат выполнения функции run().
            my_process.volatility_list.sort(key=lambda i: i[1])
        self.min_volatility = dict(my_process.volatility_list[2::-1])
        self.max_volatility = dict(my_process.volatility_list[:-4:-1])
        print('Максимальная волатильность:')
        for key, val in self.max_volatility.items():
            print(key, val)
        print('Минимальная волатильность:')
        for key, val in self.min_volatility.items():
            print(key, val)
        print('Нулевая волатильность:')
        print(Volatility.null_volatility)


start_time = datetime.now()
all_processes = Tickers()
all_processes.main()
end_time = datetime.now()
print("Время выполнения: ", end_time - start_time)