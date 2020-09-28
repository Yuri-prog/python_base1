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


    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.ticker_name = ''
        self.volatility = 0
        self.ticker_prices = []
        self.volatility_list_1 = []
        self.null_volatility_1 = []

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
                self.null_volatility_1.append(self.ticker_name)
            else:
                self.volatility_list_1.append((self.ticker_name, self.volatility))
        print(self.volatility_list_1, self.null_volatility_1)
        return (self.volatility_list_1)





class Tickers():
    directory = 'trades'
    files = os.listdir(directory)
    collector = multiprocessing.Queue()

    def __init__(self):
        self.min_volatility = {}
        self.max_volatility = {}


    def main(self):

        volatility_list = []
        null_volatility = []
        my_processes = [Volatility(file_name=file_name) for file_name in self.files]
        if __name__ == '__main__':
            for my_process in my_processes:
                #my_process.run()
                my_process.start()
                                                                                            #TODO: Команда start() должна запускать функцию run(). Почему у меня функция run() работает, a start() нет?
                print( my_process)                                                         # TODO: Тут всё работает, просто все процессы со временем виснут в ожидании, пока не освободится collector.
                print(my_process.volatility_list_1)
                                                                                           # TODO: У меня все равно не получается. Очередь сделал без ограничений.
                                                                                           # TODO: Если я запускаю run, информация из Volatility передается в Tickers и производятся вычисления,
                                                                                           # TODO: а при запуске start мы видим, что распечатка волатильности в методе класса Volatility выдает значение,
                                                                                           # TODO: а та же распечатка в методе класса Tickers выдает пустой список. Почему не передается информация?
                Tickers.collector.put(my_process.volatility_list_1)
            for my_process in my_processes:                                               # TODO: этот код успевает проделать только пару итераций, пока запущенные процессы не заполнят очередь.
                                                                                        # TODO: В результате все оставшиеся процессы заблокированы, пока не случится collector.get(),
                my_process.join()
                                                                                     # TODO: а join заблокирован, пока не завершится процесс, у которого он вызван (а он ждет освобождения очереди).

                Tickers.collector.get()
        # TODO: если увеличить max_size у очереди, то это будет работать.
        # TODO: Но в данной реализации в collector не всегда будет ровно одно значение при вызове get(), соответственно, можно потерять часть данных.
        # TODO: Нужно об этом помнить.
                volatility_list += my_process.volatility_list_1
                null_volatility += my_process.null_volatility_1
            print(volatility_list)
        volatility_list.sort(key=lambda i: i[1])
        self.min_volatility = dict(volatility_list[2::-1])
        self.max_volatility = dict(volatility_list[:-4:-1])
        print('Максимальная волатильность:')
        for key, val in self.max_volatility.items():
            print(key, val)
        print('Минимальная волатильность:')
        for key, val in self.min_volatility.items():
            print(key, val)
        print('Нулевая волатильность:')
        print(null_volatility)


start_time = datetime.now()
all_threads = Tickers()
all_threads.main()
end_time = datetime.now()
print("Время выполнения: ", end_time - start_time)