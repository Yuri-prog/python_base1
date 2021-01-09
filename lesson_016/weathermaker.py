import datetime

import requests
from bs4 import BeautifulSoup

today = datetime.datetime.today()


class WeatherMaker:
    def __init__(self):
        self.table_date = None
        self.list_of_values = []

    def take_list(self):
        response = requests.get('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow')
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            self.list_of_values = html_doc.find_all('td', {'class': "td_short_gr"})

    def take_weather(self, date):
        days = (date - today).days
        weather_date = self.list_of_values[days + 1].text
        result = {
            weather_date: {
                'День':
                    [self.list_of_values[17 + days].text, self.list_of_values[25 + days].text,
                     self.list_of_values[33 + days].text, self.list_of_values[41 + days].text, ],
                'Ночь':
                    [self.list_of_values[58 + days].text, self.list_of_values[66 + days].text,
                     self.list_of_values[74 + days].text, self.list_of_values[82 + days].text, ],
            },
        }
        w_list = [date, result[weather_date]['День'][0], result[weather_date]['День'][1],
                  result[weather_date]['День'][2], result[weather_date]['День'][3],
                  result[weather_date]['Ночь'][0], result[weather_date]['Ночь'][1],
                  result[weather_date]['Ночь'][2], result[weather_date]['Ночь'][3], ]
        return w_list, result[weather_date]['День'][1]


def test():
    weathermaker = WeatherMaker()
    weathermaker.take_list()
    print(weathermaker.take_weather(today))

# test()
