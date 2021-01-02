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

import cv2
import requests
from PIL import Image
from bs4 import BeautifulSoup

from models import Weather

today = datetime.datetime.today()

class WeatherMaker:
    def __init__(self):
        self.result = {}
        self.table_date = None
        self.weather_date = ''
        self.list_of_values = []

    def take_list(self):
        response = requests.get('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow')
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            self.list_of_values = html_doc.find_all('td', {'class': "td_short_gr"})

    def take_weather(self):
        days = (run.date.day-today.day)
        self.table_date = run.date
        self.weather_date = self.list_of_values[days+1].text
        self.result = {
            self.weather_date: {
                self.list_of_values[8].text:
                    [self.list_of_values[17 + days].text, self.list_of_values[25 + days].text,
                     self.list_of_values[33 + days].text, self.list_of_values[41 + days].text, ],
                self.list_of_values[48].text:
                    [self.list_of_values[58 + days].text, self.list_of_values[66 + days].text,
                     self.list_of_values[74 + days].text, self.list_of_values[82 + days].text, ],
            },
        }

class ImageMaker:
    def __init__(self):
        self.text = ''
        self.cloud_cover = ''

    def choose_day(self):
        gradus_1 = ''
        gradus_2 = ''
        for day_time in weathermaker.result[weathermaker.weather_date].keys():
            self.t_d = weathermaker.result[weathermaker.weather_date]["День"][0][0:-1]
            self.c_d = weathermaker.result[weathermaker.weather_date]["День"][1]
            self.w_d = weathermaker.result[weathermaker.weather_date]["День"][2]
            self.p_d = weathermaker.result[weathermaker.weather_date]["День"][3]
            self.t_n = weathermaker.result[weathermaker.weather_date]["Ночь"][0][0:-1]
            self.c_n = weathermaker.result[weathermaker.weather_date]["Ночь"][1]
            self.w_n = weathermaker.result[weathermaker.weather_date]["Ночь"][2]
            self.p_n = weathermaker.result[weathermaker.weather_date]["Ночь"][3]
            last_dig = weathermaker.result[weathermaker.weather_date][day_time][0][-2]
            if last_dig == '1':
                gradus = 'градус'
            elif last_dig == '2' or last_dig == '3' or last_dig == '4':
                gradus = 'градуса'
            else:
                gradus = 'градусов'
            if day_time == 'День':
                gradus_1 = gradus
            else:
                gradus_2 = gradus

            self.date = f' Прогноз погоды на {weathermaker.table_date.strftime("%d.%m.%Y")}:'
            self.text = (f'День: '
                         f' Температура {self.t_d} {gradus_1}. {self.c_d}.  Ветер{self.w_d}. Давление {self.p_d} мм рт.ст.'
                         f'  Ночь: '
                         f' Температура {self.t_n} {gradus_2}. {self.c_n}.  Ветер{self.w_n}. Давление {self.p_n} мм рт.ст.  '
                         )

    def viewimage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def card(self):
        background = cv2.imread('python_snippets/external_data/probe1.jpg')
        picture = cv2.imread('')
        picture_1 = cv2.imread('')
        for x in range(1024):
            yellow = (255 - (x // 4), 255, 255)
            light_blue = (255, 335 - (x // 4), 315 - (x // 4))
            blue = (255, 255 - (x // 4), 255 - (x // 4))
            gray = (295 - (x // 4), 295 - (x // 4), 295 - (x // 4))
            if 'Снег' in self.cloud_cover or 'снег' in self.cloud_cover:
                card_color = light_blue
                picture = Image.open('python_snippets/external_data/weather_img/snow.jpg')
                if 'Облачно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
                elif 'Ясно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/ыгт.jpg')
            elif 'Дождь' in self.cloud_cover or 'дождь' in self.cloud_cover:
                card_color = blue
                picture = Image.open('python_snippets/external_data/weather_img/rain.jpg')
                if 'Облачно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
                elif 'Ясно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/ыгт.jpg')
            elif 'Ясно' in self.cloud_cover:
                card_color = yellow
                picture = Image.open('python_snippets/external_data/weather_img/sun.jpg')
            elif 'Переменная облачность' in self.cloud_cover:
                card_color = yellow
                picture = Image.open('python_snippets/external_data/weather_img/sun.jpg')
                picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
            else:
                card_color = gray
                picture = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
            card = cv2.line(background, (x, 0), (x, 512), card_color, 10)
        y = 220
        card = cv2.putText(card, self.date, (3, y), cv2.FONT_HERSHEY_COMPLEX,
                           0.7, (0, 0, 200), 1, cv2.LINE_AA)
        for string in self.text.split('  '):
            card = cv2.putText(card, string, (3, y + 40), cv2.FONT_HERSHEY_COMPLEX,
                               0.5, (0, 55, 0), 1, cv2.LINE_AA)
            y += 20

        cv2.imwrite('Card.jpg', card)
        card = Image.open('Card.jpg')
        card.paste(picture, (25, 25))
        if picture_1:
            card.paste(picture_1, (125, 25))
        card.save("card_with_cloud.jpg")
        result = cv2.imread('card_with_cloud.jpg')
        cv2.imshow('window', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


imagemaker = ImageMaker()
weathermaker = WeatherMaker()


class DatabaseUpdater:
    def __init__(self):
        self.shift = 0

    def writing(self):
        date_exist = True
        try:
            Weather.select().where(Weather.date == weathermaker.table_date).get()
        except:
            date_exist = False
        if date_exist:
            Weather.delete().where(Weather.date == weathermaker.table_date).execute()
        Weather.create(
            date=weathermaker.table_date,
            temp_d=imagemaker.t_d,
            cloud_d=imagemaker.c_d,
            wind_d=imagemaker.w_d,
            pres_d=imagemaker.p_d,
            temp_n=imagemaker.t_n,
            cloud_n=imagemaker.c_n,
            wind_n=imagemaker.w_n,
            pres_n=imagemaker.p_n,
        )


'02.01.2021-07.01.2021'


class Run:
    def __init__(self):
        self.shift = None
        self.date = ''

    def base_reading(self, first_day, last_day):
        for weather in Weather.select().where(first_day <= Weather.date <= last_day):
            print(f' Дата: {weather.date.strftime("%d.%m.%Y")}.\n  День: Температура: {weather.temp_d}.'
                  f' Облачность: {weather.cloud_d}.Ветер: {weather.wind_d}. Давление: {weather.pres_d} мм рт.ст.\n '
                  f' Ночь: Температура: {weather.temp_n}. Облачность: {weather.cloud_n}. Ветер: {weather.wind_n}.'
                  f' Давление: {weather.pres_n} мм рт.ст.\n'
                                    )

    def change_str(self, text_1):
        try:
            if '-' in text_1:
                text_1 = text_1.split('-')
                first_date = datetime.datetime.strptime(text_1[0], '%d.%m.%Y')
                last_date = datetime.datetime.strptime(text_1[1], '%d.%m.%Y')
                return first_date, last_date
            else:
                date = datetime.datetime.strptime(text_1, '%d.%m.%Y')
                return date
        except ValueError:
            print('Введена неверная информация')
            return

    def run(self):
        text = input('Выберите действие:\n'
                     '1. Добавить прогноз в базу данных\n'
                     '2. Получить прогноз из базы даных\n'
                     '3. Вывести открытку с прогнозом\n'
                     '4. Вывести прогнозы на консоль\n'
                     '5. Очистить базу данных')
        if text == '1':
            text_1 = input(f'Выберите диапазон дат с {today.strftime("%d.%m.%Y")} по '
                           f'{(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")} через тире.')
            if self.change_str(text_1):
                if self.change_str(text_1)[0].day >= today.day or \
                   self.change_str(text_1)[1].day <= (today + datetime.timedelta(days=5)).day:
                    day = 0
                    while True:
                        self.date = self.change_str(text_1)[0] + datetime.timedelta(days=day)
                        if self.date > self.change_str(text_1)[1]:
                            break
                        weathermaker.take_weather()
                        imagemaker.choose_day()
                        databaseupdater.writing()
                        day += 1
                else:
                    print('Выбраны неверные даты')
                    return
        elif text == '2':
            text_1 = input(f'Выберите диапазон дат до {(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")} '
                           f'через тире.')
            if self.change_str(text_1):
                if self.change_str(text_1)[1].day <= (today + datetime.timedelta(days=5)).day:
                    self.base_reading(self.change_str(text_1)[0], self.change_str(text_1)[1])
                else:
                    print('Выбраны неверные даты')
                    return
        elif text == '3':
            text_1 = input(f'Выберите дату в диапазоне с {today.strftime("%d.%m.%Y")} по '
                           f'{(today + datetime.timedelta(days=5)).strftime("%d.%m.%Y")}.')
            if self.change_str(text_1):
                if self.change_str(text_1) <= (today + datetime.timedelta(days=5)):
                    self.date = self.change_str(text_1)
                    weathermaker.take_weather()
                    imagemaker.choose_day()
                    imagemaker.card()
                else:
                    print('Выбрана неверная дата')
                    return
        elif text == '4':
            for day in range(0, 6):
                self.date = (today + datetime.timedelta(days=day))
                weathermaker.take_weather()
                imagemaker.choose_day()
                print(imagemaker.date)
                imagemaker.text = imagemaker.text.split('  ')
                for string in imagemaker.text:
                    print(string)
        elif text == '5':
            Weather.delete().execute()
        else:
            print('Введен неправильный номер')


databaseupdater = DatabaseUpdater()
run = Run()
run.base_reading(today-datetime.timedelta(days=7), today)
weathermaker.take_list()
run.run()


