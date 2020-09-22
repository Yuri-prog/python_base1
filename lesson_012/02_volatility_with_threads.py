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
    directory = 'trades'
    files = os.listdir(directory)

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.ticker_name = ''
        self.volatility = 0
        self.file_name = ''
        self.null_volatility = []
        self.volatility_list = []

    def run(self):

        for self.file_name in self.files:
            self.ticker_prices = []
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

    def __init__(self):
        self.min_volatility = {}
        self.max_volatility = {}
        self.null_volatility = []
        self.volatility_list = []

    def main(self):
        for i in range(5):
            name = f'Thread #{(i + 1)}'
            my_thread = Volatility(name)
            my_thread.start()
            my_thread.join()
            my_thread.volatility_list.sort(key=lambda i: i[1])
            self.min_volatility = dict(my_thread.volatility_list[2::-1])
            self.max_volatility = dict(my_thread.volatility_list[:-4:-1])
        print('Максимальная волатильность:')
        for key, val in self.max_volatility.items():
            print(key, val)
        print('Минимальная волатильность:')
        for key, val in self.min_volatility.items():
            print(key, val)
        print('Нулевая волатильность:')
        print(my_thread.null_volatility)


start_time = datetime.now()
all_threads = Tickers()
if __name__ == '__main__':
    all_threads.main()

# TODO: Но проблема в том, что у вас программа делает два раза одно и то же. Так мы пользы из задания не извлечем.
# TODO: Cделайте так, чтобы каждый файл обрабатывался в отдельном треде, а класс Tickers пусть управляет тредами и собирает с них данные.
# TODO: По-моему, у меня опять потоки повторяют одно и то же, но как привязать конкретный поток к конкретному файлу я понять пока не могу.

# TODO: Можно сделать двумя способами. Первый, это заставить Volatility работать только с одним файлом.
# TODO: То есть получить где-нибудь снаружи список файлов, затем создать для каждого полученного имени файла класс Volatility, передав в инит имя файла, и внутри него этот файл обработать.
# TODO: Второй способ - это создать фиксированное число классов Volatility, передав в них куски списка файлов. Каждый тред обработает свою пачку файлов, а Tickers соберет результаты.

end_time = datetime.now()
print("Время выполнения: ", end_time - start_time)