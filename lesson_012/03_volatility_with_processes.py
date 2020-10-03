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

    # TODO: когда очередь инициализировалась тут, было ок. Но вы её зачем-то отсюда унесли

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

    # TODO: уберите вообще всё из полей класса, они вас только путают
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
        if __name__ == '__main__':  # TODO: это тут не нужно
            for my_process in my_processes:
                my_process.start()
                print(my_process.volatility_list_1)  # TODO: нельзя так просто взять и получить состояние класса из другого процесса через точку. Так вы получаете то значение поля, которое было до вызова start
                Tickers.collector.put(my_process.volatility_list_1)  # TODO: почему это происходит здесь? Отправлять что-то в очередь нужно из дочернего процесса. А дочерние процессы сейчас про нее вообще ничего не знают.
                                                                     # TODO: collector надо передавать в Volatility при инициализации, и все данные отправлять-принимаеть только через него.
            for my_process in my_processes:
                my_process.join()

                Tickers.collector.get()  # TODO: результат выполнения этой команды уходит вникуда

                volatility_list += my_process.volatility_list_1  # TODO: тут будет не то значение, которое было посчитано в дочернем процессе
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