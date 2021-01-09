import datetime

from models import Weather


class DatabaseUpdater:

    def __init__(self):
        self.shift = 0

    def writing(self, base_data):
        weather, created = Weather.get_or_create(date=base_data[0].date(), defaults={'temp_d': base_data[1],
                                                                                     'cloud_d': base_data[2],
                                                                                     'wind_d': base_data[3],
                                                                                     'pres_d': base_data[4],
                                                                                     'temp_n': base_data[5],
                                                                                     'cloud_n': base_data[6],
                                                                                     'wind_n': base_data[7],
                                                                                     'pres_n': base_data[8]})
        if not created:
            weather = Weather.update(temp_d=base_data[1], cloud_d=base_data[2], wind_d=base_data[3],
                                     pres_d=base_data[4],
                                     temp_n=base_data[5], cloud_n=base_data[6], wind_n=base_data[7],
                                     pres_n=base_data[8]).where(Weather.id == weather.id)
            weather.execute()

    def base_reading(self, first_day, last_day):
        for weather in Weather.select().where((Weather.date >= first_day) & (Weather.date <= last_day)):
            base_text = (f' Дата: {weather.date.strftime("%d.%m.%Y")}.\n  День: Температура: {weather.temp_d}.'
                         f' Облачность: {weather.cloud_d}.Ветер: {weather.wind_d}. Давление: {weather.pres_d} мм рт.ст.\n '
                         f' Ночь: Температура: {weather.temp_n}. Облачность: {weather.cloud_n}. Ветер: {weather.wind_n}.'
                         f' Давление: {weather.pres_n} мм рт.ст.\n')
            print(base_text)
        return base_text


def test():
    databaseupdater = DatabaseUpdater()
    today = datetime.datetime.today()
    base_data = [today, '1', '2', '3', '4', '5', '6', '7', '8']
    databaseupdater.writing(base_data)
    databaseupdater.base_reading(today.date(), today.date())

# test()
