# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

import datetime

from databaseupdater import DatabaseUpdater
from imagemaker import ImageMaker
from weathermaker import WeatherMaker

from models import Weather

today = datetime.datetime.today()


class Run:
    def __init__(self):
        self.shift = None

    def print_text(self, date):
        print_date = f' Прогноз погоды на {date.strftime("%d.%m.%Y")}:'
        pr_text = (f'День:'
                   f' Температура {weathermaker.take_weather(date)[0][1][:-1]} град. '
                   f'{weathermaker.take_weather(date)[0][2]}.  Ветер{weathermaker.take_weather(date)[0][3]}. '
                   f'Давление {weathermaker.take_weather(date)[0][4]} мм рт.ст.'
                   f'  Ночь:'
                   f' Температура {weathermaker.take_weather(date)[0][5][:-1]} град. '
                   f'{weathermaker.take_weather(date)[0][6]}.  Ветер{weathermaker.take_weather(date)[0][7]}.'
                   f' Давление {weathermaker.take_weather(date)[0][8]} мм рт.ст.  '
                   )
        base_data = weathermaker.take_weather(date)[0]
        return print_date, pr_text, base_data

    def change_str(self, text_1):
        try:
            time_now = today.time()
            if '-' in text_1:
                text_1 = text_1.split('-')
                first_date = datetime.datetime.combine(datetime.datetime.strptime(text_1[0], f'%d.%m.%Y'), time_now)
                last_date = datetime.datetime.combine(datetime.datetime.strptime(text_1[1], f'%d.%m.%Y'), time_now)
                return first_date, last_date
            else:
                date_card = datetime.datetime.combine(datetime.datetime.strptime(text_1, f'%d.%m.%Y'), time_now)
                return date_card
        except ValueError:
            print('Введена неверная информация. Требуется ввод в формате ДД.ММ.ГГГГ или диапазон'
                  ' ДД.ММ.ГГГГ-ДД.ММ.ГГГГ.')
            return

    def write_to_base(self):
        text_1 = input(f'Выберите диапазон дат с {today.strftime("%d.%m.%Y")} по '
                       f'{(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")} через тире.')
        if self.change_str(text_1):
            if self.change_str(text_1)[0].day >= today.day or \
                    self.change_str(text_1)[1].day <= (today + datetime.timedelta(days=5)).day:
                day = 0
                while True:
                    date = self.change_str(text_1)[0] + datetime.timedelta(days=day)
                    if date > self.change_str(text_1)[1]:
                        break
                    weathermaker.take_weather(date)
                    self.print_text(date)
                    base_data = self.print_text(date)[2]
                    databaseupdater.writing(base_data)
                    day += 1
            else:
                print('Выбраны неверные даты')
                return

    def read_from_base(self):
        text_1 = input(f'Выберите диапазон дат до {(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")} '
                       f'через тире.')
        if self.change_str(text_1):
            if self.change_str(text_1)[1].day <= (today + datetime.timedelta(days=5)).day:
                databaseupdater.base_reading(self.change_str(text_1)[0].date(), self.change_str(text_1)[1].date())
            else:
                print('Выбраны неверные даты')
                return

    def print_card(self):
        text_1 = input(f'Выберите дату в диапазоне с {today.strftime("%d.%m.%Y")} по '
                       f'{(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")}.')
        if self.change_str(text_1):
            if self.change_str(text_1) <= (today + datetime.timedelta(days=5)):
                date = self.change_str(text_1)
                weathermaker.take_weather(date)
                cloud_cover = weathermaker.take_weather(date)[1]
                self.print_text(date)
                print_date = self.print_text(date)[0]
                pr_text = self.print_text(date)[1]
                imagemaker.card(print_date, pr_text, cloud_cover)

            else:
                print('Выбрана неверная дата')
                return

    def print_forecasts(self):
        for day in range(0, 6):
            date = (today + datetime.timedelta(days=day))
            # print(date)
            weathermaker.take_weather(date)
            self.print_text(date)
            print(self.print_text(date)[0])
            imagemaker.text = self.print_text(date)[1].split('  ')
            for string in imagemaker.text:
                print(string)

    def run(self):

        text = input('Выберите действие:\n'
                     '1. Добавить прогноз в базу данных\n'
                     '2. Получить прогноз из базы даных\n'
                     '3. Вывести открытку с прогнозом\n'
                     '4. Вывести прогнозы на консоль\n'
                     '5. Очистить базу данных'
                     )
        if text == '1':
            self.write_to_base()
        elif text == '2':
            self.read_from_base()
        elif text == '3':
            self.print_card()
        elif text == '4':
            self.print_forecasts()
        elif text == '5':
            Weather.delete().execute()
        else:
            print('Введен неправильный номер. Требуется ввод числа от 1 до 5.')


imagemaker = ImageMaker()
weathermaker = WeatherMaker()
databaseupdater = DatabaseUpdater()
run = Run()
databaseupdater.base_reading(today - datetime.timedelta(days=7), today)
weathermaker.take_list()
run.run()
