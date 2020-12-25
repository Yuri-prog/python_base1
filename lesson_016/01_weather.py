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

import cv2
import requests
from PIL import Image
from bs4 import BeautifulSoup
import sqlite3

class WeatherMaker:
    def __init__(self):
        self.result = {}


    def take_weather(self):
        response = requests.get('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow')
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_values = html_doc.find_all('td', {'class': "td_short_gr"})
            self.result = {
                list_of_values[1].text: {
                    list_of_values[8].text:
                        [list_of_values[17].text, list_of_values[25].text, list_of_values[33].text,
                         list_of_values[41].text, ],
                    list_of_values[48].text:
                        [list_of_values[58].text, list_of_values[66].text, list_of_values[74].text,
                         list_of_values[82].text, ],
                },
                list_of_values[2].text: {
                    list_of_values[8].text:
                        [list_of_values[18].text, list_of_values[26].text, list_of_values[34].text,
                         list_of_values[42].text, ],
                    list_of_values[48].text:
                        [list_of_values[59].text, list_of_values[67].text, list_of_values[75].text,
                         list_of_values[83].text, ],
                },
                list_of_values[3].text: {
                    list_of_values[8].text:
                        [list_of_values[19].text, list_of_values[27].text, list_of_values[35].text,
                         list_of_values[43].text, ],
                    list_of_values[48].text:
                        [list_of_values[60].text, list_of_values[68].text, list_of_values[76].text,
                         list_of_values[84].text, ],
                },
                list_of_values[4].text: {
                    list_of_values[8].text:
                        [list_of_values[20].text, list_of_values[28].text, list_of_values[36].text,
                         list_of_values[44].text, ],
                    list_of_values[48].text:
                        [list_of_values[61].text, list_of_values[69].text, list_of_values[77].text,
                         list_of_values[85].text, ],
                },
                list_of_values[5].text: {
                    list_of_values[8].text:
                        [list_of_values[21].text, list_of_values[29].text, list_of_values[37].text,
                         list_of_values[45].text, ],
                    list_of_values[48].text:
                        [list_of_values[62].text, list_of_values[70].text, list_of_values[78].text,
                         list_of_values[86].text, ],
                },
                list_of_values[6].text: {
                    list_of_values[8].text:
                        [list_of_values[22].text, list_of_values[30].text, list_of_values[38].text,
                         list_of_values[46].text, ],
                    list_of_values[48].text:
                        [list_of_values[62].text, list_of_values[71].text, list_of_values[79].text,
                         list_of_values[87].text, ],
                },
                list_of_values[7].text: {
                    list_of_values[8].text:
                        [list_of_values[23].text, list_of_values[31].text, list_of_values[39].text,
                         list_of_values[47].text, ],
                    # list_of_values[48].text:
                    #     [list_of_values[63].text, list_of_values[72].text, list_of_values[80].text, list_of_values[88].text,],
                },
            }


class ImageMaker:
    def __init__(self, day):
        self.text = ''
        self.cloud_cover = ''
        self.day = day

    def choose_day(self):
        gradus_1 = ''
        gradus_2 = ''
        for keys in weathermaker.result.keys():
            if self.day in keys:
                for day_time in weathermaker.result[keys].keys():
                    self.t_d = weathermaker.result[keys]["День"][0][0:-1]
                    self.c_d = weathermaker.result[keys]["День"][1]
                    self.w_d = weathermaker.result[keys]["День"][2]
                    self.p_d = weathermaker.result[keys]["День"][3]
                    self.t_n = weathermaker.result[keys]["Ночь"][0][0:-1]
                    self.c_n = weathermaker.result[keys]["Ночь"][1]
                    self.w_n = weathermaker.result[keys]["Ночь"][2]
                    self.p_n = weathermaker.result[keys]["Ночь"][3]
                    last_dig = weathermaker.result[keys][day_time][0][-2]
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

                    self.date = f' Прогноз погоды на {self.day}:'
                    self.text = (f' {list(weathermaker.result[keys])[0]}:   Температура {weathermaker.result[keys]["День"][0][0:-1]}'
                                 f' {gradus_1}.  '
                            f' {weathermaker.result[keys]["День"][1]}.   Ветер{weathermaker.result[keys]["День"][2]}.'
                            f' Давление {weathermaker.result[keys]["День"][3]}.    '
                            f' {list(weathermaker.result[keys])[1]}:   Температура {weathermaker.result[keys]["Ночь"][0][0:-1]}'
                                 f' {gradus_2}.  '
                            f' {weathermaker.result[keys]["Ночь"][1]}.   Ветер{weathermaker.result[keys]["Ночь"][2]}.'
                            f' Давление {weathermaker.result[keys]["Ночь"][3]}.')
                    self.cloud_cover = weathermaker.result[keys]["День"][1]
                    print(self.cloud_cover)

    def viewimage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def card(self):
        print(self.text)
        background = cv2.imread('python_snippets/external_data/probe1.jpg')
        picture = cv2.imread('')
        picture_1 = cv2.imread('')
        for x in range(1024):
            yellow = (255-(x//4), 255, 255)
            light_blue = (255, 335-(x//4), 315-(x//4))
            blue = (255, 255-(x//4), 255-(x//4))
            gray = (295-(x//4), 295-(x//4), 295-(x//4))
            if 'Снег' in self.cloud_cover or 'снег' in self.cloud_cover:
                card_color = light_blue
                picture = Image.open('python_snippets/external_data/weather_img/snow.jpg')
                if 'Облачно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/cloud.jpg')
                elif 'Ясно' in self.cloud_cover:
                    picture_1 = Image.open('python_snippets/external_data/weather_img/ыгт.jpg')
            elif 'Дождь'in self.cloud_cover or 'дождь' in self.cloud_cover:
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
        print(self.text.split('  '))
        card = cv2.putText(card, self.date, (3, y), cv2.FONT_HERSHEY_COMPLEX,
                           0.7, (0, 0, 200), 1, cv2.LINE_AA)
        for string in self.text.split('  '):
            card = cv2.putText(card, string, (3, y+40), cv2.FONT_HERSHEY_COMPLEX,
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


class DatabaseUpdater:
    def __init__(self):
        pass

    def writing(self):
        conn = sqlite3.connect('weather.db')
        conn.text_factory = str
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS weather "
                       "(id, temp_d, cloud_d, wind_d, pres_d, temp_n, cloud_n, wind_n, pres_n);")
        imagemaker.card()
        cursor.execute("SELECT id FROM weather")
        m = cursor.fetchall()
        if m:
            n = m[-1][0]
        else:
            n = 0
        print(n)
        cursor.execute(
            f"INSERT INTO weather (id, temp_d, cloud_d, wind_d, pres_d, temp_n, cloud_n, wind_n, pres_n)"
            f" VALUES('{(int(n)+1)}', '{imagemaker.t_d}', '{imagemaker.c_d}', '{imagemaker.w_d}', '{imagemaker.p_d}',"
            f"'{imagemaker.t_n}', '{imagemaker.c_n}', '{imagemaker.w_n}', '{imagemaker.p_n}');")
        conn.commit()
        cursor.execute("SELECT * from weather")
        conn.commit()
        result = cursor.fetchall()
        print(result)

        # cursor.execute("DELETE FROM weather")
        # conn.commit()

weathermaker = WeatherMaker()
weathermaker.take_weather()
imagemaker = ImageMaker('25 декабря')
imagemaker.choose_day()
databaseupdater = DatabaseUpdater()
#imagemaker.card()
databaseupdater.writing()
